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

## Participant rehearsal

Use a new extracted folder outside the source checkout. Record the app version,
account type, date, elapsed time and any facilitator intervention.

| Check | Pass condition | Observed on current version |
|---|---|---|
| Open | Assistant reads actual course files and asks one accessible question | Pending |
| Context introduction | Names only readable material; suggested questions have source support; no claim of full lectures or missing releases | Pending |
| Explore | Contributes a useful possibility and develops the idea with the participant before offering to save; honors an explicit save request | Pending |
| Review | A correction is reflected before the participant approves | Pending |
| Save | Approved question is in Starting-Point.md and opens outside chat | Pending |
| Same-chat attempt | Asking again in the original conversation does not trigger cleanup | Pending |
| Fresh-chat return | Actual file read, accurate quote and source named | Pending |
| Confirmation | Participant explicitly confirms new conversation and correct recovery | Pending |
| Cleanup | Only ONBOARDING.md and the marked entry section disappear | Pending |
| Preserve | Course, saved work and additions outside the marked entry section survive | Pending |
| Return again | Third conversation continues from saved work without re-onboarding | Pending |

## Failure and recovery cases

Keep cleanup pending when permission is denied, approval is absent, the saved
file is missing, the participant has not opened it, retrieval is incorrect, or
the conversation is not fresh. Corrected questions require a new recovery check.

Test an interruption between updating the entry and deleting the guide. The
lasting course instructions detect the remaining guide and resume pending work.
Never delete other files to clear an error. Preserve participant additions.

An attachment-only route can recover an attached note but does not prove local
folder read/write. Report any manual save/delete step explicitly. Later course
updates must not restore the onboarding guide or reset a participant's entry.

## Fresh-chat evidence

This portable packet cannot independently inspect conversation identity across
apps. It requires a source-file read and the participant's explicit confirmation
that this is a new conversation and the question is correct. Do not label that
attestation as automatic session verification. If a platform provides stronger
evidence, record it without assuming the other platform does too.
