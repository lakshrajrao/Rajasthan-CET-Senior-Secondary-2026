# Mock Papers Audit — Consolidated Findings (Rajasthan CET Senior Secondary 2026)

- **Source audited:** `/home/hatch/workspace/cet-2026-upload/mock_papers.md` — 3 papers × 120 questions = 360 questions, each with an answer-key table and explanations.
- **Method:** Each paper was audited question-by-question by a separate auditor (Paper 1: lines 28–1267; Paper 2: lines 1278–2517; Paper 3: lines 2528–3765). Every Maths/Reasoning answer was recomputed from scratch; every factual key was checked against the auditor's own knowledge; explanations were checked for whether they actually justify the key; subject tags were checked against the 2026 Senior Secondary (12th level) syllabus; near-duplicates were checked by grep against `question_bank.csv` (300 MCQs).
- **Already verified mechanically (not re-checked here):** key-vs-explanation letter consistency = 0 mismatches across all 360 questions; numbering sequential 1–120 in each paper; 0 exact duplicate stems within or across papers; key distributions P1 A29/B33/C26/D32, P2 A35/B22/C32/D31, P3 A32/B30/C23/D35 (see `mock_audit_report.txt`).
- **Ground truth:** RSSB Adv 08/2026, exam 1–3 Dec 2026, 120Q / 240 marks / 150 min, +2 correct, −2/3 wrong, E = 0, blank = −2/3, >12 blanks disqualified. Official scheme gives NO per-subject question split. Graduation-only / out-of-syllabus for 12th level: Trigonometry, Algebra/quadratic equations, Logarithms, Internet/E-mail/Cyber-security/AI.
- **Only confirmed problems are listed.** Questions not listed were found correct (key, uniqueness, explanation) to the best of the auditors' knowledge.
- **Per-paper detail files:** `mock_paper1_findings.md`, `mock_paper2_findings.md`, `mock_paper3_findings.md` in this directory.

---

# A. WRONG KEY (5 questions — must be fixed before use)

## A1. Paper 1, Q114 — Duplicate options; no unique correct option
- **Question (short):** "Which district is Junagarh Fort located in?" Options: (A) Bikaner, (B) Bikaner, (C) Udaipur, (D) Kota. Key: **A**.
- **What is wrong:** Options (A) and (B) are character-for-character identical and both correct — Junagarh Fort is in Bikaner. A candidate picking (B) is marked wrong for the same answer as (A).
- **Correct answer/fact:** Bikaner. Replace one of (A)/(B) (e.g. with Jodhpur or Jaipur) before use.
- **Evidence:** Junagarh Fort is in Bikaner city (built by Raja Rai Singh); the duplication is visible in the question text itself.

## A2. Paper 2, Q47 — Average of 18 and 27 (keyed C = 22)
- **Question (short):** "Average of 18 and 27 is —" Options: (A) 19 (B) 32 (C) 22 (D) 27. Key: **C**. Explanation repeats the error: "Average = (18+27)/2 = 22."
- **What is wrong:** No option is correct. (18 + 27) / 2 = 45 / 2 = **22.5**, not 22.
- **Correct answer/fact:** 22.5. Re-option (e.g. 22.5 / 23 / 21 / 24) or replace the question.
- **Evidence:** 18 + 27 = 45; 45 ÷ 2 = 22.5 (recomputed by hand and in Python).

## A3. Paper 2, Q109 — Average of 30 and 45 (keyed B = 37)
- **Question (short):** "Average of 30 and 45 is —" Options: (A) 47 (B) 37 (C) 34 (D) 42. Key: **B**. Explanation repeats the error: "Average = (30+45)/2 = 37."
- **What is wrong:** No option is correct. (30 + 45) / 2 = 75 / 2 = **37.5**, not 37. Same slip as Q47 (dropping the .5 when the sum is odd).
- **Correct answer/fact:** 37.5. Re-option or replace.
- **Evidence:** 30 + 45 = 75; 75 ÷ 2 = 37.5 (recomputed by hand and in Python). Contrast P2 Q96 (average of 15 and 25 = 20, correct because 40/2 is whole).

## A4. Paper 3, Q4 — Largest port by cargo (keyed B; correct is A Paradip) — also ambiguous
- **Question (short):** "India's largest port by cargo is —" Options: (A) Paradip, (B) "Jawaharlal Nehru Port (Nhava Sheva) / Deendayal (Kandla) — varies by year", (C) Chennai, (D) Kochi. Key: **B**.
- **What is wrong:** The key is wrong, and option (B) names **two different ports** as a single option. On total cargo the correct answer among the options is **(A) Paradip**. JNPT (Nhava Sheva) has never led on total cargo; it leads on **container** traffic only. The paper's own explanation concedes this ("By cargo volume, Deendayal (Kandla) and Paradip often lead among major ports; JNPT leads in container traffic… Treat JNPT as container leader") — it contradicts the key it is supposed to justify. Further underspecification: the stem does not say "major port" — counting all ports including private Mundra (~200.7 MMT in FY 2024-25), Mundra would be largest overall and **none** of the four options would be correct.
- **Correct answer/fact:** Among government major ports, Paradip has been the largest cargo handler since FY 2023-24: FY 2024-25 Paradip 150.41 MMT vs Deendayal 150.16 MMT vs JNPA 92.12 MMT. Deendayal (Kandla) was the long-standing leader before FY 2023-24, so the "varies by year" hedge does not save option (B) — JNPT is wrong in every recent year.
- **Evidence:** Published FY 2024-25 major-port cargo ranking (Ministry of Ports, Shipping & Waterways / Indian Ports Association figures, as reported in 2025-26 port rankings); the explanation's own container-vs-cargo distinction destroys key (B).
- **Fix:** Reword stem to "largest major port by cargo handled", key (A) Paradip, rewrite the explanation with the FY 2024-25 figures and the container-vs-cargo distinction. Also delete the stem's struck-through false start "The 'Silk Route' — no:" (see §F).

