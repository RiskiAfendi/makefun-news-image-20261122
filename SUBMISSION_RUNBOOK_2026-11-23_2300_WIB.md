# MAKE.FUN SUBMISSION RUNBOOK — INTERNAL MIDNIGHT TARGET

**Task ID:** MAKEFUN-SUBMISSION-RUNBOOK-2026-11-23-2300-WIB  
**Bounty:** `news-image-20261122`  
**Target news date:** 22 November 2026  
**Timezone:** WIB (UTC+7)  
**Internal submission target:** before 24 November 2026, 00:00 WIB  
**Final Delta Check:** 23 November 2026, 23:00 WIB  
**Status:** ACCELERATED PLAN — OWNER APPROVAL REQUIRED AT EDITORIAL GATES

> The midnight target is the owner's internal deadline. It does not redefine the bounty's published deadline. Do not submit an artifact that fails a mandatory bounty gate.

---

## 1. Working schedule

| Time (WIB) | Work | Exit condition |
|---|---|---|
| 20:20–20:40 | Lock a compact editorial direction and story capacity | One approved lead-story hierarchy; no sprawling 18–22-item layout if it harms legibility. |
| 20:40–21:00 | Freeze the copy candidate set from the 19:00 verification report | Headlines, figures, attribution verbs, date labels, and caveats are internally consistent. |
| 21:00–22:10 | Produce the original final visual and typography/layout | One square master composition; no generated pseudo-text; all text placed deterministically. |
| 22:10–22:40 | Implement the Python 3.13 entry point and local output path | Root `main.py` writes `/output/entry.png` without network access or runtime dependencies. |
| 22:40–23:00 | First-pass technical and visual QA | PNG/JPEG is valid, ≤1024×1024, ≤1 MiB, and readable at 300×300. |
| **23:00–23:15** | **Final Delta Check** | Check only material changes to selected stories; update copy only if evidence requires it. |
| 23:15–23:25 | Editorial lock | Owner approves final headlines, figures, attributions, and artwork. |
| 23:25–23:40 | Final build and mandatory validation | Two executions produce byte-identical `/output/entry.png`; all format, size, dimension, and offline checks pass. |
| 23:40–23:50 | Commit, push, and evidence verification | Confirm public repository commit, final asset, `main.py`, and eligible coding-agent transcript(s). |
| 23:50–23:55 | Submit the entry | Submission receipt/status is visible and recorded. |
| 23:55–00:00 | Contingency buffer | Resolve only submission UI/metadata issues; do not introduce new design changes. |

---

## 2. Scope control

Time is limited. Prefer a polished, legible, factually defensible image over maximum story count.

- Start from the provisional Top 10 in the 19:00 verification report.
- Aim for 3 lead stories plus a small number of supporting briefs.
- Do not force the draft's 18–22-event capacity if the 300px readability test fails.
- No new story enters the image during the delta check unless its date eligibility and source evidence are clear.
- Avoid redesigning the visual system after 23:15 WIB.

## 3. Mandatory implementation gates

The repository task brief remains authoritative for technical requirements:

1. Public repository under the entrant's account.
2. Root-level `main.py`, compatible with Python 3.13.
3. No network access at runtime.
4. Two runs must produce exactly the same output bytes.
5. Final PNG/JPEG ≤1 MiB and ≤1024×1024.
6. AI coding-agent transcript(s) for the session(s) that build the entry must accompany the submission.
7. Implementation session must meet the bounty's session eligibility requirement.
8. Do not use `eval`, `Function`, `vm`, dynamic imports, or execute code derived from environment secrets.
9. Owner approval is required before submission.

Existing Prompt A/B images are references only. They are larger than the final output limit and must not be submitted unchanged.

## 4. Submission path shown in make.fun

The submission dialog offers:

- **Let your agent submit:** the coding agent builds, pushes, and submits.
- **Submit it yourself:** download the kit, push to GitHub, and paste the link.

**Preferred path:** use “Let your agent submit” only if the coding agent is the same eligible session that creates the deliverable and its transcript can be preserved. Otherwise, use manual submission and explicitly include the required transcript/evidence. Do not assume the transcript is included unless the submission flow confirms it.

Do not click submit before the final asset and all technical gates are verified.

## 5. Go / no-go checkpoints

- **22:10 WIB:** if the visual is not near completion, reduce the number of supporting briefs and preserve only the strongest, verified lead stories.
- **22:40 WIB:** if `main.py` and `assets/entry.png` do not both exist, stop adding features and finish the smallest compliant implementation.
- **23:40 WIB:** if reproducibility, size, dimensions, offline execution, or transcript requirements fail, do not submit a known-invalid entry merely to meet the internal target.
- **23:50 WIB:** begin the submission flow only after owner approval and a passing validation record.

## 6. Submission evidence checklist

- [ ] Approved final story list and copy
- [ ] Original final image at `assets/entry.png`
- [ ] Root `main.py`
- [ ] Output file at `/output/entry.png`
- [ ] PNG/JPEG signature and complete file structure verified
- [ ] Dimensions ≤1024×1024
- [ ] File size ≤1,048,576 bytes
- [ ] Two output runs byte-identical
- [ ] Offline/no-runtime-dependency check passed
- [ ] Coding-agent transcript(s) ready
- [ ] Public GitHub commit and file paths verified
- [ ] Owner approval
- [ ] make.fun submission receipt/status captured

---

**Operating rule:** midnight is the internal target. Accuracy, eligibility, reproducibility, and a valid submission remain mandatory.
