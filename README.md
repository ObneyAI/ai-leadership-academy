# Academy Memory · Cohort 2

A course workspace for the November–December 2026 AI Leadership Academy.
Participants use their own approved assistant to explore examples and real work,
understand how context shapes its help, inspect useful outputs, and carry
reviewed work across conversations.

**Version 0.1.1 is a rehearsal draft.** Package integrity is checked; the complete
Cowork and ChatGPT Work learner journeys still need rehearsal. This repository
is the single authoring home. Extracted folders are practice copies.

## Try the packet

Use the [Session 1 ZIP](dist/Academy-Session-1.zip) in a new location.
Unzip it and select the resulting **Academy** folder in your approved assistant.
Then say:

> Read ACADEMY.md and help me get started.

The assistant first asks briefly about your role, work and hopes for the Academy.
It then introduces the course and folder, with five fictional practice examples
inspired by first-cohort work themes. Say “Tell me more about C” to explore
project profitability. Your choice is an opportunity to learn; it does not
choose your personal project.

At the end of Session 1, explore a small illustration, see how context affects
the help, and save useful learning when ready. Open the saved file. Start a new
conversation with the same folder and say:

> Read ACADEMY.md and remind me what I was exploring.

After you confirm that the new conversation recovered the correct saved work,
the assistant removes the temporary setup guide and its entry-point section.
Your exploration, context and course materials remain. An assistant without
file write/delete access guides manual steps and reports the limitation.

Session 2 adds hands-on practice. After Session 2, an explicit invitation opens
exploration of your own needs for Sessions 3–5. Completing onboarding does not
automatically choose or start a personal project.

## The folder changes as you use it

Only the participant's extracted copy completes and prunes onboarding.

```text
At the start                         After confirmed recovery
Academy/                             Academy/
  ACADEMY.md                           ACADEMY.md
  AGENTS.md                            AGENTS.md
  ONBOARDING.md                        Starting-Point.md
  Course/                              Course/
```

The source template retains `ONBOARDING.md` for the next participant. The
completion gate is described in [the onboarding source](packet/Academy/ONBOARDING.md).
Fresh-chat identity is confirmed by the participant; a language model's claim
alone does not prove it. Age of the folder never triggers deletion.

## Edit and build

All participant-facing source lives in [packet/Academy](packet/Academy).

| Source | Purpose |
|---|---|
| `packet/Academy/ACADEMY.md` | Entry point that becomes a short working guide |
| `packet/Academy/AGENTS.md` | Lasting companion role: AI fluency, context and learning through work |
| `packet/Academy/ONBOARDING.md` | Temporary welcome, save, recovery and cleanup steps |
| `packet/Academy/Course/instructions.md` | Lasting assistant behavior |
| `packet/Academy/Course/examples.md` | Five fictional A–E examples with small illustrations and context lessons |
| `packet/Academy/Course/` | Course schedule, actions and Session 1 practice material |
| `scripts/build.py` | Reproducible ZIP, hash manifest and new rehearsal extraction |
| `docs/VERIFICATION.md` | Tested boundaries and remaining classroom checks |
| `docs/PUBLICATION.md` | Initial GitHub scope and public-release work |

With Python 3 installed:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/build.py
python3 scripts/build.py --check
python3 scripts/build.py --extract-to ../academy-c2-rehearsal/v0.1.1
```

The extraction destination must not exist. Do not edit generated ZIPs or practice
copies as source. Do not use the starter ZIP as an update over an existing
participant folder; update course material separately and preserve saved work.
Commit source changes and rebuilt `dist/` together. The builder packages exactly
ten allowed files and rejects participant notes or recorded onboarding progress.

`ACADEMY.md` explicitly routes the assistant to the participant's `AGENTS.md`.
No automatic loading of that filename is assumed in either app. The repository's
own root `AGENTS.md` is maintainer guidance and is not included in the packet.

## Relationship to AI Memory Folder

Inspired by [ObneyAI/ai-memory-folder](https://github.com/ObneyAI/ai-memory-folder),
which already describes temporary setup that becomes lasting personal context.
This is a separately authored Academy packet with its own repository and history.
There is no runtime dependency, submodule or automatic sync with that kit.

| AI Memory Folder | Academy Memory |
|---|---|
| General personal assistant kit | Cohort-specific learning workspace |
| Personal setup interview and About Me note | Reviewed exploration notes, later personal needs, and course context |
| Claude, ChatGPT and Grok Bot kit variants | One folder packet; Cowork and ChatGPT Work are the initial rehearsal routes |
| General note-growth guidance | Course continuity with a save/recover completion gate |

This packet does not install the general kit, collect a personal profile, or
modify its repository. Course materials and participant notes have different
owners: the participant controls sharing, and saving never submits to faculty.
