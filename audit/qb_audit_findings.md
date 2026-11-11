# Question Bank Audit — Findings

**Scope:** `question_bank.csv` (300 rows) + `question_bank/*.csv` (14 per-subject files, same 300 rows), under `~/workspace/cet-2026-upload/`.
**Audit date:** 11 Nov 2026. **Method:** all 300 rows read in full. Every Maths answer recomputed; every Reasoning item solved; Science, Computer, Public Health and Current Affairs checked row by row. 2026-dated Current Affairs claims and Rajasthan Budget 2026-27 figures were checked by web search (search results cited in the evidence lines). Where a fact could not be verified from knowledge or search, it is marked **unverified**, not guessed.
**Files NOT edited.** This is a read-only audit.

## Confirmed problems

### 1. Wrong key — Hindi samas (Neelkanth)

- **qid:** `12_GENERAL_HINDI-015`
- **File:** `question_bank.csv` and `question_bank/12_general_hindi.csv`
- **Question (short):** 'Neelkanth' me kaun sa samas hai? Keyed answer: D — Karmadharaya.
- **What is wrong:** The standard Hindi-grammar answer is **Bahuvrihi** samas. 'Neelkanth' (neela kanth wala = Shiv) is the textbook example of Bahuvrihi, where the compound refers to a third entity (Shiv) rather than to the throat itself. The bank's own explanation concedes this ("Bahuvrihi arth bhi hota hai") and then asserts, without evidence, that "pariksha me Karmadharaya mana jata hai".
- **Correct answer/fact:** **A — Tatpurush is wrong; the correct option among those given is not present.** Among the options (A Tatpurush, B Dvandva, C Dvigu, D Karmadharaya), none is Bahuvrihi, so the item as written has **no correct option**. The question must be rewritten (replace one distractor with Bahuvrihi and key it) or dropped.
- **Evidence/reasoning:** NCERT/standard Hindi vyakaran classifies 'Neelkanth', 'Dashanan', 'Chaturbhuj', 'Lambodar' as Bahuvrihi. The bank itself keys 'Dashanan' as Bahuvrihi (`12_GENERAL_HINDI-005`) — internally inconsistent with keying 'Neelkanth' as Karmadharaya, since both are the same construction (adjective + body part denoting a deity).

### 2. Ambiguous — English one-word substitution (self-love)

- **qid:** `13_GENERAL_ENGLISH-005`
- **File:** `question_bank.csv` and `question_bank/13_general_english.csv`
- **Question (short):** 'A person who loves himself' — one word? Keyed answer: A — Narcissist.
- **What is wrong:** Two options are defensible. In standard one-word-substitution lists used in Indian exams, "one who loves himself" is **Egoist** (option C); "Narcissist" is one who admires himself excessively / has excessive self-love, and is the clinical/psychological term. The bank's own explanation concedes this ("Egoist bhi paas hai, par exam me Narcissist sahi mana jata hai") without citing any exam key.
- **Correct answer/fact:** The item is ambiguous as written. Either reword the stem to "one who admires himself excessively" (then Narcissist is uniquely correct) or key Egoist for the current stem.
- **Evidence/reasoning:** Standard dictionaries: egoist = a self-centred or selfish person; narcissist = a person with excessive interest in/admiration of themselves. The stem "loves himself" matches Egoist more directly; Narcissist requires "excessively/admires".

### 3. Ambiguous — Reasoning seating question with no arrangement

- **qid:** `08_REASONING-021`
- **File:** `question_bank.csv` and `question_bank/08_reasoning.csv`
- **Question (short):** "Seating: 6 log vritt me kendra ki ore baithe hain. A ke dayein dusra kaun hoga — dayein ka matlab?" Keyed answer: D — Ghadi ki vipreet disha (anticlockwise).
- **What is wrong:** The stem asks who sits second to A's right but **gives no seating arrangement at all** — there is no person to identify. The item actually tests the convention that "right" for a person facing the centre is anticlockwise, but it is framed as a seating-arrangement question with no arrangement. A candidate cannot solve it as asked.
- **Correct answer/fact:** The convention stated in the key (D) is correct: facing the centre, a person's right is anticlockwise. The question must be rewritten, e.g. "Vritt me kendra ki ore munh karke baithe vyakti ka 'dayein' kis disha me hota hai?" — then D is uniquely correct.
- **Evidence/reasoning:** Reasoning from the stem itself: no positions of the 6 people are given, so "A ke dayein dusra kaun" has no determinable answer.

### 4. Ambiguous (minor) — Bhilwara epithet