## A5. Paper 3, Q100 — Average of 50 and 75 (keyed A = 62)
- **Question (short):** "Average of 50 and 75 is —" Options: (A) 62 (B) 67 (C) 59 (D) 72. Key: **A**. Explanation repeats the error: "Average = (50+75)/2 = 62."
- **What is wrong:** The key is arithmetically wrong and **no option is correct**. (50 + 75) / 2 = 125 / 2 = **62.5**.
- **Correct answer/fact:** 62.5. Change option (A) to 62.5 (key A) or replace the numbers with an even-sum pair (e.g. average of 50 and 74 = 62).
- **Evidence:** 50 + 75 = 125; 125 ÷ 2 = 62.5 (recomputed from scratch). The other averages in Paper 3 were recomputed and are correct (Q30: 25; Q76: 50; Q77: 15), so this is an isolated slip — but as printed the question is unanswerable and any candidate who computes correctly is penalised.

**Pattern note:** Three of the five wrong keys are the same arithmetic slip — a two-number average with an odd sum, where the .5 was dropped (P2 Q47, P2 Q109, P3 Q100). Every other average in the three papers recomputed correctly. All three must be re-optioned, not just re-keyed, because the correct value is absent from the options.

---

# B. WRONG / INADEQUATE EXPLANATION (keys correct; 13 explanation-only cases + 2 overlapping A4/A5)

## B1. Paper 1, Q13 — Explanation is a verbatim copy of Q35's explanation
- **Question (short):** "Ana Sagar Lake is located in which district/place?" Key: **C — Ajmer** (correct).
- **What is wrong:** Explanation reads "Built by Anaji Chauhan (Arnoraj); Daulat Bagh by Jahangir" — identical to Q35's explanation. It says nothing about the lake being in Ajmer, so it does not justify the key. A learner who got Q13 wrong learns the builder, not the location.
- **Correct fact:** Ana Sagar Lake is in Ajmer (built by Anaji/Arnoraja Chauhan; Daulat Bagh added by Jahangir). Explanation should state the location.
- **Evidence:** Direct comparison of the Q13 and Q35 explanation lines; verbatim identical. The builder facts are themselves correct, which is why this is a wrong-explanation finding, not a wrong-key finding.

## B2. Paper 1, Q50 — Explanation is a verbatim copy of Q118's explanation
- **Question (short):** "Who built / is chiefly associated with Jaisalmer Fort (Sonar Quila)?" Key: **A — Rawal Jaisal, 1156** (correct).
- **What is wrong:** Explanation reads "Living fort; golden sandstone; UNESCO Hill Forts" — identical to Q118's explanation ("Jaisalmer Fort is famous for — Living fort"). It does not mention Rawal Jaisal or 1156, so it does not justify the key.
- **Correct fact:** Jaisalmer Fort was founded by Rawal Jaisal in 1156; it is a living fort built of yellow/golden sandstone and is among the UNESCO Hill Forts of Rajasthan.
- **Evidence:** Direct comparison of the Q50 and Q118 explanation lines; verbatim identical text answering a different question.

## B3. Paper 1, Q60 — Explanation is a verbatim copy of Q58's explanation
- **Question (short):** "Who built / is chiefly associated with Kumbhalgarh Fort?" Key: **A — Maharana Kumbha, 15th c.** (correct).
- **What is wrong:** Explanation reads "Second-longest wall in world after Great Wall (~36 km); birthplace of Maharana Pratap" — identical to Q58's explanation ("Kumbhalgarh Fort is famous for — …"). It does not mention Maharana Kumbha as builder.
- **Correct fact:** Kumbhalgarh Fort was built by Maharana Kumbha in the 15th century (c. 1443–1458); its ~36 km wall is commonly described as the second-longest wall in the world after the Great Wall, and Maharana Pratap was born there (1540).
- **Evidence:** Direct comparison of the Q58 and Q60 explanation lines; verbatim identical text answering a different question.

## B4. Paper 2, Q16 — Explanation is Q39's explanation (Rana Sanga reign)
- **Question (short):** "Rana Sanga is associated with which state/kingdom and period?" Key: **B — Mewar, 1508–1528** (correct).
- **What is wrong:** Explanation reads verbatim "Battle of Khanwa 1527 vs Babur; united Rajput confederacy" — Q39's explanation. It never states the reign period 1508–1528.
- **Correct fact:** Rana Sanga, ruler of Mewar, reigned 1508–1528 and fought Babur at Khanwa in 1527. Explanation should state the reign dates.
- **Evidence:** Explanation text for Q16 and Q39 is identical word-for-word in the file.

## B5. Paper 2, Q75 — Explanation is Q92's explanation (Maharana Udai Singh II reign)
- **Question (short):** "Maharana Udai Singh II is associated with which state/kingdom and period?" Key: **B — Mewar, 1540–1572** (correct).
- **What is wrong:** Explanation reads verbatim "Founded Udaipur 1559; shifted capital from Chittorgarh after 1567 siege by Akbar" — Q92's explanation. It never states the reign period 1540–1572.
- **Correct fact:** Udai Singh II ruled Mewar 1540–1572; he founded Udaipur in 1559 and shifted the capital after Akbar's 1567–68 siege of Chittorgarh.
- **Evidence:** Explanation text for Q75 and Q92 is identical word-for-word in the file.

## B6. Paper 2, Q52 — Explanation never mentions the keyed district (Pushkar Lake)
- **Question (short):** "Pushkar Lake is located in which district/place?" Key: **A — Ajmer** (correct).
- **What is wrong:** Explanation reads "Sacred lake; Brahma temple nearby; Pushkar Fair (Kartik Purnima)" — identical to the Q41 explanation. It never mentions Ajmer. A candidate reading the explanation cannot see why Ajmer is the answer.
- **Correct fact:** Pushkar Lake is in Ajmer district, Rajasthan; the Brahma temple and the Kartik Purnima Pushkar Fair are associated with it.
- **Evidence:** Explanation text for Q41 and Q52 is identical word-for-word; Q52's explanation answers "what is Pushkar Lake known for", not "where is it".

