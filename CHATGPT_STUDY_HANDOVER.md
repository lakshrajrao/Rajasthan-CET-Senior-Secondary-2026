# ChatGPT Study Handover — Rajasthan CET Senior Secondary 2026

**Repository:** https://github.com/lakshrajrao/Rajasthan-CET-Senior-Secondary-2026
**Exam:** RSSB CET Senior Secondary Level (12th Level) 2026, Advt. No. 08/2026 — **1–3 Dec 2026 (tentative)**, 120 questions / 240 marks / 150 min.
**Student:** preparing since 11 Nov 2026, ~20 days, 5–6 hrs/day. Teaching language: **simple Hindi with English exam terms retained** (the notes are written that way).
**Handover date:** 11 November 2026. **Status:** final QC complete; see `AUDIT_CORRECTION_REGISTER.md` for every correction and every open gap.

---

## 1. What this repository is

A verified CET preparation database: official syllabus + exam pattern (verified from the notification), topic-wise notes, a 300-MCQ generated question bank, 360 mock questions (3 papers × 120), a 139-question classified PYQ sample, a 20-day study plan, a performance tracker, and a topic-level progress tracker. **Everything generated is labelled generated; everything from past papers is labelled PYQ. Never mix the two.**

## 2. Exam pattern — teach this first (verified, do not change without primary-source evidence)

- **120 questions, 240 marks, 2 hrs 30 min** (+10 min extra for OMR verification). All questions MCQ, equal marks (2 each). Five options A–E.
- **Marking:** correct = +2. Wrong answer = **−2/3**. **E (deliberately not attempted) = 0.** Blank (no circle darkened) = **−2/3** — a blank is NOT the same as E. **More than 10% blanks (>12 of 120) = disqualification.** Blue ball-point pen, one circle only.
- **Scoring:** Score = (Correct×2) − (Incorrect×2/3) − (Blank×2/3). Worked example: 70C/30W/20E = 120.0; the same with 20 blanks = 106.7 **and disqualified**.
- **Guessing rule (EV, verified):** blind guess EV = 0.00; 1 option eliminated (p=1/3) EV = +0.22; 2 eliminated (p=0.5) EV = +0.67; certain ≈ +2.00. **Rule: attempt only if at least 1 option can be eliminated; otherwise darken E.**
- **Qualifying marks 40% (96/240), 35% SC/ST (84/240); score valid 3 years — REPORTED, not verified from the official extract. Verify on the admit card.**
- **Official scheme gives NO per-subject question split.** The planning split (Raj GK & Admin 50, Geo India 10, Science 15, Reasoning/Maths 15, Hindi+English 15, Computer 5, CA & Public Health 10 = 120) is **reported/derived only** — always label it as such. Never present it as RSSB weightage.
- **Old pattern (2022/2024): 150Q/300 marks/3 hrs, NO negative marking.** Never mix with 2026. Sites showing 150Q for 2026 are copying the 2024 cycle.
- **2026 new syllabus items (prime "new question" territory):** VB-G RAM G in Economy; Disaster Management & Climate Change in Geography of India; Public Health as a separate head; Unfair Means Act 2022 in Current Affairs.

## 3. How to teach (instructions for ChatGPT)

1. **Read first:** `AUDIT_BRIEF_FOR_CHATGPT.md`, this file, `AUDIT_CORRECTION_REGISTER.md`, `00_Official_Syllabus_Verification.md`, `01_Official_Syllabus_and_Pattern.md`, `02_Exam_Pattern_and_Marking_Strategy.md`.
2. **Teach one topic at a time**, in the suggested teaching sequence in §5 for each subject. Simple Hindi, English exam terms retained. Explain the concept, then the facts, then the exam traps (negative marking, E-rule, common confusions listed in the notes).
3. **Use only the repo material for facts.** Where a topic is marked "needs additional verified research" (§5, and `AUDIT_CORRECTION_REGISTER.md` §G), research it from a primary or reputable source first (RSSB notification, NCERT, government sites, standard reference books) and say what the source is. **Never invent a fact, a frequency table, a weightage, a PYQ, or a source link.**
4. **Generated vs PYQ — always say which is which.** The 300 bank MCQs and 360 mock questions are **generated (predicted), syllabus-based**. The 139 PYQ rows are **actual past-paper questions** (classification metadata only — the dataset has no question text). When you set a test, say how many questions are PYQ-based and how many are generated.
5. **Chapter tests:** after each topic, give a short test from the bank MCQ IDs listed in §5 (10–15 questions), then mark it, explain every wrong answer, and update `study_progress_tracker.csv` (Questions completed, Test accuracy, Revision required). Keep the tracker honest — never mark "Explained by ChatGPT" or "PDF prepared" until it actually happened.
6. **PDFs:** you create and send the actual topic-wise study PDFs **through the conversation** with the user. Do NOT generate duplicate PDFs in this repo. Use the repo Markdown (notes + this handover) as the source. Each PDF should cover one topic: concept, facts, tables, 10–15 practice questions with answers on the last page, and a "verify before exam" box for anything in §6.
7. **Mocks:** Paper 1 on Day 11, Paper 2 on Day 15, Paper 3 on Day 18, full mock + OMR drill on Day 20 (see `study_plan_20day.md`). Score with the −2/3 rule and log in `performance_tracker.csv`. The mocks were audit-corrected on 11 Nov 2026 (see the register §B) — use the current repo version, not any earlier copy.
8. **Before the exam (last week):** update Current Affairs after 11 Nov 2026 and re-check the items in §6.

