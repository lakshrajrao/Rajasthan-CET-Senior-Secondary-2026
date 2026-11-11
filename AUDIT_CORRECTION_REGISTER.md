# Audit Correction Register — Rajasthan CET Senior Secondary 2026

**Repository:** https://github.com/lakshrajrao/Rajasthan-CET-Senior-Secondary-2026
**Audit date:** 11 November 2026 (final QC phase)
**Auditors:** Muse (parent) + two read-only content-audit agents (mock papers; question bank)
**Rule of this register:** no important fact was changed silently. Every correction below lists the file and exact location, the original problem, the correct information, the evidence/source, and its status. Items that could not be verified are listed as OPEN or UNVERIFIED, never dropped.

**Verified baseline (unchanged by this audit — do not alter without primary-source evidence):**
- Exam pattern 2026: **120 questions / 240 marks / 150 min**, +2 per correct answer, **−2/3 per wrong answer** (1/3 of the question's 2 marks), E = deliberate skip = 0, blank (no circle) = −2/3, **>12 blanks (>10%) = disqualified**, blue ball-point pen, +10 min OMR check. Source: RSSB Adv. 08/2026, pp.15–22, RajKaj Ref 22979471 (user-uploaded official extract, SHA-256 `9010141c…c4a48`). See `00_Official_Syllabus_Verification.md`.
- Official scheme gives **NO per-subject question split**. The 50/10/15/15/15/5/10 split is reported/derived only (Adda247/Testbook) and must always be labelled as such.
- 2022/2024 cycles were 150Q/300 marks/3 hrs with NO negative marking — never mix with 2026.

**How to read the status column:** `FIXED` = corrected in this audit and re-verified by an executed check. `DISCLOSED` = not an error; a deliberate design decision recorded here. `OPEN` = needs verified research or a decision; content not invented. `UNVERIFIED` = claim not proven wrong, but no primary source was found in this pass.

---

## A. Pattern / OMR / scoring corrections (29 fixes, all FIXED)

All 29 were applied by script `audit/apply_corrections.py` (all assertions passed) and confirmed by post-fix grep: the only remaining "−1/3" strings in the repo are the legitimate historical mentions in `AUDIT_BRIEF_FOR_CHATGPT.md:50` and the "NOT −1/3" contrast in `INDEX.md:6`.

| # | File : line | Original problem | Correct information | Evidence / source | Status |
|---|---|---|---|---|---|
| A1 | `01_Official_Syllabus_and_Pattern.md:7` | "−1/3" negative marking | "−2/3 (per wrong answer — 1/3 of the question's 2 marks)" | Notification p.15 note 2; p.22 Rule 3 | FIXED |
| A2 | `01_Official_Syllabus_and_Pattern.md:48` | "−1/3" negative marking | Same as A1 | Same as A1 | FIXED |
| A3 | `02_Exam_Pattern_and_Marking_Strategy.md:47` | Sources line: "−1/3 per wrong answer" and "blank = −1/3 of question marks" | Both "−2/3 (1/3 of the question's 2 marks)" (the EV table itself was already correct) | Notification p.22 Rules 2–3 | FIXED |
| A4 | `README.md:29` | "−1/3 negative marking" | "−2/3 negative marking (1/3 of the question's 2 marks)" | Notification p.15 note 2 | FIXED |
| A5 | `research/pyq/pyq_analysis.md:221` | "→ −1/3 per wrong answer" and "a blank costs −1/3" | "−2/3" in both places | Notification p.22 Rule 3 | FIXED |
| A6 | `performance_tracker.csv` (blank example) | "120 − 20×0.333 = 113.33" | "140 − 20 − 20×0.667 = 106.67" (70C/20W/20 blanks; also disqualified, >12 blanks) | Arithmetic from the scheme; Rule 5 | FIXED |
| A7 | `performance_tracker.csv` (EV RULE) | "blank EV = −0.333" | "blank EV = −0.667" | Rule 3 | FIXED |
| A8 | `notes_hindi_english.md:5` (header warning) | Stale "⚠️ VERIFY BEFORE EXAM — pattern discrepancy (150Q?)" flag | Rewritten as superseded/VERIFIED from the official extract | Notification extract pp.15–22 | FIXED |
| A9 | `notes_hindi_english.md:765` and `notes/13_general_english.md:41` (appendix) | "33% par EV ≈ 0" and "kam se kam 2 options eliminate karo" | EV at 1/3 probability = **+0.22**; threshold = "kam se kam **1 option** eliminate" | EV = (1/3×2) − (2/3×2/3) = +0.222; consistent with File 02 / plan / tracker | FIXED |
| A10 | `notes_hindi_english.md:221` and `notes/03_geography_india.md:47` | Railway zones "16 zones (2026 tak)" | **18 zones** (South Coast Railway, Visakhapatnam, 18th zone) | Gazette 4 May 2026; operational 1 June 2026 (Indian Express / Jagran Josh / Adda247) | FIXED |
| A11 | `notes_hindi_english.md:551` and `notes/08_reasoning_mathematics.md:100` | "Ghadi ki suiyan 1 ghante me 11 baar (lagbhag) milti hain" | "**12 ghante me 11 baar**" | Clock arithmetic (11 meetings per 12 h) | FIXED |
| A12 | `INDEX.md:38` | Answer balance stale | "A 74 / B 72 / C 75 / D 79 overall (audit-verified 11 Nov 2026)" | Executed count, `audit/check_consistency.py` | FIXED |
| A13 | `INDEX.md` ("How to use") | Scoring formula missing blank term | Formula now includes "− (Blank×2/3)" | Notification p.22 Rule 3 | FIXED |
| A14 | `notes/12_general_hindi.md` §12.6 and `notes_hindi_english.md:721` (§12.6) | Ras/Chhand/Alankar presented without syllabus status | Heading now labelled "⚠️ EXTRA, 2026 12th-level syllabus me NAHI" | File 00 syllabus (Hindi head has no Ras/Chhand/Alankar) | FIXED |
| A15 | `study_plan_20day.md` (Day 6) | Computer block "internet" taught as in-syllabus | Marked EXTRA / low-priority | File 00 syllabus (Computer head has no Internet) | FIXED |
| A16 | `study_plan_20day.md` (weekly checkpoint) | "all 10 subject areas" | "all 13 syllabus heads" | File 00 (13 heads) | FIXED |
| A17 | `gen.py` (9 spots, lines ~308, 331, 359, 360, 366, 369, 441, 443, 444) | Stale "−1/3" / "−0.333" blank-penalty text and the 113.3 / 6.7-mark-swing worked example | "−2/3" / "−0.667" / 106.7 / 13.3-mark swing | Notification p.22 Rule 3 | FIXED |
| A18 | `performance_tracker.csv` (formula line, OMR rule line, first worked example) | — | Checked: already correct, no change needed | Notification pp.15–22 | FIXED (verified, no edit) |

Notes on A: the tracker formula line, OMR rule line and first worked example were already correct; mock-log dates 22/26/29 Nov + 1 Dec match plan Days 11/15/18/20. `gen_qb.py` / `raj_pool.py` had no such errors.

---

## B. Mock-paper corrections (`mock_papers.md`, all FIXED)

Audit evidence: `audit/mock_audit_findings.md` (302 lines) + per-paper reports `mock_paper1_findings.md`, `mock_paper2_findings.md`, `mock_paper3_findings.md`. All 360 questions checked; every Maths/Reasoning answer recomputed. Fixes applied by `audit/fix_mocks.py` (all assertions passed) and re-verified with `audit/check_mocks.py`: 0 duplicate stems, 0 key-vs-explanation mismatches, keys/explanations complete 1–120 per paper. Key distributions after fixes: P1 A29/B33/C26/D32; P2 A35/B22/C32/D31; P3 **A33/B29/C23/D35** (Q4 flipped B→A).

### B1. Wrong keys (5)

| # | Location | Original problem | Correct information | Evidence / source | Status |
|---|---|---|---|---|---|
| B1.1 | Paper 1, Q114 (Junagarh Fort district) | Options (A) Bikaner and (B) Bikaner — duplicate options; key A meaningless | Option (B) changed to **Jodhpur**; key A (Bikaner) now unique | Question text itself (duplicate visible) | FIXED |
| B1.2 | Paper 2, Q47 (average of 18 & 27) | Keyed 22; correct average 22.5 was not among the options | Option (C) changed to **22.5**; explanation "(18+27)/2 = 22" → "= 45/2 = 22.5". Key C unchanged | Arithmetic (45/2 = 22.5) | FIXED |
| B1.3 | Paper 2, Q109 (average of 30 & 45) | Keyed 37; correct average 37.5 was not among the options | Option (B) changed to **37.5**; explanation → "75/2 = 37.5". Key B unchanged | Arithmetic (75/2 = 37.5) | FIXED |
| B1.4 | Paper 3, Q4 (largest port by cargo) | Key B wrong; option B named two ports; stem carried the stray fragment "The 'Silk Route' — no:" | Stem reworded to "India's largest **major port by cargo handled**"; option (B) = JNPT only; **key B → A (Paradip)**; explanation rewritten with FY 2024-25 figures: Paradip 150.41 MMT vs Deendayal (Kandla) 150.16 MMT; JNPT (92.12 MMT) leads only in container traffic; private port Mundra handles more overall, so the question is about major ports | Auditor's published figures (see findings §A4); stem/option text itself | FIXED |
| B1.5 | Paper 3, Q100 (average of 50 & 75) | Keyed 62; correct average 62.5 was not among the options | Option (A) changed to **62.5**; explanation → "125/2 = 62.5". Key A unchanged | Arithmetic (125/2 = 62.5) | FIXED |

The three average errors (B1.2, B1.3, B1.5) are the same slip: an odd sum with the .5 dropped. They were fixed by re-optioning, not just re-keying.

### B2. Wrong / inadequate explanations (13 with correct keys + B1.4/B1.5 above)

| # | Location | Original problem | Correct information | Evidence / source | Status |
|---|---|---|---|---|---|
| B2.1 | Paper 1, Q13 (Ana Sagar) | Explanation copied verbatim from Q35 (builder facts, no location) | "Ana Sagar Lake is in Ajmer (built by Anaji/Arnoraja Chauhan; Daulat Bagh added by Jahangir)." | Standard GK (Ana Sagar, Ajmer) | FIXED |
| B2.2 | Paper 1, Q50 (Jaisalmer Fort) | Explanation copied from Q118 (generic fort facts, no builder) | "Founded by Rawal Jaisal in 1156; a living fort of golden sandstone, among the UNESCO Hill Forts of Rajasthan." | Standard GK | FIXED |
| B2.3 | Paper 1, Q60 (Kumbhalgarh Fort) | Explanation copied from Q58 (wall/birthplace, no builder) | "Built by Maharana Kumbha in the 15th century (c. 1443–1458); ~36 km wall, commonly described as second-longest after the Great Wall; Maharana Pratap born there (1540)." | Standard GK | FIXED |
| B2.4 | Paper 2, Q16 (Rana Sanga) | Explanation copied from Q39 (battle only, no reign/state) | "Rana Sanga ruled Mewar 1508–1528; fought Babur at Khanwa (1527) leading a Rajput confederacy." | Standard GK | FIXED |
| B2.5 | Paper 2, Q75 (Udai Singh II) | Explanation copied from Q92 (Udaipur founding only, no reign) | "Udai Singh II ruled Mewar 1540–1572; founded Udaipur (1559); shifted capital from Chittorgarh after Akbar's 1567–68 siege." | Standard GK | FIXED |
| B2.6 | Paper 2, Q52 (Pushkar Lake) | Explanation copied from Q41 (generic lake facts, no district) | "Pushkar Lake is in Ajmer district; sacred lake with the Brahma temple nearby and the Kartik Purnima Pushkar Fair." | Standard GK | FIXED |
| B2.7 | Paper 2, Q51 (Mahi river terminus) | Explanation omits the terminus (dam only) | "The Mahi flows through MP, Rajasthan and Gujarat and empties into the Gulf of Khambhat (an inlet of the Arabian Sea) — hence 'Gulf of Khambhat', not 'Arabian Sea directly'." | Standard geography | FIXED |
| B2.8 | Paper 2, Q81 (Sabarmati river terminus) | Explanation omits the terminus | "The Sabarmati (short course in Rajasthan, then Gujarat) empties into the Gulf of Khambhat." | Standard geography | FIXED |
| B2.9 | Paper 2, Q87 (Kali Sindh river terminus) | Explanation omits the terminus | "The Kali Sindh (origin Dewas, MP; flows through Jhalawar-Kota) joins the Chambal in Rajasthan." | Standard geography | FIXED |
| B2.10 | Paper 2, Q89 (Chittorgarh Fort) | "Jauhar of Rani Padmini (1303)" presented as dated fact | "Jauhar of 1535 under Rani Karnavati. (The 1303 'Rani Padmini' story is from Jayasi's Padmavat legend, not verified history.)" | Padmavat (c.1540) is a literary work; attested jauhar is 1535 | FIXED |
| B2.11 | Paper 3, Q50 (Junagarh Fort builder) | Explanation names no builder (generic fort facts) | "Built by Raja Rai Singh of Bikaner, 1589–94; a ground-level fort (not on a hill), never conquered; Anup Mahal inside." | Standard GK | FIXED |
| B2.12 | Paper 3, Q57 (Ganga Singh) | Explanation copied from Q41 (canal/Versailles only, no reign/state) | "Maharaja Ganga Singh ruled Bikaner 1888–1943; built the Ganga Canal (1927, from the Sutlej) and represented India at Versailles (1919)." | Standard GK | FIXED |
| B2.13 | Paper 3, Q85 (Chittorgarh Fort) | "Jauhar of Rani Padmini (1303)" presented as dated fact | "Jauhar of 1303 (Alauddin Khalji's siege) and of 1535 under Rani Karnavati. ('Rani Padmini' is the Padmavat legend, not verified history.)" | Same as B2.10 | FIXED |

### B3. Ambiguous / two-correct (4, plus B1.4)

| # | Location | Original problem | Correct information | Evidence / source | Status |
|---|---|---|---|---|---|
| B3.1 | Paper 1, Q10 (Hindi sarvanam) | Stem "'जो पढ़ेगा, वह सफल होगा।' — सर्वनाम है —" — both जो and वह are pronouns | Stem reworded: "'जो' किस प्रकार का सर्वनाम है?" (key D, संबंधवाचक, now unique) | Hindi grammar (जो = relative, वह = personal) | FIXED |
| B3.2 | Paper 1, Q81 (highest peak in India) | "Highest peak in India" — Kangchenjunga vs K2 (in PoK, claimed by India) | Stem qualified: "highest peak located within India's undisputed territory"; option (B) = "Kangchenjunga (8,586 m, Sikkim)" | Kangchenjunga 8,586 m; K2 8,611 m in PoK | FIXED |
| B3.3 | Paper 2, Q46 (सत्य का विलोम) | Option (C) झूठ is also a valid antonym of सत्य (keyed A असत्य) | Option (C) replaced with **सुंदर** (unrelated word); key A unchanged | Hindi usage (झूठ = false, valid antonym) | FIXED |
| B3.4 | Paper 3, Q88 (Chambal "longest river") | Unqualified "Longest river of Rajasthan" conflicts with Q7 (Banas = longest flowing entirely within Rajasthan) | Option (D) and explanation qualified: "Longest river (**by total course**, ~1,024 km)"; explanation notes Banas (~512 km) is the longest river flowing *entirely within* Rajasthan (see Q7). Key D unchanged | Chambal ~1,024 km total course; Banas ~512 km intra-state | FIXED |

### B4. Out-of-syllabus in mocks (3)

| # | Location | Original problem | Correct information | Evidence / source | Status |
|---|---|---|---|---|---|
| B4.1 | Paper 1, Q52 (WWW full form) | Internet topic — Graduation-level, not in 2026 12th syllabus | Tagged **[EXTRA — Internet topic, NOT in 2026 12th syllabus; PYQ-style awareness only]** in the question header and explanation. Key D (World Wide Web) is factually correct | File 00 syllabus (Computer head has no Internet) | FIXED (tagged, kept) |
| B4.2 | Paper 1, Q56 (E-mail full form) | E-mail topic — Graduation-level, not in 2026 12th syllabus | Tagged **[EXTRA — E-mail topic, NOT in 2026 12th syllabus; PYQ-style awareness only]**. Key A (Electronic Mail) correct | File 00 syllabus | FIXED (tagged, kept) |
| B4.3 | Paper 3, Q116 (email address @) | E-mail topic — Graduation-level, not in 2026 12th syllabus | Tagged **[EXTRA — E-mail topic, NOT in 2026 12th syllabus; PYQ-style awareness only]**. Key B (@) correct | File 00 syllabus | FIXED (tagged, kept) |

Kept (not deleted) so each paper stays at 120 questions and the facts remain available as low-priority awareness — the 2024 paper did ask HTTP. No Trigonometry, Algebra, Logarithm, Cyber-security or AI question exists anywhere in the mocks. Paper 2 has zero out-of-syllabus questions.

### B5. Minor wording (12)

| # | Location | Original problem | Correction | Status |
|---|---|---|---|---|
| B5.1 | Paper 1, Q86 | Option (B) "The (only)" — editorial aside inside an option | "The" | FIXED |
| B5.2 | Paper 1, Q117 | Option (C) "She-lion (not standard)" — editorial aside inside an option | "She-lion" | FIXED |
| B5.3 | Paper 1, Q55 (Chiranjeevi) | Explanation ended with an open "Verify current name/limit" note | Explanation now states the history (cover raised to ₹25 lakh per family per year, 2023; renamed Mukhyamantri Ayushman Arogya Yojana, 2024) with "(current limit — re-check before the exam; see audit register)" | FIXED (see §H) |
| B5.4 | Paper 1, Q74 (largest district) | "Dholpur smallest (before 2023 changes)" — dated hedge | "Dholpur smallest (33 districts after the Dec 2024 reorganisation — re-check the current list before the exam)" | FIXED (see §H) |
| B5.5 | Paper 2, Q7 | Stem "The 'Bhakti' — no: Bhakra Dam is on which river?" — garbled fragment | "Bhakra Dam is on which river?" | FIXED |
| B5.6 | Paper 2, Q50; Paper 2, Q77; Paper 3, Q22 | "for 1 years" (3 occurrences) | "for 1 year" | FIXED |
| B5.7 | Paper 2, Q100 | Stem "sum ×? — CAT letters sum=24" — stray notation | "(C=3,A=1,T=20; letters sum to 24)" | FIXED |
| B5.8 | Paper 2, Q37 (Jaisamand) | Option (C) "Udaipur (Salumbar)" — confusing after district changes | "Salumbar (formerly Udaipur district)" | FIXED |
| B5.9 | Paper 3, Q17 | Stem "Choose the correctly spelt word — (2):" — stray "(2)" | Numbered "— (1):" (see B5.10) | FIXED |
| B5.10 | Paper 3, Q93 | Identical stem to Q17 ("Choose the correctly spelt word:") — duplicate stems created when B5.9 was first fixed | Numbered "— (2):". `check_mocks.py` now reports 0 duplicate stems within and across papers | FIXED |
| B5.11 | Paper 3, Q4 | Stray "The 'Silk Route' — no:" fragment in stem | Deleted (see B1.4) | FIXED |

### B6. Mock-paper header disclosure (added)

`mock_papers.md` header now states: the 11 Nov 2026 audit corrected 5 wrong keys, 13 wrong explanations, 4 ambiguous wordings and 3 out-of-syllabus questions (see this register); [EXTRA]-tagged questions are Graduation-level / PYQ-awareness only; ~39 mock questions test the same facts as the 300-MCQ question bank — kept deliberately as revision overlap (see §E).

---

## C. Question-bank corrections (`question_bank.csv` + `question_bank/*.csv`, all FIXED)

Audit evidence: `audit/qb_audit_findings.md`. All 300 rows read in full; every Maths answer recomputed; every Reasoning item solved; Science, Computer, Public Health and Current Affairs checked row by row. Fixes applied by `audit/fix_qb.py` (all assertions passed); post-fix `audit/check_consistency.py` reports 0 FAILs and combined vs per-subject files in sync (300 = 300, 0 differing rows). Answer distribution unchanged: A74/B72/C75/D79, E 0.

| # | Row (qid) | File(s) | Original problem | Correct information | Evidence / source | Status |
|---|---|---|---|---|---|---|
| C1 | `12_GENERAL_HINDI-015` | `question_bank.csv`, `question_bank/12_general_hindi.csv` | 'Neelkanth' keyed D — Karmadharaya. No correct option existed: the standard answer is Bahuvrihi, which was not among the options. The bank's own explanation conceded this ("Bahuvrihi arth bhi hota hai") and asserted without evidence that "pariksha me Karmadharaya mana jata hai" | Option (D) replaced with **Bahuvrihi**; key D now correct. Explanation rewritten: "Neelkanth (neela kanth wala — Shiv) — samas kisi teesre (Shiv) ko darshata hai, isliye Bahuvrihi samas hai. (Dashanan, Lambodar bhi isi prakar Bahuvrihi hain.)" | NCERT / standard Hindi vyakaran: 'Neelkanth', 'Dashanan', 'Chaturbhuj', 'Lambodar' are textbook Bahuvrihi. The bank itself keys 'Dashanan' as Bahuvrihi (`12_GENERAL_HINDI-005`) — the old key was internally inconsistent | FIXED |
| C2 | `13_GENERAL_ENGLISH-005` | `question_bank.csv`, `question_bank/13_general_english.csv` | Stem "'A person who loves himself'" — two defensible answers: Egoist (C) and Narcissist (A, keyed). Explanation conceded "Egoist bhi paas hai" without citing any exam key | Stem reworded to "'A person who **admires himself excessively**'"; key A (Narcissist) now uniquely correct. Explanation: "Egoist = one who loves himself / self-centred; Narcissist = excessive self-admiration." | Standard dictionaries: egoist = self-centred person; narcissist = excessive interest in/admiration of oneself | FIXED |
| C3 | `08_REASONING-021` | `question_bank.csv`, `question_bank/08_reasoning.csv` | Seating question asked "A ke dayein dusra kaun hoga" but gave **no seating arrangement** — unsolvable as asked | Stem rewritten as a convention question: "Vritt me kendra ki ore munh karke baithe vyakti ka 'dayein' kis disha me hota hai?" Key D (anticlockwise) unchanged; difficulty Hard → Medium | Reasoning from the stem itself (no positions given); convention: facing the centre, right = anticlockwise | FIXED |
| C4 | `06_ECONOMY_RAJASTHAN-004` | `question_bank.csv`, `question_bank/06_economy_rajasthan.csv` | Bhilwara epithet: option (B) "Textile City of India" is also a valid description of Bhilwara (keyed D "Manchester of Rajasthan") | Option (B) replaced with **"Sun City"** (Jodhpur's epithet — clearly wrong for Bhilwara). Key D unchanged | Bhilwara's textile industry makes both epithets common in GK material | FIXED |
| C5 | `08_REASONING-020` | `question_bank.csv`, `question_bank/08_reasoning.csv` | Option (C) read "Koi A, B nahi hai — galat" — meta-commentary inside the option | Option (C) = "Koi A, B nahi hai". Key A correct (from "All A are B", "All B are A" does not follow) | Syllogism logic | FIXED |
| C6 | `08_REASONING-024` | `question_bank.csv`, `question_bank/08_reasoning.csv` | Exam tip presented as a reasoning question ("which option is usually wrong in assumption questions?") — heuristic, not a fact; unfalsifiable | **Replaced with a real assumption item:** "Kathn: 'Rajasthan ke sabhi jilon me khel maidan banaye jayenge.' — Is kathn me kaun si purvadharana antarnit hai?" Key A ("Khel maidan banane se khel pratibha badhegi"). B is false (grounds already exist); C and D do not follow | Standard statement–assumption format | FIXED |
| C7 | `13_GENERAL_ENGLISH-020` | `question_bank.csv`, `question_bank/13_general_english.csv` | Study advice presented as an English question ("what to do first in Reading Comprehension?") — no unique factual answer | **Replaced with a real comprehension item:** short passage on the camel ("ship of the desert") + "Camel ko 'ship of the desert' kyun kaha jata hai?" Key A ("It carries people and loads across the desert") | Passage-based comprehension; answer is stated in the passage | FIXED |
| C8 | `13_GENERAL_ENGLISH-005` (stem tag) | Same files as C2 | Stem carried the tag "(2024 PYQ)" — unverified provenance; the bank is generated questions and the PYQ dataset has no question text to confirm it | Tag **removed** from the stem (found during fix application, not in the audit report) | User's standing rule: keep actual PYQs separate from generated questions; no evidence this item is a 2024 PYQ | FIXED |

---

## D. Checker fix (FIXED)

| # | File | Original problem | Correction | Status |
|---|---|---|---|---|
| D1 | `audit/check_consistency.py` (mock duplicate-stem check) | Regex `^\*\*Q\d+…` matched **explanation** lines too ("**Q12. Answer A** — …"), so 8 identical explanation fragments were misreported as "duplicate mock question stems: 8" | Regex restricted to question lines only (`^\*\*Q\d+\.\s*\[…\]` — the tag bracket after the Q number). Re-run: **0 FAILs** in `automated_checks_report.txt`; `check_mocks.py` independently confirms 0 duplicate stems | FIXED |

---

## E. Disclosed design notes (not errors — DISCLOSED)

| # | Item | Detail | Decision |
|---|---|---|---|
| E1 | Mock ↔ bank near-duplicates | **39 strong + 3 weaker** near-duplicates between the 360 mock questions and the 300-MCQ bank (P1 19+3, P2 9, P3 11; full ID mapping in `audit/mock_audit_findings.md` §E). 0 exact stem duplicates (mechanically verified). The bank itself asks PM-JAY ₹5 lakh twice (`06_ECONOMY_RAJASTHAN-014` and `10_PUBLIC_HEALTH-001`) | Kept deliberately as **revision overlap** (same fact, usually a different angle). Disclosed in the mock header, here, and in the handover. ChatGPT may replace them during teaching if it prefers fresh items — it must not silently present them as new facts |
| E2 | Within-paper repetition (mocks) | P1: SI ×4; P2: SI ×6, Average ×3; P3: Average ×4, SI ×3, discount ×2 — plus paired fact-questions listed in `audit/mock_audit_findings.md` §F1 (e.g. P3 Q27/Q87, Q23/Q82, Q2/Q104, where one question's explanation effectively answers another) | Kept; recorded as a **design weakness**. Chapter tests prepared by ChatGPT should vary the numbers/facts rather than repeat these clusters |
| E3 | Bank cross-subject duplicate pairs (3) | `03_GEOGRAPHY_INDIA-020` vs `06_ECONOMY_RAJASTHAN-013` (PM-KISAN ₹6,000/year); `06_ECONOMY_RAJASTHAN-014` vs `10_PUBLIC_HEALTH-001` (PM-JAY ₹5 lakh/family/year — near-identical); `07_EVERYDAY_SCIENCE-029` vs `10_PUBLIC_HEALTH-007` (malaria via Anopheles). All answers correct and consistent — effectively 297 distinct facts, not 300 | Kept as **cross-subject revision**; noted here and in the handover. No key/explanation change needed |
| E4 | 10 Computer EXTRA rows in the bank | `11_COMPUTER_KNOWLEDGE-007, 008, 009, 010, 011, 012, 013, 015, 016, 017` (WWW, SMTP, binary, LAN, phishing, firewall, e-Mitra, UPI, Jan Aadhaar) are the **ONLY** out-of-syllabus rows in the bank (audit-verified); all facts correct | Kept, labelled "EXTRA — not in 2026 12th syllabus (PYQ-style general awareness)" in the subtopic field. Low priority only |

---

## F. Verified correct in this audit (PASS — no change needed)

- **Exam pattern & OMR rules:** 120Q/240/150 min, −2/3, E/blank/disqualification rules — verified from the official extract (File 00). No change.
- **Mock structure:** each paper 120 questions numbered 1–120, all A–E options, key tables complete 1–120, explanations complete 1–120, 0 key-vs-explanation letter mismatches, 0 duplicate stems, 0 mock stems in the bank.
- **Bank structure:** 300 rows; combined CSV matches the 14 per-subject CSVs exactly; 0 duplicates; 0 E-correct; distribution A74/B72/C75/D79; option E identical on all rows (the "Unattempted" instruction text).
- **PYQ framing:** `research/pyq/pyq_inventory.md` and `pyq_analysis.md` correctly frame the 139-question sample as a sample (7.7% of the 1,800-question pool: Q1–30 of 2024 Phases 1–4 + Q1–20 of 2023 11 Feb Shift 2 minus Q16; per-shift counts 30/30/30/30/19). No false full-paper claim. The dataset has **no question-text column — classification metadata only** (limitation, not an error).
- **Bank content spot-checks that passed:** all 24 Maths rows recomputed (0 errors); all 24 Reasoning rows solved (0 wrong keys apart from §C3/C5/C6); all 36 Science rows (0 errors); all 14 Public Health rows (0 errors); all 18 Computer rows (0 wrong keys); History/Art/Geography/Polity rows read against standard GK (0 errors); Hindi rows except C1 (0 errors); English rows except C2/C7 (0 errors).
- **Current Affairs spot-checks (web-verified 11 Nov 2026):** CWG 2026 Glasgow India 4th, 39 medals (13G/17S/9B); Asian Games 2026 India 4th, 85 medals (21/27/37), women's hockey gold after 44 years (1982→2026); Asian Para Games 2026 India 4th, record 114 medals (30/35/49), previous best Hangzhou 108; Nobel 2026 — Medicine Deisseroth/Hegemann/Nagel (optogenetics), Physics Francis Halzen (IceCube), Chemistry Kagan/Soai, Literature Anne Carson, Peace Navi Pillay, Economics Hall/Woodford; ISRO NVS-03 on GSLV-F18, 30 Oct 2026; Ashoke Sen Oskar Klein Medal, first Indian, lecture 22 Oct 2026; Ajit Doval Lokmanya Tilak National Award, 1 Aug 2026; National Sports Awards 2025 announced 18 Aug 2026, 17 Arjuna awardees, no Khel Ratna; **V. Srinivas is Rajasthan Chief Secretary** (took charge 17 Nov 2025, succeeding Sudhansh Pant; extension to 28 Feb 2027); Ahmedabad = CWG 2030 host; 1 Jan 2026 = Thursday; all 20 study-plan weekdays verified correct via `date`.
- **Notes spot-checks that passed:** History integration dates (Matsya Sangh 17 Mar 1948 … 1 Nov 1956); Science formulas/facts (1 HP = 746 W, sound 343 m/s, 206 bones, O donor/AB recipient, Project Tiger 1973); Maths solved examples recomputed correct (LCM 36, cylinder 1540, SI/CI diff ₹100, successive −4%, ranking 29th, direction √10 km NE, clock 90° at 3:00); English one-word set; Geo Raj Census 2011 figures; Polity amendments table.
- **Study plan:** 12 Nov–1 Dec 2026 (20 days); mocks Days 11/15/18; Day 20 full mock + OMR drill; all weekdays verified.

---

## G. OPEN — coverage gaps (need verified research; do NOT invent content)

These syllabus topics are missing or thin in the notes and/or question bank. They are listed in `study_progress_tracker.csv` as Research verified = No/Partial and Revision required = Yes. ChatGPT must research each from a primary or reputable source before teaching it, and must not present generated material as verified fact.

| # | Subject | Missing / thin topic | Detail |
|---|---|---|---|
| G1 | Public Health | **First Aid & CPR** | Notes: CPR is one line. Bank: **zero** questions. Needs: detailed First Aid steps; CPR steps (30:2 compression-to-ventilation ratio, 100–120 compressions/min — standard guidance, to be verified before teaching) |
| G2 | Public Health | **Drug abuse types & prevention** | No coverage in notes or bank (grep confirms) |
| G3 | Public Health | **Social-media addiction risks & prevention** | No coverage in notes or bank (grep confirms) |
| G4 | Public Health | **Youth physical & mental fitness** | No coverage in notes or bank |
| G5 | Everyday Science | Oxidation/reduction + catalyst; allotropes (diamond/graphite); Indian space programme/ISRO; genetics/Mendel; biotechnology; economic importance of plants/animals | Missing from notes (Science spot-checks passed for covered topics only) |
| G6 | Geography of India | Dams, lakes & oceans; wildlife & sanctuaries; disaster management & climate change (NEW 2026) | Missing from notes |
| G7 | Geography of Rajasthan | Livestock; major tribes (Bhil, Meena, Garasia); tourism | Missing from notes |
| G8 | Indian Political System | Supreme Court detail; Election Commission detail (both Partial); State Information Commission / State Human Rights Commission detail (missing) | Thin/missing in notes |
| G9 | Economy of Rajasthan | VB-G RAM G (NEW 2026); unemployment; drought & famine; financial institutions; PRI role in rural development; animal husbandry detail (Partial) | Missing/thin in notes |
| G10 | General Hindi | Sangya/sarvanam/visheshan/avyaya detail (Partial); shabd-yugm; shabd-shuddhi; vakya-shuddhi; Hindi equivalents of English technical terms; office letters | Missing/thin in notes |
| G11 | General English | Translation Hindi↔English; official & technical terms; letter writing; determiners detail (Partial) | Missing/thin in notes |
| G12 | Logical Reasoning & Mathematics | Ellipse area formula (πab) | Missing from notes (other areas covered) |
| G13 | History of Rajasthan | Tribal movements detail | Thin in notes |
| G14 | Art & Culture of Rajasthan | Dresses/ornaments/customs; theatre | Missing from notes (theatre thin) |
| G15 | Computer Knowledge | File-system coverage | Thin in notes (acceptable, noted as thin) |
| G16 | Current Affairs | Events after 11 Nov 2026 | Needs a pre-exam update (last week before the exam) |

---

## H. UNVERIFIED — not proven wrong, needs a primary-source check before being taught as fact

| # | Item | Why unverified |
|---|---|---|
| H1 | Mock-paper superlatives (12 items) | Jaisamand "largest artificial lake"; Nakki Lake claims; Raj Prashasti; "never conquered" Junagarh; post-2024 district lists (Deeg/Phalodi/Kotputli-Behror/Khairthal-Tijara); VB-G RAM G Act 2025 currency (matches Dec 2025 legislation replacing MGNREGA with 125-day guarantee — re-check against gazette before exam); Chiranjeevi current limit (see B5.3); spelling/builder details. None flagged as wrong |
| H2 | Bank: `06_ECONOMY_RAJASTHAN-005` | Rajasthan renewable ~51.6 GW / solar ~45 GW (Nov 2026) — directionally plausible (Rajasthan leads India in solar), exact figures unverified |
| H3 | Bank: `06_ECONOMY_RAJASTHAN-006` | Mukhyamantri Yuva Swarojgar Yojana: 100% interest subsidy on loans up to ₹10 lakh |
| H4 | Bank: `06_ECONOMY_RAJASTHAN-007` | Lakhpati Didi loan limit raised to ₹1.5 lakh in Budget 2026-27 |
| H5 | Bank: `06_ECONOMY_RAJASTHAN-008` | Gargi Puraskar: 3.63 lakh girls, ₹109 crore (CM speech 3 Nov 2026) |
| H6 | Bank: `06_ECONOMY_RAJASTHAN-016` | Thar Cultural Circuit ₹5,000 crore in Budget 2026-27 |
| H7 | Bank: `06_ECONOMY_RAJASTHAN-017` | Uniform/Bag DBT ₹800/student; 66 lakh students, ₹482 crore by Nov 2026 |
| H8 | Bank: `09_CURRENT_AFFAIRS-010` | Rajasthan RE-SAF National Award on 6 Nov 2026 (presented by VP C.P. Radhakrishnan — his being VP is correct) |
| H9 | Bank: `09_CURRENT_AFFAIRS-011` | 235 medal-winning athletes approved for government jobs in Nov 2026 (9 DSP, 2 Excise, 224 others; 73 para-athletes) |
| H10 | Bank: `09_CURRENT_AFFAIRS-015` | 'Sapnon Ki Udaan' programme on 1 Nov 2026; ₹74 crore+ pension DBT |
| H11 | Bank: `09_CURRENT_AFFAIRS-016` | National Sports Awards 2025: 17 Arjuna awardees, announced 18 Aug 2026 |
| H12 | Notes: RBI repo rate 5.50% (Oct 2026) | Flagged "verify before exam" in the notes; NOT independently re-verified in this QC |
| H13 | Notes: district count post-2023–24 reorganisation; Rajya Pashu Chinkara vs Unt (2014); Jaisamand "Asia's largest artificial lake"; Panchayat women-reservation % | Already-flagged ambiguities from the notes audit; still unresolved |
| H14 | Qualifying marks 40% (96/240), 35% SC/ST (84/240); score valid 3 years | REPORTED, not verified from the official extract — verify on the admit card |

---

## I. Unresolved / standing items

| # | Item | Status |
|---|---|---|
| I1 | RSSB live-site verification | **FAILED 11 Nov 2026, 13:49–14:00 IST** — rssb.rajasthan.gov.in timed out repeatedly (ERR_TIMED_OUT, not a CAPTCHA/block); address confirmed correct via Bing (site has a Latest News item dated 06-11-2026). No live-site verification obtained; retry later. This does NOT weaken the pack — pattern/syllabus/OMR rest on the user-uploaded official extract (pp.15–22, RajKaj 22979471) |
| I2 | PYQ coverage | Only the 139-question sample is classified (7.7% of the 1,800-question pool). 2024 P5/P6 (24 Oct) located but not classified; no official RSSB key PDF downloaded (2024 answers via ShikshaNagari "as per official key"; 2023 via Examzy unofficial key). Two questions excluded for bad published answers (2024-P1 Q31 garbled; 2023-S2 Q16 physically wrong); 2024-P4 Q6 flagged. Dataset has classification metadata only, no question text |
| I3 | Current Affairs after 11 Nov 2026 | Needs a pre-exam update (see G16) |
| I4 | Near-duplicate policy (mocks ↔ bank) | Decided and disclosed (§E1–E3); no silent replacement. If ChatGPT replaces them during teaching, the register must be updated |
| I5 | Mock-paper design weakness | Within-paper SI/Average repetition (§E2) — not fixed; ChatGPT should vary numbers/facts in chapter tests |

---

## J. Audit method summary

- **Automated checks (executed):** `audit/check_consistency.py` — question_bank.csv 300 rows, 0 duplicates, 0 E-correct, distribution A74/B72/C75/D79; combined = per-subject files exactly; PYQ dataset 139 rows, 0 duplicate (Year, Shift, Question_ID), difficulty Easy 63/Medium 59/Hard 17; mock papers structurally clean (see §F). `audit/check_mocks.py` — 360 questions, 0 duplicates, 0 key-vs-explanation mismatches. Final run after all fixes: **0 FAILs** in `audit/automated_checks_report.txt`.
- **Content audits (executed, read-only):** mock papers — all 360 questions, every Maths/Reasoning answer recomputed (`audit/mock_audit_findings.md` + per-paper reports). Question bank — all 300 rows read in full (`audit/qb_audit_findings.md`).
- **Web verifications (executed 11 Nov 2026):** CA spot-checks in §F; railway zones (A10); Nobel 2026; ISRO NVS-03; Rajasthan Chief Secretary; exam-date press notes.
- **Not done (and not claimed):** full 900+900Q PYQ classification; live RSSB site verification (I1); exhaustive per-topic verification of every notes line (spot-checks only — see `study_progress_tracker.csv` for the per-topic status).

---

## K. Learning methodology adoption (11 Nov 2026 — permanent standard)

- **What changed:** `LEARNING_METHODOLOGY.md` created as the permanent teaching/note standard. Research foundation read in full 11 Nov 2026: Weinstein, Madan & Sumeracki (2018, PMC5780548 — six strategies); Dunlosky et al. (2013) + Frontiers meta-analysis 2021 (242 studies, 1,619 effects, 169,179 participants, mean d = 0.56 — distributed practice + practice testing most effective; mnemonics/imagery/re-reading low utility); Carpenter et al. (2022, Nature Reviews Psychology s44159-022-00089-1 — spacing + retrieval in classrooms); Castro-Alonso et al. (2021, PMC7940870 — multimedia, split-attention, coherence, signaling, segmenting). The methodology states the honest limits (mnemonics supplementary only; no learning-styles claim; no score guarantee).
- **Pilot samples (audited, `samples/SAMPLE_AUDIT.md`):** History — Integration of Rajasthan; Science — Blood groups & transfusion. Both follow the A–K structure; all dates/names/mechanisms fact-checked (7 integration stages verified via Testbook + rajras.in; blood-group facts via standard references). **Verdict: PASS.** Two minor issues found and fixed: an unsupported superlative ("most prestigious state" → "among the most senior and prestigious"); genotype rules stated without exception → Bombay blood group (hh) noted as beyond-syllabus.
- **MCQ explanation pilot (60 rows, `LEARNING_METHODOLOGY.md` §4 format):** all 24 History + all 36 Science bank rows rewritten — `Sahi: … | Galat kyun: … | Concept: … | Yaad rakhne ke liye: … | Source: …`. No keys changed; no questions changed; only explanations. Verified: all 60 rows carry all 5 segments; automated checks re-run after the pilot — **0 FAILs**; combined CSV = per-subject CSVs still in sync.
- **Docs updated:** `INDEX.md` (file table + methodology section), `README.md` (Start-here + Contents), `CHATGPT_STUDY_HANDOVER.md` (new §3A + §3 item 1 + §8 first message now includes `LEARNING_METHODOLOGY.md` + §9 rule), master notes pointer (see below).
- **Master notes:** a pointer to `LEARNING_METHODOLOGY.md` + the samples was added to `notes_hindi_english.md`; the full A–K rewrite of the master notes and the remaining 11 subject notes is **pending** (rollout after the sample audit — see `LEARNING_METHODOLOGY.md` §8).
- **Pending rollout:** remaining 240 bank MCQs + 360 mock explanations to the §4 format; remaining 11 subject notes to A–K; master notes to A–K.