- **qid:** `06_ECONOMY_RAJASTHAN-004`
- **File:** `question_bank.csv` and `question_bank/06_economy_rajasthan.csv`
- **Question (short):** Bhilwara ko kis naam se jana jata hai? Keyed answer: D — Manchester of Rajasthan. Option B: "Textile City of India".
- **What is wrong:** Bhilwara is widely called **both** "Manchester of Rajasthan" and "Textile City (of India)". Option B is therefore also a defensible description of Bhilwara, so the item has two plausible answers.
- **Correct answer/fact:** D is the standard exam answer, but B should be replaced with a clearly wrong distractor (e.g. "Steel City of India", which is Bhilai/Jamshedpur) to make D unique.
- **Evidence/reasoning:** Bhilwara's textile industry makes both epithets common in GK material; the key is the more standard one, but the distractor is not false.

### 5. Minor wording — syllogism option contains meta-commentary

- **qid:** `08_REASONING-020`
- **File:** `question_bank.csv` and `question_bank/08_reasoning.csv`
- **Question (short):** Statement: 'Sabhi A, B hain.' Isse kya nahi nikalta? Keyed answer: A — Sabhi B, A hain.
- **What is wrong:** Option C reads "Koi A, B nahi hai — galat" — the words "— galat" embed meta-commentary inside the option itself, which is confusing and non-standard. The key (A) is logically correct (the converse does not follow).
- **Correct answer/fact:** Key A is correct. Fix option C to a clean distractor, e.g. "Koi A, B nahi hai" (without "— galat").
- **Evidence/reasoning:** Logic: from "All A are B", "All B are A" does not follow; "Some B are A" and "Some A are B" do follow. The defect is wording only.

### 6. Minor content — meta test-tip presented as a reasoning question

- **qid:** `08_REASONING-024`
- **File:** `question_bank.csv` and `question_bank/08_reasoning.csv`
- **Question (short):** "Assumption wale prashn me kaun sa option aam taur par galat hota hai?" Keyed answer: A — Extreme shabd (sabhi/kabhi nahi/hamesha) wala.
- **What is wrong:** This is not a reasoning question; it is a test-taking tip. The keyed claim ("extreme words are usually wrong") is a heuristic, not a fact — an assumption containing "always/never" can be correct. It tests exam strategy, not logical reasoning, and cannot be marked right/wrong by logic.
- **Correct answer/fact:** Replace with a real assumption question (statement + assumption, identify which assumption is implicit), or move to a tips section outside the question bank.
- **Evidence/reasoning:** The item has no determinable truth value by reasoning; it is advice, and the "usually" hedge makes the key unfalsifiable.

### 7. Minor content — reading-comprehension tip presented as an English question

- **qid:** `13_GENERAL_ENGLISH-020`
- **File:** `question_bank.csv` and `question_bank/13_general_english.csv`
- **Question (short):** "Reading Comprehension me sabse pehle kya karna chahiye?" Keyed answer: D — Questions padhna, phir passage padhna.
- **What is wrong:** This is study advice, not an English-language test item. D is reasonable advice, but there is no factually unique answer (many teachers advise reading the passage first).
- **Correct answer/fact:** Move to a tips section, or replace with a real comprehension item (passage + question).
- **Evidence/reasoning:** No verifiable fact is tested; the "correct" answer is a matter of strategy preference.

### 8. Minor duplicates — same fact tested twice in different subjects

- **qids:** `03_GEOGRAPHY_INDIA-020` vs `06_ECONOMY_RAJASTHAN-013` (PM-KISAN, ₹6,000/year; the second adds the 2019 start year); `06_ECONOMY_RAJASTHAN-014` vs `10_PUBLIC_HEALTH-001` (Ayushman Bharat/PM-JAY, ₹5 lakh/family/year — identical fact, near-identical options); `07_EVERYDAY_SCIENCE-029` vs `10_PUBLIC_HEALTH-007` (Malaria spreads via Anopheles mosquito — identical fact).
- **File:** `question_bank.csv` and the respective per-subject files.
- **What is wrong:** Three facts are tested twice each across subjects. The answers are all correct and consistent with each other (no contradiction found), but the bank's claim of 300 unique questions is weakened — effectively 297 distinct facts.
- **Correct answer/fact:** Keep one of each pair and replace the other with a new question, or keep both deliberately as cross-subject revision (in which case note it in the file). No key/explanation change is needed.
- **Evidence/reasoning:** Direct comparison of question and option text in the CSV. No exact-duplicate question strings exist (programmatic check: 0 exact duplicates).

## Checks that passed (no problem found)

