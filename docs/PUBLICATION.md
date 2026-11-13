# Publication status

Keep source availability, public release and classroom readiness distinct.

## Source and download

`ObneyAI/2026-academy-memory` is intended to be a public repository. On
November 13 it was still private; these changes prepare it for the switch. It
contains the editable packet, maintainer documentation, builder, tests and
generated ZIP. The source remains independent of `ai-memory-folder`.

`main` is the release. Drafts stay on branches. Earlier commits on `main` still
show the Session 2 draft and Session 3 illustration that were drafted there
before the move; that history was reviewed on November 13 and holds no secrets,
participant data or local paths.

The v0.1.2 ZIP is publicly available through the approved
[Session 1 setup page](https://obney-academy-c2-s1.pages.dev/setup).
On November 4, the hosted ZIP matched the source archive byte for byte.
Source is now v0.1.3, which adds the course update route. The hosted ZIP is
still v0.1.2 and no longer matches `dist/` until it is redeployed.

## Course update route

From v0.1.3, `Course/instructions.md` names this repository's `main` branch as
the only verified release, with web addresses for the release index and course
files. `/la start` checks it. `Course/release-index.json` records the same
addresses under `source`.

- **Not rehearsed.** No assistant has fetched an update on a participant
  account. See `docs/VERIFICATION.md`.
- **Folders from the v0.1.2 ZIP don't know the address.** Participants who set
  up on November 13 need it given to them once, for example on a Session 2
  slide. After that first update their folder carries it.
- **The addresses work only after the repository is public.**
- **The builder accepts only the eleven Session 1 files plus drafts.** Releasing
  `02-Applications/` on `main` needs a decision first: whether the starter ZIP
  grows, or stays at Session 1 and later material arrives only by update.

## Included material

The packet contains the published cohort schedule, participant action wording
revised to reflect Justin’s November 3 teaching direction, and a practice guide/questions for Justin's Session 1 block.
The practice guide is not Andrew's handout or a recap of a delivered session.
The course index retains rehearsal status. The A–E practice scenarios are fictional
examples inspired by broad first-cohort work themes. They carry no participant
names, distinctive disclosures, quotations or outcome claims. No participant
data is included.

## Drafts

The Session 2 draft and the Session 3 illustration are on the
`draft/sessions-2-3` branch, with release-index status `draft`. A draft on a
branch of a public repository is readable by anyone, but participants'
assistants read only `main`.

## Remaining classroom checks

- Complete the Cowork and ChatGPT Work save/recovery/cleanup rehearsals and
  document any manual steps. Confirm required account access and classroom timing.
- Test the setup-page download and extraction on a participant account.
- Rehearse the `/la` commands before introducing them in Session 2.
- Rehearse a course update on each offered assistant, including the failure
  fallback and preservation of participant work.
- Review and release later-session material separately. Future course updates must preserve participant
  work and must not reinstall onboarding into a completed workspace.

Andrew's handout, participant introduction recordings and prior participant
surveys are excluded. Faculty material goes in this repository only with the
owner's agreement to public release; anything else keeps a separate route.
