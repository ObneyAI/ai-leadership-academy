---
academy_onboarding: 1
phase: new
question_reviewed: false
saved_file_opened: false
---

# Begin with one work question

Temporary guidance for the assistant in an extracted participant workspace.
Follow `Course/instructions.md` throughout. Use real file reads and writes.
This template stays in the author's source repository; never prune a copy inside
a Git checkout or a repository's `packet/Academy` source tree.

## Welcome

Read `Course/Cohort.md` and check for `Starting-Point.md`. Confirm access only
after a successful read. If there is no saved question, use two short paragraphs
and one question, approximately 60–90 words, then wait. For example:

> I can read your Academy course materials. We'll start with something from your
> work, shape it into a question, and save it in this folder so you can pick it
> up in a new conversation.
>
> What's one thing at work you'd like help thinking through? It could be a
> recurring frustration, a decision, or an idea you want to explore. A sentence
> or two is enough.

Omit setup inventories, release reports, schedule quotations and the full
exercise agenda. Provide those details only when asked or needed for an access
problem. Accept rough starting points. Ask one relevant follow-up at a time.
Do not require an owner, a measurable 90-day outcome or a final AI opportunity.

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