## 4. Repository map (exact paths)

| File | What it is |
|---|---|
| `00_Official_Syllabus_Verification.md` | Verified syllabus (all 13 heads, every micro-topic) + OMR rules, from the official extract |
| `01_Official_Syllabus_and_Pattern.md` | Exam pattern, key facts, reported (not official) subject split |
| `02_Exam_Pattern_and_Marking_Strategy.md` | Marking strategy, EV tables, attempt rules |
| `AUDIT_CORRECTION_REGISTER.md` | Every correction, every open gap, every unverified claim |
| `AUDIT_BRIEF_FOR_CHATGPT.md` | Original audit brief (pattern, OMR, cautions) |
| `INDEX.md` | Master index + per-subject coverage checklist |
| `README.md` | Repo overview |
| `notes_hindi_english.md` | Master notes, all 13 subjects, Hindi+English (767 lines) |
| `notes/01_history_rajasthan.md` … `notes/13_general_english.md` | Per-subject notes (13 files) |
| `question_bank.csv` | 300 generated MCQs (combined) |
| `question_bank/01_…csv` … `question_bank/13_…csv` | Same 300 MCQs, per-subject files (in sync with the combined file) |
| `mock_papers.md` | 3 papers × 120 generated questions, keys + explanations |
| `research/pyq/pyq_dataset.csv` | 139 classified actual PYQs (metadata only, no question text) |
| `research/pyq/pyq_inventory.md`, `pyq_analysis.md` | PYQ inventory + per-subject analysis (sample only, 7.7% of 1,800) |
| `study_plan_20day.md` | 20-day plan, 12 Nov–1 Dec 2026 |
| `study_progress_tracker.csv` | Topic-level tracker (104 topics; see §7) |
| `performance_tracker.csv` | Mock-test log + scoring/EV reference |
| `gen.py`, `gen_qb.py`, `raj_pool.py` | Generator scripts (do not re-run without checking the register) |
| `audit/` | Audit evidence: `mock_audit_findings.md`, per-paper findings, `qb_audit_findings.md`, `automated_checks_report.txt`, `mock_audit_report.txt`, fix scripts |

## 5. Subject-by-subject handover

**Reading the tables:** "Bank" = generated MCQs in `question_bank.csv` (IDs are `question_bank.csv` qids; the same rows are in the per-subject file). "PYQ" = actual past-paper questions in `research/pyq/pyq_dataset.csv`, identified as `Year — Shift — Q#` (e.g. `2024-P1 Q24` = 2024 Phase 1, 22 Oct AM, question 24). "Mocks" = generated questions in `mock_papers.md`, counted by their subject tags (tag→head mapping: Forts→Art & Culture; Rivers/Lakes/Census/Environment→Geography of Rajasthan; all other tags map directly). **PYQ counts are small because the sample is only 139 of 1,800 questions — never claim full-paper analysis.**

### 5.1 History of Rajasthan

- **Official syllabus topics (File 00 order):** (1) major ancient civilisations & archaeological sites; (2) prominent rulers & achievements; (3) Revolt of 1857; (4) peasant movements; (5) tribal movements; (6) Praja Mandal movements; (7) Integration of Rajasthan; (8) prominent historical personalities.
- **Notes:** `notes/01_history_rajasthan.md` (80 lines) + master notes §1. Coverage: all topics; **tribal movements detail is thin** (tracker: Partial).
- **Bank MCQs (24, generated):** `01_HISTORY_RAJASTHAN-001` to `01_HISTORY_RAJASTHAN-024`.
- **Actual PYQs (5):** 2023-11Feb-S2 Q18; 2024-P3 Q8; 2024-P4 Q18, Q19, Q20.
- **Mock questions (22, generated):** tag `[Raj: History | …]` across the 3 papers.
- **Topics needing additional verified research:** tribal movements detail.
- **Suggested teaching sequence:** civilisations/sites → rulers (Guhila/Chauhan/Rathore/Kachhwaha) → 1857 → peasant movements → tribal movements → Praja Mandal → Integration (1948–1956 timeline: Matsya Sangh 17 Mar 1948 … 1 Nov 1956) → personalities.
- **Suggested chapter tests:** (a) civilisations + rulers (bank 001–012); (b) movements + integration (bank 013–024); then PYQ 5 as a mixed drill.
- **PDF revision checklist:** integration timeline table; rulers-and-forts mapping; movements table (year, leader, place, outcome); 1857 centres in Rajasthan.

### 5.2 Art & Culture of Rajasthan

