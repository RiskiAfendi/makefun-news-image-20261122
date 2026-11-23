# STAGE 3 — HYBRID V3 PROVISIONAL BUILD (START NOW)

**Task ID:** `MAKEFUN-NEWS-IMAGE-HYBRID-V3-PREDELTA-2026-11-23`  
**Bounty:** `news-image-20261122`  
**Working platform:** GitHub Copilot Web → `Global News Image Editor` → Cloud / Autopilot  
**Time zone:** WIB (UTC+7)  
**Authorization:** Owner authorizes **provisional production now** (23 November evening). This does **not** authorize final news lock or submission.  
**19:00 news verification:** COMPLETE  
**23:00 delta verification:** PENDING  
**Internal owner target:** Valid entry submitted **before 24 November 00:00 WIB**  
**Status:** `BUILD AUTHORIZED — CONTENT PROVISIONAL — NO SUBMISSION`

---

## 1. Mission

**Begin implementation immediately. Do not wait until 23:00 WIB.**

Build a real, testable **Hybrid V3** news-image generator using the existing original GPT Image references and the 19:00 verified fact sheet. Make headline text, numbers, status tags, source labels, and story order **data-driven**, so the owner can edit only the content file after the 23:00 delta check, without recreating artwork or rewriting the layout engine.

This task authorizes creating/editing working code, layout assets, tests, and provisional previews. It does **not** authorize final news approval or submission.

## 2. Required source review (read before building)

- `COPILOT_TASK_BRIEF.md`
- `SUBMISSION_RUNBOOK_2026-11-23_2300_WIB.md`
- `research/04-final-news-verification/FINAL_NEWS_VERIFICATION_2026-11-23_1900_WIB.md` (**the main factual baseline**)
- `research/03-evidence-inventory/EVIDENCE_INVENTORY_REPORT_2026-11-23.md`
- `design/concepts/GLOBAL_EDITORIAL_ATLAS_CONCEPT_V2_2026-11-23_DRAFT.md`
- `design/qa/PROMPT_A_VS_B_VISUAL_QA_2026-11-23.md`
- `design/prompts/PROMPT_A_FULL_EDITORIAL_IMAGE_2026-11-23.md`
- `design/prompts/PROMPT_B_ILLUSTRATION_FIRST_UNDERLAY_2026-11-23.md`
- `assets/references/generated/prompt-a-full-editorial-draft-1254x1254.png`
- `assets/references/generated/prompt-b-illustration-first-draft-1254x1254.png`

The original A/B images are **references only**. You may use safe, original illustration crops or visually reconstruct their style, but do not blindly copy incorrect captions or unsupported depictions.

## 3. Provisional content baseline (NOT FINAL)

Use the 19:00 report as sole authoritative content baseline. Do not go back to old Prompt A text or the 19:00-predecessor fact sheets for current figures.

### Provisional lead-story candidates (3)

| Slot | Story | Suggested safe short headline | Non-negotiable caveat |
|---|---|---|---|
| Lead 1 | COP31 Antalya | `COP31: NO CONSENSUS ON ANTALYA PACT` | Other COP decisions/outcomes progressed; do not imply total conference failure |
| Lead 2 | Kyiv-region strikes | `KYIV REGION: 14 REPORTED DEAD` | Latest regional administration total; individual locality figures have a documented discrepancy |
| Lead 3 | Benghazi corvette | `RUSSIAN CORVETTE CAPSIZES` | Ukraine **claims** responsibility; don't imply independent confirmation |

### Provisional secondary-story candidates (up to 7)

1. **Cikande, Indonesia** — `FACTORY FIRE: SEARCH CONTINUES`; 24 body bags recovered, 30 missing and 24 safe in cited SAR list; **do not equate bags with confirmed deaths**.
2. **US House** — `DEMOCRATS REACH AT LEAST 258 SEATS`; AP election call on Sunday, not a new election.
3. **DR Congo** — `FIGHTING DISRUPTS EBOLA RESPONSE`; do not depict direct hospital bombing.
4. **Bangladesh** — `GARMENT UNREST HITS INDUSTRY`; BGMEA's US$682m figure is a multi-day survey estimate, not Sunday's losses.
5. **South Korea** — `EDUCATION MINISTER RESIGNS`; distinguish resignation from earlier exam confusion.
6. **Sudan/Khartoum** — `DRONES DAMAGE UN PREMISES`; no attacker attribution.
7. **Gulf of Oman** — `UKMTO REPORTS TANKER INCIDENT`; **no confirmed mine strike, explosion, sinking, or named tanker**.

