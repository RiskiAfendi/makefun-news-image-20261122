# VISUAL QA — PROMPT A vs PROMPT B
## The World in One Day — Global Editorial Atlas

**Task ID:** `MAKEFUN-GLOBAL-EDITORIAL-ATLAS-VISUAL-QA-20261123`  
**Bounty:** `news-image-20261122`  
**Audit time:** 23 November 2026, 15.40 WIB  
**Inputs:**  
- Image 1 — `The World in One Day_ Global News Atlas.png` (**Prompt A — Full Editorial Image**)  
- Image 2 — `Global Affairs Editorial Atlas(1).png` (**Prompt B — Illustration-First**)  
**Status:** `VISUAL REVIEW COMPLETE · NEWS LOCK PENDING`  
**Important:** This review does not certify the news as final. The requested last news verification must happen **after 23 November 2026, 19.00 WIB**. At the time of this visual audit it is only 15.40 WIB, so that cutoff has not yet passed.

---

## 1. Executive verdict

**Prompt A is the stronger first-pass editorial composition. Prompt B is the stronger illustration asset source. Neither file is ready for submission as-is.**

Recommended production route: **hybrid workflow**.

1. Keep Prompt A's editorial hierarchy as the layout reference.
2. Reuse/recreate the coherent flat-vector illustration language from Prompt B.
3. Do not use Prompt B's contact-sheet collage as the final image.
4. Render every headline, number, region label, and status label with a deterministic layout program or vector/text renderer—not with image-generation text.
5. Rebuild the final composition at exactly **1024 × 1024**, then perform a 300 × 300 legibility review.
6. Re-verify every story after 19.00 WIB before locking the news and numbers.

**No win rate can be guaranteed at 100%.** The goal is to improve the factors we control: date relevance, factual accuracy, editorial priority, readable hierarchy, and visual craft.

---

## 2. File and technical measurements

| Measurement | Prompt A — Full Editorial | Prompt B — Illustration-First |
|---|---:|---:|
| Original dimensions | 1254 × 1254 | 1254 × 1254 |
| Original mode | RGBA | RGBA |
| Original file size | 3,287,738 bytes | 2,532,744 bytes |
| Maximum allowed dimensions | 1024 × 1024 | 1024 × 1024 |
| Maximum allowed file size | 1,048,576 bytes | 1,048,576 bytes |
| Passes as uploaded? | **NO** | **NO** |

Both files exceed the bounty's dimension and file-size gates. Neither may be submitted unchanged.

### 2.1 1024 × 1024 compression simulation

The originals were resized to 1024 × 1024, converted to RGB, then encoded as optimized progressive JPEG. This is a feasibility test, **not a final approved export**.

| Variant | Prompt A | Prompt B | Under 1 MiB? |
|---|---:|---:|---|
| JPEG quality 92 | 426,215 bytes | 235,079 bytes | Yes |
| JPEG quality 88 | 366,182 bytes | 196,532 bytes | Yes |
| JPEG quality 84 | 323,608 bytes | 169,582 bytes | Yes |
| Optimized PNG | 1,610,002 bytes | 1,107,141 bytes | No |

Both images can fit the size gate as JPEG after resizing. However, Prompt A contains small typography and thin separators, so final encoding must be inspected for text-edge artifacts. Do not optimize the final file at the expense of headline sharpness.

---

## 3. Prompt A — Full Editorial Image

### 3.1 What works

- The date and masthead are immediately visible.
- The visual hierarchy is clear: title → three key numbers → regional ribbon → three lead stories → seven secondary stories → brief list → source/date footer.
- The three lead stories create a useful global mix: climate diplomacy, security in Libya, and US politics.
- The seven secondary cards add geographical and topical range: Ukraine, Sudan, DRC/health, Gulf of Oman, Indonesia, South Korea, and Bangladesh.
- The ivory/navy/red palette feels like a coherent international newspaper.
- Illustrations, borders, labels, and typography share a consistent visual language.
- The top-level statistics give a fast entry point for a viewer.

### 3.2 Weaknesses and risks

1. **Too much microcopy.** The “Also on Sunday” list and much of the explanatory text become unreadable at 300 × 300.
2. **Secondary cards are crowded.** Seven cards in one row make their headlines very small; at thumbnail size, the viewer sees images and bold words but cannot reliably read each story.
3. **Region strip is incomplete.** It lists Global, Africa, Europe, Americas, Middle East, and Asia, but not Oceania. Do not add Oceania merely to claim seven-region coverage; add a real, verified story if one qualifies.
4. **COP31 emblem may be interpreted as an official logo.** The generated mark should not be presented as an official UNFCCC/COP logo unless it is an authorized, verified asset. Prefer a neutral globe/conference illustration and a text label.
5. **The statistic “24 body bags recovered” needs careful framing.** Do not change it to “24 dead” unless the source confirms 24 deaths. Consider whether this is the best top-strip statistic or whether a less ambiguous figure would communicate the day more responsibly.
6. **US seat headline needs precise wording.** “US Democrats reach 258 seats” is concise, but the supporting line should make clear that a race was called on Sunday and the figure is a projected/called seat count, not a new election held on Sunday.
7. **Source line is generic.** “Official agencies, UN bodies, AP / Reuters / Yonhap / local reporting” does not show which source supports each story. If space permits, place short source tags on individual cards or keep the footer source families while preserving precise source mapping in the master fact sheet.
8. **No explicit map or timeline.** These are not mandatory, but the current composition has no geographical map or time context. Add either only if it adds more value than the space it consumes.

