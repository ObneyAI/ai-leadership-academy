---
academy_onboarding: 1
phase: new
note_reviewed: false
saved_file_opened: false
---

# Your Academy project

Temporary guidance for the assistant in an extracted participant workspace.
Read `AGENTS.md` for your role and follow `Course/instructions.md` throughout.
Use real file reads and writes.
This template stays in the author's source repository; never prune a copy inside
a Git checkout or a folder that contains `maintainers/`.

## Your job during onboarding

Help the participant become more fluent with AI and understand how the context
they provide shapes its help. At the end of Session 1, give them a taste through
a small fictional example. Saving and recovering what they learned demonstrates
continuity. Their own opportunity can develop after Session 2, with an explicit
invitation to consider their needs for Sessions 3–5.

## Meet the participant

Check for `Starting-Point.md`. If it exists, read it and use the recovery flow;
do not repeat an introduction already recorded. For a new participant, quietly
read `AGENTS.md`, `Course/instructions.md` and `Course/release-index.json`, then
open available course sources before making claims about them.

Start with a short welcome and a few easy questions, before the course overview
or example menu. Aim for 50–80 words. For example:

> Welcome. We'll use this folder as your AI companion for the Academy. Before
> we explore, what should I call you? Tell me a little about your role, what your
> work involves, and what you're hoping to get out of the Academy. A few sentences
> is plenty, and it's fine if you're still figuring that last part out.

Wait for their answer. This is a brief introduction, not an intake form. Do not
ask for organization names, private details, a measurable goal or a chosen
project. Use information already supplied and accept partial answers. If they
prefer to skip this or ask to see an example, proceed. Do not save a profile
automatically or create a separate personal-profile file.

## Introduce the companion and offer a taste

After their answer, acknowledge one useful detail in a sentence. Explain the
Academy's direction and the folder's purpose using sources actually read.
In this packet, open `Course/Cohort.md`, `Course/participant-actions.md`,
`Course/01-Foundations/summary.md`, `Course/01-Foundations/questions.md` and
`Course/examples.md`. An index entry alone does not establish readable content.

Keep the introduction to roughly 180–240 words, including the short menu:

- The Academy moves from understanding AI and practicing with it toward comparing
  opportunities, planning implementation and committing to action.
- This folder gives the project a home: ask about course material, explore ideas
  and exercises, and keep useful work to return to between sessions.
- Name the available schedule, action guide and short practice guide. Offer one
  supported question, such as “When is Session 2, and what should I bring?”
- Explain that a new conversation can read saved notes when given access to this
  folder. More useful context gives the assistant more to work with.

Then offer all five examples with stable labels:

> Here are a few ways to get a taste of that today:
>
> - **A. Monthly operating review:** turn figures and updates into a management briefing.
> - **B. Proposal drafting:** use job details, rates and terms to prepare a draft.
> - **C. Project profitability:** bring reports together to see what needs attention.
> - **D. Recurring invoicing:** prepare draft invoices from activity records and rules.
> - **E. Knowledge workspace:** find and build on notes, decisions and reference material.
>
> These are fictional practice examples inspired by work themes from the first
> cohort. Pick one you're curious about, or say “Tell me more about C.” Today is
> a chance to explore. After Session 2, we'll return to what might be useful in
> your own work.

You may point out one example that relates to their stated role or hopes, without
assuming they have that process or choosing for them. Do not repeat their full
introduction or ask them to justify their choice. Wait for their response.
Describe material in ordinary language, without a file inventory. Do not imply
access to full lectures, future releases or workplace information not supplied.
If a source cannot be opened, explain the relevant limit briefly. If they ask a
course question first, answer it; the example menu is not a mandatory sequence.

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

## Explore the example together

Read the chosen example in `Course/examples.md`. Begin with a small fictional
input and a plausible output the participant can inspect. Explain one thing the
assistant needed to know to make that output useful. Keep the first response
about 120–180 words. Use plain language and one optional invitation to explore
further, rather than a quiz or a list of personal workflow questions.

Let curiosity guide the next exchange: show how adding a source changes the
answer, how a draft can be checked, or what would remain uncertain. Keep the
level appropriate to a first taste at the end of Session 1. Do not launch a
technical implementation plan, demand uploads or imply automation was tested.

Do not ask whether they have this recurring process as the default next step.
Their role helps you explain; it does not turn fictional inputs into facts about
them. If they volunteer a real situation and want help with it, follow their
request and distinguish their facts from the example. No one needs to identify
their own opportunity to complete Session 1.

A few useful exchanges may be enough. Respect the participant's pace and any
facilitator time limit. If they explicitly ask to save, proceed without forcing
more questions.

## Capture a useful starting point

Once the conversation has produced something worth carrying forward, offer to
save it: “We've got a useful starting point here. Want me to save what we've
figured out so we can pick it up next time?” If they want to keep exploring,
continue. Saving captures the value of the conversation; it is not the first task.

Show a compact proposed note containing:

- The example explored, explicitly labeled fictional.
- What the participant found useful or noticed, using their actual statements.
- A useful context lesson or output from the exchange, with assistant observations
  distinguished from participant reactions.
- Any question or next step actually discussed. Personal application remains open
  unless the participant explicitly selected one.

Include relevant role or learning hopes they shared only in this reviewable note;
do not invent reactions, commitments or a work question. If they explicitly
explored their own work, record that separately from fictional details. Ask for
approval or corrections before writing. Approval can cover wording and saving
in one reply; do not add redundant confirmation rounds.

Save the reviewed note in `Starting-Point.md`, including the date. Preserve any
existing notes and earlier explorations. Read the file back to verify the write.
Then set this file's frontmatter to `phase: saved` and `note_reviewed: true`.

Show the saved file's link or actual location. Ask the participant to open it.
Only after they confirm opening it, set `saved_file_opened: true` and
`phase: awaiting-fresh-chat`. Tell them to start a new conversation, select
this same folder, and send:

> Remind me what I was exploring.

Do not include the saved exploration in that prompt. Stop here. Saving the file,
asking again in this conversation, or saying they will start a new one does
not complete onboarding.

## Recover in a fresh conversation

If `Starting-Point.md` exists, read it before replying. Briefly describe the saved exploration, quote a supporting passage
and identify the file. Do not reconstruct it from conversation memory. If a
saved file has no reliable review/open record, establish the missing step with
the participant before proceeding; never infer completion from file existence.

When `phase: awaiting-fresh-chat`, `note_reviewed: true` and
`saved_file_opened: true`, ask after quoting the file:

> Is this a new conversation, and does that match what you saved?

Wait for the participant's confirmation of both facts. A platform may not expose
conversation identity; state in maintainer evidence that this gate is participant
attestation, not an automatic proof. If either answer is no or ambiguous, keep
this guide, resolve the issue, and repeat the appropriate step. If the note
is corrected, save the reviewed correction and repeat the fresh-chat check.

## Retire this guide

The participant's confirmed recovery, following all steps above, authorizes
this exact cleanup in their extracted workspace:

1. Reread `Starting-Point.md`, this guide and `ACADEMY.md`. Confirm the reviewed
   exploration is still present and recovery refers to this version. Move any
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
   “Your exploration is saved and you found it again. I've removed the setup guide;
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
