# Paper 3 Audit — Rajasthan CET 2026 Mock Papers (READ-ONLY)

- **Source file:** `/home/hatch/workspace/cet-2026-upload/mock_papers.md`
- **Paper 3 scope audited:** Q1–Q120 (lines 2528–3489), answer-key table (lines 3490–3526), explanations (lines 3527–3765). All 120 questions read and checked.
- **Cross-check file:** `/home/hatch/workspace/cet-2026-upload/question_bank.csv` (300 MCQs) — grepped by key terms for near-duplicates.
- **Ground truth used:** RSSB Adv 08/2026, exam 1–3 Dec 2026, 120Q / 240 marks / 150 min, +2 / −2/3, E = 0, blank = −2/3, >12 blanks disqualified. No per-subject question split in the official scheme.
- **Method:** every Maths/Reasoning answer recomputed from scratch; every factual claim checked against the auditor's own knowledge; explanations checked against the keyed option; subject tags checked against the 13-head 2026 Senior Secondary (12th level) syllabus, with Trigonometry / Algebra-quadratic / Logarithms / Internet / E-mail / Cyber-security / AI treated as Graduation-only (out of syllabus) per the audit brief.
- **Only confirmed problems are listed below.** The other questions in Paper 3 were found correct on key, explanation and syllabus fit (subject to the "could not verify" notes in the summary).

---

## 1. Q4 — WRONG KEY + AMBIGUOUS (Geo India: largest port by cargo)

- **Question (short):** "India's largest port by cargo is —" Options: (A) Paradip, (B) "Jawaharlal Nehru Port (Nhava Sheva) / Deendayal (Kandla) — varies by year", (C) Chennai, (D) Kochi. Keyed answer: **B**.
- **What is wrong:** The key is wrong, and option (B) is itself defective — it names **two different ports** as a single option, so a candidate cannot tell which port is being asserted. On total cargo the correct answer among the options is **(A) Paradip**, not (B). JNPT (Nhava Sheva) has never led on total cargo; it leads on **container** traffic only. The paper's own explanation concedes this: "By cargo volume, Deendayal (Kandla) and Paradip often lead among major ports; JNPT leads in container traffic. … Treat JNPT as container leader." That explanation contradicts the key it is supposed to justify — the stem asks about cargo, not containers.
- **Correct answer / fact:** Among government major ports, Paradip has been the largest cargo handler since FY 2023-24: FY 2024-25 Paradip 150.41 MMT vs Deendayal 150.16 MMT vs JNPA 92.12 MMT (Ministry of Ports, Shipping & Waterways / Indian Ports Association figures, as reported in 2025-26 port rankings). Deendayal (Kandla) was the long-standing leader before FY 2023-24, so the "varies by year" hedge in option (B) does not save it — JNPT is wrong in every recent year, and Deendayal is no longer first.
- **Evidence / reasoning:** (i) Recomputed ranking from published FY 2024-25 major-port cargo: Paradip 150.41 > Deendayal 150.16 > JNPA 92.12. (ii) The explanation's own container-vs-cargo distinction destroys key (B). (iii) Note a further underspecification: the stem does not say "major port" — counting all ports including private Mundra (~200.7 MMT in FY 2024-25), Mundra would be largest overall and **none** of the four options would be correct. The question must be reworded to "largest major port by cargo" with (A) Paradip as key, or dropped.
- **Fix:** Reword stem to "largest major port by cargo handled", key (A) Paradip, and rewrite the explanation to give the FY 2024-25 figures and the container-vs-cargo distinction.

## 2. Q100 — WRONG KEY: NO CORRECT OPTION LISTED (Maths: Average)

