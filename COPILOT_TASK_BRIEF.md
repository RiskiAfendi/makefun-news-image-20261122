# Copilot Task Brief — Make.fun News Image

**Bounty:** https://make.fun/bounty/news-image-20261122  
**Target news date:** Sunday, 22 November 2026  
**Repository:** https://github.com/RiskiAfendi/makefun-news-image-20261122  
**Required runtime:** Python 3.13  
**Entry point:** `main.py` at repository root

## Mission

Build an original, editorial-quality one-image summary of the world's news on 22 November 2026, plus a deterministic offline program that writes it to `/output/entry.png`.

## Mandatory bounty gates

1. Keep this repository public and under the entrant's own GitHub account. The existing MIT license is the OSI-approved project license.
2. Put the executable entry point at root as `main.py` for Python 3.13.
3. The program runs without network access.
4. Both executions must write exactly the same bytes to `/output/entry.png`.
5. The image must be a complete PNG or JPEG, at most 1 MiB (1,048,576 bytes), and at most 1024 × 1024 pixels.
6. AI coding-agent transcripts for the sessions that build the entry must be included with the make.fun submission.
7. The session that builds the entry must begin after this bounty opened. Keep all implementation work and its evidence in the eligible session.
8. For entries received from 23 November 2026 00:00 UTC onward, do not execute code obtained from environment secrets. Do not use `eval`, `Function`, `vm`, dynamic imports, or shells/interpreters fed with environment-secret values to run program code.
9. Do not copy another entrant's submitted code or image. Do not use downloaded code as the deliverable. Write the implementation in this Copilot session and keep provenance clear.

## Implementation approach

- Prefer a simple, auditable Python 3.13 entry point using only the standard library.
- Store the finished, original image at `assets/entry.png`.
- Have `main.py` copy those exact bytes to `/output/entry.png`; create the output directory if needed.
- Do not make HTTP requests, access external services, install packages at runtime, or depend on machine-specific fonts/assets.
- Keep `main.py` small and deterministic. It must not generate timestamps, random values, or other run-dependent output.
- Add a local validation script or tests only if useful; keep the actual required entry point at repository root.

## Editorial and factual standards

- Use the owner's verified research and approved concept documents as the source of news selection and visual direction.
- Do not invent events, dates, casualty figures, quotes, statistics, or causal claims.
- Prioritize a clear hierarchy: a small number of dominant lead stories, concise supporting stories, restrained data points, legible labels, and an original visual system.
- The image itself must communicate the target date and a coherent global-news picture without relying on a caption outside the image.
- Do not copy, trace, or imitate another entrant's image. Public entries may be studied only as high-level reference; create an original composition and artwork.
- If the verified research files or final approved visual concept are unavailable in this session, stop and ask the owner to provide them rather than guessing.

## Required verification before any submission

- Confirm the PNG/JPEG signature and complete file structure.
- Confirm dimensions are no greater than 1024 × 1024.
- Confirm image size is no greater than 1,048,576 bytes.
- Run `main.py` twice in the actual target-compatible environment.
- Compare the two output files byte-for-byte.
- Confirm there are no network calls or runtime dependencies.
- Confirm the transcript(s) for the session that authored the deliverable are ready to upload.
- Do not submit until every check passes and the owner approves.

## Current state

As of the Stage 3 task creation, `main.py`, final image, and tests are not yet present. Stage 1 and 19:00 WIB news verification are complete. The owner has authorized a provisional Hybrid V3 build in Copilot Cloud now, with final delta check at 23:00 WIB and internal submission target before 00:00 WIB. This statement must be rechecked against the live repository before reporting build status.


## Research source pack (read before planning)

The two original research reports are stored separately:

- `research/01-gpt-web-search/GPT_WEB_SEARCH_MASTER_FACT_SHEET_2026-11-22_PROVISIONAL.md` — GPT Web Search master fact sheet; marked provisional and requiring more research.
- `research/02-gemini-deep-research/GEMINI_DEEP_RESEARCH_GLOBAL_NEWS_INTELLIGENCE_2026-11-22.md` — Gemini Deep Research global news intelligence; marked ready for art direction but still requiring the stated post-cutoff update.

Read both documents independently. Preserve their separate candidate IDs, claims, timestamps, confidence labels, and exclusions. Build a reconciliation table before choosing stories. Do not silently merge conflicting shortlists or treat either report as a final post-cutoff fact freeze. See `research/README.md`.

The research files are supporting inputs only. They are not runtime dependencies and must not be read by `main.py` during execution.


## Design references and concept

- Concept draft: `design/concepts/GLOBAL_EDITORIAL_ATLAS_CONCEPT_V2_2026-11-23_DRAFT.md` — **DRAFT FOR DISCUSSION, NOT APPROVED FOR PRODUCTION**.
- Prompt A/B visual QA: `design/qa/PROMPT_A_VS_B_VISUAL_QA_2026-11-23.md` — Prompt A is the layout reference; Prompt B is the illustration-style reference. Neither is final.
- Generated image references are expected under `assets/references/generated/`. See that folder's README for the exact filenames and original measurements.

Do not assume the concept is final-approved. The owner expressly approved **provisional** production before the 23:00 WIB delta check; require final editorial approval before content lock or submission. The generated drafts exceed the bounty's output limits and must not be submitted unchanged.


## GPT Image prompt source files

The exact Prompt A and Prompt B used to generate the current reference drafts are preserved under `design/prompts/`:

- `design/prompts/PROMPT_A_FULL_EDITORIAL_IMAGE_2026-11-23.md` — exact extraction of the one-shot full editorial image prompt.
- `design/prompts/PROMPT_B_ILLUSTRATION_FIRST_UNDERLAY_2026-11-23.md` — exact extraction of the text-free illustration underlay prompt.
- `design/prompts/MAKEFUN_GLOBAL_EDITORIAL_ATLAS_IMAGE_GENERATION_PROMPT_20261123.md` — unchanged combined source prompt pack.
- `design/prompts/README.md` — provenance and usage guidance.

Prompt A/B are historical generation instructions and visual references, not final approved news copy. The current image drafts are stored in `assets/references/generated/`. Use Prompt B as the preferred illustration-first production direction, but only after the final news verification/content lock. Keep all exact headlines and figures in code-rendered text rather than asking the image model to typeset them.


## Immediate next step — Stage 3 Provisional Hybrid V3 Build

Stage 1 evidence inventory is complete and the 19:00 WIB broad verification report is committed. The owner now authorizes starting **provisional** image/code production without waiting for 23:00 WIB. Follow `production/STAGE3_HYBRID_V3_PROVISIONAL_BUILD_2026-11-23.md` in a genuine eligible Copilot Cloud coding-agent session. Produce working renderer, story-data file, preview, root `main.py`, and real QA results. **Do not submit** or mark news final before the 23:00 WIB delta check and owner approval. Preserve original research and image references.
