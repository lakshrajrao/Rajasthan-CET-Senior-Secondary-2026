# Paper 2 Audit — Rajasthan CET 2026 Mock Papers (READ-ONLY)

- **Source file:** `/home/hatch/workspace/cet-2026-upload/mock_papers.md`
- **Scope audited:** Paper 2, Q1–Q120 (questions lines 1278–2239, answer key lines 2240–2276, explanations lines 2277–2517). All 120 questions read.
- **Ground truth used:** RSSB Adv 08/2026, exam 1–3 Dec 2026, 120Q / 240 marks / 150 min, +2 correct, −2/3 wrong, E = 0, blank = −2/3, >12 blanks disqualified. Syllabus heads as in the task brief.
- **Method:** Every Maths/Reasoning answer recomputed from scratch; every factual key checked against the auditor's own knowledge; explanations checked for whether they actually justify the key; question-bank near-duplicates checked by `grep` on `/home/hatch/workspace/cet-2026-upload/question_bank.csv` (300 MCQs).
- **Only confirmed problems are listed below.** Questions not listed were found correct (key, uniqueness and explanation) to the best of the auditor's knowledge.

---

## WRONG KEY

### Q47 — Average of 18 and 27 (keyed C = 22)
- **Question:** "Average of 18 and 27 is —" Options: (A) 19 (B) 32 (C) 22 (D) 27. Key: **C**.
- **What is wrong:** No option is correct. (18 + 27) / 2 = 45 / 2 = **22.5**, not 22. The explanation repeats the error: "Average = (18+27)/2 = 22."
- **Correct answer/fact:** 22.5. The question as printed has no correct option and must be replaced or re-optioned (e.g. options 22.5 / 23 / 21 / 24).
- **Evidence/reasoning:** 18 + 27 = 45; 45 ÷ 2 = 22.5. Recomputed by hand and verified in Python.

### Q109 — Average of 30 and 45 (keyed B = 37)
- **Question:** "Average of 30 and 45 is —" Options: (A) 47 (B) 37 (C) 34 (D) 42. Key: **B**.
- **What is wrong:** No option is correct. (30 + 45) / 2 = 75 / 2 = **37.5**, not 37. The explanation repeats the error: "Average = (30+45)/2 = 37." Same arithmetic slip as Q47 (dropping the .5 when the sum is odd).
- **Correct answer/fact:** 37.5. The question as printed has no correct option and must be replaced or re-optioned.
- **Evidence/reasoning:** 30 + 45 = 75; 75 ÷ 2 = 37.5. Recomputed by hand and verified in Python. (Contrast Q96, average of 15 and 25 = 20, which is correct because 40/2 is whole.)

---

## WRONG / MISMATCHED EXPLANATION

### Q16 — Rana Sanga reign (key B correct; explanation is Q39's explanation)
- **Question:** "Rana Sanga is associated with which state/kingdom and period?" Key: **B — Mewar, 1508–1528** (correct: Rana Sanga ruled Mewar 1508–1528).
- **What is wrong:** The explanation does not justify the key. It reads verbatim: "Battle of Khanwa 1527 vs Babur; united Rajput confederacy" — which is the explanation for Q39, not for a reign-dates question. It never states the reign period 1508–1528.
- **Correct fact:** Rana Sanga, ruler of Mewar, reigned 1508–1528 and fought Babur at Khanwa in 1527. The explanation should state the reign dates.
- **Evidence/reasoning:** Explanation text for Q16 and Q39 is identical word-for-word in the file; the Q16 explanation answers a different question.

### Q75 — Maharana Udai Singh II reign (key B correct; explanation is Q92's explanation)
- **Question:** "Maharana Udai Singh II is associated with which state/kingdom and period?" Key: **B — Mewar, 1540–1572** (correct: Udai Singh II ruled Mewar 1540–1572).
- **What is wrong:** The explanation does not justify the key. It reads verbatim: "Founded Udaipur 1559; shifted capital from Chittorgarh after 1567 siege by Akbar" — which is the explanation for Q92, not for a reign-dates question. It never states the reign period 1540–1572.
- **Correct fact:** Udai Singh II ruled Mewar 1540–1572; he founded Udaipur in 1559 and shifted the capital after Akbar's 1567–68 siege of Chittorgarh. The explanation should state the reign dates.
- **Evidence/reasoning:** Explanation text for Q75 and Q92 is identical word-for-word in the file; the Q75 explanation answers a different question.