## B7. Paper 2, Q51 — Explanation gives no terminus (Mahi river)
- **Question (short):** "The Mahi river finally joins / ends in —" Key: **C — Gulf of Khambhat** (correct).
- **What is wrong:** Explanation ("Flows through Banswara/Dungarpur; Mahi Bajaj Sagar Dam") says nothing about where the river ends. It does not justify choosing the Gulf of Khambhat over option (B) "Arabian Sea directly".
- **Correct fact:** The Mahi flows through Madhya Pradesh, Rajasthan and Gujarat and empties into the Gulf of Khambhat (an inlet of the Arabian Sea), which is why "Gulf of Khambhat" is the precise answer and "Arabian Sea directly" is not.
- **Evidence:** The explanation contains no terminus information at all.

## B8. Paper 2, Q81 — Explanation gives no terminus (Sabarmati river)
- **Question (short):** "The Sabarmati river finally joins / ends in —" Key: **A — Gulf of Khambhat** (correct).
- **What is wrong:** Explanation ("Flows through Gujarat; short course in Rajasthan") says nothing about where the river ends. It does not justify choosing the Gulf of Khambhat over option (D) "Arabian Sea directly".
- **Correct fact:** The Sabarmati empties into the Gulf of Khambhat. Same pattern as Q51.
- **Evidence:** The explanation contains no terminus information at all.

## B9. Paper 2, Q87 — Explanation gives no confluence (Kali Sindh river)
- **Question (short):** "The Kali Sindh river finally joins / ends in —" Key: **B — Chambal** (correct).
- **What is wrong:** Explanation ("Flows through Jhalawar-Kota; Jhalrapatan") says nothing about the river joining the Chambal. It does not justify the key.
- **Correct fact:** The Kali Sindh (origin Dewas, MP) joins the Chambal in Rajasthan.
- **Evidence:** The explanation contains no confluence information at all.

## B10. Paper 3, Q50 — Explanation names no builder (Junagarh Fort)
- **Question (short):** "Who built / is chiefly associated with Junagarh Fort?" Key: **B — Raja Rai Singh (1589-94)** (correct).
- **What is wrong:** Explanation reads in full: "Never conquered; Anup Mahal; not built on a hill." None of those phrases names Raja Rai Singh or the 1589-94 construction dates, so a candidate cannot see from the explanation why (B) is right and (A) Raja Bhoj / (C) Maharana Sanga / (D) Maharaja Ranjit Singh are wrong.
- **Correct fact:** Junagarh Fort, Bikaner, was built by Raja Rai Singh (reigned 1571-1612) in 1589-94; it is a plain (non-hill) fort that was never conquered.
- **Evidence:** The keyed option (B) is the only option containing a builder + date; the explanation supplies no builder information at all. Compare P3 Q82, whose explanation correctly names Rao Jodha (1459) for Mehrangarh.
- **Fix:** Rewrite as: "Built by Raja Rai Singh of Bikaner, 1589-94; a ground-level fort (not on a hill), never conquered; Anup Mahal inside."

## B11. Paper 3, Q57 — Explanation is a verbatim copy of Q41's explanation (Maharaja Ganga Singh)
- **Question (short):** "Maharaja Ganga Singh is associated with which state/kingdom and period?" Key: **D — Bikaner, 1888–1943** (correct).
- **What is wrong:** Explanation is a verbatim copy of the Q41 explanation ("Built Ganga Canal (1927, from Sutlej); represented India at Versailles 1919") and says nothing about **Bikaner** or the **1888–1943** period — the two things option (D) actually asserts.
- **Correct fact:** Maharaja Ganga Singh ruled Bikaner 1888-1943 (born 1880, died 1943). The Ganga Canal (1927) and Versailles 1919 facts are true of him, but they do not establish the state/period in the keyed option.
- **Evidence:** Q41 and Q57 test the same person; Q41's explanation is appropriate for Q41 (event-based), but Q57 needs a state/period justification. The copy-paste is visible in the file: the Q41 and Q57 explanation lines are identical. (Also a within-paper near-duplicate pair; see §E.)
- **Fix:** Rewrite as: "Ganga Singh, Maharaja of Bikaner, reigned 1888-1943; built the Ganga Canal (1927) and represented India at Versailles (1919)."

## B12. Paper 3, Q85 — Explanation presents legend as fact (Chittorgarh Fort)
- **Question (short):** "Chittorgarh Fort is famous for —" Key: **A — Largest fort in India** (correct).
- **What is wrong:** The explanation adds a historically unsound claim: "Jauhar of Rani Padmini (1303)". Rani Padmini is a literary figure from Malik Muhammad Jayasi's epic poem *Padmavat* (c. 1540); her existence and a 1303 jauhar led by her are not established historical facts. Presenting it alongside the genuinely historical 1535 jauhar (Rani Karnavati, during Bahadur Shah of Gujarat's siege) as if both were equally factual misleads candidates.
- **Correct fact:** Key (A) stands — Chittorgarh, ~700 acres, is India's largest fort. The 1303 siege of Chittorgarh by Alauddin Khalji is historical; a jauhar occurred, but attributing it to "Rani Padmini" is the *Padmavat* legend, not verified history. The 1535 jauhar under Rani Karnavati is the historically attested one usually cited alongside it.
- **Evidence:** Padmini first appears in Jayasi's *Padmavat*, written ~237 years after 1303; no contemporary source names her. Standard history texts treat her as legendary.
- **Fix:** Rewrite as: "Largest fort in India (~700 acres); Vijay Stambh; jauhar of 1303 (Alauddin Khalji's siege) and of 1535 under Rani Karnavati." Drop "Rani Padmini (1303)" or label it explicitly as legend.

