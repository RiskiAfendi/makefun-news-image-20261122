# HYBRID V3 Provisional Build Report

**Task ID:** `MAKEFUN-NEWS-IMAGE-HYBRID-V3-PREDELTA-2026-11-23`
**Date/time:** 23 November 2026 provisional build
**Status:** `TECHNICALLY VALIDATED — EDITORIAL AND TRANSCRIPT GATES PENDING`

## Editorial baseline

The implementation uses the 19:00 WIB verified fact sheet in `research/04-final-news-verification/FINAL_NEWS_VERIFICATION_2026-11-23_1900_WIB.md`.

- Three provisional leads: COP31, Kyiv region, Benghazi.
- Seven provisional secondary stories: Cikande, US House, DRC, Bangladesh, South Korea, Sudan, Gulf of Oman.
- Three compact briefs: Poland, BepiColombo, Thailand.
- No final content lock or 23:00 WIB delta is represented.

## Deliverables

- `content/stories_2026-11-22.json`
- `tools/render_editorial.py`
- `assets/entry.png`
- `assets/previews/entry-300.png`
- `main.py`
- `tests/test_entry.py`

## Originality and provenance

The layout uses Prompt A as a hierarchy reference and Prompt B as an illustration-language reference only. The implementation-created flat-vector scenes are original vector/shape compositions in the renderer. No Prompt A/B image or contestant artwork is copied as the final canvas. All headline, number, status, and footer text is rendered by Pillow at authoring time.

## Runtime

`main.py` is Python standard-library-only and copies `assets/entry.png` byte-for-byte to `/output/entry.png`. It creates `/output` if needed and rejects missing/non-PNG sources, files above 1 MiB, dimensions above 1024×1024, and invalid PNG structure with a clear error.

## Validation commands

Run:

```sh
python3.13 -m pytest -q tests/test_entry.py
python3.13 tests/test_entry.py
sha256sum assets/entry.png
```

## Actual validation results

- Current Git snapshot before repository documentation updates: commit `99e279de4e4b56d5163cb61570cc00189b785967`.
- `assets/entry.png` is a complete 1024×1024 PNG.
- `assets/entry.png` size: `618,099 bytes`.
- SHA-256 for `assets/entry.png`: `40e643afa838938fcc3b2668a0cb983b1b8dca6864db9c3a2df92bc70af130fa`.
- The Git blob SHA and locally validated file match as provided in the verified snapshot.
- `assets/previews/entry-300.png` is present, 300×300, 202,086 bytes, SHA-256 `9b8b73e44920c05b1bce4d69c062f9e1055e74b6079d8d305b35d9b9a3bb7033`. It is QA-only and is not a runtime dependency.
- Earlier repository validation evidence under Python 3.13.5: `2 passed in 1.42s`, source/output SHA-256 match, and byte-identical output.
- Post-edit rerun on 23 November 2026 used Python 3.13.18 via `uv`: `3 passed in 0.07s`; direct test printed `1024×1024`, 618099 bytes, SHA-256 `40e643afa838938fcc3b2668a0cb983b1b8dca6864db9c3a2df92bc70af130fa`.
- Runtime imports only `shutil`, `struct`, `sys`, `zlib`, and `pathlib`; no network or third-party dependency is used.

## Known pending items

- The current image says 24 killed/confirmed across Cikande. The 19:00 fact sheet (§3.4) says only 24 body bags were recovered and the death toll remained disputed.
- Owner approval is required before replacing this copy with wording such as “24 BODY BAGS RECOVERED — DEATH TOLL DISPUTED” or removing the statistic.
- The final 23:00 editorial/owner gates are not represented as complete.
- Official Make.fun transcript bundle/check could not be run because `RULES.txt` and `cli/makefun.mjs` are absent from this repository and session artifact set.
- Copilot Cloud session `e6b47c34-7344-4d61-8408-095b0fb1829e` and transcript discovery are pending official kit support.

No submission or account/payment/wallet action was performed.
