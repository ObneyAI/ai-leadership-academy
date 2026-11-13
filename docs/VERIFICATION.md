# Verification

Record package checks separately from what a participant has demonstrated.

## What the automated tests cover

The package tests cover package contents, reproducibility, stale output,
symlinks, participant-content rejection, draft exclusion and non-overwriting
extraction. They do not establish that an assistant follows the
natural-language protocol in the packet.

## What still needs a participant rehearsal

No complete participant journey has been verified on any assistant: opening,
exploring, saving, fresh-chat recovery, cleanup, the `/la` commands and a course
update all need a rehearsal on each offered route. The course update addresses
return nothing until the repository is public.

Use a new extracted folder outside the source checkout. Record the app version,
account type, date, elapsed time and any facilitator intervention. Keep
rehearsal records and screenshots outside this repository.

| Check | Pass condition |
|---|---|
| Open | Assistant reads course sources and briefly asks for preferred name, role, work and learning hopes; waits before overview/menu |
| Context introduction | Names only readable material; suggested questions have source support; no claim of full lectures or missing releases |
| Explore | Shows a small fictional illustration and one context lesson; follows curiosity before offering to save |
| Example choice | “Tell me more about C” shows fictional report consolidation without treating it as the participant’s process |
| Personal transition | Only an explicit post-Session-2 invitation starts personal-needs exploration; completion, dates and example choice do not |
| Review | A correction is reflected before the participant approves |
| Save | Reviewed exploration is in Starting-Point.md and opens outside chat |
| Same-chat attempt | Asking again in the original conversation does not trigger cleanup |
| Fresh-chat return | Actual file read, accurate quote and source named |
| Confirmation | Participant explicitly confirms new conversation and correct recovery |
| Cleanup | Only ONBOARDING.md and the marked entry section disappear |
| Preserve | Course, saved work and additions outside the marked entry section survive |
| Return again | Third conversation continues from saved work without re-onboarding |
| Commands | A message starting with “/” reaches the assistant as text; `la start` works without the slash; a cold `/la start` in a new chat finds `AGENTS.md` |
| Course update | Assistant reaches the release addresses, saves files only inside `Course/`, skips draft entries, and leaves participant files and completed onboarding alone |
| Failed update | A failed fetch is reported plainly, with the manual step; no course content is invented |

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