Optional briefs ONLY if readable and source/date-qualified: Poland missile-identification update, BepiColombo (cross-zone qualifier and 21 Nov event locally), Thailand river-control **proposal**. Do not fill the image with unsupported or outdated headlines.

**Critical:** the lead arrangement and exact copy above are *provisional engineering content*, not the final editorial selection. The data layout must permit easy reordering, removing, or replacing stories at 23:00.

## 4. Build architecture

Use a **two-phase pipeline**:

1. **Authoring/build phase:** a local, source-controlled graphics generation script and source-data file render `assets/entry.png` from verified story data, original illustration assets, and precise typography. A development-only renderer (e.g. Pillow, if available) is acceptable if documented; do not depend on it at make.fun runtime.
2. **Submission runtime:** root `main.py` on Python 3.13 uses the **standard library only**, reads the already-rendered valid `assets/entry.png`, and writes the exact same bytes to `/output/entry.png`.

Recommended editable files (adapt if necessary, document deviations):
- `content/stories_2026-11-22.json` — story slots, headlines, labels, safe numbers, evidence pointers, provisional status.
- `tools/render_editorial.py` — authoring-time rendering and layout.
- `assets/illustrations/` — only original/owned artwork selected from the two GPT Image references or newly created.
- `assets/entry.png` — provisional image, replaced after 23:00 lock.
- `main.py` — deterministic make.fun runtime.
- `tests/test_entry.py` — format, size, dimensions, determinism, offline constraints.
- `production/PROVISIONAL_BUILD_REPORT_2026-11-23.md` — implementation and QA record.

The goal is to update **content only** after 23:00; changing layout code should be exceptional.

## 5. Visual requirements

- Canvas **1024×1024** square.
- Strong masthead **THE WORLD IN ONE DAY**, prominent **SUNDAY 22 NOVEMBER 2026**.
- 3 visually differentiated lead stories; retain 5–7 secondary stories only if readable.
- 0–4 single-line briefs if they survive the **300×300** legibility test. Trim briefs rather than turning them into illegible microtext.
- Flat-vector / editorial illustration identity, ivory `#F7F3E9`, navy `#14213C`, restrained red `#A9322D`, teal `#23767A`, ochre `#C89034`.
- **All words and numbers rendered by code**, not by the image model.
- No copied contestants' art/code, no fake logos, no invented maps, claims, or victims.
- Never portray an uncertain attack attribution as independently confirmed.

## 6. Mandatory engineering and QA

- Valid complete **PNG** at `/output/entry.png`.
- Width and height `<=1024`; output file `<=1,048,576` bytes.
- No internet/network access during `main.py` runtime.
- No downloads, external APIs, or package installation at runtime.
- Execute `main.py` **twice** and compare bytes/SHA-256.
- Check PNG signature, IHDR, CRCs, chunk boundaries, and IEND.
- Preview at 1024×1024 **and** 300×300.
- Correct/attribute each headline and numeric statement against the 19:00 report.
- Document evidence for every checked claim.
- Do not rely on a JPEG renamed `.png` as the final PNG.
- Preserve real **Copilot coding-agent session transcript(s)**; do not fabricate or edit log metadata. Verify make.fun bundling acceptance before submission.
- Do **not** submit without explicit owner approval.

## 7. Timing and handoff

**Start now:** create and test the provisional production files in a genuine eligible Copilot Cloud coding-agent session; push/commit implementation work so that authorship is documented.

**Before 23:00 WIB:** deliver a usable provisional image preview, source-controlled code, actual test results, SHA-256 and byte size. Report any failures honestly.

**At 23:00 WIB:** owner completes Final Delta Check and supplies the locked content changes; apply these to `content/stories_2026-11-22.json`, rerender, retest, and commit. Avoid redesign or new dependencies.

**Before midnight:** owner checks submission package and uses the make.fun UI. The platform's published deadline remains 07:00 WIB, but the owner has chosen midnight as the internal target.

Do not wait for 23:00 to start coding. Do not claim 23:00 verification is already complete.

## 8. First agent response and completion criteria

First, summarize which source files actually exist, and propose a **brief 3–5 step execution plan**. Then proceed with implementation and tool execution in the same session; do not stop after merely making a plan. You have owner authorization for **provisional build only**.

Finish with:
- Actual changed/committed file paths and commit/branch.
- Preview location and instructions to view image.
- Image dimensions, file size, hash and 300px QA outcome.
- Two-run deterministic test outputs.
- Known provisional facts awaiting 23:00 verification.
- Transcript status and exact blocker if bundling isn't verified.
- **Status:** `PROVISIONAL BUILD READY — WAITING FOR 23:00 DELTA`, or an honest blocking status.

**Never press Submit or take payment/wallet action.**