- **All 24 Maths rows recomputed — 0 errors.** Percentage, profit/loss, SI/CI, average, time-work, speed, mensuration, LCM/HCF, ratio, series, number system, age problems all correct, including 08_MATHEMATICS-004 (CI−SI = ₹100), -013 (net −4%), -016 (252 = 2²×3²×7¹), -018 (cylinder volume 1,540 cm³), -020 (father 30 years). No Trigonometry, Algebra/quadratic, or Logarithm question present — the earlier out-of-syllabus Maths items are gone.
- **All 24 Reasoning rows solved — 0 wrong keys** (apart from the wording issues in §3, §5, §6 above). Includes 08_REASONING-015 (√10 km), -017 (1 Jan 2026 is a Thursday; 8 Jan 2026 is a Thursday — correct), -018 (hands meet 11 times in 12 hours).
- **All 36 Science rows — 0 errors.** Physics, chemistry, biology, human body, diseases, environment all factually correct; explanations accurate.
- **All 14 Public Health rows — 0 errors.** PM-JAY ₹5 lakh, ASHA full form, Mission Indradhanush, JSY, BMI formula, polio-free 2014, Poshan Abhiyaan 2018, IMR, PHC, BCG, Swachh Bharat 2014, Jal Jeevan Mission, Mukhyamantri Nishulk Dava Yojana — all correct against standard guidance. No CPR/first-aid item exists in the bank (the syllabus head mentions First Aid/CPR, but no question tests it — a coverage gap, not an error).
- **All 18 Computer rows — 0 wrong keys.** The 10 EXTRA rows (007, 008, 009, 010, 011, 012, 013, 015, 016, 017) are all labelled "EXTRA — not in 2026 12th syllabus (PYQ-style general awareness)" in the subtopic field, and their facts are correct (WWW, SMTP, binary 10 = 1010, LAN, phishing, e-Mitra, UPI, binary 101 = 5, firewall, Jan Aadhaar).
- **Out-of-syllabus check — the 10 EXTRA Computer rows are the ONLY out-of-syllabus rows in the bank.** No other row touches Trigonometry, Algebra/quadratic equations, Logarithms, Internet/E-mail/Cyber-security/AI, or advanced physics. The 8 in-syllabus Computer rows (001–006, 014, 018) cover basics, hardware, memory, MS Office, input devices and operating systems only.
- **Current Affairs (18 rows) — 13 of 18 dated claims verified by web search on 11 Nov 2026:** Asian Games 2026 India 85 medals (21G/27S/37B), 4th — verified (Outlook India, Indian Express, Business Standard); Asian Para Games 2026 India 114 medals (30/35/49), 4th — verified (Times of India, ETV Bharat); CWG 2026 Glasgow India 39 medals (13/17/9), 4th — verified (Economic Times, Times of India, IOA); CWG 2030 Ahmedabad — verified (flag handed over at Glasgow closing ceremony); Nobel 2026 all six — Physics Francis Halzen, Peace Navi Pillay, Literature Anne Carson, Medicine Deisseroth/Hegemann/Nagel (optogenetics), Economics Robert E. Hall & Michael Woodford — verified (Britannica, Taipei Times, Manila Times); women's hockey gold after 44 years — verified (Dynamite News headline "44-Year Hockey Wait Ends"; India last won women's hockey Asian Games gold in 1982); ISRO NVS-03 launched 30 Oct 2026 on GSLV-F18 from Sriharikota — verified (The Hindu, PIB); Ashoke Sen first Indian Oskar Klein Medal, lecture 22 Oct 2026 — verified (The Hindu, ICTS); Rajasthan Budget 2026-27 ₹6,10,956 crore, presented 11 Feb 2026 by Diya Kumari, GSDP projected ₹21,52,100 crore — verified (PRS Budget Analysis 2026-27, Indian Express, The Statesman); RSTA announced in Budget 2026-27 on NTA lines — verified (PTI via Newsdrum, Testbook).
- **History, Art & Culture, Geography, Polity rows — 0 errors found** on read-through against standard GK (Kalibangan ploughed field, Bairat Ashokan edicts, Khanwa 1527, Haldighati 18 June 1576, Matsya Sangh 17 Mar 1948, Brihat Rajasthan 30 Mar 1949, Kalbeliya UNESCO 2010, Hill Forts UNESCO 2013, Jantar Mantar UNESCO 2010, Gagron jal-durg, India area 32,87,263 sq km, IST 82°30′E, Kangchenjunga 8,586 m, NH-44, Census 2011 population 121.08 crore / sex ratio 943, Guru Shikhar 1,722 m, Banas longest intra-Rajasthan river, Sambhar largest saline lake, Bhadla Solar Park (Jodhpur district), Rajasthan–Pakistan border ~1,070 km, 42nd/44th/61st/73rd/101st/106th Amendments, Panchayati Raj Nagaur 2 Oct 1959, Rajasthan High Court Jodhpur, CM Bhajan Lal Sharma, Governor Haribhau Bagade — all correct as of Nov 2026).
- **Hindi rows (except §1) — 0 errors.** Sandhi, samas (Dashanan = Bahuvrihi, Tribhuvan = Dvigu, Yathashakti = Avyayibhav), Kaurav = Kuru + A, paryayvachi/vilom, muhavare, ling, kaal, upsarg, ras, samshruti — all correct.
- **English rows (except §2, §7) — 0 errors.** Tenses, active-passive, direct-indirect, antonym/synonym, one-word substitution (Omniscient, Ambidextrous, Hydrophobia, Aviary), articles, prepositions, subject-verb agreement — all correct.
- **Structural checks (programmatic):** 300 rows in `question_bank.csv`; per-subject files total 300 rows with identical qid sets and zero differing rows; 0 exact-duplicate question strings; 0 empty fields; option E identical on all 300 rows ("Unattempted — mark E only if deliberately leaving this question blank"); correct-answer distribution A 74 / B 72 / C 75 / D 79, E 0 (balanced, no E keyed correct).