### Q52 — Pushkar Lake location (key A = Ajmer correct; explanation does not answer the question)
- **Question:** "Pushkar Lake is located in which district/place?" Key: **A — Ajmer** (correct).
- **What is wrong:** The explanation never mentions Ajmer. It reads verbatim: "Sacred lake; Brahma temple nearby; Pushkar Fair (Kartik Purnima)" — identical to the Q41 explanation. A candidate reading the explanation cannot see why Ajmer is the answer.
- **Correct fact:** Pushkar Lake is in Ajmer district, Rajasthan; the Brahma temple and the Kartik Purnima Pushkar Fair are associated with it.
- **Evidence/reasoning:** Explanation text for Q41 and Q52 is identical word-for-word; Q52's explanation answers "what is Pushkar Lake known for", not "where is it".

### Q51 — Mahi river terminus (key C correct; explanation does not justify the key)
- **Question:** "The Mahi river finally joins / ends in —" Key: **C — Gulf of Khambhat** (correct).
- **What is wrong:** The explanation ("Flows through Banswara/Dungarpur; Mahi Bajaj Sagar Dam") says nothing about where the river ends. It does not justify choosing the Gulf of Khambhat over option (B) "Arabian Sea directly".
- **Correct fact:** The Mahi flows through Madhya Pradesh, Rajasthan and Gujarat and empties into the Gulf of Khambhat (an inlet of the Arabian Sea), which is why "Gulf of Khambhat" is the precise answer and "Arabian Sea directly" is not.
- **Evidence/reasoning:** The explanation contains no terminus information at all.

### Q81 — Sabarmati river terminus (key A correct; explanation does not justify the key)
- **Question:** "The Sabarmati river finally joins / ends in —" Key: **A — Gulf of Khambhat** (correct).
- **What is wrong:** The explanation ("Flows through Gujarat; short course in Rajasthan") says nothing about where the river ends. It does not justify choosing the Gulf of Khambhat over option (D) "Arabian Sea directly".
- **Correct fact:** The Sabarmati empties into the Gulf of Khambhat. Same pattern as Q51.
- **Evidence/reasoning:** The explanation contains no terminus information at all.

### Q87 — Kali Sindh river terminus (key B correct; explanation does not justify the key)
- **Question:** "The Kali Sindh river finally joins / ends in —" Key: **B — Chambal** (correct).
- **What is wrong:** The explanation ("Flows through Jhalawar-Kota; Jhalrapatan") says nothing about the river joining the Chambal. It does not justify the key.
- **Correct fact:** The Kali Sindh (origin Dewas, MP) joins the Chambal in Rajasthan.
- **Evidence/reasoning:** The explanation contains no confluence information at all.

---

## AMBIGUOUS / TWO-CORRECT

### Q46 — Antonym of 'सत्य' (keyed A = असत्य; C = झूठ also defensible)
- **Question:** "'सत्य' का विलोम है —" Options: (A) असत्य (B) न्याय (C) झूठ (D) सही. Key: **A**.
- **What is wrong:** Two options are defensible antonyms. झूठ (lie/falsehood) is a genuine antonym of सत्य (truth) in ordinary Hindi usage, not merely a synonym of असत्य — the question stem itself concedes this in parentheses: "झूठ (synonym of असत्य, but standard antonym is असत्य)". If झूठ is a synonym of the correct answer असत्य, it cannot be unambiguously wrong. A candidate choosing C has a legitimate grievance.
- **Correct answer/fact:** असत्य is the standard textbook pair, but झूठ is also a valid antonym of सत्य. The question is not uniquely answerable as printed.
- **Evidence/reasoning:** सत्य ↔ असत्य and सत्य ↔ झूठ are both standard antonym pairs in Hindi; the stem's own parenthetical admits the overlap. Fix by replacing option (C) with a clearly unrelated word.
- **Note:** Q14 ('अंधकार' — प्रकाश vs अंधेरा) is NOT flagged: अंधेरा is a synonym of अंधकार, not an antonym, so that question is uniquely answerable.