## B13. Paper 2, Q89 — Explanation presents the same Padmini legend as fact
- **Question (short):** "Which district is Chittorgarh Fort located in?" Key: **D — Chittorgarh** (correct).
- **What is wrong:** The explanation adds "Jauhar of Rani Padmini (1303)". Rani Padmini is a literary figure from Malik Muhammad Jayasi's *Padmavat* (1540); her historicity and a 1303 jauhar are not established history, unlike the 1535 jauhar of Rani Karnavati also cited.
- **Correct fact:** Chittorgarh Fort is in Chittorgarh district; it is India's largest fort and the site of the Vijay Stambh. The Padmini reference should be dropped or labelled as legend.
- **Evidence:** Same as B12. (Listed here rather than under minor wording because the explanation states a legend as a dated fact.)

**Pattern note:** The dominant explanation defect is copy-paste: B1, B2, B3, B4, B5, B6 and B11 are explanations copied verbatim from another question in the same paper. B7–B9 are a second pattern — river-terminus questions whose explanations omit the terminus/confluence entirely.

---

# C. AMBIGUOUS / TWO-CORRECT (4 ambiguity-only cases + A4)

## C1. Paper 1, Q10 — Two pronouns in the sentence
- **Question (short):** "'जो पढ़ेगा, वह सफल होगा।' — सर्वनाम है —" Key: **D** (जो, संबंधवाचक सर्वनाम). Options: (A) सफल (B) पढ़ेगा (C) वह (पुरुषवाचक) (D) जो (संबंधवाचक सर्वनाम).
- **What is wrong:** As worded ("सर्वनाम है" — "is the pronoun"), both (C) वह and (D) जो are pronouns occurring in the sentence. वह is a pronoun (in this correlative construction it is the correlative pronoun paired with जो); जो is the relative (संबंधवाचक) pronoun. The intended distinction (which *kind* of pronoun जो is) is not what the stem asks.
- **Correct fact:** जो is indeed a संबंधवाचक (relative) pronoun, so D is the intended answer — but C is not a wrong option under the stem as written.
- **Evidence:** Standard Hindi grammar: जो = संबंधवाचक सर्वनाम; वह = सर्वनाम (पुरुषवाचक/निश्चयवाचक in other classifications). Both words in the sentence belong to the pronoun class.
- **Fix:** Reword the stem, e.g. "'जो' किस प्रकार का सर्वनाम है?" ("What kind of pronoun is 'जो'?"), to make D uniquely correct.

## C2. Paper 1, Q81 — "Highest peak in India" (Kangchenjunga vs K2)
- **Question (short):** "Which is the highest peak in India?" Key: **B** (Kangchenjunga, with the parenthetical "K2 is in PoK, claimed").
- **What is wrong:** The stem is ambiguous as written. K2 (8,611 m) is higher than Kangchenjunga (8,586 m) and lies in Pakistan-occupied Kashmir, which India claims as its territory; Kangchenjunga is the highest peak within India's undisputed/controlled territory. The option's parenthetical tries to rescue the ambiguity, but a candidate answering on the claimed-territory reading could legitimately argue for K2, and K2 is not even offered as an option.
- **Correct fact:** Kangchenjunga (8,586 m, Sikkim) is the standard textbook answer for "highest peak in India" and is the intended key.
- **Evidence:** Heights: K2 8,611 m > Kangchenjunga 8,586 m; K2 is in the Karakoram in PoK. Standard Indian GK convention answers Kangchenjunga — counted as ambiguous, not as wrong key.
- **Fix:** Say "highest peak within India's undisputed territory" (or "highest peak located in India").

## C3. Paper 2, Q46 — Antonym of 'सत्य' (keyed A = असत्य; C = झूठ also defensible)
- **Question (short):** "'सत्य' का विलोम है —" Options: (A) असत्य (B) न्याय (C) झूठ (D) सही. Key: **A**.
- **What is wrong:** Two options are defensible antonyms. झूठ (lie/falsehood) is a genuine antonym of सत्य (truth) in ordinary Hindi usage, not merely a synonym of असत्य — the question stem itself concedes this in parentheses: "झूठ (synonym of असत्य, but standard antonym is असत्य)". If झूठ is a synonym of the correct answer असत्य, it cannot be unambiguously wrong. A candidate choosing C has a legitimate grievance.
- **Correct fact:** असत्य is the standard textbook pair, but झूठ is also a valid antonym of सत्य. The question is not uniquely answerable as printed.
- **Evidence:** सत्य ↔ असत्य and सत्य ↔ झूठ are both standard antonym pairs in Hindi; the stem's own parenthetical admits the overlap.
- **Fix:** Replace option (C) with a clearly unrelated word.
- **Note:** P2 Q14 ('अंधकार' — प्रकाश vs अंधेरा) is NOT flagged: अंधेरा is a synonym of अंधकार, not an antonym, so that question is uniquely answerable.

## C4. Paper 3, Q88 — "Longest river of Rajasthan" for Chambal, unqualified; conflicts with Q7 in the same paper
- **Question (short):** "Which statement about the Chambal river is correct?" Key: **D — "Longest river of Rajasthan; Kota, Rawatbhata atomic power, Chambal ravines"**.
- **What is wrong:** The key is defensible under the standard Rajasthan-GK convention (Chambal, ~1,024 km total, is called the longest river of Rajasthan), but in the **same paper** Q7 keys (D) "Longest river flowing entirely within Rajasthan (~512 km); Bisalpur Dam" for the **Banas**. A candidate who has just been told in Q7 that the Banas is the "longest river" of Rajasthan will reasonably read Q88's unqualified "Longest river of Rajasthan" as contradicting Q7. The distinction — Chambal longest overall / by total course through Rajasthan, Banas longest flowing *entirely within* Rajasthan — is real but is not stated in either option, so the pair is ambiguous as printed.
- **Correct fact:** Both underlying facts are true: Chambal is the longest river associated with Rajasthan (total length ~1,024 km, originating in Madhya Pradesh); Banas (~512 km) is the longest river flowing entirely within Rajasthan. Neither option states its qualifier.
- **Evidence:** The question bank confirms the convention — `04_GEOGRAPHY_RAJASTHAN-004` asks "Rajasthan ki sabse lambi nadi … jo keval Rajasthan me behti hai?" and answers Banas, i.e. the bank itself needs the "keval Rajasthan me" qualifier to make Banas the answer. Q88 omits any qualifier.
- **Fix:** Reword Q88 option (D) to "Longest river (by total course) in Rajasthan; …" and keep Q7's qualifier. Do not change the key.

