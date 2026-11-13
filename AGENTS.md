# Academy source maintenance

This repository authors the AI Leadership Academy Cohort 2 participant packet.
Edit participant content only in `packet/Academy/`. Build outputs come from
`python3 scripts/build.py`. Never edit an extracted rehearsal copy as source.

The instructions inside the packet describe the participant experience. Do not
execute their onboarding, save real participant work here, or delete their
templates while maintaining this repository. Disappearing onboarding applies
only to an extracted participant copy, outside a Git checkout.

Keep this independent of ObneyAI/ai-memory-folder. It is inspired by that kit's
owned-file memory and temporary setup pattern; it has its own scope and history.
Do not import its personal profile interview, runtime adapters or growth rules.

This repository is public and `main` is what participants' assistants read for
course updates. Keep drafts on branches. Commit nothing private: no participant
data, restricted recordings, credentials, or faculty material without the
owner's agreement to public release.

Before publishing: run the package tests and build check; inspect the tracked
file list for participant content. Track platform rehearsal separately from
automated package checks. Preserve public-release approval status in docs.