---

## NEAR-DUPLICATES vs THE QUESTION BANK (question_bank.csv)

Each item below asks the same fact, the same way, as a question-bank item (found by `grep` on key terms). Same fact in a mock and in the bank is a duplication of practice material, not a wrong key.

### Q13 — Lok Sabha seats from Rajasthan (key D = 25)
- **Near-duplicate of:** QB line 95, `05_POLITY_RAJASTHAN-008`: "Rajasthan se Lok Sabha aur Rajya Sabha ki seatein kitni hain?" — keyed "25 aur 10". Same core fact (Lok Sabha = 25); the QB item additionally asks Rajya Sabha (10), which is also the Paper 2 explanation.
- **Evidence:** `grep -i "Lok Sabha" question_bank.csv` → line 95.

### Q39 — Battle of Khanwa (key C = 1527, Rana Sanga vs Babur)
- **Near-duplicate of:** QB line 8, `01_HISTORY_RAJASTHAN-007`: "Khanwa ka yuddh kab hua aur kin ke beech hua?" — keyed "1527, Rana Sanga vs Babur", with the same distractors (1576 Pratap vs Akbar; 1526 Babur vs Lodi; 1192 Prithviraj vs Ghori).
- **Evidence:** `grep -i "Khanwa" question_bank.csv` → line 8.

### Q45 — Swachh Bharat Mission launch date (key D = 2 October 2014)
- **Near-duplicate of:** QB line 241, `10_PUBLIC_HEALTH-012`: "Swachh Bharat Mission kab shuru hua?" — keyed 2014. Paper 2 asks the exact date (2 Oct 2014) rather than the year, so this is the weakest of the nine — same fact family, one step more specific.
- **Evidence:** `grep -i "Swachh Bharat" question_bank.csv` → line 241.

### Q66 — 73rd Constitutional Amendment (key D = Panchayati Raj)
- **Near-duplicate of:** QB line 97, `05_POLITY_RAJASTHAN-010`: "73rd Amendment kis se sambandhit hai?" — keyed Panchayati Raj, same distractor (Municipalities = 74th Amendment).
- **Evidence:** `grep -i "73rd" question_bank.csv` → line 97.

### Q98 — Kota Doria (key A = lightweight cotton fabric/saree from Kota)
- **Near-duplicate of:** QB line 32, `02_ART_CULTURE_RAJASTHAN-007`: "Kota Doria kis cheez ke liye prasiddh hai?" — keyed "Saree (halki bunai)", same distractors (Blue pottery, Marble, Kathputli).
- **Evidence:** `grep -i "Kota Doria" question_bank.csv` → line 32.

### Q102 — Battle of Haldighati year (key B = 1576)
- **Near-duplicate of:** QB line 9, `01_HISTORY_RAJASTHAN-008`: "Haldighati ka yuddh kab hua?" — keyed "18 June 1576", same distractor years (1527, 1582, 1568).
- **Evidence:** `grep -i "Haldighati" question_bank.csv` → line 9.

### Q105 — Indira Gandhi Canal origin (key D = Harike Barrage)
- **Near-duplicate of:** QB line 79, `04_GEOGRAPHY_RAJASTHAN-014`: "Indira Gandhi Nahar ka udgam kahan se hai?" — keyed "Harike Barrage, Punjab", same distractors (Bhakra, Bisalpur, Gandhi Sagar).
- **Evidence:** `grep -i "Indira Gandhi Canal\|Indira Gandhi Nahar" question_bank.csv` → line 79.

### Q108 — Synonym of 'Abandon' (key C = Leave)
- **Near-duplicate of:** QB line 299, `13_GENERAL_ENGLISH-018`: "'Abandon' ka synonym kya hai?" — keyed Leave, with the identical option set (Keep, Hold, Leave, Protect).
- **Evidence:** `grep -i "Abandon" question_bank.csv` → line 299.