---

# D. OUT OF SYLLABUS — Graduation-only / EXTRA topics (3 questions; keys factually correct)

## D1. Paper 1, Q52 — WWW (Internet)
- **Question (short):** "The full form of WWW is —" Key: **D — World Wide Web** (factually correct).
- **What is wrong:** Subject-tag fit, not fact. Internet topics are Graduation-only / EXTRA for the 2026 Senior Secondary (12th-level) Computer Knowledge syllabus (the question bank likewise retagged Internet/Binary/LAN/Phishing items as EXTRA, kept only as low-priority PYQ-style awareness — the 2024 paper did ask HTTP). WWW is an Internet topic.
- **Correct fact:** World Wide Web (Tim Berners-Lee, 1989) is correct.
- **Fix:** Remove from the core 12th-level set or explicitly tag EXTRA / low-priority. (Also a near-duplicate of bank `11_COMPUTER_KNOWLEDGE-007`; see §E.)

## D2. Paper 1, Q56 — E-mail
- **Question (short):** "The full form of E-mail is —" Key: **A — Electronic Mail** (factually correct).
- **What is wrong:** E-mail is explicitly a Graduation-only / EXTRA topic for the 2026 Senior Secondary syllabus, on the same basis as D1.
- **Correct fact:** Electronic Mail is correct.
- **Fix:** Remove from the core 12th-level set or explicitly tag EXTRA / low-priority.

## D3. Paper 3, Q116 — E-mail
- **Question (short):** "An email address must contain —" Options: (A) % (B) @ (C) $ (D) #. Key: **B (@)** (factually correct).
- **What is wrong:** The topic — **E-mail** — is Graduation-only / out of syllabus for the 2026 Senior Secondary (12th level) CET. It should not appear in a 12th-level mock at all.
- **Correct fact:** The @ symbol is indeed required in an email address. The problem is syllabus fit, not factual accuracy.
- **Evidence:** The question bank itself tags the analogous E-mail items as EXTRA — e.g. `11_COMPUTER_KNOWLEDGE-008` (SMTP protocol for sending email) and `11_COMPUTER_KNOWLEDGE-011` (phishing via fake email) are both tagged "EXTRA — not in 2026 12th syllabus (PYQ-style general awareness): Internet / Security". Q116 belongs in the same EXTRA category. The other Computer questions in Paper 3 (Q52 MS Word, Q83 Ctrl+V, Q86 CPU, Q111 USB) are basic computer knowledge and are in syllabus.
- **Fix:** Remove Q116 from the 12th-level paper (or move it to an explicitly labelled EXTRA / PYQ-awareness set) and replace it with an in-syllabus Computer question.

**No other out-of-syllabus topics found:** No Trigonometry, Algebra/quadratic equations, Logarithm, Cyber-security or AI questions appear in any of the three papers. All Maths is SI / average / percentage / series / ratio-type, and all Reasoning is direction / series / analogy / coding / calendar / odd-one, which are in syllabus. Paper 2 has zero out-of-syllabus questions.

---

# E. NEAR-DUPLICATES vs THE QUESTION BANK (same fact, same way; 0 exact stem duplicates)

## Paper 1 — 19 strong + 3 weaker
- **Q8** (Mission Indradhanush = immunisation of children & pregnant women) — bank `10_PUBLIC_HEALTH-003`.
- **Q9** (Mitochondria = powerhouse of the cell) — bank `07_EVERYDAY_SCIENCE-021`.
- **Q11** (POSHAN Abhiyaan launched 2018; options 2020/2014/2016/2018) — bank `10_PUBLIC_HEALTH-008`, identical options and answer.
- **Q16** (AB+ = universal recipient) — bank `07_EVERYDAY_SCIENCE-024`. Paired with Q51.
- **Q19** (Blue Pottery = Jaipur) — bank `02_ART_CULTURE_RAJASTHAN-006`, identical ask and options.
- **Q21** (Makrana marble, Taj Mahal use) — bank `02_ART_CULTURE_RAJASTHAN-020` (bank asks what Makrana marble is famous for — use in the Taj Mahal; Q21 asks where it comes from — Makrana).
- **Q25** (Gagron Fort = water fort) — bank `02_ART_CULTURE_RAJASTHAN-017`, same ask (jal-durg).
- **Q40** (PM-JAY = ₹5 lakh per family per year) — bank `06_ECONOMY_RAJASTHAN-014` **and** `10_PUBLIC_HEALTH-001` (the bank itself contains this fact twice).
- **Q42** (Vijay Stambh built by Maharana Kumbha) — bank `01_HISTORY_RAJASTHAN-010` (bank adds the reason, victory over Mahmud Khilji / Malwa).
- **Q47** (Zawar mines = zinc and lead) — bank `04_GEOGRAPHY_RAJASTHAN-015`, identical ask and answer.
- **Q51** (O negative = universal donor) — bank `07_EVERYDAY_SCIENCE-023`. Paired with Q16.
- **Q52** (WWW = World Wide Web) — bank `11_COMPUTER_KNOWLEDGE-007` (also out-of-syllabus; see §D1).
- **Q54** (PM-KISAN = ₹6,000 per year) — bank `03_GEOGRAPHY_INDIA-020` and `06_ECONOMY_RAJASTHAN-013`.
- **Q58** (Kumbhalgarh wall = second-longest in the world after the Great Wall) — bank `02_ART_CULTURE_RAJASTHAN-015`.
- **Q60** (Kumbhalgarh Fort built by Maharana Kumbha) — bank `01_HISTORY_RAJASTHAN-020`, identical ask and answer.
- **Q82** (Keyboard = input device; same distractors Printer/Speaker/Monitor) — bank `11_COMPUTER_KNOWLEDGE-014`.
- **Q87** (Phad painting = Shahpura, Pabuji & Devnarayan tales) — bank `02_ART_CULTURE_RAJASTHAN-004`.
- **Q88** (Pichwai painting = Nathdwara) — bank `02_ART_CULTURE_RAJASTHAN-005`, identical ask and answer.
- **Q92** (Baking soda = sodium bicarbonate, NaHCO₃) — bank `07_EVERYDAY_SCIENCE-014`.
- Weaker (same topic/fact cluster, different angle — flagged for awareness, not counted as full duplicates): **Q20** (Jaisamand = Dhebar Lake, built by Maharana Jai Singh) — bank `04_GEOGRAPHY_RAJASTHAN-020` asks Jaisamand's other name (Dhebar Lake); **Q100** (Matsya Sangh members: Alwar, Bharatpur, Dholpur, Karauli) — bank `01_HISTORY_RAJASTHAN-015` asks its formation date (17/18 Mar 1948) and names the same four states in its explanation; **Q101** (Tropic of Cancer passes through 8 states) — bank `03_GEOGRAPHY_INDIA-003` asks which state it does *not* pass through, on the same 8-state fact.

