---
academy_onboarding: 1
phase: new
question_reviewed: false
saved_file_opened: false
---

# Your Academy project

Temporary guidance for the assistant in an extracted participant workspace.
Follow `Course/instructions.md` throughout. Use real file reads and writes.
This template stays in the author's source repository; never prune a copy inside
a Git checkout or a repository's `packet/Academy` source tree.

## Welcome

Read `Course/Cohort.md` and check for `Starting-Point.md`. Confirm access only
after a successful read. If there is no saved question, first orient the
participant to the project they are beginning. Explain its home in this folder,
three uses throughout the Academy, and how saved work supports the next
conversation. Then invite one starting interest and wait. Aim for approximately
130–170 words with a short three-item list. Use this model:

> Your Academy project now has a home in this folder. I can read the course
> materials here, and we'll use this space throughout the Academy to:
>
> - Ask questions about what you're learning and connect it to your work.
> - Think through decisions, explore ideas, and work on the course exercises.
> - Keep useful notes and work so you can return to them between sessions.
>
> As we go, we'll save the parts you want to keep. When you start a new
> conversation with this same folder, I can read that saved work and help you
> continue.
>
> To get started, what's one part of your work you'd like to explore here?
> It could be a recurring frustration, a decision you're considering, or an
> idea you're curious about. A sentence or two is enough; we'll shape it together.

Here, “project” means the participant's ongoing Academy work organized around
this folder. Do not claim a platform's named Project feature was created unless
that is actually known. Avoid a tour of app terminology. Explain persistence
through saved files and renewed folder access, not automatic chat memory.

Do not lead with a file-access report or a demand to produce a work question.
Omit setup inventories, release reports, schedule quotations and the full
exercise agenda unless asked or needed for an access problem. Accept rough
starting points. Do not ask the participant to choose their biggest, costliest
or highest-priority issue. Ask one relevant follow-up at a time. Do not require
an owner, a measurable 90-day outcome or a final AI opportunity.

## Review and save

Reflect the participant's concern and propose one concise work question with
any useful context they supplied. Ask whether it captures what they mean. Wait
for approval; accept corrections. Do not invent background or commitments.

Save the approved wording in `Starting-Point.md`, including the date and useful
participant-provided context. Keep unknowns explicit. Preserve any existing
notes and earlier questions. Read the file back to verify the write. Then set
this file's frontmatter to `phase: saved` and `question_reviewed: true`.

Show the saved file's link or actual location. Ask the participant to open it.
Only after they confirm opening it, set `saved_file_opened: true` and
`phase: awaiting-fresh-chat`. Tell them to start a new conversation, select
this same folder, and send:

> Read ACADEMY.md and tell me what work question I saved.

Do not include the saved question in that prompt. Stop here. Saving the file,
asking again in this conversation, or saying they will start a new one does
not complete onboarding.

## Recover in a fresh conversation

If `Starting-Point.md` exists, read it before replying. Quote the saved question
and identify the file. Do not reconstruct it from conversation memory. If a
saved file has no reliable review/open record, establish the missing step with
the participant before proceeding; never infer completion from file existence.

When `phase: awaiting-fresh-chat`, `question_reviewed: true` and
`saved_file_opened: true`, ask after quoting the file:

> Is this a new conversation, and is that the question you saved?

Wait for the participant's confirmation of both facts. A platform may not expose
conversation identity; state in maintainer evidence that this gate is participant
attestation, not an automatic proof. If either answer is no or ambiguous, keep
this guide, resolve the issue, and repeat the appropriate step. If the question
is corrected, save the reviewed correction and repeat the fresh-chat check.

## Retire this guide

The participant's confirmed recovery, following all steps above, authorizes
this exact cleanup in their extracted workspace:

1. Reread `Starting-Point.md`, this guide and `ACADEMY.md`. Confirm the reviewed
   question is still present and recovery refers to this version. Move any
   useful participant-provided context found only in this guide into the saved
   note with their review before deleting it. Preserve all participant work.
2. Remove only the section between `<!-- academy-onboarding:start -->` and
   `<!-- academy-onboarding:end -->` in `ACADEMY.md`, including the markers.
   Keep everything outside that section, including any participant additions.
   If markers are missing, ambiguous or duplicated, preserve the file and
   explain the issue. Do not replace the whole file with a template.
3. Read the updated entry and saved note to verify they remain useful. Then
   delete only this exact file, `ONBOARDING.md`. Do not delete other files,
   folders, course material or notes. Do not use wildcard cleanup.
4. Verify the guide is gone and the saved note remains readable. Say briefly:
   “Your question is saved and you found it again. I've removed the setup guide;
   this folder is ready for your next conversation.” Only claim actions that
   actually succeeded. If cleanup fails, report the remaining step accurately.

If interrupted after removing the marked section, the durable instructions
route back here while this file exists. Reconfirm recovery before finishing;
an already-removed section is acceptable only when the lasting entry is intact.
Never restore deleted onboarding during a course update.

## Manual fallback

If the assistant cannot write or delete, give the participant the approved text
and one step at a time to save/open it and record progress in this guide. In a
fresh conversation they must supply the actual saved file again. After confirmed
recovery, they may remove the marked entry section and this file manually. Until
the participant verifies cleanup, report it as pending. Do not claim a tested
folder workflow for an attachment-only route.