### Q110 — Janani Suraksha Yojana (key A = institutional delivery / safe motherhood)
- **Near-duplicate of:** QB line 233, `10_PUBLIC_HEALTH-004`: "Janani Suraksha Yojana (JSY) kis ko badhava deti hai?" — keyed "Sansthagat prasav (institutional delivery)", same scheme and year (2005).
- **Evidence:** `grep -i "Janani Suraksha" question_bank.csv` → line 233.

---

## IN-PAPER NEAR-DUPLICATES / TEMPLATE REPETITION (within Paper 2 itself)

### Systemic — same fact asked twice in Paper 2, and one formula repeated six times
- **What is wrong:** Five pairs of questions in Paper 2 test the same fact from nearly the same angle, and two Maths templates are repeated with only the numbers changed:
  - **Q16 ↔ Q39** — Rana Sanga (reign 1508–1528 vs Battle of Khanwa 1527). Same person, same battle in both explanations.
  - **Q75 ↔ Q92** — Maharana Udai Singh II (reign 1540–1572 vs founded Udaipur 1559). Identical explanations.
  - **Q84 ↔ Q102** — Battle of Haldighati (event vs year 1576). Same battle, same date in both.
  - **Q65 ↔ Q73** — Ranthambore Fort (district Sawai Madhopur vs "famous for — inside Ranthambore Tiger Reserve"). Identical explanations.
  - **Q41 ↔ Q52** — Pushkar Lake ("known for" vs location). Identical explanations; see Q52 above.
  - **Simple Interest × 6** — Q10, Q15, Q18, Q50, Q77, Q95 are the identical formula (P×R×T/100) with only the numbers changed. Six of 120 questions (5%) test one computation.
  - **Average × 3** — Q47, Q96, Q109 are the identical two-number average; two of the three (Q47, Q109) are also wrong-keyed (see above).
- **Correct fact:** None of the keys in these pairs is wrong (except Q47/Q109); the problem is wasted coverage — a 120-question mock should not spend ~11 slots on five repeated facts plus one repeated formula.
- **Evidence/reasoning:** Direct comparison of stems, options and explanations within lines 1278–2517 of the file.

---

## MINOR WORDING

### Q7 — Garbled stem ("'Bhakti' — no:")
- **Question:** "The 'Bhakti' — no: Bhakra Dam is on which river?" The stray "'Bhakti' — no:" is an editing leftover. Key (A — Sutlej) is correct. Fix by deleting the stray fragment.

### Q50 and Q77 — "for 1 years"
- **Questions:** Q50 "…at 12% p.a. for 1 years is —" and Q77 "…at 20% p.a. for 1 years is —". Both keys are correct (₹144 and ₹180), but "1 years" is ungrammatical; should be "for 1 year".

### Q100 — Garbled rule hint ("sum ×?")
- **Question:** "If CAT = 24 (C=3,A=1,T=20; sum ×? — CAT letters sum=24), then DOG = ?" The "sum ×?" fragment is a leftover; the rule is a plain letter-position sum (D+O+G = 4+15+7 = 26, key C — correct). Fix by deleting "sum ×? —".

### Q37 — Jaisamand Lake district wording
- **Question:** "Jaisamand Lake is located in which district/place?" Key: **C — Udaipur (Salumbar)**. Jaisamand (Dhebar) Lake is in Salumbar district, which was carved out of Udaipur district in 2023 — so "Udaipur (Salumbar)" is defensible but confusing as printed; a candidate answering "Salumbar" has no clean option. Recommend rewording the option to "Salumbar (formerly Udaipur district)".

### Q89 — Explanation presents a legendary episode as fact
- **Question:** "Which district is Chittorgarh Fort located in?" Key: **D — Chittorgarh** (correct).
- **What is wrong:** The explanation adds "Jauhar of Rani Padmini (1303)". Rani Padmini is a literary figure from Malik Muhammad Jayasi's *Padmavat* (1540); her historicity and a 1303 jauhar are not established history, unlike the 1535 jauhar of Rani Karnavati also cited. Presenting the Padmini jauhar as a dated fact in an explanation is misleading.
- **Correct fact:** Chittorgarh Fort is in Chittorgarh district; it is India's largest fort and the site of the Vijay Stambh. The Padmini reference should be dropped or labelled as legend.

