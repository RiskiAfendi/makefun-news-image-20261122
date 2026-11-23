# Research Source Pack — Make.fun News Image

**Bounty:** `news-image-20261122`  
**Target date:** Sunday, 22 November 2026  
**Purpose:** Evidence and research context for the Global News Image Editor custom agent.

## Source documents

| Research track | Repository file | Original source filename | Status at time of writing |
|---|---|---|---|
| GPT Web Search | [GPT Web Master Fact Sheet](01-gpt-web-search/GPT_WEB_SEARCH_MASTER_FACT_SHEET_2026-11-22_PROVISIONAL.md) | `MASTER_FACT_SHEET_MAKEFUN_NEWS_IMAGE_2026-11-22_PROVISIONAL(1).md` | PROVISIONAL — NEEDS MORE RESEARCH |
| Gemini Deep Research | [Gemini Global News Intelligence](02-gemini-deep-research/GEMINI_DEEP_RESEARCH_GLOBAL_NEWS_INTELLIGENCE_2026-11-22.md) | `Intelijen Berita 22 November 2026.md` | READY FOR ART DIRECTION, with a mandatory final update after 23 Nov 19:00 WIB |

Both documents are preserved as separate research tracks. Their contents have been copied without editorial rewriting; only repository filenames and paths have been normalized. Do not overwrite either source document with a reconciled version.

## How the agent must use these sources

1. Read both documents independently before proposing any story list.
2. Preserve each report's original shortlist, candidate IDs, confidence labels, timestamps, and exclusions.
3. Build a reconciliation table: overlap, GPT-only candidates, Gemini-only candidates, conflicting facts, conflicting timestamps, source-strength differences, and unresolved claims.
4. Do not assume the report marked READY FOR ART DIRECTION is automatically final. It still requires the stated post-cutoff update.
5. Do not silently merge different candidate IDs or treat a claim as confirmed.
6. Use the strongest directly supported facts only. If a discrepancy cannot be resolved from the source links and the final verification pass, ask the owner or exclude the story.
7. Produce a separate final fact sheet only after the final verification pass. Keep these two original source reports unchanged.

## Important interpretation

These documents are **supporting research inputs**, not the final image and not runtime dependencies. The Make.fun program must not read these research documents or access the network at runtime. Only the final approved image asset and the deterministic entry program belong in the runtime path.

## Planned next folders

- `research/03-final-verification/` — post-cutoff verification and final fact freeze.
- `research/04-editorial-decisions/` — approved story selection and visual-content decisions.
- `assets/references/generated/` — earlier GPT-generated visual drafts used as references.
- `assets/final/` — owner-approved final image asset.
- `main.py` — required root-level Python 3.13 entry point.


## Design source documents

- Concept draft: [Global Editorial Atlas V2](../design/concepts/GLOBAL_EDITORIAL_ATLAS_CONCEPT_V2_2026-11-23_DRAFT.md) — not yet approved for production.
- Visual review: [Prompt A vs Prompt B QA](../design/qa/PROMPT_A_VS_B_VISUAL_QA_2026-11-23.md) — Prompt A is the layout reference; Prompt B is the illustration-style reference.
- Generated image reference assets: `../assets/references/generated/` — originals should be uploaded without alteration; see that folder's README.