## Paper 2 — 9
- **Q13** (Lok Sabha seats from Rajasthan = 25) — bank `05_POLITY_RAJASTHAN-008` (also asks Rajya Sabha = 10, which is also the Paper 2 explanation).
- **Q39** (Battle of Khanwa 1527, Rana Sanga vs Babur) — bank `01_HISTORY_RAJASTHAN-007`, with the same distractors (1576 Pratap vs Akbar; 1526 Babur vs Lodi; 1192 Prithviraj vs Ghori).
- **Q45** (Swachh Bharat Mission launch, 2 October 2014) — bank `10_PUBLIC_HEALTH-012` (asks the year 2014; Paper 2 asks the exact date — weakest of the nine, same fact family, one step more specific).
- **Q66** (73rd Constitutional Amendment = Panchayati Raj) — bank `05_POLITY_RAJASTHAN-010`, same distractor (Municipalities = 74th Amendment).
- **Q98** (Kota Doria = lightweight cotton fabric/saree from Kota) — bank `02_ART_CULTURE_RAJASTHAN-007`, same distractors (Blue pottery, Marble, Kathputli).
- **Q102** (Battle of Haldighati year = 1576) — bank `01_HISTORY_RAJASTHAN-008`, same distractor years (1527, 1582, 1568).
- **Q105** (Indira Gandhi Canal origin = Harike Barrage) — bank `04_GEOGRAPHY_RAJASTHAN-014`, same distractors (Bhakra, Bisalpur, Gandhi Sagar).
- **Q108** (Synonym of 'Abandon' = Leave) — bank `13_GENERAL_ENGLISH-018`, identical option set (Keep, Hold, Leave, Protect).
- **Q110** (Janani Suraksha Yojana = institutional delivery / safe motherhood) — bank `10_PUBLIC_HEALTH-004`, same scheme and year (2005).