### 3.3 Thumbnail test at 300 × 300

**Readable at a glance:**
- masthead and date;
- three main statistics;
- three lead headlines, though their descriptions become small;
- dominant story illustrations.

**Partly readable / too small:**
- seven secondary headlines;
- story locations and category labels;
- status tags on secondary cards.

**Not reliably readable:**
- most one-line briefs;
- detailed story descriptions;
- source footer and detailed date notes.

**Verdict:** Strongest composition of the two, but it tries to carry more text than the 300px view can comfortably support. Reduce copy, increase the lead/secondary hierarchy, and consider removing the full brief list or limiting it to a small number of highly legible lines.

---

## 4. Prompt B — Illustration-First

### 4.1 What works

- The illustrations have a coherent editorial flat-vector style.
- The color palette is consistent and suitable for a serious global-news graphic.
- The image subjects generally correspond to the same ten story slots as Prompt A: three leads and seven supporting stories.
- The illustrations avoid the common image-generation failure of malformed small text because no headlines are embedded.
- The artwork can be used as a visual asset/reference board for a separately typeset composition.
- At 300 × 300, the visual scenes remain recognizable because they do not rely on tiny text.

### 4.2 Weaknesses and risks

1. **It is not a complete news image.** It has no date, title, headlines, locations, status labels, numbers, or source information.
2. **Large empty space at the top and bottom.** The illustration grid occupies only the middle portion of the square; the composition feels unfinished rather than intentionally editorial.
3. **It is a contact sheet, not a final layout.** Panel proportions and gutters are inconsistent with a finished editorial page.
4. **Some illustrations do not communicate the exact event.**
   - Ukraine: drones and a launcher are shown, but the scene could imply a specific air-defence deployment not established by the story.
   - Khartoum: a damaged UN compound is suggested, but the specific incident and drone damage are not self-evident.
   - DRC: healthcare workers are shown, but the fighting that disrupted the Ebola response is absent.
   - Gulf of Oman: tanker and military vessel suggest a maritime incident, but not a verified mine strike or attack.
   - Cikande: the building appears structurally collapsed; do not imply collapse unless the source verifies it. The known story is a factory fire and search/rescue operation.
   - South Korea: an exam desk suggests AI cheating, but not the minister's resignation.
5. **No visual hierarchy among stories.** All panels are presented as a grid; the three lead stories do not clearly dominate.
6. **No geographical or temporal context.** The image alone does not explain that all stories belong to Sunday, 22 November 2026.

### 4.3 Thumbnail test at 300 × 300

The illustrations remain visible and recognizable, but because the title and labels are absent, a viewer cannot know what day is being summarized or what each illustration means.

**Verdict:** Good art direction and illustration source; not a submission candidate by itself.

---

## 5. Direct comparison

| Evaluation | Prompt A | Prompt B | Winner |
|---|---|---|---|
| Date is immediately clear | Strong | Missing | A |
| News can be understood from image alone | Partial/strong | Weak | A |
| Editorial hierarchy | Strong | Weak | A |
| Illustration consistency | Good | Very good | B |
| Text accuracy/control | Needs proofreading | No text | B as an asset source |
| 300px information legibility | Partial | No labels to read | A, but revise |
| Geographic/topic coverage | Clear | Implied only | A |
| Factual visual restraint | Some generated-symbol risks | Some scene-specific risks | Neither without review |
| Technical gate as supplied | Fail | Fail | Neither |
| Best use | Layout reference / first draft | Illustration asset board | Hybrid |

---

## 6. Recommended production strategy — Hybrid V3

### 6.1 Keep from Prompt A

- Large date and masthead.
- Three lead stories.
- Clear region/category labels.
- Ivory/navy/red editorial identity.
- Compact secondary story grid.
- Explicit `CONFIRMED`, `REPORTED`, and `CLAIM` distinctions.
- Small but readable source/date footer.

### 6.2 Keep from Prompt B

- Flat-vector illustration language.
- Consistent lighting, palette, edge treatment, and perspective.
- Original scenes for COP31, Libya, US politics, Ukraine, Khartoum, DRC, Oman, Cikande, South Korea, and Bangladesh.

### 6.3 Rebuild instead of reusing the current whole images

Use the Prompt B image as a style/reference board. For production, create separate, well-framed illustrations or crop/rework each scene as an individual asset. Do not retain the large blank canvas or the contact-sheet grid as the final composition.

Use code/vector layout for all text:
- exact date;
- exact headlines;
- numbers and units;
- locations;
- status labels;
- source tags;
- footer.

