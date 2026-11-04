import importlib.util
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
            self.assertEqual(10, len(archive.namelist()))
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

    def test_stale_archive_is_detected(self):
        builder.build(self.root)
        path = self.root / "packet/Academy/Course/Cohort.md"
        path.write_text(path.read_text() + "\nChanged schedule\n")
        with self.assertRaises(ValueError):
            builder.check(self.root)


if __name__ == "__main__":
    unittest.main()
