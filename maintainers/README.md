# Maintaining the Academy workspace

This repository is the AI Leadership Academy Cohort 2 participant folder. It is
public. The repository root **is** the folder a participant gives their
assistant, so root files are participant-facing.

## How participants get it

- **Set up:** they download the ZIP that GitHub builds from `main`
  (<https://github.com/ObneyAI/2026-academy-memory/archive/refs/heads/main.zip>), unzip it and select the folder. No Git is needed. The setup page
  links to that address.
- **Updates:** their assistant reads `Course/release-index.json` on `main` and
  fetches new or changed files from `Course/`, as `Course/instructions.md`
  describes. The manual route is to download the ZIP again and copy only
  `Course/` across.

So a push to `main` publishes: new downloads get it at once, and existing
folders get the `Course/` part at their next update check.

## What is in the ZIP

`.gitattributes` marks `maintainers/`, the root `README.md`, `.gitattributes`
and `.gitignore` as `export-ignore`. GitHub leaves those out of the ZIP. The
ZIP holds only:

| File | Purpose |
|---|---|
| `ACADEMY.md` | Entry point that becomes a short working guide |
| `AGENTS.md` | Lasting companion role: AI fluency, context and learning through work |
| `ONBOARDING.md` | Temporary welcome, save, recovery and cleanup steps |
| `Course/instructions.md` | Lasting assistant behavior, including course updates |
| `Course/commands.md` | The `/la start`, `/la save` and `/la wrap` routines |
| `Course/examples.md` | Five fictional A–E examples |
| `Course/release-index.json` | Every course file, its version and the update addresses |
| `Course/…` | Schedule, participant actions and session material |

GitHub names the unzipped folder `2026-academy-memory-main`. Participants can
rename it.

## Working in this checkout

The root `AGENTS.md` and `ONBOARDING.md` are written for a participant's
assistant. An assistant opened here must not run onboarding, save participant
work or prune `ONBOARDING.md`; the root `AGENTS.md` says so when it sees this
folder. Disappearing onboarding applies only to a participant's copy.

- Commit nothing private: no participant data, restricted recordings,
  credentials, or faculty material without the owner's agreement to public
  release.
- Keep rehearsal records, screenshots and feedback on drafts outside this
  repository.
- Never edit a rehearsal copy as source.

## Releases and drafts

`main` is the release. Draft later-session material on a branch; the Session 2
draft and the Session 3 illustration are on `draft/sessions-2-3`. A draft on a
branch is publicly readable, but participants' assistants read only `main`.

Every file under `Course/` needs an entry in `Course/release-index.json`. To
release a file, raise its `version`, set its `updated` date and merge to
`main`. A correction is a new version. An entry with `"status": "draft"` must
not reach `main`; assistants skip such entries, and the checks reject them on
`main`.

Only `Course/` reaches existing folders. A change to `ACADEMY.md`, `AGENTS.md`
or `ONBOARDING.md` reaches new downloads only.

## Checks

With Python 3 and Git installed:

```sh
python3 -m unittest discover -s maintainers -v
```

The checks cover what the ZIP will contain, the release index, a clean
onboarding state and the update addresses. They do not show that an assistant
follows the instructions; see [VERIFICATION.md](VERIFICATION.md). Release
status is in [PUBLICATION.md](PUBLICATION.md).

To make a rehearsal copy the way GitHub will, outside this checkout:

```sh
git archive --format=zip --prefix=2026-academy-memory-main/ -o ../academy-rehearsal.zip HEAD
```

## Relationship to AI Memory Folder

Inspired by [ObneyAI/ai-memory-folder](https://github.com/ObneyAI/ai-memory-folder),
which describes temporary setup that becomes lasting personal context. This is
a separately authored Academy workspace with its own repository and history.
There is no runtime dependency, submodule or automatic sync with that kit, and
it does not collect a personal profile.
