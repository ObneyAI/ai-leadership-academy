import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("build", ROOT / "scripts/build.py")
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "source"
        shutil.copytree(ROOT / "packet", self.root / "packet")

    def test_build_is_repeatable_and_contains_only_template(self):
        builder.build(self.root)
        first = (self.root / "dist" / builder.ARCHIVE).read_bytes()
        builder.build(self.root)
        self.assertEqual(first, (self.root / "dist" / builder.ARCHIVE).read_bytes())
        builder.check(self.root)
        with zipfile.ZipFile(self.root / "dist" / builder.ARCHIVE) as archive:
            self.assertEqual(11, len(archive.namelist()))
            self.assertIn("Academy/AGENTS.md", archive.namelist())
            self.assertIn("Academy/Course/examples.md", archive.namelist())

    def test_participant_file_blocks_packaging(self):
        (self.root / "packet/Academy/Starting-Point.md").write_text("Private question")
        with self.assertRaises(ValueError):
            builder.build(self.root)

    def test_used_onboarding_blocks_packaging(self):
        path = self.root / "packet/Academy/ONBOARDING.md"
        path.write_text(path.read_text().replace("phase: new", "phase: saved", 1))
        with self.assertRaises(ValueError):
            builder.build(self.root)

    def test_symlink_is_not_packaged(self):
        path = self.root / "packet/Academy/Course/Cohort.md"
        path.unlink()
        path.symlink_to(ROOT / "README.md")
        with self.assertRaises(ValueError):
            builder.build(self.root)

    def test_existing_workspace_is_never_overwritten(self):
        dest = Path(self.temp.name) / "learner"
        builder.extract(dest, self.root)
        note = dest / "Academy/Starting-Point.md"
        note.write_text("Keep my question")
        (dest / "Academy/ONBOARDING.md").unlink()
        with self.assertRaises(FileExistsError):
            builder.extract(dest, self.root)
        self.assertEqual("Keep my question", note.read_text())
        self.assertFalse((dest / "Academy/ONBOARDING.md").exists())

    def test_cannot_extract_inside_source(self):
        with self.assertRaises(ValueError):
            builder.extract(self.root / "rehearsal", self.root)

    def test_committed_session_1_zip_matches_a_fresh_build(self):
        builder.build(self.root)
        for name in (builder.ARCHIVE, "manifest.json"):
            self.assertEqual((ROOT / "dist" / name).read_bytes(), (self.root / "dist" / name).read_bytes())

    def add_draft(self, name="09-Draft/notes.md"):
        """Add a draft file and its index entry, so the tests don't depend on real drafts."""
        path = self.root / "packet/Academy/Course" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("Draft\n")
        index_path = self.root / "packet/Academy/Course/release-index.json"
        index = json.loads(index_path.read_text())
        index["files"].append(
            {"path": name, "session": 9, "type": "practice-guide", "version": 1, "updated": "2026-11-13", "status": "draft"}
        )
        index_path.write_bytes(builder.index_json(index))

    def test_draft_files_stay_out_of_session_1_zip(self):
        self.add_draft()
        builder.build(self.root)
        with zipfile.ZipFile(self.root / "dist" / builder.ARCHIVE) as archive:
            names = archive.namelist()
            index = json.loads(archive.read("Academy/Course/release-index.json"))
        self.assertEqual(11, len(names))
        self.assertFalse([name for name in names if "09-Draft" in name])
        self.assertNotIn("draft", {item["status"] for item in index["files"]})
        for name in (builder.ARCHIVE, "manifest.json"):
            self.assertEqual((ROOT / "dist" / name).read_bytes(), (self.root / "dist" / name).read_bytes())

    def test_unrecorded_session_file_blocks_packaging(self):
        path = self.root / "packet/Academy/Course/09-Draft/recap.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("Not in the index")
        with self.assertRaises(ValueError):
            builder.build(self.root)

    def test_session_1_file_cannot_be_marked_draft(self):
        path = self.root / "packet/Academy/Course/release-index.json"
        index = json.loads(path.read_text())
        index["files"][0]["status"] = "draft"
        path.write_bytes(builder.index_json(index))
        with self.assertRaises(ValueError):
            builder.build(self.root)

    def test_stale_archive_is_detected(self):
        builder.build(self.root)
        path = self.root / "packet/Academy/Course/Cohort.md"
        path.write_text(path.read_text() + "\nChanged schedule\n")
        with self.assertRaises(ValueError):
            builder.check(self.root)


if __name__ == "__main__":
    unittest.main()
