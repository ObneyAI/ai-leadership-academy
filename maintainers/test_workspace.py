"""Checks for the participant folder that GitHub zips from this repository.

Standard library and Git only. Run: python3 -m unittest discover -s maintainers -v
"""

import io
import json
from pathlib import Path
import subprocess
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
INDEX = "Course/release-index.json"
ENTRY = ("ACADEMY.md", "AGENTS.md", "ONBOARDING.md")
REPO = "ObneyAI/ai-leadership-academy"
RAW = f"https://raw.githubusercontent.com/{REPO}/main/"
PARTICIPANT = ("Starting-Point.md", "Session-Notes/", "Session-Notes.md", "Builds/", "AI Opportunities/", "Notes/", "Personal/")


def git(*args):
    return subprocess.run(("git", "-C", str(ROOT)) + args, check=True, capture_output=True).stdout


def tracked():
    return [name for name in git("ls-files", "-z").decode().split("\0") if name]


def exported():
    """Tracked files that GitHub's ZIP will contain: none marked export-ignore, nor inside a folder that is."""
    names = tracked()
    prefixes = {"/".join(name.split("/")[:n]) for name in names for n in range(1, name.count("/") + 2)}
    out = subprocess.run(
        ("git", "-C", str(ROOT), "check-attr", "--stdin", "-z", "export-ignore"),
        input="\0".join(sorted(prefixes)).encode(), check=True, capture_output=True,
    ).stdout.decode().split("\0")
    ignored = {out[i] for i in range(0, len(out) - 2, 3) if out[i + 2] == "set"}
    return {
        name for name in names
        if not any("/".join(name.split("/")[:n]) in ignored for n in range(1, name.count("/") + 2))
    }


def index():
    return json.loads((ROOT / INDEX).read_text())


def expected():
    return set(ENTRY) | {INDEX} | {"Course/" + item["path"] for item in index()["files"]}


class WorkspaceTests(unittest.TestCase):
    def test_zip_holds_exactly_the_participant_folder(self):
        self.assertEqual(expected(), exported())

    def test_every_course_file_is_indexed_once(self):
        paths = [item["path"] for item in index()["files"]]
        self.assertEqual(len(paths), len(set(paths)))
        for path in paths:
            self.assertTrue((ROOT / "Course" / path).is_file(), path)

    def test_index_uses_the_standard_layout(self):
        raw = (ROOT / INDEX).read_bytes()
        self.assertEqual((json.dumps(index(), indent=2, ensure_ascii=False) + "\n").encode(), raw)

    def test_update_addresses_match_the_repository_layout(self):
        source = index()["source"]
        self.assertEqual("main", source["branch"])
        self.assertEqual(RAW + "Course/", source["files"])
        self.assertEqual(RAW + INDEX, source["index"])
        self.assertEqual(f"https://github.com/{REPO}/archive/refs/heads/main.zip", source["archive"])
        instructions = (ROOT / "Course/instructions.md").read_text()
        for address in (source["index"], source["files"], source["archive"]):
            self.assertIn(address, instructions)

    def test_onboarding_is_unused(self):
        header = (ROOT / "ONBOARDING.md").read_text().split("---", 2)[1].splitlines()
        for field in ("phase: new", "note_reviewed: false", "saved_file_opened: false"):
            self.assertIn(field, header)
        entry = (ROOT / "ACADEMY.md").read_text()
        for marker in ("<!-- academy-onboarding:start -->", "<!-- academy-onboarding:end -->"):
            self.assertEqual(1, entry.count(marker))

    def test_no_participant_work_or_symlinks_are_tracked(self):
        for name in tracked():
            self.assertFalse(name.startswith(PARTICIPANT), name)
            self.assertFalse((ROOT / name).is_symlink(), name)

    def test_source_checkout_is_marked_for_assistants(self):
        self.assertIn("maintainers/", (ROOT / "AGENTS.md").read_text())
        self.assertIn("maintainers/", (ROOT / "ONBOARDING.md").read_text())
        self.assertNotIn("maintainers/README.md", exported())

    def test_main_carries_no_drafts(self):
        if git("rev-parse", "--abbrev-ref", "HEAD").decode().strip() != "main":
            self.skipTest("drafts are allowed on branches other than main")
        self.assertNotIn("draft", {item["status"] for item in index()["files"]})

    def test_git_archive_of_the_last_commit_matches(self):
        """Build the ZIP as GitHub does and compare it with the working tree."""
        if git("status", "--porcelain").strip():
            self.skipTest("commit first: the archive is built from the last commit")
        data = git("archive", "--format=zip", "--prefix=ai-leadership-academy-main/", "HEAD")
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            self.assertIsNone(archive.testzip())
            names = {n.split("/", 1)[1] for n in archive.namelist() if not n.endswith("/")}
            self.assertEqual(expected(), names)
            for name in names:
                self.assertEqual((ROOT / name).read_bytes(), archive.read("ai-leadership-academy-main/" + name))


if __name__ == "__main__":
    unittest.main()