## Paper 3 — 11
- **Q7** (Banas = longest river flowing entirely within Rajasthan) — bank `04_GEOGRAPHY_RAJASTHAN-004`, same question in Hindi.
- **Q35** (Second Battle of Tarain 1192, Prithviraj vs Ghori) — bank `01_HISTORY_RAJASTHAN-021`.
- **Q38** (Sambhar = India's largest inland saline lake, salt production) — bank `04_GEOGRAPHY_RAJASTHAN-006`.
- **Q49** (Ghoomar = state dance of Rajasthan) — bank `02_ART_CULTURE_RAJASTHAN-001`.
- **Q64** (Guru Shikhar = highest peak, 1,722 m, Mount Abu) — bank `04_GEOGRAPHY_RAJASTHAN-002`.
- **Q65** (Kalbeliya = UNESCO Intangible Heritage 2010, Gulabo Sapera) — bank `02_ART_CULTURE_RAJASTHAN-002`.
- **Q66** (India declared polio-free 2014) — bank `10_PUBLIC_HEALTH-006`.
- **Q85** (Chittorgarh = largest fort in India) — bank `02_ART_CULTURE_RAJASTHAN-014` (also explanation defect; see §B12).
- **Q99** (Battle of Khanwa — Babur vs Rana Sanga, 1527) — bank `01_HISTORY_RAJASTHAN-007`.
- **Q115** (Maharana Kumbha — Vijay Stambh, 1448, Malwa victory) — bank `01_HISTORY_RAJASTHAN-010`.
- **Q120** (Terah Taali — 13 manjiras tied to body) — bank `02_ART_CULTURE_RAJASTHAN-011` (partial: bank asks the community — Kamad — while Paper 3 asks the description, but both hinge on the identical "13 manjiras" fact).

**Total vs question bank: 39 strong near-duplicates (P1 19 + P2 9 + P3 11) + 3 weaker (P1).** Generic arithmetic templates with different numbers (e.g. SI questions) were NOT counted; only identical facts were. If the mock papers and the bank are meant to be independent practice sets, these should be replaced or re-angled (different fact about the same entity). If overlap is intentional (bank = revision pool for mocks), that should be stated explicitly.

---

# F. WITHIN-PAPER REPETITION AND MINOR WORDING

## F1. Within-paper repetition (same fact twice in one paper)
- **Paper 1 — 3 topic pairs:** Q13/Q35 Ana Sagar Lake (location vs builder; identical explanations — see §B1); Q50/Q118 Jaisalmer Fort (builder vs "famous for"; identical explanations — see §B2); Q58/Q60 Kumbhalgarh Fort (famous for vs builder; identical explanations — see §B3). Also Q16/Q51 (AB+ recipient / O− donor — complementary pair, defensible) and Q79/Q113 (Banganga river twice — complementary, same river).
- **Paper 1 — template repetition:** Simple Interest ×4 (Q2, Q12, Q34, Q89 — all recomputed, all correct); percentage-discount ×2 (Q32, Q83 — both correct); doubling series ×2 (Q41, Q62 — both correct). 4 of 120 slots on one SI formula is heavy repetition for a mock.
- **Paper 2 — 5 fact-pairs:** Q16/Q39 Rana Sanga (reign vs Khanwa; identical explanations — see §B4); Q75/Q92 Udai Singh II (reign vs founded Udaipur; identical explanations — see §B5); Q84/Q102 Haldighati (event vs year 1576); Q65/Q73 Ranthambore Fort (district vs "famous for"; identical explanations); Q41/Q52 Pushkar Lake ("known for" vs location; identical explanations — see §B6).
- **Paper 2 — template repetition:** Simple Interest ×6 (Q10, Q15, Q18, Q50, Q77, Q95 — identical formula, numbers changed only; 5% of the paper on one computation); Average ×3 (Q47, Q96, Q109 — two of the three are also wrong-keyed; see §A2/A3).
- **Paper 3 — 6 pairs:** Q18/Q62 Fire Dance / Agni Nritya (Jasnath sect); Q27/Q87 Kachchhi Ghodi (Q27's explanation is exactly Q87's keyed answer — the two questions swap stem and explanation); Q23/Q82 Mehrangarh Fort (Q23's explanation adds "Rao Jodha founded Jodhpur", which is Q82's keyed answer); Q41/Q57 Maharaja Ganga Singh (identical explanations — see §B11); Q55/Q98 Rajasthan Unfair Means (Prevention) Act (year 2022 vs what it relates to); Q2/Q104 VB-G RAM G Act, 2025 (what it relates to vs which Act it replaced — Q104's answer is already contained in Q2's keyed option).
- **Paper 3 — template repetition:** Average of two numbers ×4 (Q30, Q76, Q77, Q100 — Q100 wrong-keyed; see §A5); Simple Interest ×3 (Q11, Q22, Q92); percentage discount ×2 (Q61, Q103). Nine slots on three two-number drills; all keys/explanations in this group are correct except Q100.

## F2. Minor wording / editorial defects (keys unaffected unless noted)
- **P1 Q55** (Chiranjeevi / Mukhyamantri Ayushman Arogya Yojana = ₹25 lakh) — key B correct on the scheme's history (₹5 lakh at launch 2021, raised to ₹10 lakh, then ₹25 lakh in 2023; renamed in 2024). The explanation itself says "Verify current name/limit" — an open verification note left in a candidate-facing explanation. Confirm the current figure before use (see also "Could not verify").
- **P1 Q74** (largest district = Jaisalmer) — key B correct. Explanation's qualifier "Dholpur smallest (before 2023 changes)" is a dated hedge; district boundaries changed in 2023 and again in Dec 2024 (new districts abolished), so the "smallest district" aside should be re-checked rather than left qualified.
- **P1 Q86** — option (B) printed as "The (only)", an odd phrasing for an article question; key A ("An honest man") correct and unaffected.
- **P1 Q117** — option (C) printed as "She-lion (not standard)", an editorial aside inside an option; key D (Lioness) correct and unaffected.
- **P2 Q7** — garbled stem: "The 'Bhakti' — no: Bhakra Dam is on which river?" The stray "'Bhakti' — no:" is an editing leftover. Key (A — Sutlej) correct. Delete the stray fragment.
- **P2 Q50 and Q77** — "for 1 years" (should be "for 1 year"). Both keys correct (₹144 and ₹180).
- **P2 Q100** — garbled rule hint ("sum ×?") in the CAT/DOG letter-sum question; the rule is a plain letter-position sum (D+O+G = 4+15+7 = 26, key C — correct). Delete "sum ×? —".
- **P2 Q37** — Jaisamand Lake district wording: key **C — Udaipur (Salumbar)**. Jaisamand (Dhebar) Lake is in Salumbar district, carved out of Udaipur district in 2023 — "Udaipur (Salumbar)" is defensible but confusing; a candidate answering "Salumbar" has no clean option. Recommend rewording the option to "Salumbar (formerly Udaipur district)".
- **P3 Q4** — stem contains a struck-through false start: "The 'Silk Route' — no: India's largest port by cargo is —". Delete the fragment (substantive problem is §A4).
- **P3 Q17** — stray marker: "Choose the correctly spelt word — (2):" — the "(2)" serves no purpose; delete.
- **P3 Q22** — "Simple Interest on ₹4000 at 10% p.a. for 1 years is —" — should be "for 1 year".

---

# G. COULD NOT VERIFY (not flagged as wrong; re-check before exam use)

- **P1 Q20** — "Jaisamand was the second-largest artificial lake in Asia (then)": the superlative's scope and date ("then") could not be independently verified from the auditor's own knowledge beyond the standard Rajasthan-GK textbook claim; not flagged as wrong.
- **P1 Q64** — "Nakki Lake is the only natural lake in the Aravalli region": the "only" scope could not be independently verified beyond the standard Rajasthan-GK claim; not flagged as wrong.
- **P1 Q55** — current (post-2024 rename) cover limit/name of the Chiranjeevi / Mukhyamantri Ayushman Arogya Yojana: the paper's own explanation flags "verify current name/limit"; the ₹25 lakh key is correct on the scheme's published history but the live current figure was not verifiable in this read-only audit.
- **P1 Q79** — Banganga joining the Yamuna via the Gambhir: accepted as correct on the auditor's knowledge (Banganga → Gambhir → Yamuna) but no official source was consulted in this audit.
- **P2 Q30** — Junagarh Fort "Never conquered": standard Rajasthan-GK guidebook claim, accepted; the absolute claim could not be verified from the auditor's own knowledge alone. Treat as a conventional guidebook answer.
- **P2 Q56** — Raj Prashasti as "longest Sanskrit inscription": widely repeated guidebook claim, accepted, not independently verifiable from the auditor's own knowledge; not flagged.
- **P2 Q22** — Bhavai "famous in Nagaur, Jodhpur": accepted as printed; the precise district association could not be verified from the auditor's own knowledge and is not load-bearing for the key (B — Rajasthan, balancing pots).
- **P2 Q34** — 11 vowels in the Hindi alphabet: accepted as the standard CET/school answer (अ आ इ ई उ ऊ ऋ ए ऐ ओ औ); some counts include अं/अः, but 11 is the conventional answer and the key is not disputed.
- **P3 Q12** — minor detail: the keyed option says the Kali Sindh "flows through Jhalawar-Kota; Jhalrapatan". The Jhalawar-Kota course is correct; whether Jhalrapatan town itself stands on the Kali Sindh (some sources associate Jhalrapatan with the Chandrabhaga) could not be verified; the option is the only plausible correct choice either way — no flag.
- **P3 Q23** — spelling detail: "Bhakurcheeria hill" (Mehrangarh) — the hill name is given in this spelling in Rajasthan GK sources known to the auditor, but the spelling could not be independently verified; the fact (Mehrangarh on that hill in Jodhpur) is not in doubt — no flag.
- **P3 Q108** — builder detail: Gagron Fort "Dodal / Khinchi Chauhan" — the fort's association with the Dodal/Khinchi Chauhan line is as stated in Rajasthan GK sources known to the auditor, but the precise founder attribution could not be independently verified — no flag.
- **P3 Q2 / Q104** — currency of the 2025 Act: the VB-G RAM G Act, 2025 replacing MGNREGA with a 125-day guarantee (passed December 2025) is as stated in the paper and matches the auditor's knowledge of the December 2025 legislation; it is a fast-moving current-affairs fact and should be re-checked against the official gazette/notification immediately before the 1–3 Dec 2026 exam, as should the retained-district lists in Q9/Q16/Q19/Q60 (Deeg, Phalodi, Kotputli-Behror, Khairthal-Tijara — all created 2023 and retained after the December 2024 abolition of 9 of the 17 new districts, per the paper's own "verify current list" notes).

