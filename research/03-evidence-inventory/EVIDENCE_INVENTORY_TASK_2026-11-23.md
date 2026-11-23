# STAGE 1 — EVIDENCE INVENTORY & SOURCE RECONCILIATION

**Task ID:** `MAKEFUN-NEWS-IMAGE-EVIDENCE-INVENTORY-2026-11-23`  
**Bounty:** `news-image-20261122`  
**Target news date:** Sunday, 22 November 2026  
**Owner:** Riski Afendi  
**Agent:** Global News Image Editor  
**Stage:** `STAGE 1 — READ-ONLY REVIEW`  
**Output required:** `research/03-evidence-inventory/EVIDENCE_INVENTORY_REPORT_2026-11-23.md`

---

## 1. Mission

Perform a repository-wide evidence inventory before any editorial selection, image generation, or coding.

Read the actual files in the repository. Verify paths and contents. Do not infer file existence from this task document or from an earlier chat. Inspect the two uploaded PNG references directly if the agent environment supports image inspection; otherwise state that limitation and use the existing visual QA report as secondary evidence.

The goal is to establish exactly what evidence exists, what each source supports, where the sources disagree, and what is still missing.

## 2. Mandatory source files

### Repository and compliance

- `README.md`
- `LICENSE`
- `COPILOT_TASK_BRIEF.md`
- `.github/agents/global-news-image-editor.agent.md`

### Original news research — read independently

- `research/01-gpt-web-search/GPT_WEB_SEARCH_MASTER_FACT_SHEET_2026-11-22_PROVISIONAL.md`
- `research/02-gemini-deep-research/GEMINI_DEEP_RESEARCH_GLOBAL_NEWS_INTELLIGENCE_2026-11-22.md`
- `research/README.md`

Do not overwrite, normalize, or merge these two source reports. Preserve their candidate IDs, timestamps, confidence/status labels, source links, exclusions, and original wording.

### Design and visual references

- `design/concepts/GLOBAL_EDITORIAL_ATLAS_CONCEPT_V2_2026-11-23_DRAFT.md`
- `design/qa/PROMPT_A_VS_B_VISUAL_QA_2026-11-23.md`
- `design/prompts/README.md`
- `design/prompts/PROMPT_A_FULL_EDITORIAL_IMAGE_2026-11-23.md`
- `design/prompts/PROMPT_B_ILLUSTRATION_FIRST_UNDERLAY_2026-11-23.md`
- `design/prompts/MAKEFUN_GLOBAL_EDITORIAL_ATLAS_IMAGE_GENERATION_PROMPT_20261123.md`
- `assets/references/generated/README.md`
- `assets/references/generated/prompt-a-full-editorial-draft-1254x1254.png`
- `assets/references/generated/prompt-b-illustration-first-draft-1254x1254.png`

Prompt A and Prompt B are historical image-generation instructions. Their embedded story choices, statistics, and copy are **provisional**, not a final news lock.

The concept V2 is explicitly `DRAFT FOR DISCUSSION — NOT APPROVED FOR PRODUCTION`. Do not treat its lead-story option, story count, layout, or art direction as owner-approved.

The current image references are drafts. Neither is approved for submission unchanged.

## 3. Required inventory

Create a table with one row per relevant repository artifact and these columns:

- Exact repository path
- Found / missing / unreadable
- File type and size (where available)
- What the file actually contains
- Evidence role (primary research, secondary research, visual reference, prompt, compliance, implementation, etc.)
- Authority/status (provisional, draft, reviewed, approved, not started)
- Important limitation or dependency

Verify the repository's MIT license from the actual `LICENSE` file. Do not claim that the repository is submission-ready merely because the license exists.

For each image, record actual dimensions, byte size, format, and whether it is a complete readable image. If possible, inspect the image itself and describe only visible, supported details. Distinguish image inspection from information copied out of the existing QA report.

## 4. GPT–Gemini source reconciliation

Read both reports independently before comparing them.

