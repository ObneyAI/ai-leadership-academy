# Academy commands

These commands give each part of a session a short, predictable routine. The
participant types `/la` followed by a word. Accept the same words without the
slash (`la start`) and in any letter case, because some apps open a menu when a
message begins with "/".

## When to mention them

Session 1 doesn't use these commands, and plain-language requests always work.
Don't introduce, suggest or list the commands until the participant uses one,
asks what commands exist, or says a facilitator introduced them. From then on,
follow this file.

## Where notes go

Session notes go in `Session-Notes/` beside `Course/`, one file per day, named
by date, for example `Session-Notes/2026-11-20.md`. Start a new note with the
date and, on a session day, the session's name from `Course/Cohort.md`. Add to
an existing note for the same day; never replace it. These notes belong to the
participant, and saving never sends anything to faculty.

If you don't know today's date, ask. If you can't write files, show the text and
give a manual save step, as `Course/instructions.md` describes.

## `/la start`

For the first minutes of a session, or when the participant sits down to work.

1. If `ONBOARDING.md` exists, the Session 1 setup isn't finished. Say so in one
   line, then continue its current step instead.
2. Check `Course/Cohort.md` for today's session. Check for a course update as
   `Course/instructions.md` describes, and bring in any new released material.
   Then read `Course/release-index.json` and name any course material for that
   session. If the participant mentions material that still isn't in the
   folder, say it isn't there yet and ask them to attach it. Never invent
   course content.
3. Read `Starting-Point.md` and the most recent note in `Session-Notes/`. Recap
   in two or three sentences and name the file you read.
4. Ask one warm-up question about what they tried or noticed since then. Ask a
   second only after they answer. Use answers already given.

On a day with no session, say so and name the next session from
`Course/Cohort.md`. Offer a short check-in: at most three questions, one at a
time, skipping anything their notes already answer. Save the answers to today's
note. If they stop partway, the next `/la start` picks up where they left off. A
check-in doesn't mean they attended a session.

## `/la save <thought>`

For keeping a thought or question while someone else is teaching.

- Add the text after the command to today's note, under "Saved for later", in
  the participant's words.
- Confirm in one line and name the file. Don't answer the thought, comment on it
  or ask a follow-up: the participant is listening to someone else.
- If nothing follows the command, ask in one line what to save.

## `/la wrap`

For the last minutes of a session. `/la recap` and `/la end` do the same.

1. Find the course folder for today's session: its number matches the session's
   place in `Course/Cohort.md`, so Session 2 is `Course/02-…/`. If it has a
   `questions.md` from the facilitator, ask up to three of those questions, one
   at a time. If not, ask what stood out today, what's still uncertain, and one
   next step.
2. Keep each exchange short; it's practice that reinforces what was just taught.
   Add a useful point when it helps, then move on.
3. Write today's note: their answers, everything under "Saved for later", and
   the next step in their words. Show the note and say where it was saved; they
   can correct it.
4. Offer to take up a saved thought now, without insisting.

## `/la` on its own

Also `/la help`, or any word this file doesn't define. List the commands in four
short lines, one line each on what it's for. Nothing else.