## Summary

| Item | Count |
|---|---|
| Rows checked (read in full, key + explanation + options) | 300 / 300 |
| Confirmed problems | 8 sections covering 10 rows |
| — Wrong key | 1 row (12_HINDI-015; no correct option exists as written) |
| — Ambiguous (two defensible answers / unsolvable as written) | 3 rows (13_ENGLISH-005, 08_REASONING-021, 06_ECONOMY-004) |
| — Wrong explanation only (key correct) | 0 rows |
| — Minor wording / non-test content | 3 rows (08_REASONING-020, 08_REASONING-024, 13_ENGLISH-020) |
| — Minor duplicates (same fact, different subject) | 3 pairs = 6 rows (03-020/06-013, 06-014/10-001, 07-029/10-007) |
| Out-of-syllabus rows beyond the 10 labelled EXTRA | 0 |
| Rows with wrong keys in Maths / Science / Reasoning / Computer / Public Health | 0 |

## Rows that could NOT be verified (unverified, not errors)

These make specific claims I could not check against my own knowledge or by web search in this pass. They are **not** flagged as wrong; each needs a primary-source check before being taught as fact:

- `06_ECONOMY_RAJASTHAN-005` — Rajasthan renewable ~51.6 GW / solar ~45 GW (Nov 2026). Directionally plausible (Rajasthan leads India in solar), exact figures unverified.
- `06_ECONOMY_RAJASTHAN-006` — Mukhyamantri Yuva Swarojgar Yojana: 100% interest subsidy on loans up to ₹10 lakh.
- `06_ECONOMY_RAJASTHAN-007` — Lakhpati Didi loan limit raised to ₹1.5 lakh in Budget 2026-27.
- `06_ECONOMY_RAJASTHAN-008` — Gargi Puraskar: 3.63 lakh girls, ₹109 crore (CM speech 3 Nov 2026).
- `06_ECONOMY_RAJASTHAN-016` — Thar Cultural Circuit ₹5,000 crore in Budget 2026-27.
- `06_ECONOMY_RAJASTHAN-017` — Uniform/Bag DBT ₹800/student; 66 lakh students, ₹482 crore by Nov 2026.
- `09_CURRENT_AFFAIRS-010` — Rajasthan RE-SAF National Award on 6 Nov 2026 (presented by VP C.P. Radhakrishnan — his being VP is correct).
- `09_CURRENT_AFFAIRS-011` — 235 medal-winning athletes approved for government jobs in Nov 2026 (9 DSP, 2 Excise, 224 others; 73 para-athletes).
- `09_CURRENT_AFFAIRS-015` — 'Sapnon Ki Udaan' programme on 1 Nov 2026; ₹74 crore+ pension DBT.
- `09_CURRENT_AFFAIRS-016` — National Sports Awards 2025: 17 Arjuna awardees, announced 18 Aug 2026.

## Coverage note (not an error)

The Public Health head of the 2026 syllabus includes First Aid and CPR, but the bank contains **no** First Aid/CPR question (14 rows cover schemes, programmes, indicators and nutrition only). If a First Aid/CPR item is added later, it must be checked against current standard guidance (e.g. 30:2 compression-to-ventilation ratio, 100–120 compressions/min) — no such fact was verified in this audit because no such row exists.