- **Official syllabus topics:** (1) architecture & painting; (2) folk music, musical instruments, dance & theatre; (3) major religious sects & folk deities; (4) social life — dresses, ornaments, fairs, festivals, customs, traditions; (5) language, dialects & literature; (6) prominent personalities in art & culture.
- **Notes:** `notes/02_art_culture_rajasthan.md` (91 lines) + master notes §2. Coverage: **dresses/ornaments/customs missing; theatre thin** (tracker: No/Partial).
- **Bank MCQs (20, generated):** `02_ART_CULTURE_RAJASTHAN-001` to `02_ART_CULTURE_RAJASTHAN-020`.
- **Actual PYQs (9):** 2023-11Feb-S2 Q6; 2024-P1 Q24, Q25, Q26; 2024-P2 Q24, Q25, Q26; 2024-P4 Q21, Q22.
- **Mock questions (53, generated):** tags `[Raj: Art]`, `[Raj: Culture]`, `[Raj: Folk Dance]`, `[Raj: Fairs]`, `[Raj: Symbols]`, `[Raj: Language]`, `[Raj: Forts]`.
- **Topics needing additional verified research:** dresses/ornaments/customs; theatre.
- **Suggested teaching sequence:** architecture & painting (incl. forts as architecture) → folk music & instruments → dance → theatre → sects & folk deities → social life (fairs/festivals/customs) → language/dialects/literature → personalities.
- **Suggested chapter tests:** (a) architecture/painting/forts (bank 001–008); (b) music/dance/fairs/deities (bank 009–020); then PYQ 9.
- **PDF revision checklist:** forts table (builder, district, special feature); painting schools; instruments table (type, how played); dance table (region, occasion); fairs/festivals calendar.

### 5.3 Geography of India

- **Official syllabus topics:** (1) physical features (mountains, plateaus, deserts, plains); (2) major rivers, dams, lakes & oceans; (3) wildlife & sanctuaries; (4) disaster management & climate change (NEW 2026).
- **Notes:** `notes/03_geography_india.md` (56 lines) + master notes §3. Coverage: physical features only — **rivers/dams/lakes/oceans, wildlife/sanctuaries, disaster management & climate change are missing** (tracker: No).
- **Bank MCQs (20, generated):** `03_GEOGRAPHY_INDIA-001` to `03_GEOGRAPHY_INDIA-020`.
- **Actual PYQs (6):** 2023-11Feb-S2 Q1, Q7, Q14; 2024-P4 Q1, Q2, Q3.
- **Mock questions (30, generated):** tag `[Geo India | …]` — exactly 10 per paper.
- **Topics needing additional verified research:** rivers/dams/lakes/oceans; wildlife & sanctuaries; disaster management & climate change (research from NCERT/standard geography before teaching).
- **Suggested teaching sequence:** physical features → rivers → dams & lakes → oceans/coasts → wildlife & sanctuaries → disaster management → climate change.
- **Suggested chapter tests:** (a) physical features + rivers (bank 001–010); (b) dams/lakes/wildlife/disasters (bank 011–020, after gap research); then PYQ 6.
- **PDF revision checklist:** rivers table (origin, tributaries, terminus, dam); dams table; national parks/sanctuaries table; disaster types + agencies; climate-change terms.

### 5.4 Geography of Rajasthan

- **Official syllabus topics:** (1) major physical features; (2) climatic conditions; (3) natural vegetation; (4) major soils; (5) rivers, dams & lakes; (6) natural resources (mineral, forest, water); (7) livestock; (8) wildlife, sanctuaries & conservation; (9) population (distribution, growth, density, literacy, sex ratio); (10) major tribes; (11) tourism.
- **Notes:** `notes/04_geography_rajasthan.md` (49 lines) + master notes §4. Coverage: **livestock, major tribes (Bhil, Meena, Garasia), tourism missing** (tracker: No).
- **Bank MCQs (22, generated):** `04_GEOGRAPHY_RAJASTHAN-001` to `04_GEOGRAPHY_RAJASTHAN-022`.
- **Actual PYQs (2):** 2024-P3 Q9, Q10. (Only 2 in the sample — the sample is skewed; do not treat this as the real weightage.)
- **Mock questions (49, generated):** tags `[Raj: Geography]`, `[Raj: Rivers]`, `[Raj: Lakes]`, `[Raj: Census]`, `[Raj: Environment]`.
- **Topics needing additional verified research:** livestock; major tribes; tourism.
- **Suggested teaching sequence:** physical features & climate → soils & vegetation → rivers/dams/lakes → minerals/forest/water → livestock → wildlife & sanctuaries → population (Census 2011) → tribes → tourism.
- **Suggested chapter tests:** (a) physical/climate/soils/rivers (bank 001–011); (b) resources/population/tribes/tourism (bank 012–022, after gap research); then PYQ 2.
- **PDF revision checklist:** rivers table (origin, district, terminus/dam); lakes table (natural vs artificial, district); minerals table (mineral, district); Census 2011 figures; tribes table; tourist circuits.

