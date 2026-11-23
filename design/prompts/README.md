# Image-generation prompts — Global Editorial Atlas

**Project:** `news-image-20261122`  
**Source document:** `design/prompts/MAKEFUN_GLOBAL_EDITORIAL_ATLAS_IMAGE_GENERATION_PROMPT_20261123.md`  
**Source created:** 23 November 2026  
**Status:** `REFERENCE PROMPTS — CONTENT PROVISIONAL — NOT FINAL PRODUCTION COPY`

## Prompt files

1. [Prompt A — Full Editorial Image](PROMPT_A_FULL_EDITORIAL_IMAGE_2026-11-23.md)
   - Exact extraction of Section A from the source document.
   - Intended for a one-shot full editorial poster candidate.
   - Main risk: small text, statistics, and labels may be malformed or inaccurate.

2. [Prompt B — Illustration-First Underlay](PROMPT_B_ILLUSTRATION_FIRST_UNDERLAY_2026-11-23.md)
   - Exact extraction of Section B from the source document.
   - Intended to generate a text-free illustration underlay.
   - All headlines, dates, statistics, labels, and source tags should be added later by code.

3. [Full source prompt pack](MAKEFUN_GLOBAL_EDITORIAL_ATLAS_IMAGE_GENERATION_PROMPT_20261123.md)
   - Original combined document copied without editorial changes.
   - Includes the source prompt sections, copy deck/layout guidance, quality gate, and usage strategy.

## Provenance and handling

- Prompt A and Prompt B were extracted verbatim from the source document. No wording inside either prompt section was rewritten.
- The source document remains preserved as the canonical record.
- The generated reference images are stored separately in `assets/references/generated/`; they are outputs, not prompt text.
- The current images are visual drafts only. Neither is approved as the final submission image.
- News copy, numbers, attributions, and story selection are provisional. Do not treat them as final until the post-cutoff verification and final content lock are complete.
- Prefer Prompt B's text-free illustration approach for Hybrid V3, then render all text deterministically with the project code.
- Do not submit either generated reference image unchanged. The final output must pass the make.fun image and deterministic-program requirements.
