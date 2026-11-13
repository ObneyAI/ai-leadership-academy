# Publication status

Keep source availability, public release and classroom readiness distinct.

## Source and download

`ObneyAI/ai-leadership-academy` is intended to be a public repository. On
November 13 it was still private; these changes prepare it for the switch.

`main` is the release, and the repository root is the participant folder.
Participants set up from the ZIP that GitHub builds from `main`:
<https://github.com/ObneyAI/ai-leadership-academy/archive/refs/heads/main.zip>. Maintainer files are left out of that ZIP. No Git is needed.

Until the repository is public, that address and the update addresses return
nothing. The [Session 1 setup page](https://links.obney.ai/c2-setup) still
serves the earlier v0.1.2 ZIP, which unzips to a folder named `Academy`. The
setup page needs its link and its folder wording changed when the repository
goes public.

## Course update route

`Course/instructions.md` names this repository's `main` branch as the only
verified release, with web addresses for the release index and course files.
`/la start` checks it. `Course/release-index.json` records the same addresses
under `source`. The manual route is to download the ZIP again and copy only
`Course/`.

- **Not rehearsed.** No assistant has fetched an update on a participant
  account, and the GitHub ZIP has not been downloaded on one. See
  [VERIFICATION.md](VERIFICATION.md).
- **Folders from the v0.1.2 ZIP don't know the address.** Participants who set
  up on November 13 need it given to them once, for example on a Session 2
  slide. After that first update their folder carries it.

## Included material

The folder contains the published cohort schedule, participant actions, and a
practice guide and questions for Session 1. The practice guide is not a faculty
handout or a recap of a delivered session. The course index retains rehearsal
status. The A–E practice scenarios are fictional examples inspired by broad
first-cohort work themes. They carry no participant names, distinctive
disclosures, quotations or outcome claims. No participant data is included.

Andrew Schwarz's Session 1 material is in `Course/01-Foundations/`, added
November 13 at Justin's direction:

- `andrew-schwarz-slides.pdf`: the 126-slide deck as a PDF, without speaker
  notes. The participant survey quotes on slides 102–106 are replaced with
  "Participant examples were shared in the room." Slides 75–82 keep the
  cohort's aggregate pre-assessment figures as presented. Text sizes on slides
  14, 38, 41, 57, 80 and 115 were adjusted so nothing overlaps or disappears in
  the PDF. Built with LibreOffice using Carlito and Caladea, the
  metric-compatible stand-ins for Calibri and Cambria.
- `andrew-schwarz-prompts.pdf` and `andrew-schwarz-prompts.md`: his "Prompts
  for Your Company" handout, printable and assistant-readable.

Participant recordings and participant surveys are excluded. Other faculty
material goes in this repository only with the owner's agreement to public
release; anything else keeps a separate route.

## Drafts

The Session 2 draft and the Session 3 illustration are on the
`draft/sessions-2-3` branch, with release-index status `draft`.

## Remaining classroom checks

- Download and unzip the GitHub ZIP on a participant account, without Git.
- Complete the Cowork and ChatGPT Work save/recovery/cleanup rehearsals and
  document any manual steps. Confirm required account access and classroom timing.
- Rehearse the `/la` commands before introducing them in Session 2.
- Rehearse a course update on each offered assistant, and the manual route.
- Review and release later-session material separately. Course updates must
  preserve participant work and must not reinstall onboarding into a completed
  workspace.
