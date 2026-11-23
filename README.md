# Make.fun — World News Image (22 November 2026)

[![make.fun competition](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![Competition rank](https://make.fun/badge/news-image-20261122/RiskiAfendi/makefun-news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![Competition reward](https://make.fun/badge/news-image-20261122/RiskiAfendi/makefun-news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)

This repository contains the source and runtime deliverables for the make.fun bounty:

- **Bounty:** [Sum up 22 November's world news in one image](https://make.fun/bounty/news-image-20261122)
- **Target date:** Sunday, 22 November 2026
- **Runtime entry point:** `main.py`
- **License:** MIT
- **Repository status:** technical repository implementation complete; editorial and transcript gates remain

## Repository deliverables

- `assets/entry.png`: uploaded owner-authored final-candidate image, currently 1024 × 1024 and 618,099 bytes.
- `assets/previews/entry-300.png`: 300 × 300 supporting QA preview; not used by the runtime.
- `main.py`: offline, standard-library-only runtime that validates and copies `assets/entry.png` byte-for-byte to `/output/entry.png`.
- `tests/test_entry.py`: PNG structure, limit, source/output, and deterministic-run tests.
- `content/stories_2026-11-22.json`: provisional story copy and evidence pointers.
- `tools/render_editorial.py`: authoring renderer; not a runtime dependency.
- `production/PROVISIONAL_BUILD_REPORT_2026-11-23.md`: build and validation record.

## Technical gates

- No network access, downloads, APIs, or third-party packages are used by `main.py`.
- `main.py` rejects missing, oversized, oversized-dimension, or structurally invalid PNG files.
- The runtime validates PNG signature, IHDR dimensions, chunk boundaries and CRCs, IEND, and the 1 MiB limit.
- The runtime writes identical bytes to `/output/entry.png` on repeated executions.
- The final-candidate image SHA-256 is `40e643afa838938fcc3b2668a0cb983b1b8dca6864db9c3a2df92bc70af130fa`.

## Validation

Run under Python 3.13:

```sh
python3.13 -m pytest -q tests/test_entry.py
python3.13 tests/test_entry.py
```

## Remaining gates

- The image contains disputed Cikande casualty wording. It must not be treated as editorially final until the owner approves corrected copy or removal.
- The Make.fun coding-agent transcript bundle/check remains pending until the official kit and session discovery are available.
- No Make.fun submission or account/payment action has been performed.