### 5.5 Indian Political System (special reference to Rajasthan)

- **Official syllabus topics:** (1) nature of Constitution, Preamble, Fundamental Rights, DPSP; (2) President, PM & Council of Ministers, Parliament; (3) Supreme Court; (4) Election Commission; (5) Governor, CM, Legislative Assembly, High Court, RPSC; (6) State Election Commission, State Information Commission, State Human Rights Commission, Chief Secretary, District Administration; (7) local self-government & Panchayati Raj.
- **Notes:** `notes/05_polity_rajasthan.md` (59 lines) + master notes §5. Coverage: Supreme Court and Election Commission detail thin (Partial); **State Information Commission / State Human Rights Commission detail missing** (tracker: No).
- **Bank MCQs (22, generated):** `05_POLITY_RAJASTHAN-001` to `05_POLITY_RAJASTHAN-022`.
- **Actual PYQs (5):** 2023-11Feb-S2 Q5; 2024-P3 Q7; 2024-P4 Q27, Q28, Q29.
- **Mock questions (17, generated):** tag `[Raj: Polity | …]`.
- **Topics needing additional verified research:** Supreme Court detail; Election Commission detail; State Information Commission; State Human Rights Commission.
- **Suggested teaching sequence:** Constitution/Preamble/FR/DPSP → Union executive & Parliament → Supreme Court → Election Commission → Governor/CM/Assembly/High Court/RPSC → state commissions & Chief Secretary/District Administration → Panchayati Raj (Nagaur, 2 Oct 1959).
- **Suggested chapter tests:** (a) Constitution + Union (bank 001–011); (b) State + local self-government (bank 012–022); then PYQ 5.
- **PDF revision checklist:** amendments table (42nd/44th/61st/73rd/101st/106th); articles table; state institutions table (who appoints, tenure, function); Panchayati Raj three-tier diagram.

### 5.6 Economy of Rajasthan

- **Official syllabus topics:** (1) role of industry, agriculture, animal husbandry & mineral sector; (2) features & issues; (3) concepts of state income & budget; (4) handicraft industry; (5) unemployment; (6) drought & famine; (7) welfare schemes & Acts; (8) development institutions; (9) small enterprises; (10) financial institutions; (11) PRI role in rural development; (12) MGNREGA; (13) **VB-G RAM G (Viksit Bharat Guarantee for Rozgar and Aajeevika Mission – Gramin) (NEW 2026)**.
- **Notes:** `notes/06_economy_rajasthan.md` (48 lines) + master notes §6. Coverage: **VB-G RAM G, unemployment, drought & famine, financial institutions, PRI role in rural development missing; animal husbandry detail thin** (tracker: No/Partial).
- **Bank MCQs (18, generated):** `06_ECONOMY_RAJASTHAN-001` to `06_ECONOMY_RAJASTHAN-018`.
- **Actual PYQs (6):** 2023-11Feb-S2 Q3; 2024-P3 Q18; 2024-P4 Q23, Q24, Q25, Q26.
- **Mock questions (9, generated):** tags `[Raj: Economy]`, `[Raj: Schemes]`, `[Raj: CA/Schemes]`.
- **Topics needing additional verified research:** VB-G RAM G (check the Dec 2025 legislation/gazette before teaching — the mock-paper wording on this is unverified, register §H1); unemployment; drought & famine; financial institutions; PRI role; animal husbandry detail.
- **Suggested teaching sequence:** features & issues → sectors (industry/agriculture/animal husbandry/minerals) → state income & budget (Budget 2026-27 figures) → handicrafts & small enterprises → unemployment → drought & famine → welfare schemes & Acts → institutions → PRI & rural development → MGNREGA → VB-G RAM G.
- **Suggested chapter tests:** (a) sectors + budget (bank 001–009); (b) schemes/institutions/MGNREGA/VB-G RAM G (bank 010–018, after gap research); then PYQ 6.
- **PDF revision checklist:** Budget 2026-27 key figures (verify: ₹6,10,956 crore, GSDP ₹21,52,100 crore); schemes table (scheme, benefit, beneficiary); MGNREGA vs VB-G RAM G comparison table; minerals/industries table.
- **Caution:** 6 Economy bank rows carry exact scheme figures that could NOT be verified in this audit (register §H2–H7: renewable/solar GW, Yuva Swarojgar subsidy, Lakhpati Didi limit, Gargi Puraskar, Thar Cultural Circuit, Uniform/Bag DBT). Teach them as "as per the bank — verify before the exam", not as settled fact.

### 5.7 Everyday Science