---

# H. SUMMARY

- **Questions checked:** 360 (120 per paper; every Maths/Reasoning answer recomputed from scratch; every factual key checked; every explanation checked against its key).
- **Problems found by severity:**
  - **Wrong key: 5** — P1 Q114 (duplicate options, both "Bikaner"); P2 Q47 (average 18 & 27 = 22.5, no such option); P2 Q109 (average 30 & 45 = 37.5, no such option); P3 Q4 (largest port by cargo; key B, correct A Paradip); P3 Q100 (average 50 & 75 = 62.5, no such option). Three of the five are the same arithmetic slip (odd-sum average, .5 dropped).
  - **Wrong / inadequate explanation: 15** — P1 Q13, Q50, Q60; P2 Q16, Q75, Q52, Q51, Q81, Q87, Q89; P3 Q4, Q50, Q57, Q85, Q100. Of these, 13 have correct keys (all except P3 Q4 and P3 Q100, which also have wrong keys). Dominant pattern: 7 explanations copied verbatim from another question in the same paper (P1 Q13/Q50/Q60, P2 Q16/Q75/Q52, P3 Q57); 3 river-terminus explanations omit the terminus (P2 Q51/Q81/Q87); 2 present the Rani Padmini legend as dated fact (P2 Q89, P3 Q85); 1 names no builder (P3 Q50).
  - **Ambiguous / two-correct: 5** — P1 Q10 (two pronouns), P1 Q81 (Kangchenjunga vs K2), P2 Q46 (सत्य: असत्य vs झूठ), P3 Q88 (Chambal "longest river" vs Q7 Banas), P3 Q4 (option B names two ports; also wrong key — counted in §A).
  - **Out-of-syllabus (Graduation-only / EXTRA): 3** — P1 Q52 (WWW / Internet), P1 Q56 (E-mail), P3 Q116 (E-mail). Keys factually correct; fault is syllabus fit. No Trigonometry, Algebra/quadratic, Logarithm, Cyber-security or AI questions in any paper. Paper 2 has zero out-of-syllabus questions.
  - **Near-duplicate vs question bank: 39 strong + 3 weaker** — P1 19 strong + 3 weak, P2 9, P3 11. No exact stem duplicates (mechanical check: 0).
  - **Within-paper repetition:** P1 3 topic pairs + SI ×4 / discount ×2 / doubling-series ×2; P2 5 fact-pairs + SI ×6 / Average ×3; P3 6 fact-pairs + Average ×4 / SI ×3 / discount ×2.
  - **Minor wording: 12 items** — P1 Q55, Q74, Q86, Q117; P2 Q7, Q50, Q77, Q100, Q37; P3 Q4 (stem artefact), Q17, Q22 (plus template repetition counted above).
  - **Distinct questions with at least one substantive problem (wrong key, wrong explanation, ambiguous, out-of-syllabus, or near-duplicate): ~89 of 360** — Paper 1: 30 of 120; Paper 2: 29 of 120; Paper 3: ~30 of 120. Of these, only **5 have a wrong key** and **13 have a wrong explanation with a correct key**; the bulk of the ~89 is near-duplication vs the question bank (~39) and within-paper repetition.
  - **Questions fully clean (no flag of any kind, including minor wording): ~271 of 360.**
- **Could not verify:** 12 items listed in §G (guidebook superlatives, district lists post-2024 reorganisation, VB-G RAM G Act currency, spelling/builder details). None flagged as wrong.
- **Overall verdict:** The three papers must NOT be used as printed. Five questions have wrong keys (three have no correct option at all), three questions are out of syllabus for the 12th level, twelve further explanations do not justify their (correct) keys, and roughly a quarter of the 360 slots repeat material already in the question bank or elsewhere in the same paper. The remaining ~271 questions were found correct. Minimum fixes before use: re-option/replace the 5 wrong-key questions; rewrite the 12 wrong explanations; reword or replace the 4 ambiguity-only questions; remove or tag EXTRA the 3 out-of-syllabus questions; and decide explicitly whether the ~39 bank near-duplicates are intentional revision overlap or should be replaced.
