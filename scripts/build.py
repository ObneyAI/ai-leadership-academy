#!/usr/bin/env python3
"""Build a participant packet from the single source tree; standard library only."""

import argparse
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
FILES = (
    "ACADEMY.md",
    "AGENTS.md",
    "ONBOARDING.md",
    "Course/Cohort.md",
    "Course/instructions.md",
    "Course/commands.md",
    "Course/examples.md",
    "Course/participant-actions.md",
    "Course/release-index.json",
    "Course/01-Foundations/summary.md",
    "Course/01-Foundations/questions.md",
)
ARCHIVE = "Academy-Session-1.zip"
INDEX = "Course/release-index.json"


def index_json(index):
    return (json.dumps(index, indent=2, ensure_ascii=False) + "\n").encode()


def payload(root=ROOT):
    """Return the Session 1 files. Files the index marks "draft" stay in source only."""
    source = root / "packet" / "Academy"
    found = set()
    for path in source.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"Source must not contain symlinks: {path}")
        if path.is_file() and path.name != ".DS_Store":
            found.add(path.relative_to(source).as_posix())
    raw_index = (source / INDEX).read_bytes()
    full_index = json.loads(raw_index)
    if index_json(full_index) != raw_index:
        raise ValueError("Release index must use the builder's JSON layout")
    drafts = {"Course/" + item["path"] for item in full_index["files"] if item["status"] == "draft"}
    if drafts & set(FILES):
        raise ValueError(f"A Session 1 file cannot be a draft: {drafts & set(FILES)}")
    if found != set(FILES) | drafts:
        raise ValueError(f"Unexpected or missing source files: {found ^ (set(FILES) | drafts)}")
    data = {f"Academy/{name}": (source / name).read_bytes() for name in FILES}
    released = dict(full_index, files=[item for item in full_index["files"] if item["status"] != "draft"])
    data[f"Academy/{INDEX}"] = index_json(released)
    guide = data["Academy/ONBOARDING.md"].decode()
    header = guide.split("---", 2)[1]
    for field in ("phase: new", "note_reviewed: false", "saved_file_opened: false"):
        if field not in header.splitlines():
            raise ValueError("Onboarding source contains participant progress")
    entry = data["Academy/ACADEMY.md"].decode()
    for marker in ("<!-- academy-onboarding:start -->", "<!-- academy-onboarding:end -->"):
        if entry.count(marker) != 1:
            raise ValueError("Entry must contain exactly one onboarding section")
    index = json.loads(data["Academy/Course/release-index.json"])
    for item in index["files"]:
        if "Academy/Course/" + item["path"] not in data:
            raise ValueError("Release index references a file outside the packet")
    return data


def manifest(data):
    return {
        "version": "0.1.3",
        "status": "draft-rehearsal",
        "archive": ARCHIVE,
        "files": {name: hashlib.sha256(content).hexdigest() for name, content in sorted(data.items())},
    }


def build(root=ROOT):
    data = payload(root)
    output = root / "dist"
    output.mkdir(exist_ok=True)
    with zipfile.ZipFile(output / ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, content in sorted(data.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 11, 3, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
    (output / "manifest.json").write_text(json.dumps(manifest(data), indent=2) + "\n")
    check(root)


def check(root=ROOT):
    data = payload(root)
    output = root / "dist"
    actual = json.loads((output / "manifest.json").read_text())
    if actual != manifest(data):
        raise ValueError("Manifest is stale; rebuild")
    with zipfile.ZipFile(output / ARCHIVE) as archive:
        if archive.testzip() or sorted(archive.namelist()) != sorted(data):
            raise ValueError("Archive is corrupt or contains unexpected entries")
        if any(archive.read(name) != content for name, content in data.items()):
            raise ValueError("Archive differs from source; rebuild")


def extract(destination, root=ROOT):
    """Create only a new folder. Never overlay or reset an existing learner folder."""
    data = payload(root)
    destination = Path(destination).resolve()
    if destination == root.resolve() or root.resolve() in destination.parents:
        raise ValueError("Rehearse outside the source repository")
    destination.mkdir(parents=True, exist_ok=False)
    for name, content in data.items():
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify existing generated files")
    parser.add_argument("--extract-to", type=Path, help="Create a new rehearsal directory")
    args = parser.parse_args()
    if args.check:
        check()
    else:
        build()
    if args.extract_to:
        extract(args.extract_to)
    print(f"Verified: {len(FILES)} source files, ZIP contents and SHA-256 manifest.")