Build a reconciliation matrix that preserves the original candidate IDs and source labels. Include:

1. Candidates appearing in both reports.
2. GPT-only candidates.
3. Gemini-only candidates.
4. Different shortlist or lead-story recommendations.
5. Conflicting facts, figures, event dates, first-report dates, and timestamps.
6. Attribution and confidence/status differences.
7. Primary-source versus secondary-source strength.
8. Claims that remain unresolved or cannot be confirmed from the supplied documents.

For each candidate, quote only short factual fragments where necessary and cite the exact source filename and section/heading. Do not silently repair discrepancies or promote a reported claim to confirmed fact.

Do not select the final stories in this stage. The reconciliation matrix is an evidence map, not an editorial decision.

## 5. Visual-source reconciliation

Compare the two prompt documents with the two generated reference images and the existing Prompt A/B QA report.

Record:

- What Prompt A attempted to generate.
- What Prompt B attempted to generate.
- Which visible layout/illustration characteristics are actually present in each image.
- Which existing QA findings are directly supported by the images.
- Any mismatches between prompt intent and generated output.
- Any unsupported visual implication or text/number risk that needs later correction.

Use the existing QA report as a review input, not as a substitute for opening the images when image inspection is available.

## 6. Submission-readiness gap check

Verify whether these items actually exist:

- Root `main.py` using Python 3.13.
- Owner-approved final image asset.
- Final image no larger than 1024 × 1024 and 1 MiB.
- Deterministic output to `/output/entry.png`.
- Two-run byte-identical test.
- Local tests or validation evidence.
- AI coding-agent transcript for the session that builds the deliverable.
- Any submission record.

Do not create placeholders or claim tests/transcripts exist when they do not. Confirm the license separately.

## 7. Required report structure

Write exactly one report at:

`research/03-evidence-inventory/EVIDENCE_INVENTORY_REPORT_2026-11-23.md`

Use these sections:

1. Executive status and scope.
2. Repository artifact inventory.
3. Original GPT research inventory.
4. Original Gemini research inventory.
5. GPT–Gemini reconciliation matrix.
6. Prompt A/B and generated-image inventory.
7. Visual evidence and existing QA cross-check.
8. Submission-readiness gaps.
9. Unresolved questions requiring owner decision.
10. Recommended next stage, with dependencies and stop conditions.

Every conclusion must be traceable to a file and section, or explicitly labelled as an inference. If a source is missing or inaccessible, say so; do not fill the gap from general knowledge.

## 8. Hard boundaries — READ ONLY

During this task:

- Do not edit or overwrite either original research report.
- Do not edit the original Prompt A/B documents or generated reference images.
- Do not change the concept V2 or mark it approved.
- Do not choose the final story list or freeze any headline/statistic.
- Do not generate or edit the final image.
- Do not create `main.py`, install dependencies, or start implementation.
- Do not conduct the post-cutoff final news sweep early.
- Do not submit anything to make.fun.

Only create the evidence inventory report. Keep all other repository content unchanged.

## 9. Date and verification gate

The separate final-news plan requires:

- **23 November 2026, 19.00 WIB:** broad final verification after 22 November has ended in every time zone.
- **23 November 2026, 23.30 WIB:** focused final delta check and content lock.

This Stage 1 inventory may be completed before that cutoff, but it must not claim that the 22 November news list is final.

## 10. Completion criteria

Stage 1 is complete only when:

- Every required file is accounted for.
- Both research reports have been read independently.
- The reconciliation matrix identifies overlaps, differences, conflicts, and unresolved evidence.
- Both image references have been accounted for, with image-inspection limitations disclosed.
- Submission blockers are stated accurately.
- The report is saved at the exact required path.
- No production or submission action has occurred.

End the report with one of: `STAGE 1 COMPLETE — READY FOR OWNER REVIEW`, `STAGE 1 BLOCKED — SOURCE MISSING`, or `STAGE 1 INCOMPLETE — MORE EVIDENCE REQUIRED`.