- **Question (short):** "Average of 50 and 75 is —" Options: (A) 62, (B) 67, (C) 59, (D) 72. Keyed answer: **A (62)**.
- **What is wrong:** The key is arithmetically wrong, and **no option is correct**. The explanation repeats the error: "Average = (50+75)/2 = 62."
- **Correct answer / fact:** (50 + 75) / 2 = 125 / 2 = **62.5**. That value does not appear among the options.
- **Evidence / reasoning:** Recomputed from scratch: 50 + 75 = 125; 125 ÷ 2 = 62.5. The other averages in the paper were recomputed and are correct (Q30: 25; Q76: 50; Q77: 15), so this is an isolated slip, not a systematic error — but as printed the question is unanswerable and any candidate who computes correctly is penalised.
- **Fix:** Change option (A) to 62.5 (key A) or replace the numbers with an even-sum pair (e.g. average of 50 and 74 = 62).

## 3. Q116 — OUT OF SYLLABUS (Computer: E-mail)

- **Question (short):** "An email address must contain —" Options: (A) % (B) @ (C) $ (D) #. Keyed answer: **B (@)**.
- **What is wrong:** The answer itself (@) is factually correct, but the topic — **E-mail** — is Graduation-only / out of syllabus for the 2026 Senior Secondary (12th level) CET, per the audit brief's out-of-syllabus list (Internet / E-mail / Cyber-security / AI). It should not appear in a 12th-level mock at all.
- **Correct answer / fact:** The @ symbol is indeed required in an email address. The problem is syllabus fit, not factual accuracy.
- **Evidence / reasoning:** The question bank itself tags the analogous E-mail items as EXTRA — e.g. `11_COMPUTER_KNOWLEDGE-008` (SMTP protocol for sending email) and `11_COMPUTER_KNOWLEDGE-011` (phishing via fake email) are both tagged "EXTRA — not in 2026 12th syllabus (PYQ-style general awareness): Internet / Security". Q116 belongs in the same EXTRA category. The other Computer questions in Paper 3 (Q52 MS Word, Q83 Ctrl+V, Q86 CPU, Q111 USB) are basic computer knowledge and are in syllabus.
- **Fix:** Remove Q116 from the 12th-level paper (or move it to an explicitly labelled EXTRA / PYQ-awareness set) and replace it with an in-syllabus Computer question.

## 4. Q50 — WRONG / INADEQUATE EXPLANATION (Raj: Junagarh Fort builder)

- **Question (short):** "Who built / is chiefly associated with Junagarh Fort?" Keyed answer: **B — Raja Rai Singh (1589-94)**.
- **What is wrong:** The key is correct, but the explanation does not justify it. The explanation reads in full: "Never conquered; Anup Mahal; not built on a hill." None of those three phrases names Raja Rai Singh or the 1589-94 construction dates, so a candidate cannot see from the explanation why (B) is right and (A) Raja Bhoj / (C) Maharana Sanga / (D) Maharaja Ranjit Singh are wrong.
- **Correct answer / fact:** Junagarh Fort, Bikaner, was built by Raja Rai Singh (reigned 1571-1612) in 1589-94; it is a plain (non-hill) fort that was never conquered. The "never conquered / not built on a hill" facts are true but are properties of the fort, not evidence for its builder.
- **Evidence / reasoning:** The keyed option (B) is the only option containing a builder + date; the explanation supplies no builder information at all, so the key-explanation link is broken. Compare Q82 in the same paper, whose explanation correctly names Rao Jodha (1459) for Mehrangarh.
- **Fix:** Rewrite the explanation as: "Built by Raja Rai Singh of Bikaner, 1589-94; a ground-level fort (not on a hill), never conquered; Anup Mahal inside."

## 5. Q57 — WRONG / INADEQUATE EXPLANATION, DUPLICATED FROM Q41 (Raj: Maharaja Ganga Singh)

- **Question (short):** "Maharaja Ganga Singh is associated with which state/kingdom and period?" Keyed answer: **D — Bikaner, 1888–1943**.
- **What is wrong:** The key is correct, but the explanation is a verbatim copy of the Q41 explanation ("Built Ganga Canal (1927, from Sutlej); represented India at Versailles 1919") and says nothing about **Bikaner** or the **1888–1943** period — the two things option (D) actually asserts. A candidate reading the explanation cannot verify the key.
- **Correct answer / fact:** Maharaja Ganga Singh ruled Bikaner 1888-1943 (reigned 1888-1943; born 1880, died 1943). The Ganga Canal (1927) and Versailles 1919 facts in the explanation are true of him, but they do not establish the state/period in the keyed option.
- **Evidence / reasoning:** Q41 and Q57 test the same person; Q41's explanation is appropriate for Q41 (event-based), but Q57 needs a state/period justification. The copy-paste is visible in the file: the Q41 and Q57 explanation lines are identical.
- **Fix:** Rewrite the Q57 explanation as: "Ganga Singh, Maharaja of Bikaner, reigned 1888-1943; built the Ganga Canal (1927) and represented India at Versailles (1919)." (Also see §8 — Q41/Q57 are a within-paper near-duplicate pair; consider replacing one of them.)