This prevents a generated image from silently changing a number, misspelling a location, or inventing a label.

### 6.4 Proposed information density

The current image is too dense at thumbnail size. Recommended baseline:

- **3 lead stories** — large illustrations and clear headlines.
- **6–7 secondary cards** — shorter headline, location, and status.
- **0–6 news briefs** — only if they remain readable at 300px; do not force 8–12.
- **3–4 top statistics** — all must be significant, unambiguous, and independently checked.
- **Optional mini-map** — only if it improves understanding more than the space it occupies.

The final story count should follow the verified news, not a target number.

---

## 7. Content-specific QA before locking

These are editorial review flags from the two generated drafts. They are not a replacement for the final post-19.00 news update.

| Item | Current image wording/depiction | QA requirement |
|---|---|---|
| COP31 | “NO MAIN CLIMATE DEAL”; cover decisions not adopted | Confirm exact final status; do not say all COP outcomes failed. Avoid an invented official logo. |
| Libya | Russian warship capsizes after suspected drone attack | Preserve attribution/uncertainty. Do not identify attacker as confirmed if not independently established. |
| US | Democrats reach 258 seats | Verify exact called/projected count and timestamp of Sunday race call. |
| Ukraine | 186 drones reported; 161 downed/intercepted in research | Attribute to Ukrainian Air Force; confirm exact update time and distinction between shot down/suppressed. |
| Indonesia | 24 body bags recovered | Do not convert bags to identified deaths. Recheck search/rescue update and terminology. |
| Khartoum | Drone damage to UN site | Verify exact facility, damage, and date; avoid depicting a specific attacker. |
| DRC | Fighting disrupts Ebola response | Ensure image does not imply hospital was directly struck if reports only say fighting nearby. |
| Gulf of Oman | Tanker–military incident | Do not label as a confirmed mine strike or explosion without independent confirmation. |
| Cikande | Factory fire search continues | Do not depict building collapse unless verified. |
| South Korea | Education minister resigns | Verify resignation acceptance and date; distinguish the exam incident from the resignation date. |
| Bangladesh | Garment worker protest | Verify Sunday event and separate estimated industry losses from actual same-day losses. |
| Brief list | West Bank, Poland, Thailand, Nvidia, India, Brazil, Bahrain | Re-check event date vs first-reported date and source timestamp for every item. |

---

## 8. Required post-19.00 WIB final verification

At the time of this review, it is **15.40 WIB on 23 November 2026**, so the requested 19.00 WIB checkpoint has not yet happened. Do not mark the news as final before it.

After 19.00 WIB:

1. Recheck every lead and secondary story against primary sources and at least one reliable independent source where available.
2. Check whether casualty counts, drone counts, COP31 status, Libya attribution, and election seat projections changed.
3. Recheck all “Also on Sunday” briefs individually.
4. Remove any story whose only link to 22 November is unclear timezone conversion or a later retrospective article.
5. Add an update timestamp to the fact sheet.
6. Lock the story list and numbers only after the source audit is complete.

For each story record:
`event_date_local`, `first_reported_at`, `source_published_at`, `source_timezone`, `verified_claim`, `attribution`, `confidence`, `visual_risk`.

---

## 9. Final visual QA checklist

### 300 × 300 review
- [ ] Date and year remain readable.
- [ ] Main lead headlines remain recognizable.
- [ ] At least the core meaning of each lead is understood without opening the image.
- [ ] Secondary headlines do not collapse into unreadable microtext.
- [ ] Status tags remain distinguishable.
- [ ] The bottom briefs are either readable or removed.
- [ ] No tiny source footer is carrying essential facts.

### Factual/illustration review
- [ ] No invented official logos.
- [ ] No unsupported attacker attribution.
- [ ] No unsupported casualty total.
- [ ] No unsupported building collapse, explosion, or direct hospital strike.
- [ ] Claims are labelled as claims.
- [ ] No event from the wrong date is silently presented as Sunday news.

### Technical review
- [ ] Final dimensions no larger than 1024 × 1024.
- [ ] Final PNG/JPEG is no larger than 1,048,576 bytes.
- [ ] File is a complete valid PNG/JPEG.
- [ ] Final render is visually checked after compression.
- [ ] Program writes exactly `/output/entry.png`.
- [ ] Two program runs produce identical bytes.
- [ ] Required coding-agent transcripts and repository gates are satisfied.

---

## 10. Final recommendation

**Prompt A wins as a complete first-pass editorial image. Prompt B wins as an illustration style/asset source. The best route is not A versus B: it is a hybrid V3.**

Do not submit either current image:
- Prompt A is oversized and too dense at 300px.
- Prompt B is oversized and lacks all editorial information.

**Next decision:** use Prompt A's layout hierarchy and Prompt B's illustration style, then simplify the secondary layer and either remove or sharply limit the bottom briefs. Wait until after 19.00 WIB for the final news update before locking any story, statistic, or headline.

**Status:** `VISUAL DIRECTION APPROVED FOR ITERATION — NEWS NOT LOCKED — FINAL IMAGE NOT APPROVED`.