- **Official syllabus topics:** (1) physical & chemical changes, oxidation/reduction, catalyst; (2) metals, non-metals & important compounds; (3) carbon & compounds, hydrocarbons, allotropes, CFC/Freons, CNG, polymers, soap & detergents; (4) reflection of light, laws, dispersion, lenses, vision defects; (5) space & IT, Indian space programme; (6) genetics (terminology, Mendel's laws, chromosomes, nucleic acids, central dogma, sex determination); (7) environmental study (ecosystem structure, biotic factors, energy flow, biogeochemical cycles); (8) biotechnology (general info, bio-patent, new plant varieties, transgenic organisms); (9) economic importance of animals & plants; (10) blood groups, transfusion, Rh factor, pathogens, human health, malnutrition, human diseases — causes & cures.
- **Notes:** `notes/07_everyday_science.md` (80 lines) + master notes §7. Coverage: **oxidation/reduction + catalyst, allotropes, Indian space programme/ISRO, genetics/Mendel, biotechnology, economic importance of plants/animals missing** (tracker: No). Covered topics were spot-check verified (1 HP = 746 W, sound 343 m/s, 206 bones, O donor/AB recipient, Project Tiger 1973).
- **Bank MCQs (36, generated):** `07_EVERYDAY_SCIENCE-001` to `07_EVERYDAY_SCIENCE-036` — the largest bank section.
- **Actual PYQs (20):** 2023-11Feb-S2 Q4, Q8, Q10, Q20; 2024-P1 Q8, Q9, Q10, Q16, Q17; 2024-P2 Q8, Q9, Q10, Q16, Q17; 2024-P3 Q5, Q19, Q20, Q21, Q22, Q23.
- **Mock questions (45, generated):** tags `[Science: Physics]`, `[Science: Chemistry]`, `[Science: Biology]` — 15 per paper.
- **Topics needing additional verified research:** oxidation/reduction + catalyst; allotropes; Indian space programme/ISRO; genetics/Mendel; biotechnology; economic importance of plants/animals.
- **Suggested teaching sequence:** physics (light, motion, energy) → chemistry (metals, carbon, compounds) → biology (human body, blood, diseases) → genetics → environment → biotechnology → space programme.
- **Suggested chapter tests:** (a) physics (bank 001–012); (b) chemistry (bank 013–024); (c) biology + genetics + environment (bank 025–036, after gap research); then PYQ 20.
- **PDF revision checklist:** formulas table (units, values); human-body table (bones, blood groups, organs); diseases table (cause, pathogen, cure); genetics terms; space missions table (verify ISRO facts from a primary source).

### 5.8 Logical Reasoning & Mathematics

- **Official syllabus topics:** blood relation; number series; alphabet series; clock; calendar; LCM & HCF; average; profit & loss; percentage; SI; CI; ratio-proportion; time-speed-distance; work & time; area (triangle, circle, **ellipse**, rectangle, sphere, cylinder); volume (sphere, cylinder, cube, cone); graphical representation of data; code & decode; sitting arrangement; mental & analytical ability. **No trigonometry, algebra, logarithms — Graduation-level only.**
- **Notes:** `notes/08_reasoning_mathematics.md` (109 lines) + master notes §8. Coverage: all topics except **ellipse area formula (πab) missing** (tracker: Partial). All solved examples were recomputed and verified correct in the audit (LCM 36, cylinder 1540, SI/CI diff ₹100, successive −4%, ranking 29th, direction √10 km NE, clock 90° at 3:00).
- **Bank MCQs (48, generated):** Reasoning `08_REASONING-001` to `08_REASONING-024`; Mathematics `08_MATHEMATICS-001` to `08_MATHEMATICS-024`. All 48 were recomputed/solved in the audit — 0 wrong keys (3 wording fixes applied, register §C3/C5/C6).
- **Actual PYQs (35):** Reasoning 18 — 2023-11Feb-S2 Q12, Q15; 2024-P1 Q4, Q6, Q7; 2024-P2 Q4, Q6, Q7, Q18, Q19, Q20, Q21; 2024-P3 Q11, Q12, Q13, Q29; 2024-P4 Q8, Q9. Mathematics 17 — 2023-11Feb-S2 Q9, Q11; 2024-P1 Q5, Q18, Q19, Q20, Q21, Q30; 2024-P2 Q5, Q30; 2024-P3 Q1, Q2, Q3, Q27, Q28; 2024-P4 Q16, Q17.
- **Mock questions (45, generated):** Reasoning 18 + Mathematics 27 (tags `[Reasoning: …]`, `[Maths: …]`). Note: mocks repeat SI/Average heavily (SI ×4/×6/×3, Average ×3/×4 across papers) — vary the numbers in chapter tests.
- **Topics needing additional verified research:** ellipse area formula only.
- **Suggested teaching sequence:** number/alphabet series → coding-decoding → blood relation → direction → sitting arrangement → clock & calendar → LCM/HCF → average → percentage → profit & loss → SI/CI → ratio → time-speed-distance → work & time → area & volume → data interpretation.
- **Suggested chapter tests:** (a) reasoning set 1 (bank Reasoning 001–012); (b) reasoning set 2 (bank Reasoning 013–024); (c) maths set 1 (bank Maths 001–012); (d) maths set 2 (bank Maths 013–024); then PYQ 35 as a timed drill (75 sec/question).
- **PDF revision checklist:** formula sheet (SI/CI, average, %, ratio, speed, area, volume incl. ellipse πab); solved-example bank; clock/calendar rules; series patterns.

### 5.9 Current Affairs

- **Official syllabus topics:** (1) major contemporary events at state & national level (politics, economy, society, culture, technology, geography, ecology, sports); (2) famous personalities; (3) state & national programmes & policies; (4) civic duties (Fundamental Duties, moral values); (5) salient provisions of the **Rajasthan Public Examination (Prevention of Unfair Means) Act, 2022**.
- **Notes:** `notes/09_current_affairs.md` (52 lines) + master notes §9. Coverage: events Dec 2025–Nov 2026, web-verified 11 Nov 2026 (see register §F). **Events after 11 Nov 2026 are missing — needs a pre-exam update** (tracker: No).
- **Bank MCQs (18, generated):** `09_CURRENT_AFFAIRS-001` to `09_CURRENT_AFFAIRS-018`. 13 of 18 dated claims web-verified in the audit; 5 rows carry figures that could NOT be verified (register §H8–H11: RE-SAF award, 235 athletes' jobs, 'Sapnon Ki Udaan', National Sports Awards 2025 details) — teach as "as per the bank — verify before the exam".
- **Actual PYQs (16):** 2023-11Feb-S2 Q13, Q17, Q19; 2024-P2 Q2, Q3, Q27, Q28, Q29; 2024-P3 Q14, Q15, Q16, Q17, Q30; 2024-P4 Q5, Q6, Q7.
- **Mock questions (16, generated):** tags `[CA: …]` — 6 in Paper 1, 4 in Paper 2, 6 in Paper 3.
- **Topics needing additional verified research:** all events after 11 Nov 2026 (update in the last week before the exam).
- **Suggested teaching sequence:** national events (month-wise, Dec 2025–Nov 2026) → Rajasthan events → sports → awards & personalities → programmes & policies → civic duties & Fundamental Duties → Unfair Means Act 2022.
- **Suggested chapter tests:** (a) national + sports (bank 001–009); (b) Rajasthan + schemes + Act (bank 010–018); then PYQ 16.
- **PDF revision checklist:** month-wise event timeline; awards table (award, recipient, date); sports results table (CWG 2026: 39 medals 13G/17S/9B, 4th; Asian Games 2026: 85 medals 21/27/37, 4th; Asian Para Games 2026: 114 medals 30/35/49, 4th); Nobel 2026 table; Unfair Means Act provisions (up to 3 yrs + ₹1,00,000 fine).

### 5.10 Public Health

- **Official syllabus topics (NEW 2026 head):** (1) basics of first aid; (2) CPR; (3) types of drug abuse & prevention; (4) physical & mental fitness of youth; (5) health risks of social-media addiction & prevention.
- **Notes:** `notes/10_public_health.md` (41 lines) + master notes §10. Coverage: programmes/nutrition/indicators only — **the official core (First Aid, CPR, drug abuse, social-media addiction, youth fitness) is missing** (tracker: No). This is the biggest coverage gap in the repo.
- **Bank MCQs (14, generated):** `10_PUBLIC_HEALTH-001` to `10_PUBLIC_HEALTH-014` — all on programmes/nutrition/indicators; **zero** on the official core. All 14 were verified correct in the audit (PM-JAY ₹5 lakh, ASHA, Mission Indradhanush, JSY, BMI, polio-free 2014, Poshan Abhiyaan 2018, IMR, PHC, BCG, Swachh Bharat 2014, Jal Jeevan Mission, Mukhyamantri Nishulk Dava Yojana).
- **Actual PYQs (0):** Public Health is a new 2026 head — there are no PYQs. Say so explicitly; do not invent any.
- **Mock questions (14, generated):** tag `[Public Health | …]` — 4 in Paper 1, 6 in Paper 2, 4 in Paper 3.
- **Topics needing additional verified research:** First Aid steps; CPR steps (verify 30:2 ratio, 100–120 compressions/min from standard guidance); drug abuse types & prevention; youth physical & mental fitness; social-media addiction risks & prevention.
- **Suggested teaching sequence:** research the official core first (from a standard first-aid/CPR source) → First Aid basics → CPR → drug abuse → youth fitness → social-media addiction → programmes & indicators (already in notes).
- **Suggested chapter tests:** (a) programmes & indicators (bank 001–014); (b) a new test on the official core **only after the gap research is done** — do not test untaught material.
- **PDF revision checklist:** First Aid steps table; CPR steps (with the verified ratio/rate); drug types table; addiction signs & prevention; programmes table.

### 5.11 Computer Knowledge

- **Official syllabus topics:** (1) characteristics & applications of computers; (2) computer organisation incl. memory (RAM, ROM); (3) file system; (4) input/output devices; (5) MS Office (Word, Excel/Spreadsheet, PowerPoint). **No internet, e-mail, cyber-security, AI — Graduation-level only.**
- **Notes:** `notes/11_computer_knowledge.md` (36 lines) + master notes §11. Coverage: file system thin (Partial); §11.2/11.3 carry EXTRA labels for out-of-syllabus topics.
- **Bank MCQs (18, generated):** `11_COMPUTER_KNOWLEDGE-001` to `11_COMPUTER_KNOWLEDGE-018`. **In-syllabus (8):** 001–006, 014, 018 (basics, hardware, memory, MS Office, input devices, operating systems). **EXTRA (10, labelled in the subtopic field):** 007, 008, 009, 010, 011, 012, 013, 015, 016, 017 (WWW, SMTP, binary, LAN, phishing, firewall, e-Mitra, UPI, Jan Aadhaar) — low-priority PYQ-style awareness only (the 2024 paper asked HTTP).
- **Actual PYQs (5):** 2024-P1 Q22, Q23; 2024-P2 Q1; 2024-P3 Q4, Q6.
- **Mock questions (15, generated):** tag `[Computer | …]` — 5 per paper. **3 are tagged [EXTRA]** (P1 Q52 WWW, P1 Q56 E-mail, P3 Q116 E-mail) — teach them only as low-priority awareness.
- **Topics needing additional verified research:** file system (thin).
- **Suggested teaching sequence:** characteristics & applications → organisation & memory (RAM/ROM) → file system → input/output devices → MS Office (Word → Excel → PowerPoint).
- **Suggested chapter tests:** (a) in-syllabus set (bank 001–006, 014, 018); (b) EXTRA set only if time remains (bank 007–013, 015–017) — label it EXTRA.
- **PDF revision checklist:** memory table (RAM vs ROM); devices table (input vs output); MS Office shortcuts/functions table; file-system terms.

### 5.12 General Hindi

- **Official syllabus topics:** sangya; sarvanam; visheshan; avyaya; kriya; sandhi & sandhi-vichhed; samas & samas-vigrah; upsarg; pratyaya; paryayvachi; vilom; anekarthak; shabd-yugm; shabd-shuddhi; vakya-shuddhi; vakyaansh ke liye ek shabd; muhavare & lokoktiyaan; Hindi equivalents of English technical terms; office letters (aadesh, paripatra, adhisoochna, ardh-shaskiya patra, nivida, press vigyapti).
- **Notes:** `notes/12_general_hindi.md` (50 lines) + master notes §12. Coverage: sangya/sarvanam/visheshan/avyaya detail thin (Partial); **shabd-yugm, shabd-shuddhi, vakya-shuddhi, Hindi equivalents of English technical terms, office letters missing** (tracker: No). Ras/Chhand/Alankar is labelled EXTRA in §12.6 — it is NOT in the 12th-level syllabus, do not teach it as syllabus.
- **Bank MCQs (20, generated):** `12_GENERAL_HINDI-001` to `12_GENERAL_HINDI-020`. All verified correct except one fix: `12_GENERAL_HINDI-015` ('Neelkanth') was wrongly keyed Karmadharaya — **corrected to Bahuvrihi** (register §C1). Note: the bank keys 'Dashanan' as Bahuvrihi (005) — consistent now.
- **Actual PYQs (20):** 2023-11Feb-S2 Q2; 2024-P1 Q1, Q2, Q3, Q11, Q12, Q13, Q14, Q15, Q27, Q28, Q29; 2024-P2 Q22, Q23; 2024-P3 Q24, Q25, Q26; 2024-P4 Q4, Q10, Q30.
- **Mock questions (23, generated):** tags `[Hindi: …]` across the 3 papers.
- **Topics needing additional verified research:** sangya/sarvanam/visheshan/avyaya detail; shabd-yugm; shabd-shuddhi; vakya-shuddhi; Hindi equivalents of English technical terms; office letters.
- **Suggested teaching sequence:** sangya → sarvanam → visheshan → avyaya/kriya → sandhi → samas (incl. Neelkanth = Bahuvrihi) → upsarg/pratyaya → paryayvachi/vilom/anekarthak → shabd-yugm → shuddhi (shabd + vakya) → ek shabd → muhavare/lokoktiyaan → technical-term equivalents → office letters.
- **Suggested chapter tests:** (a) vyakaran set 1 — sangya/sarvanam/sandhi/samas (bank 001–010); (b) vyakaran set 2 — paryayvachi/vilom/muhavare/ek shabd (bank 011–020, after gap research for shabd-yugm/shuddhi); then PYQ 20.
- **PDF revision checklist:** sandhi rules table; samas types with examples (Bahuvrihi: Neelkanth, Dashanan, Lambodar; Dvigu: Tribhuvan; Avyayibhav: Yathashakti); paryayvachi/vilom tables; muhavare list; office-letter formats.

### 5.13 General English

- **Official syllabus topics:** tenses/sequence of tenses; active & passive voice; direct & indirect narration; articles & determiners; prepositions; translation (Hindi↔English); official & technical terms (with Hindi versions); synonyms; antonyms; one-word substitution; unseen passage comprehension; letter writing (official, demi-official, informal).
- **Notes:** `notes/13_general_english.md` (43 lines) + master notes §13. Coverage: **translation, official & technical terms, letter writing missing; determiners detail thin** (tracker: No/Partial).
- **Bank MCQs (20, generated):** `13_GENERAL_ENGLISH-001` to `13_GENERAL_ENGLISH-020`. Two fixes applied: `13_GENERAL_ENGLISH-005` stem reworded so Narcissist is uniquely correct ("admires himself excessively"; an unverified "(2024 PYQ)" tag was also removed); `13_GENERAL_ENGLISH-020` replaced with a real comprehension item (register §C2/C7/C8).
- **Actual PYQs (10):** 2024-P2 Q11, Q12, Q13, Q14, Q15; 2024-P4 Q11, Q12, Q13, Q14, Q15.
- **Mock questions (22, generated):** tags `[English: …]` across the 3 papers.
- **Topics needing additional verified research:** translation Hindi↔English; official & technical terms; letter writing; determiners detail.
- **Suggested teaching sequence:** tenses → voice → narration → articles & determiners → prepositions → synonyms/antonyms → one-word substitution → translation → official & technical terms → comprehension → letter writing.
- **Suggested chapter tests:** (a) grammar set 1 — tenses/voice/narration (bank 001–010); (b) grammar set 2 + vocabulary + comprehension (bank 011–020, after gap research for translation/terms/letters); then PYQ 10.
- **PDF revision checklist:** tense table; voice/narration conversion rules; preposition list; one-word substitution list (Omniscient, Ambidextrous, Hydrophobia, Aviary, Narcissist); letter formats (official, demi-official, informal).

## 6. Things to verify before the exam (do not teach as settled fact)

- Current Affairs after 11 Nov 2026 (update in the last week).
- RBI repo rate 5.50% (Oct 2026) in the notes — flagged "verify before exam".
- Chiranjeevi / Mukhyamantri Ayushman Arogya Yojana current cover limit (bank/mock say ₹25 lakh per family per year as of 2023).
- District list after the Dec 2024 reorganisation (33 districts; smallest = Dholpur, largest = Jaisalmer).
- VB-G RAM G Act 2025 currency (Dec 2025 legislation replacing MGNREGA with a 125-day guarantee — re-check against the gazette).
- Qualifying marks 40%/35% and 3-year score validity — verify on the admit card.
- The 10 unverified Economy/CA bank rows and 12 unverified mock superlatives listed in `AUDIT_CORRECTION_REGISTER.md` §H.
- Exam dates 1–3 Dec 2026 are **tentative** (RSSB press notes 28 Sep & 14 Oct 2026) — check the admit card / RSSB site.

## 7. Progress tracker

`study_progress_tracker.csv` — 104 topic rows (one per official micro-topic, File 00 sequence), columns: Subject, Topic, Research verified, Notes verified, Explained by ChatGPT, PDF prepared, Questions completed, Test accuracy, Revision required.

- **Current state:** Research verified Yes 63 / No 32 / Partial 9. Notes verified the same. **Explained by ChatGPT: No on all 104 rows. PDF prepared: No on all 104 rows. Questions completed: 0 on all rows. Test accuracy: blank.** Nothing is pre-marked complete — update a row only after the work actually happened.
- **Revision required = Yes on 41 rows** — these are the audit-identified gaps/thin topics (register §G). Fill them with verified research before or during teaching, then flip the row.
- Update the CSV after each chapter test and each PDF. Keep it in the repo so the next session can pick up exactly where this one stopped.

## 8. Exact handover instructions for ChatGPT

When the user pastes this repo link into ChatGPT, the first message should be:

> "This is my Rajasthan CET Senior Secondary 2026 preparation repo: https://github.com/lakshrajrao/Rajasthan-CET-Senior-Secondary-2026
> Read AUDIT_BRIEF_FOR_CHATGPT.md and CHATGPT_STUDY_HANDOVER.md first, then teach me one topic at a time in simple Hindi (English exam terms retained), following the teaching sequence in the handover. Use only the repo material for facts. Where the handover says a topic needs additional verified research, research it from a primary or reputable source first and tell me the source. Never present generated questions as PYQs. After each topic, give me a 10–15 question chapter test from the listed MCQ IDs, mark it, explain my mistakes, update the progress tracker, and prepare a topic-wise PDF for me in this conversation."

## 9. What ChatGPT must NOT do

- Do not present the reported 50/10/15/15/15/5/10 subject split as official RSSB weightage.
- Do not present generated (bank/mock) questions as actual PYQs, and do not claim full-paper PYQ analysis (only 139 of 1,800 questions are classified).
- Do not teach Ras/Chhand/Alankar, Trigonometry, Algebra, Logarithms, Internet, E-mail, Cyber-security or AI as 12th-level syllabus — they are Graduation-level (the EXTRA-tagged items are low-priority awareness only).
- Do not change the verified exam pattern (120Q/240/150 min, −2/3, E/blank rules) without primary-source evidence.
- Do not mark tracker rows complete without the work having happened.
- Do not generate duplicate PDFs in the repo — PDFs are created and sent in the conversation.