## 6. Q85 — EXPLANATION PRESENTS LEGEND AS FACT (Raj: Chittorgarh Fort)

- **Question (short):** "Chittorgarh Fort is famous for —" Keyed answer: **A — Largest fort in India**.
- **What is wrong:** The key is correct (Chittorgarh, ~700 acres, is India's largest fort), but the explanation adds a historically unsound claim: "Jauhar of Rani Padmini (1303)". Rani Padmini is a literary figure from Malik Muhammad Jayasi's epic poem *Padmavat* (c. 1540); her existence and a 1303 jauhar led by her are not established historical facts. Presenting it alongside the genuinely historical 1535 jauhar (Rani Karnavati, during Bahadur Shah of Gujarat's siege) as if both were equally factual misleads candidates.
- **Correct answer / fact:** Key (A) stands. The 1303 siege of Chittorgarh by Alauddin Khalji is historical; a jauhar occurred, but attributing it to "Rani Padmini" is the *Padmavat* legend, not verified history. The 1535 jauhar under Rani Karnavati is the historically attested one usually cited alongside it.
- **Evidence / reasoning:** Padmini first appears in Jayasi's *Padmavat*, written ~237 years after 1303; no contemporary source names her. Standard history texts treat her as legendary. The explanation should not state her jauhar as a dated fact.
- **Fix:** Rewrite the explanation as: "Largest fort in India (~700 acres); Vijay Stambh; jauhar of 1303 (Alauddin Khalji's siege) and of 1535 under Rani Karnavati." Drop "Rani Padmini (1303)" or label it explicitly as legend.

## 7. Q88 — AMBIGUOUS WORDING, CONFLICTS WITH Q7 IN THE SAME PAPER (Raj: Chambal river)

- **Question (short):** "Which statement about the Chambal river is correct?" Keyed answer: **D — "Longest river of Rajasthan; Kota, Rawatbhata atomic power, Chambal ravines"**.
- **What is wrong:** The key is defensible under the standard Rajasthan-GK convention (Chambal, ~1,024 km total, is called the longest river of Rajasthan), but in the **same paper** Q7 keys (D) "Longest river flowing entirely within Rajasthan (~512 km); Bisalpur Dam" for the **Banas**. A candidate who has just been told in Q7 that the Banas is the "longest river" of Rajasthan will reasonably read Q88's unqualified "Longest river of Rajasthan" as contradicting Q7. The distinction — Chambal longest overall / by total course through Rajasthan, Banas longest flowing *entirely within* Rajasthan — is real but is not stated in either option, so the pair is ambiguous as printed.
- **Correct answer / fact:** Both underlying facts are true: Chambal is the longest river associated with Rajasthan (total length ~1,024 km, originating in Madhya Pradesh); Banas (~512 km) is the longest river flowing entirely within Rajasthan. Neither option states its qualifier.
- **Evidence / reasoning:** The question bank confirms the convention — `04_GEOGRAPHY_RAJASTHAN-004` asks "Rajasthan ki sabse lambi nadi … jo keval Rajasthan me behti hai?" and answers Banas, i.e. the bank itself needs the "keval Rajasthan me" qualifier to make Banas the answer. Q88 omits any qualifier.
- **Fix:** Reword Q88 option (D) to "Longest river (by total course) in Rajasthan; …" and Q7 option (D) already carries its qualifier — keep it. Do not change the key.

## 8. WITHIN-PAPER NEAR-DUPLICATES — SAME FACT TESTED TWICE IN PAPER 3 (6 pairs)

- **What is wrong:** Six facts are each tested twice in the same 120-question paper, wasting slots that should cover distinct syllabus ground. In several pairs the explanation of one question literally gives away the answer to the other.
- **Pairs (all confirmed by reading the paper):**
  1. **Q18 & Q62 — Fire Dance / Agni Nritya (Jasnath sect).** Q18: "Which fact about Fire Dance is correct?" → (C) dancing on burning embers; Jasnath sect devotees. Q62: "Fire Dance is associated with —" → (A) Bikaner — Jasnathi sect. Same fact, same answer content.
  2. **Q27 & Q87 — Kachchhi Ghodi.** Q27: associated with (A) Shekhawati; its explanation is "Dummy horse dance; men at weddings/fairs" — which is exactly Q87's keyed answer (B) "Dummy horse dance; men at weddings/fairs". The two questions swap stem and explanation.
  3. **Q23 & Q82 — Mehrangarh Fort.** Q23: famous for (B) "On Bhakurcheeria hill"; its explanation adds "Rao Jodha founded Jodhpur" — which is Q82's keyed answer (B) "Rao Jodha (1459)". Same fort, overlapping content.
  4. **Q41 & Q57 — Maharaja Ganga Singh.** Q41 (events: Ganga Canal 1927, Versailles 1919) and Q57 (Bikaner, 1888-1943) test the same person, and the Q57 explanation is a verbatim copy of the Q41 explanation (see §5).
  5. **Q55 & Q98 — Rajasthan Unfair Means (Prevention) Act.** Q55 asks the year (key D, 2022); Q98 asks what it relates to (key B, prevention of cheating / paper leaks). Same Act, two slots.
  6. **Q2 & Q104 — VB-G RAM G Act, 2025.** Q2 asks what it relates to (key C, rural employment guarantee replacing MGNREGA); Q104 asks which Act it replaced (key B, MGNREGA 2005). Same Act, two slots, and Q104's answer is already contained in Q2's keyed option.
- **Evidence / reasoning:** Each pair shares the same subject, same named entity and (except Q23/Q82 and Q55/Q98, which are different facets of one entity) the same answer fact. The Q27 explanation / Q87 key identity and the Q41/Q57 identical explanation lines are verbatim in the file.
- **Fix:** Keep one question from each pair and replace the other with a distinct syllabus topic (e.g. replace Q62 with another folk dance, Q87 with another dance's region, Q57 with another ruler, Q98 with another Rajasthan Act, Q104 with another 2025 scheme).

## 9. NEAR-DUPLICATES VS THE QUESTION BANK (11 Paper 3 questions)

- **What is wrong:** The brief states the bank was mechanically checked for exact stem duplicates (0 found). Grepping the bank by key terms shows 11 Paper 3 questions ask the **same fact, with the same answer**, as a bank item — same-fact near-duplicates, not just same topic. (Generic arithmetic templates with different numbers — e.g. the SI questions — were **not** counted; only identical facts were.)
- **Confirmed matches (Paper 3 Q → bank item):**
  | Paper 3 | Fact | Bank item |
  |---|---|---|
  | Q7 | Banas = longest river flowing entirely within Rajasthan | `04_GEOGRAPHY_RAJASTHAN-004` — same question in Hindi, answer Banas |
  | Q35 | Second Battle of Tarain 1192, Prithviraj vs Ghori | `01_HISTORY_RAJASTHAN-021` — "dusri Tarain ladai kab hui?" answer 1192 |
  | Q38 | Sambhar = India's largest inland saline lake, salt production | `04_GEOGRAPHY_RAJASTHAN-006` — "Bharat ki sabse badi khare pani ki jheel?" answer Sambhar |
  | Q49 | Ghoomar = state dance of Rajasthan | `02_ART_CULTURE_RAJASTHAN-001` — "Rajasthan ka rajya nritya?" answer Ghoomar |
  | Q64 | Guru Shikhar = highest peak, 1,722 m, Mount Abu | `04_GEOGRAPHY_RAJASTHAN-002` — same fact, answer Guru Shikhar 1,722 m |
  | Q65 | Kalbeliya = UNESCO Intangible Heritage 2010, Gulabo Sapera | `02_ART_CULTURE_RAJASTHAN-002` — "UNESCO ne kab … 2010", Gulabo Sapera |
  | Q66 | India declared polio-free 2014 | `10_PUBLIC_HEALTH-006` — "Bharat kab se polio-mukt hai?" answer 2014 |
  | Q85 | Chittorgarh = largest fort in India | `02_ART_CULTURE_RAJASTHAN-014` — "Sabse bada kila (Bharat)?" answer Chittorgarh |
  | Q99 | Battle of Khanwa — Babur vs Rana Sanga (1527) | `01_HISTORY_RAJASTHAN-007` — Khanwa 1527, Rana Sanga vs Babur |
  | Q115 | Maharana Kumbha — Vijay Stambh (1448, Malwa victory) | `01_HISTORY_RAJASTHAN-010` — "Vijay Stambh kisne aur kyun banwaya?" answer Rana Kumbha, Malwa vijay |
  | Q120 | Terah Taali — 13 manjiras tied to body | `02_ART_CULTURE_RAJASTHAN-011` — Terah Taali, "shareer par 13 manjire bandhkar" |
- **Evidence / reasoning:** Each row was found by `grep -i` on the bank CSV for the distinctive term (e.g. "Guru Shikhar", "Terah Taali", "polio-mukt", "Sabse bada kila") and the bank stem + correct answer match the Paper 3 stem + key on the same fact. Q120 is a partial near-duplicate (bank asks the community — Kamad — while Paper 3 asks the description, but both hinge on the identical "13 manjiras" fact).
- **Fix:** If the mock papers and the bank are meant to be independent practice sets, replace or re-angle these 11 questions (different fact about the same entity, e.g. Terah Taali's community, Kalbeliya's UNESCO year asked the other way, a different lake/fort). If overlap is intentional (bank = revision pool for mocks), no action is needed — but that should be stated explicitly, since the brief presents the bank check as a de-duplication exercise.

## 10. MINOR WORDING / DRAFTING DEFECTS

- **Q4 stem contains a struck-through false start:** The stem reads "The 'Silk Route' — no: India's largest port by cargo is —". The "The 'Silk Route' — no:" fragment is a leftover drafting artefact; it is confusing as printed and should be deleted. (Substantive problem with Q4 is §1.)
- **Q17 stray marker:** "Choose the correctly spelt word — (2):" — the "(2)" serves no purpose and should be deleted.
- **Q22 grammar:** "Simple Interest on ₹4000 at 10% p.a. for 1 years is —" — should be "for 1 year".
- **Template repetition (same drill, different numbers, 9 questions):** average of two numbers is asked **four** times (Q30: 20 & 30; Q76: 40 & 60; Q77: 12 & 18; Q100: 50 & 75), simple interest **three** times (Q11: ₹6000/5%/2yr; Q22: ₹4000/10%/1yr; Q92: ₹800/15%/2yr), and a percentage discount **twice** (Q61: ₹500 at 10%; Q103: ₹800 at 25%). All keys/explanations in this group are correct except Q100 (§2), but nine slots on three two-number drills is poor coverage for a 120-question mock; replace most of them with other in-syllabus Maths (ratio, time & work, HCF/LCM, volume, number series already present) or Reasoning items.
- **Evidence / reasoning:** All four average stems, three SI stems and two discount stems are verbatim in the file (lines 2528-3489) with only the numbers changed; recomputation confirms the non-Q100 ones are correct.

---

## Summary

- **Questions checked:** 120 (Q1–Q120, key table and all explanations read in full).
- **Problems found by severity:**
  - **Wrong key: 2** — Q4 (largest port by cargo; key B, correct is A Paradip), Q100 (average of 50 & 75; key A 62, correct is 62.5, which is not among the options).
  - **Wrong / inadequate explanation: 5** — Q4 (explanation contradicts the key: JNPT is the container leader, not the cargo leader), Q50 (no builder named), Q57 (verbatim copy of Q41's explanation; does not justify Bikaner 1888-1943), Q85 (Rani Padmini 1303 jauhar presented as fact; it is *Padmavat* legend), Q100 (explanation repeats the arithmetic error, "(50+75)/2 = 62"). Q4 and Q100 overlap with the wrong-key count.
  - **Ambiguous: 2** — Q4 (option (B) names two different ports; stem does not specify "major port", so private Mundra would also beat every option), Q88 ("Longest river of Rajasthan" for Chambal, unqualified, clashes with Q7's "longest river flowing entirely within Rajasthan" for Banas).
  - **Out of syllabus: 1** — Q116 (E-mail — Graduation-only topic for the 12th-level CET; the bank itself tags the analogous email items EXTRA).
  - **Near-duplicate: 6 within-paper pairs + 11 vs the question bank** — within-paper: Q18/Q62, Q27/Q87, Q23/Q82, Q41/Q57, Q55/Q98, Q2/Q104; vs bank: Q7, Q35, Q38, Q49, Q64, Q65, Q66, Q85, Q99, Q115, Q120 (see §9 table).
  - **Minor wording: 4 items** — Q4 stem artefact ("The 'Silk Route' — no:"), Q17 stray "(2)", Q22 "1 years", and template repetition (average ×4, SI ×3, discount ×2 = 9 slots).
- **Distinct questions affected:** 2 wrong-key + 1 out-of-syllabus + 3 explanation-only (Q50, Q57, Q85) + 1 ambiguous-only (Q88) + near-duplicate-only questions not already counted ≈ 30 of 120 questions carry at least one flag (several questions carry two flags, e.g. Q4, Q85, Q57). The remaining ~90 questions were found correct.
- **No other out-of-syllabus topics found:** no Trigonometry, Algebra/quadratic, Logarithm, Internet, Cyber-security or AI questions appear in Paper 3; all Maths is SI / average / percentage / series and all Reasoning is calendar / analogy / coding / series, which are in syllabus.
- **Could NOT verify (marked unverified, not counted as problems):**
  - **Q12, minor detail:** the keyed option says the Kali Sindh "flows through Jhalawar-Kota; Jhalrapatan". The Jhalawar-Kota course is correct; whether Jhalrapatan town itself stands on the Kali Sindh (some sources associate Jhalrapatan with the Chandrabhaga) could not be verified from the auditor's knowledge, and the option is the only plausible correct choice either way — so no flag.
  - **Q23, spelling detail:** "Bhakurcheeria hill" (Mehrangarh) — the hill name is given in this spelling in Rajasthan GK sources known to the auditor, but the spelling could not be independently verified; the fact (Mehrangarh on that hill in Jodhpur) is not in doubt — no flag.
  - **Q108, builder detail:** Gagron Fort "Dodal / Khinchi Chauhan" — the fort's association with the Dodal/Khinchi Chauhan line is as stated in Rajasthan GK sources known to the auditor, but the precise founder attribution could not be independently verified — no flag.
  - **Q2 / Q104, currency of the 2025 Act:** the VB-G RAM G Act, 2025 replacing MGNREGA with a 125-day guarantee (passed December 2025) is as stated in the paper and matches the auditor's knowledge of the December 2025 legislation; it is a fast-moving current-affairs fact and should be re-checked against the official gazette/notification immediately before the 1-3 Dec 2026 exam, as should the retained-district lists in Q9/Q16/Q19/Q60 (Deeg, Phalodi, Kotputli-Behror, Khairthal-Tijara — all created 2023 and retained after the December 2024 abolition of 9 of the 17 new districts, per the paper's own "verify current list" notes).
- **Overall verdict:** Paper 3 is largely sound — ~90 of 120 questions are clean — but it must not be used as printed: Q4 and Q100 have wrong keys (Q100 has no correct option at all), Q116 is out of syllabus, three explanations are wrong or do not justify their keys, and roughly a quarter of the paper is duplicated material (6 repeated facts inside the paper, 11 repeated from the bank) plus 9 slots spent on three repeated arithmetic drills.
