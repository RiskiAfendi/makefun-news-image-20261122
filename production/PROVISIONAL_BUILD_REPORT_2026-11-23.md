# HYBRID V3 Provisional Build Report

**Task ID:** `MAKEFUN-NEWS-IMAGE-HYBRID-V3-PREDELTA-2026-11-23`
**Date/time:** 23 November 2026 provisional build
**Status:** `PROVISIONAL BUILD READY — WAITING FOR 23:00 DELTA`

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

`main.py` is Python standard-library-only and copies `assets/entry.png` byte-for-byte to `/output/entry.png`. It creates `/output` if needed and rejects missing/non-PNG sources with a clear error.

## Validation commands

Run:

```sh
python3 tools/render_editorial.py
python3 -m pytest -q tests/test_entry.py
python3 tests/test_entry.py
sha256sum assets/entry.png
```

## Actual validation results

- Authoring render completed successfully.
- PNG signature and complete chunk structure passed; IHDR is `1024 × 1024`, IEND and all chunk CRCs passed.
- `assets/entry.png` size: `111,220 bytes`.
- SHA-256 for `assets/entry.png`: `8e6017d990c715eb7d91a045d8e490fe7d0eeb78b3687c4ee7687186bac5c645`.
- `main.py` ran twice and `/output/entry.png` matched `assets/entry.png` byte-for-byte on both runs.
- The first and second runtime output hashes both match the asset SHA-256 above.
- The 300×300 preview was inspected. Date/masthead, lead hierarchy, status bands, and seven secondary illustrations remain recognizable; supporting copy and three brief lines are intentionally not considered reliable at thumbnail text size.
- No runtime network/API/download/import of third-party packages is present in `main.py`.
- Local authoring uses Python 3.12 plus system Pillow; Python 3.13 itself was not available for a target-compatible runtime test.

## Known pending items

- Final COP31 headline/wording remains provisional.
- Kyiv/Vyshneve casualty discrepancy remains in the fact ledger.
- Benghazi attribution remains a Ukrainian claim.
- Cikande death toll remains unresolved.
- 23:00 WIB delta verification is not represented as complete.
- Python 3.13 is not installed in this local authoring environment; runtime source is 3.13-compatible and uses standard-library-only syntax.
- Owner/editorial approval and the 23:00 WIB delta remain outstanding.
- Coding-agent transcript status was not verified by this repository process and must be preserved by the owner/platform for later submission.

No submission or account/payment/wallet action was performed.