---

## SUMMARY

- **Questions checked:** 120 (Q1–Q120, key table and all 120 explanations read in full).
- **Problems found by severity:**
  - **Wrong key (no correct option as printed): 2** — Q47, Q109 (both two-number averages with an odd sum; correct answers 22.5 and 37.5 are absent from the options; explanations repeat the arithmetic error).
  - **Wrong / mismatched explanation: 6** — Q16, Q75 (copy-pasted explanation of a different question), Q52 (explanation never mentions the keyed district), Q51, Q81, Q87 (explanations give no terminus/confluence information and do not justify the key). Keys themselves are correct in all six.
  - **Ambiguous / two-correct: 1** — Q46 (झूठ is a defensible antonym of सत्य alongside keyed असत्य).
  - **Out-of-syllabus: 0** — No Trigonometry, Algebra/quadratic equations, Logarithms, or Internet/E-mail/Cyber-security/AI questions were found in Paper 2. All subject tags fit the 2026 Senior Secondary (12th level) syllabus. (Q7, Q50, Q77, Q100 wording slips are editorial, not syllabus, issues.)
  - **Near-duplicate: 9 vs the question bank** — Q13, Q39, Q45 (weakest — year vs exact date), Q66, Q98, Q102, Q105, Q108, Q110; **plus in-paper repetition** — 5 fact-pairs (Q16/Q39, Q75/Q92, Q84/Q102, Q65/Q73, Q41/Q52) and template repetition (Simple Interest ×6, Average ×3).
  - **Minor wording: 5 items** — Q7 (garbled stem), Q50 + Q77 ("1 years"), Q100 ("sum ×?"), Q37 (Salumbar/Udaipur district wording), Q89 (Padmini jauhar presented as fact).
- **Total distinct questions affected:** 29 of 120 (Q7, Q13, Q16, Q37, Q39, Q41, Q45, Q46, Q47, Q50, Q51, Q52, Q65, Q66, Q73, Q75, Q77, Q81, Q84, Q87, Q89, Q92, Q98, Q100, Q102, Q105, Q108, Q109, Q110); 33 question slots touched if the four additional SI-template items (Q10, Q15, Q18, Q95) are counted individually.
- **Nothing else failed:** All other keys, including every recomputed Maths/Reasoning item (Q10, Q15, Q18, Q27, Q50, Q61, Q62, Q77, Q80, Q95, Q96, Q100) and all checked Science/History/Geography/Polity/Economy/Computer/Public Health/Current Affairs facts, were correct with a unique answer and a justifying explanation.

## COULD NOT VERIFY (and why)

- **Q30 — Junagarh Fort "Never conquered":** The key (B) follows the standard Rajasthan-GK claim repeated in guidebooks, so it is not flagged as wrong. The absolute claim ("never conquered" across all history) could not be verified from the auditor's own knowledge alone, and no source was invented. Left as-is; treat as a conventional guidebook answer.
- **Q56 — Raj Prashasti as "longest Sanskrit inscription":** Same position — a widely repeated guidebook claim, accepted, not independently verifiable from the auditor's own knowledge; not flagged.
- **Q22 — Bhavai "famous in Nagaur, Jodhpur":** Accepted as printed; the precise district association of Bhavai could not be verified from the auditor's own knowledge and is not load-bearing for the key (B — Rajasthan, balancing pots).
- **Q34 — 11 vowels in the Hindi alphabet:** Accepted as the standard CET/school answer (अ आ इ ई उ ऊ ऋ ए ऐ ओ औ); some counts include अं/अः, but 11 is the conventional answer and the key is not disputed.
- No other fact in Paper 2 was left unverified; everything else was checked against the auditor's own knowledge as instructed, with no sources invented.
