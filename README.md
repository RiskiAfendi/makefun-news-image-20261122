# Make.fun — World News Image (22 November 2026)

This repository is the source deliverable for the make.fun bounty:

- **Bounty:** [Sum up 22 November's world news in one image](https://make.fun/bounty/news-image-20261122)
- **Target date:** Sunday, 22 November 2026
- **Runtime entry point:** `main.py` (Python 3.13), to be authored in the GitHub Copilot agent session
- **License:** MIT

## Intended deliverables

- `main.py` at the repository root.
- `assets/entry.png`: the original, owner-authored final image.
- The program writes the exact image bytes to `/output/entry.png`.

## Hard constraints

- No network access at runtime.
- The program must write identical bytes on both runs.
- The image must be a complete PNG or JPEG, no larger than 1 MiB and no larger than 1024 × 1024 pixels.
- The submitted repository must remain public and include the required AI coding-agent session transcripts with the submission.

## Current status

Repository setup only. The image, runtime program, reproducibility tests, and submission have **not** been completed. Do not submit this repository until all bounty gates and transcript requirements have been verified.

See [COPILOT_TASK_BRIEF.md](COPILOT_TASK_BRIEF.md) before starting implementation.
