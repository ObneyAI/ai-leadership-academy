# Verification

Record package checks separately from what a participant has demonstrated.

## Evidence as of November 3, 2026

- An earlier Cowork rehearsal showed folder selection, an access permission
  dialog, the folder in Context, and a completed response to the short entry
  prompt. That response reported course reads and quoted the schedule file.
- That opening was too long and asked for too much. A second screenshot showed
  a shorter opening and one invitation, but it still led with access/saving and
  added a highest-time-or-attention criterion. The current revision explains the
  folder-based Academy project, three uses, the materials actually read and
  source-supported example questions before inviting an interest. Justin approved this welcome after observing it in Cowork on November 3.
  The subsequent response jumped too quickly to wording approval; v0.1.1 adds
  exploratory thought partnership before offering to save. That behavior awaits
  rehearsal.
- No completed save, fresh-chat recovery or onboarding cleanup has been observed
  in Cowork or ChatGPT Work. Claude Code remains an optional Session 2 route.
- Automated tests cover package contents, reproducibility, stale output,
  symlinks, participant-content rejection and non-overwriting extraction.
  They do not establish that an assistant follows the natural-language protocol.

## `/la` commands, v0.1.2 (November 4)

`Course/commands.md` ships in the Session 1 ZIP but stays unused: the assistant
doesn't mention the commands until the participant uses one or says a facilitator
introduced them. Session 1 still teaches plain lines only. The aim is to teach
`/la start`, `/la save` and `/la wrap` in Session 2. None has run in Cowork or
ChatGPT Work. Check there that a message starting with "/" reaches the assistant
as text, that `la start` works without the slash, and that a cold `/la start` in
a new chat finds `AGENTS.md` without the opening line.

## Windows ChatGPT opening observed

Justin supplied four screenshots on November 3 showing app onboarding, project
creation with a local Academy source folder, the folder trust dialog, and the
Academy prompt's response. GPT-6.1 Sol Medium and “Ask for approval” are visible;
app build, account tier and exact extracted packet revision are unrecorded.

The response briefly introduces the folder and asks about role, work and hopes
for the Academy, then waits before the course overview or menu. This is a partial
opening pass. Source reads are not independently visible. The name question
added in `4ba28b0` is absent; the screenshots do not establish whether the Windows
copy predates that revision or the model omitted it. Check on the next run.
Saving, fresh-chat recovery and cleanup remain unobserved.

## Current teaching direction

Justin's later November 3 direction supersedes the earlier personal-question
entry: start with a brief role/work/learning-hopes introduction, then introduce
the course and five examples. Session 1 explores a fictional example and saves
learning. After Session 2, an explicit transition invites personal needs for
Sessions 3–5. The brief introduction is observed on Windows; the complete sequence still needs rehearsal.

## Participant rehearsal

Use a new extracted folder outside the source checkout. Record the app version,
account type, date, elapsed time and any facilitator intervention.

| Check | Pass condition | Observed on current version |
|---|---|---|
| Open | Assistant reads course sources and briefly asks for preferred name, role, work and learning hopes; waits before overview/menu | Partial on Windows: introduction/wait observed; name absent, source reads and revision unverified |
| Context introduction | Names only readable material; suggested questions have source support; no claim of full lectures or missing releases | Pending |
| Explore | Shows a small fictional illustration and one context lesson; follows curiosity before offering to save | Pending |
| Example choice | “Tell me more about C” shows fictional report consolidation without treating it as the participant’s process | Pending |
| Personal transition | Only an explicit post-Session-2 invitation starts personal-needs exploration; completion, dates and example choice do not | Pending |
| Review | A correction is reflected before the participant approves | Pending |
| Save | Reviewed exploration is in Starting-Point.md and opens outside chat | Pending |
| Same-chat attempt | Asking again in the original conversation does not trigger cleanup | Pending |
| Fresh-chat return | Actual file read, accurate quote and source named | Pending |
| Confirmation | Participant explicitly confirms new conversation and correct recovery | Pending |
| Cleanup | Only ONBOARDING.md and the marked entry section disappear | Pending |
| Preserve | Course, saved work and additions outside the marked entry section survive | Pending |
| Return again | Third conversation continues from saved work without re-onboarding | Pending |

## Failure and recovery cases

Keep cleanup pending when permission is denied, approval is absent, the saved
file is missing, the participant has not opened it, retrieval is incorrect, or
the conversation is not fresh. Corrected notes require a new recovery check.

Test an interruption between updating the entry and deleting the guide. The
lasting course instructions detect the remaining guide and resume pending work.
Never delete other files to clear an error. Preserve participant additions.

An attachment-only route can recover an attached note but does not prove local
folder read/write. Report any manual save/delete step explicitly. Later course
updates must not restore the onboarding guide or reset a participant's entry.

## Fresh-chat evidence

This portable packet cannot independently inspect conversation identity across
apps. It requires a source-file read and the participant's explicit confirmation
that this is a new conversation and the recovered note is correct. Do not label that
attestation as automatic session verification. If a platform provides stronger
evidence, record it without assuming the other platform does too.
