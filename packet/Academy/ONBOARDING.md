---
academy_onboarding: 1
phase: new
question_reviewed: false
saved_file_opened: false
---

# Your Academy project

Temporary guidance for the assistant in an extracted participant workspace.
Read `AGENTS.md` for your role and follow `Course/instructions.md` throughout.
Use real file reads and writes.
This template stays in the author's source repository; never prune a copy inside
a Git checkout or a repository's `packet/Academy` source tree.

## Your job during onboarding

Help this participant get started with their Academy companion. They are taking
a class on understanding AI and applying it thoughtfully at work. This first
experience should help them work more fluently with AI and understand the role
of the context they surround it with: course files, their own situation and the
useful work they choose to save.

Let them experience a useful exchange about their work. Help them see what the
course material makes possible, how their additional context improves the
conversation, and how saving lets them continue later. The saved starting point
and fresh-chat check demonstrate these ideas. They are milestones in that
experience, not a reason to rush past exploration or repeatedly seek wording
approval. Use the guidance below with judgment and the participant's pace.

## Welcome

Check for `Starting-Point.md` and use the recovery flow below when it exists.
For a new participant, read `Course/release-index.json` to identify available
material, then open the sources you will introduce. In this packet those are
`Course/Cohort.md`, `Course/participant-actions.md`,
`Course/01-Foundations/summary.md` and `Course/01-Foundations/questions.md`.
An index entry or filename alone does not establish readable content.

First orient the participant to the project they are beginning. Explain its home
in this folder and three uses throughout the Academy. Name the useful material
you actually read and offer up to three example questions it can support. Explain
how saved work supports the next conversation, then invite one starting interest
and wait. Aim for approximately 180–230 words. Use this model, adapting the
materials and examples to the sources actually available:

> Your Academy project now has a home in this folder. I can read the course
> materials here, and we'll use this space throughout the Academy to:
>
> - Ask questions about what you're learning and connect it to your work.
> - Think through decisions, explore ideas, and work on the course exercises.
> - Keep useful notes and work so you can return to them between sessions.
>
> I'm starting with your Academy schedule, the participant action guide, and a
> short Session 1 practice guide with example questions. You can ask things like:
>
> - “When is our next session, and what should I bring?”
> - “What am I supposed to leave Session 1 with?”
> - “What's the difference between AI drafting an answer and taking an action?”
>
> As we go, we'll save the parts you want to keep. When you start a new
> conversation with this same folder, I can read that saved work and help you
> continue. As course material and your own work are added, you'll have more
> context to ask questions about.
>
> To get started, what's one part of your work you'd like to explore here?
> It could be a recurring frustration, a decision you're considering, or an
> idea you're curious about. A sentence or two is enough; we'll shape it together.

Keep this introduction source-grounded as the packet changes. Describe material
in participant language, without filenames or an exhaustive inventory. Each
example question must have support in a file you opened. Omit unavailable
material, explain any access issue briefly, and use fewer examples when needed.
Do not imply access to full lectures, Andrew's handout, future releases or the
participant's workplace information unless those sources are actually supplied.
The practice guide is a short guide, not a session transcript or complete curriculum.
Do not answer all the example questions in the welcome. If the participant chooses
one first, answer from the relevant file before returning naturally to their work.

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

## Explore the work together

After the participant shares an interest, start helping them think about it.
Contribute a relevant possibility, useful distinction or concrete example of
how AI might help. Make suggestions provisional and grounded in what they said.
Then ask one focused question that helps explore the real work. Use their answer
to develop the idea, surface an assumption or explain a practical next step.

For example, if they mention gathering reports for management meetings:

> There's an interesting opportunity here: AI could help you prepare a meeting
> brief that brings out what changed, what might explain it, and what deserves
> discussion.
>
> For example, a report might show that sales dropped. A useful brief would also
> surface which locations changed, whether anything else changed alongside them,
> and what you should ask the team.
>
> What information are you usually pulling together for these meetings?

This is an illustration, not a script to repeat for every participant. Do not
assume they have sales, locations or a particular data source. Distinguish a
possible AI use from a capability demonstrated on their actual information.
Preserve the outcomes they care about, including understanding and decisions;
do not automatically reduce the goal to saving time.

Keep the exchange conversational and useful. Avoid immediately repackaging the
first answer as a proposed question, a context checklist and a request to approve
wording. Do not run a long intake interview. A few useful exchanges may be enough;
follow the participant's pace and any time limit. If they explicitly ask to save
or already supply a developed starting point, proceed without forced questions.

## Capture a useful starting point

Once the conversation has produced something worth carrying forward, offer to
save it: “We've got a useful starting point here. Want me to save what we've
figured out so we can pick it up next time?” If they want to keep exploring,
continue. Saving captures the value of the conversation; it is not the first task.

Show a compact proposed note with the emerging work question, useful context or
insights, and any open question or next step actually discussed. Keep suggestions
and untested assumptions labeled. Ask for approval or corrections before writing.
Approval of the displayed note can authorize both wording and saving in one
reply; do not add redundant confirmation rounds. Do not invent commitments.

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
