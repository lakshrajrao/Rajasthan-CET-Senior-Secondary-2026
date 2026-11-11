# LOGICAL REASONING & MATHEMATICS — Rajasthan CET Senior Secondary 2026

**Redesigned 11 Nov 2026 under `LEARNING_METHODOLOGY.md` (A–K structure). Subject: Logical Reasoning & Mathematics | Syllabus head 8.**
**Sources:** previous notes `notes/08_reasoning_mathematics.md` (109 lines — every verified fact and solved example preserved, see "Preservation note" at the end; every solved example recomputed by the author of this file); master notes §8; bank MCQs `08_MATHEMATICS-001..024` + `08_REASONING-001..024` (all 48 recomputed/solved in the audit — 0 wrong keys); PYQ dataset (`research/pyq/pyq_dataset.csv`).
**PYQ note (applies to the whole file):** the dataset classifies **35** Reasoning/Maths PYQs — Reasoning 18, Mathematics 17 — and its **Subtopic column identifies each PYQ's topic**. Chapters link a PYQ only where its subtopic matches that chapter. No PYQ question text is invented anywhere.
**⚠️ OUT OF SYLLABUS for the 2026 12th level — DO NOT STUDY:** Trigonometry, Algebra (quadratic equations), Logarithms. These are **Graduation-level only** (Advt 08/2026). Two PYQs from the 2024 paper belong to that old, wider syllabus and are **not** 2026 topics: **2024-P1 Q21 (Trigonometry — tower height)** and **2024-P3 Q27 (Quadratic roots m²+n²)**. They are listed here only so you do not waste time on them.
**One bank oddity, stated plainly:** bank MCQ `08_REASONING-019` ("Each of the students ___ present") is a **grammar** question (subject–verb agreement; answer D — "is", because "Each" is singular), not a reasoning question. It sits in the Reasoning bank because that is where the bank file puts it; it is noted in Chapter 17, not hidden.

## Chapter map (handover teaching sequence)

| Ch | Topic (official syllabus) | Bank MCQs (generated) |
|---|---|---|
| 1 | Number series & alphabet series | Maths-015; Reasoning-003, -004, -005, -023 |
| 2 | Coding–decoding | Reasoning-001, -002, -014 |
| 3 | Blood relations | Reasoning-006 |
| 4 | Direction sense | Reasoning-015 |
| 5 | Seating arrangement & ranking | Reasoning-007, -021 |
| 6 | Clock & calendar | Reasoning-008, -017, -018 |
| 7 | LCM & HCF + number system | Maths-010, -016, -021, -022; Reasoning-022 |
| 8 | Average (+ median) | Maths-005 |
| 9 | Percentage | Maths-001, -013, -024 |
| 10 | Profit & loss (+ discount) | Maths-002, -014 |
| 11 | Simple & compound interest | Maths-003, -004 |
| 12 | Ratio–proportion & age problems | Maths-011, -020 |
| 13 | Time–speed–distance & work–time | Maths-006, -007, -017 |
| 14 | Mensuration — area & volume | Maths-008, -009, -018, -019, -023 |
| 15 | Data interpretation (graphical representation) | Maths-012 |
| 16 | Analogy, odd one out & classification | Reasoning-009, -010, -011, -012, -016 |
| 17 | Syllogism, Venn & statement–assumption/conclusion | Reasoning-013, -020, -024 (+ -019 grammar note) |
| 18 | Mental & analytical ability (figures, cubes, puzzles) | — (PYQ-driven only; no bank MCQs) |

---

## Chapter 1 — Number Series & Alphabet Series

### A. VISUAL INTRODUCTION — the difference ladder

```
NUMBER SERIES — likho antar ko, pattern dikh jayega:

  2      6      12      20      30      ?
     +4     +6      +8     +10     +12
  antar khud badh raha hai: 4, 6, 8, 10, ... agla antar 12 → 30 + 12 = 42

ALPHABET SERIES — akshar ko uski sankhya banao (A=1 ... Z=26):

  A(1)   C(3)   F(6)   J(10)   O(15)   ?
           +2     +3     +4      +5      +6  →  15 + 6 = 21 = U
```

> **How to use this diagram:** Har series me pehle **antar** nikalo. Antar constant hai, badh raha hai, ya guna ho raha hai? Wahi ek sawaal 80% series solve kar deta hai.

### B. STORY-BASED EXPLANATION — pattern dhundhna hi kaam hai

Series ka sawaal ek chhota sa jasoosi ka kaam hai: kuchh sankhyaen ya akshar diye hain, aur tumhe batana hai ki agla kya hoga. Exam me series isliye aati hai kyunki yah **pattern pehchanne** ki kshamata napti hai — wahi kshamata jo baad me data, code aur logic me kaam aati hai. Do tarah ki series aati hain: **number series** (2, 6, 12, 20, 30…) aur **alphabet series** (A, C, F, J, O…). Dono me ek hi tareeka: pehle do padosi padon ke beech ka **antar** dekho; phir antar ka antar dekho; phir guna/bhag ya varg/ghan dekho.

### C. WHY DOES IT HAPPEN? — pattern kyun banta hai

- **Why does the difference method work?** Series banane wale hamesha ek **niyam** se banate hain — antar badhana, guna karna, varg lena. Niyam chhupa hota hai, lekin antar nikalne se niyam dikhai dene lagta hai. Antar ka antar (second difference) constant ho to series **varg** (square) par based hoti hai.
- **Why convert letters to numbers?** Akshar ka koi "antar" nahi hota — lekin A=1…Z=26 likhte hi akshar sankhya ban jate hain, aur wahi antar/guna wale niyam lagne lagte hain. A, C, F, J, O me antar +2, +3, +4, +5 hai — yah aksharon ko dekhkar nahi, sankhyaon ko dekhkar dikhta hai.
- **Why squares and cubes?** 1, 4, 9, 16, 25 — yah 1², 2², 3², 4², 5² hain. Agla 6² = 36. Varg aur ghan exam ke sabse aam series pattern hain.

### D. HOW DOES IT WORK? — series ko 4 steps me hal karo

1. **Antar nikalo** — har do padosi padon ke beech ka farak likho.
2. **Antar ka pattern dekho** — constant? Badh raha hai (+2, +4, +6…)? Guna ho raha hai (×2, ×3)?
3. **Na mile to varg/ghan check karo** — kya pad 1, 4, 9, 16… (varg) ya 1, 8, 27, 64… (ghan) hain? Ya varg ± 1?
4. **Akshar series me pehle A=1 likho**, phir wahi 3 steps.

### E. VISUAL MEMORY CONNECTION

Series ko **seedhi** (ladder) samjho: har pad ek seedhi ka paaydaan hai. Antar = do paaydaanon ke beech ki unchai. Agar unchai har baar badh rahi hai, to seedhi upar ki ore tedhi ho rahi hai — agla paaydaan usi badhti unchai par hoga.

### F. IMPORTANT FACTS

| Pattern | Pehchan | Example (old notes, recomputed) |
|---|---|---|
| Constant difference (AP) | Antar har baar same | 3, 7, 11, 15 → +4 → agla 19 |
| Increasing difference | Antar khud badhta hai | 2, 6, 12, 20, 30 → antar 4, 6, 8, 10 → agla **42** |
| Multiplication (GP) | Har pad × same number | 3, 9, 27, 81 → ×3 → agla **243** |
| Squares | 1², 2², 3²… | 1, 4, 9, 16, 25 → agla **36** (= 6²) |
| Alphabet → numbers | A=1…Z=26 | A, C, F, J, O → +2, +3, +4, +5 → agla **U** (21) |
| Primes | 2, 3, 5, 7, 11… | Agla prime **13** |
| Sum of first n naturals | n(n+1)/2 | 1+…+10 = 10×11/2 = **55** |
| Infinite GP sum (stretch) | a/(1−r), |r\|<1 | 2024-P1 Q5 me puchha gaya — §I dekho |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| Antar vs antar ka antar | Pehle antar nikalo; agar antar me bhi pattern na dikhe to **antar ka antar** nikalo (varg series me second difference constant hota hai). |
| A, C, F, J, O me +2, +2 sochna | Antar +2, **+3**, +4, +5 hai — har baar ek badhta hai; agla +6 hai, +2 nahi. |
| 2, 6, 12, 20, 30 me ×2 ya ×3 lagana | Guna nahi, **antar** badh raha hai (4, 6, 8, 10). Guna check karne se pehle antar check karo. |
| Prime series me 1 ya 9 lena | **1 prime nahi hai; 9 composite hai** (3×3). Prime: 2, 3, 5, 7, 11, 13… |
| Sum 1+…+10 ko gin kar nikalna | Formula n(n+1)/2 = **55** — ginne me time aur galti dono badhte hain. |

**⚠️ Mistakes box:** (1) Series me pehla antar dekhkar turant "constant difference" maan lena — hamesha **kam se kam 3 antar** likho. (2) Akshar series ko akshar hi rehne dena — bina A=1 likhe pattern nahi dikhega. (3) Varg series (1, 4, 9, 16) me antar 3, 5, 7 dekhkar "odd numbers" sochna — varg ko pehchano, antar ko nahi.

### H. MEMORY TECHNIQUE (one only)

**"Antar–Antar–Guna–Varg"** — har series par yahi 4 shabd dohrao: pehle **antar**, phir **antar ka antar**, phir **guna**, phir **varg**. Is kram se pattern chhoot-ta hi nahi.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** `08_MATHEMATICS-015` (2, 6, 12, 20, 30 → 42); `08_REASONING-003` (A, C, F, J, O → U); `08_REASONING-004` (3, 9, 27, 81 → 243); `08_REASONING-005` (1, 4, 9, 16, 25 → 36); `08_REASONING-023` (2, 3, 5, 7, 11 → 13).
- **Actual PYQs (dataset subtopics):** **2024-P2 Q4** (Number series); **2024-P3 Q13** (Letter series); **2024-P1 Q5** (Infinite series sum) — yah ek **kathin variant** hai: infinite GP ka yog a/(1−r) hota hai; 2026 ke 12th syllabus me sirf "number series" likha hai, isliye ise stretch topic samjho, core nahi.
- **Recurring exam angles:** antar badhta hua; guna (×2/×3); varg; akshar → sankhya.

### J. ACTIVE RECALL — answer from memory, then check

1. 2, 6, 12, 20, 30, … agla pad kya hai, aur kyun?
2. A, C, F, J, O ke baad kaun sa akshar aayega?
3. 3, 9, 27, 81 ke baad kya hai?
4. 1, 4, 9, 16, 25 ke baad kya hai?
5. Pehli 10 prakritik sankhyaon ka yog kitna hai?
6. 2, 3, 5, 7, 11 ke baad kaun sa prime aayega?
7. Series hal karne ke 4 steps kya hain?
8. Infinite GP ka yog ka formula kya hai?

**Answers (check after attempting):** 1. 42 — antar 4, 6, 8, 10, agla 12. 2. U (21) — antar +2, +3, +4, +5, agla +6. 3. 243 (×3). 4. 36 (= 6²). 5. 55 (10×11/2). 6. 13. 7. Antar → antar ka pattern → guna → varg. 8. a/(1−r), jab |r| < 1.

### K. REVISION SUMMARY (one page — test yourself against it)

```
SERIES LADDER: antar likho → antar ka pattern dekho → guna → varg
KEY: 2,6,12,20,30 → 42 (antar 4,6,8,10) · A,C,F,J,O → U (+2,+3,+4,+5) · 3,9,27,81 → 243 (×3)
     1,4,9,16,25 → 36 (varg) · primes 2,3,5,7,11 → 13 · 1+…+10 = 55 = n(n+1)/2
TRAPS: sirf pehla antar dekhna · akshar ko sankhya na banana · 1 ya 9 ko prime samajhna
MNEMONIC: Antar–Antar–Guna–Varg
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (bank Maths-015 + Reasoning-003–005, 023) → tomorrow (recall + redraw the difference ladder) → after 3 days (mixed with Chapter 2) → after 7 days (timed: bank set + PYQ 2024-P2 Q4, 2024-P3 Q13).

---

## Chapter 2 — Coding–Decoding

### A. VISUAL INTRODUCTION — the letter-shift strip

```
A=1 ... Z=26 — akshar ko sankhya banao, phir shift dikhega:

  C A T  →  3 + 1 + 20 = 24        D O G  →  4 + 15 + 7 = 26
  C A T  →  D B U  (har akshar +1)  D O G  →  E P H  (har akshar +1)

  OPPOSITE LETTERS (vipreet — yog hamesha 27):
  A↔Z  B↔Y  C↔X  D↔W  E↔V  ...  M↔N
  1+26 = 27 · 2+25 = 27 · 13+14 = 27
```

> **How to use this diagram:** Coding me pehle **A=1…Z=26** likho. Phir har akshar ke neeche uski sankhya likho — shift (+1, −2) ya yog (24, 26) turant dikh jayega.

### B. STORY-BASED EXPLANATION — akshar ka code todna

Coding–decoding ek **gupt bhasha** (secret code) todne jaisa hai. Koi shabd diya hai aur uska code diya hai — tumhe niyam dhundhna hai. Do hi niyam aam taur par hote hain: **(1) akshar ko sankhya me badlo aur jodo** (CAT = 24), ya **(2) har akshar ko aage/peeche khis kao** (CAT → DBU, har akshar +1). Teesra aam niyam: **vipreet akshar** (opposite letters) — A ka vipreet Z, B ka Y — inka yog hamesha 27 hota hai.

### C. WHY DOES IT HAPPEN? — code kyun kaam karta hai

- **Why A=1…Z=26?** Yeh ek **convention** hai — aksharon ka kram (alphabetical order) hi unki sankhya hai. Isme koi gehri wajah nahi; yah ek tai kiya hua niyam hai, aur exam isi niyam par chalta hai.
- **Why does the opposite-letter sum equal 27?** Kyunki alphabet me 26 akshar hain: pehla (A=1) + aakhri (Z=26) = 27; dusra (B=2) + dusra-aakhri (Y=25) = 27. Yeh ganit hai, yaad karne ki baat nahi — 26 + 1 = 27.
- **Why check +/− first?** Kyunki zyada tar code **ek hi shift** se bante hain. Pehle +1 ya −1 check karo; na mile to ulta (reverse) check karo; phir yog (sum) check karo.

### D. HOW DOES IT WORK? — code ko 4 steps me todo

1. **A=1 likho** — shabd ke har akshar ke neeche uski sankhya likho.
2. **Code ki sankhya se compare karo** — antar (+1? −2? yog?).
3. **Pattern lagao** — wahi niyam naye shabd par lagao.
4. **Vipreet check** — agar shift na mile to A↔Z (yog 27) try karo.

### E. VISUAL MEMORY CONNECTION

Akshar-patti (alphabet strip) ko **scale** (tarazu) samjho: A ek taraf, Z dusri taraf — dono ka yog hamesha 27 hota hai, jaise tarazu ke dono palde barabar. B–Y, C–X — har joda 27 par santulit hai.

### F. IMPORTANT FACTS

| Rule | Example (old notes, recomputed) |
|---|---|
| Letter values | A=1, B=2, …, Z=26 |
| Sum code | CAT = 3+1+20 = **24**; DOG = 4+15+7 = **26** |
| Shift code (+1) | CAT → **DBU**; DOG → **EPH** |
| Opposite letters | A↔Z, B↔Y, C↔X… (yog **27**); A ka vipreet **Z** |
| Check order | Pehle +/− pattern → phir reverse → phir sum |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| CAT = 24 ko "C+A+T = 24" na samajhna | Yeh **sankhyaon ka yog** hai (3+1+20) — aksharon ka yog nahi, unke **sthan** ka yog hai. |
| Shift code me sirf pehla akshar badalna | **Har akshar** par wahi shift lagta hai — CAT → DBU me C→D, A→B, T→U teeno +1 hain. |
| Opposite letter me "A ka vipreet B" sochna | A ka vipreet **Z** hai (1+26=27); B ka vipreet **Y** (2+25=27). |
| +1 shift aur +1 yog me confuse hona | Shift = har akshar **aage**; yog = sab aksharon ki sankhya **jodna**. Alag niyam hain. |

**⚠️ Mistakes box:** (1) A=0 se ginna shuru karna — A=1 hai, 0 nahi. (2) Z ke baad A aana bhoolna — shift wrap karta hai (Z+1 = A). (3) Vipreet akshar me 27 ke bajaye 26 yaad rakhna — 26 akshar hain, yog 27 hota hai (1+26).

### H. MEMORY TECHNIQUE (one only)

**"27 ka joda"** — A–Z, B–Y, C–X… har vipreet jode ka yog 27. Sirf yah ek sankhya yaad rakho; vipreet akshar usi se nikal aayega.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** `08_REASONING-001` (CAT = 24 → DOG = 26); `08_REASONING-002` (CAT = DBU → DOG = EPH); `08_REASONING-014` (A ka vipreet = Z).
- **Actual PYQs (dataset subtopics):** **2024-P1 Q4** (Coding-decoding MEDICAL); **2024-P2 Q6** (Code language); **2024-P3 Q11** (Coding-decoding PARK/SHIRT); **2023-11Feb-S2 Q15** (Word-code arithmetic — akshar ko sankhya me badal kar ganit).
- **Recurring exam angles:** yog-code (CAT=24); shift-code (+1/−1); vipreet akshar (yog 27).

### J. ACTIVE RECALL — answer from memory, then check

1. CAT = 24 kyun hai? DOG ka maan kya hoga?
2. CAT = DBU ho to DOG kya hoga?
3. A ka vipreet akshar kaun sa hai, aur yog kitna hota hai?
4. M ka vipreet akshar kaun sa hai?
5. Coding me pehle kya check karna chahiye?
6. Z+1 shift me kya hota hai?
7. "Word-code arithmetic" ka matlab kya hai?

**Answers (check after attempting):** 1. 3+1+20 = 24; DOG = 4+15+7 = 26. 2. EPH (har akshar +1). 3. Z; yog 27. 4. N (13+14 = 27). 5. +/− pattern, phir reverse, phir yog. 6. A (wrap hota hai). 7. Aksharon ko unki sankhya (A=1) me badal kar jodna/ghatana/guna karna.

### K. REVISION SUMMARY (one page — test yourself against it)

```
CODE STRIP: A=1 ... Z=26 · CAT = 3+1+20 = 24 · DOG = 26 · CAT → DBU (+1) · DOG → EPH
OPPOSITE: A↔Z, B↔Y, C↔X ... yog hamesha 27 · M↔N
STEPS: A=1 likho → antar dekho → niyam lagao → vipreet check karo
TRAPS: A=0 se ginna · sirf pehla akshar badalna · yog 27 ke bajaye 26 yaad rakhna
MNEMONIC: "27 ka joda"
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (bank Reasoning-001, -002, -014) → tomorrow (recall + alphabet strip redraw) → after 3 days (mixed with Chapter 1) → after 7 days (timed: bank set + PYQ 2024-P1 Q4, 2024-P3 Q11).

---

## Chapter 3 — Blood Relations

### A. VISUAL INTRODUCTION — khud se shuru karo

```
"Ram ne kaha — woh meri MAA ki IKLOTI BETI ki BETI hai"

        Ram
         │  (Ram ki maa)
      [Maa] ─── Maa ki IKLOTI BETI = Ram ki BEHEN
                    │
                 (uski beti)
                  LADKI = Ram ki BHANJI

RULE: Hamesha "main" (bolne wala) se shuru karo, phir ek-ek rishta jodo.
```

> **How to use this diagram:** Har blood-relation sawaal me pehle bolne wale ko beech me rakho, phir rishta ek kadam-ek kadam jodo. Seedha "ladki kaun hai" mat socho — rishte ko tod kar jodo.

### B. STORY-BASED EXPLANATION — rishta ek chain hai

Blood relation ka sawaal ek **chain** hai: "A, B ka kya lagta hai?" — iska jawab ek hi kadam me nahi milta; beech ke rishte jodne padte hain. Jaise: "Maa ki ikloti beti" — maa ki ek hi beti hai, to woh **bolne wale ki behen** hai (kyunki maa ki beti = behen). Phir "uski beti" = behen ki beti = **bhanji**. Chain tod di, jawab mil gaya.

### C. WHY DOES IT HAPPEN? — rishta kyun ulajhta hai

- **Why do these questions confuse?** Kyunki bhasha me ek hi rishte ke kai naam hain, aur "ikloti" (only) jaise shabd chain ko **ek hi raasta** dete hain. "Maa ki ikloti beti" ka matlab hai: maa ki sirf ek beti hai — isliye woh behen hi hogi, koi aur nahi.
- **Why start from the speaker?** Kyunki saare rishte **bolne wale ke nazariye** se bante hain. "Meri maa" = Ram ki maa. "Meri maa ki beti" = Ram ki behen. Nazariya badla to rishta badal jayega.

### D. HOW DOES IT WORK? — rishta 3 steps me nikalo

1. **Bolne wale ko beech me rakho** (yahan Ram).
2. **Rishta tod-tod kar jodo** — "maa ki beti" = behen; "behen ki beti" = bhanji.
3. **"Ikloti/ekmatra" par dhyaan do** — yah chain ko ek hi raasta deta hai; iska matlab hai doosra koi nahi.

### E. VISUAL MEMORY CONNECTION

Rishton ko **seedhi** (ladder) samjho: upar maa, beech me behen, neeche bhanji. Har kadam ek rishta hai — seedhi se utarte jao, naam badalta jayega.

### F. IMPORTANT FACTS

| Rishta | Matlab |
|---|---|
| Maa ka bhai | **Mama** |
| Pita ka bhai | **Chacha** |
| Behen ka beta | **Bhanja** |
| Behen ki beti | **Bhanji** |
| Maa ki ikloti beti | Bolne wale ki **behen** (agar bolne wala ladka hai) |
| Pita ka pita / Maa ka pita | **Dada / Nana** |
| Bhai ki patni / Behen ka pati | **Bhabhi / Jija** |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| Bhanja vs bhanji | Bhanja = behen ka **beta**; bhanji = behen ki **beti**. Ling par dhyaan do. |
| Mama vs chacha | Mama = **maa ka** bhai; chacha = **pita ka** bhai. |
| "Maa ki beti" ko "maa" samajhna | "Maa ki beti" = **behen** (bolne wale ki) — maa nahi. Chain ko tod kar padho. |
| Ikloti beti ko ignore karna | "Ikloti" ka matlab hai sirf ek — isliye woh behen hi hai, koi doosri ladki nahi. |

**⚠️ Mistakes box:** (1) Sawaal ko seedha padhkar guess karna — hamesha chain banao. (2) Bolne wale ka ling bhoolna — "meri maa ki ikloti beti" ladke ke liye behen hai, ladki ke liye **khud** (agar bolne wali ladki hai to maa ki ikloti beti woh khud hai!). (3) Mama/chacha me confuse hona — maa ki taraf ya pita ki taraf, yah pehle tay karo.

### H. MEMORY TECHNIQUE (one only)

No mnemonic for this chapter — rishta **chain banakar** nikala jata hai, rat kar nahi. Chain banana hi technique hai.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** `08_REASONING-006` (Ram — "maa ki ikloti beti ki beti" = bhanji).
- **Actual PYQs (dataset subtopics):** **2024-P2 Q19** (Blood relation); **2024-P4 Q8** (Blood relation).
- **Recurring exam angles:** "ikloti beti/beta" wale sawaal; mama/chacha/bhanja/bhanji; bolne wale se rishta.

### J. ACTIVE RECALL — answer from memory, then check

1. "Maa ki ikloti beti ki beti" bolne wale ki kya lagti hai?
2. Maa ka bhai kya kehlata hai? Pita ka bhai?
3. Behen ke bete ko kya kehte hain?
4. Blood relation me pehla kadam kya hai?
5. "Ikloti" shabd kyun mahatvapurna hai?
6. Agar bolne wali ladki ho to "meri maa ki ikloti beti" kaun hai?

**Answers (check after attempting):** 1. Bhanji. 2. Mama; chacha. 3. Bhanja. 4. Bolne wale ko beech me rakhna. 5. Yeh chain ko ek hi raasta deta hai — doosra koi nahi. 6. Woh khud.

### K. REVISION SUMMARY (one page — test yourself against it)

```
CHAIN RULE: bolne wale se shuru karo → rishta tod-tod kar jodo → "ikloti" = ek hi raasta
KEY: Maa ka bhai = Mama · Pita ka bhai = Chacha · Behen ka beta = Bhanja · Behen ki beti = Bhanji
EXAMPLE: "Maa ki ikloti beti ki beti" = BHANJI
TRAPS: bhanja/bhanji ling · mama/chacha taraf · bolne wale ka ling bhoolna
NO MNEMONIC — chain banana hi technique hai
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (bank Reasoning-006) → tomorrow (recall + chain diagram redraw) → after 3 days (mixed with Chapter 2) → after 7 days (timed: bank set + PYQ 2024-P2 Q19, 2024-P4 Q8).

---

## Chapter 4 — Direction Sense

### A. VISUAL INTRODUCTION — disha chakra

```
              UTTAR (N)
                 ▲
                 │ 5 km
                 │
  PASHCHIM (W) ◄─┼─► PURAB (E)
                 │     3 km →
                 │ 4 km ↓
                 ▼
            DAKSHIN (S)

  Uttar 5 km → dayein 3 km → dayein 4 km
  Antim sthiti: shuruaat se 3 km PURAB, 1 km UTTAR
  Doori = √(3² + 1²) = √10 km, disha = UTTAR-PURAB
```

> **How to use this diagram:** Har disha sawaal me pehle **chakra** banao (N upar, E dayein). Phir kadam-dar-kadam chalo — har mod par disha badalti hai.

### B. STORY-BASED EXPLANATION — chalte-chalte disha badalti hai

Disha ka sawaal ek **chalna** (walk) hai: koi vyakti uttar ki ore 5 km chalta hai, phir dayein mudta hai, phir dayein mudta hai. Har mod par uski disha badal jati hai — aur ant me poochha jata hai: woh shuruaat se kitni door hai, aur kis disha me? Iska raaz hai: **har mod ke baad nayi disha** likhna, aur ant me seedhi doori Pythagoras se nikalna.

### C. WHY DOES IT HAPPEN? — dayein mudne se disha kyun badalti hai

- **Why does "right" change direction?** Kyunki "dayein" **tumhare munh ki disha** par nirbhar karta hai, na ki map par. Uttar ki ore munh ho to dayein = purab. Purab ki ore munh ho to dayein = dakshin. Har mod ke baad tumhara munh badal jata hai, isliye dayein bhi badal jata hai.
- **Why Pythagoras?** Antim sthiti shuruaat se **seedhi** (straight-line) doori par hoti hai — woh ek samkon tribhuj ka karn (hypotenuse) hai. Uttar–dakshin ka antar ek bhuja, purab–pashchim ka antar doosri bhuja: doori = √(bhuja₁² + bhuja₂²).
- **Why is the direction North-East?** Kyunki antim sthiti shuruaat se **purab bhi** hai aur **uttar bhi** — dono ka mel = Uttar-Purab.

### D. HOW DOES IT WORK? — disha 4 steps me nikalo

1. **Chakra banao** — N upar, E dayein, S neeche, W bayein.
2. **Kadam-dar-kadam chalo** — har mod ke baad nayi disha likho (dayein = clockwise).
3. **Antim sthiti nikalo** — shuruaat se purab/pashchim kitna, uttar/dakshin kitna.
4. **Doori = Pythagoras; disha = dono ka mel** (purab+uttar = Uttar-Purab).

### E. VISUAL MEMORY CONNECTION

Disha chakra ko **ghadi** samjho: uttar = 12 baje, purab = 3 baje, dakshin = 6 baje, pashchim = 9 baje. Dayein mudna = ghadi ki disha me ghumna (clockwise).

### F. IMPORTANT FACTS

| Fact | Value |
|---|---|
| Main directions | Uttar (N), Dakshin (S), Purab (E), Pashchim (W) |
| Dayein (right) | **Clockwise** (jab uttar ki ore munh ho) |
| Bayein (left) | **Anticlockwise** |
| Worked example (old notes, recomputed) | Uttar 5 km → dayein 3 km → dayein 4 km → antim: 3 km purab, 1 km uttar; doori **√10 km**, disha **Uttar-Purab** |
| Pythagoras | Doori = √(purab–pashchim antar² + uttar–dakshin antar²) |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| Dayein ko hamesha "purab" samajhna | Dayein = **munh ki disha** par nirbhar karta hai. Uttar ki ore munh ho to dayein = purab; purab ki ore munh ho to dayein = dakshin. |
| Chali hui kul doori ko seedhi doori samajhna | Kul chalna = 5+3+4 = 12 km; **seedhi doori** = √10 km. Exam seedhi doori poochhta hai. |
| Uttar-Purab vs Purab-Uttar | Dono ek hi baat hain — jis disha ka antar **zyada** ho, use pehle bolte hain (yahan purab 3 > uttar 1, phir bhi "Uttar-Purab" standard hai). |
| Mod ke baad purani disha se chalna | Har mod ke baad **nayi disha** likho — purani disha se aage mat badho. |

**⚠️ Mistakes box:** (1) Dayein mudne par disha na badalna — sabse aam galti. (2) Kul doori (12 km) ko jawab banana — seedhi doori (√10 km) chahiye. (3) Disha chakra ulta banana — N hamesha upar.

### H. MEMORY TECHNIQUE (one only)

**"Ghadi ka chakra"** — uttar 12, purab 3, dakshin 6, pashchim 9. Dayein = ghadi ki disha me. Yeh ek hi tasveer disha aur dayein dono yaad dilati hai.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** `08_REASONING-015` (Uttar 5 km → dayein 3 → dayein 4 → √10 km, Uttar-Purab).
- **Actual PYQs (dataset subtopics):** **2024-P2 Q20** (Direction sense).
- **Recurring exam angles:** dayein/bayein mod; antim sthiti; Pythagoras se seedhi doori; disha ka naam.

### J. ACTIVE RECALL — answer from memory, then check

1. Disha chakra me N, E, S, W kis kram me hote hain?
2. Uttar ki ore munh ho to dayein kis disha me hota hai?
3. Purab ki ore munh ho to dayein kis disha me hota hai?
4. Uttar 5 km, dayein 3 km, dayein 4 km — antim sthiti kya hai?
5. Seedhi doori kaise nikalte hain?
6. Kul chali doori aur seedhi doori me kya antar hai?
7. "Ghadi ka chakra" me dakshin kitne baje hai?

**Answers (check after attempting):** 1. N upar, E dayein, S neeche, W bayein (clockwise). 2. Purab. 3. Dakshin. 4. Shuruaat se 3 km purab, 1 km uttar. 5. Pythagoras: √(3²+1²) = √10 km. 6. Kul = 12 km; seedhi = √10 km. 7. 6 baje.

### K. REVISION SUMMARY (one page — test yourself against it)

```
DISHA CHAKRA: N(12) → E(3) → S(6) → W(9) · Dayein = clockwise (munh par nirbhar)
EXAMPLE: N 5 km → right 3 km → right 4 km → 3 km E, 1 km N → √10 km, Uttar-Purab
FORMULA: Doori = √(E–W antar² + N–S antar²)
TRAPS: dayein ko hamesha purab samajhna · kul doori ko seedhi doori samajhna · mod ke baad disha na badalna
MNEMONIC: "Ghadi ka chakra"
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (bank Reasoning-015) → tomorrow (recall + chakra redraw) → after 3 days (mixed with Chapter 3) → after 7 days (timed: bank set + PYQ 2024-P2 Q20).

---

## Chapter 5 — Seating Arrangement & Ranking

### A. VISUAL INTRODUCTION — circle and line

```
SEATING (vritt — kendra ki ore munh):
              A
           ↙     ↘
        D           B        Dayein = ghadi ki VIPREET disha
           ↖     ↗           (kendra ki ore munh ho to ulta!)
              C

RANKING (line — upar se / neeche se):
  Upar se 12th  ──►  [1][2]...[12 Ram]...[40]
  Neeche se = Kul − Upar + 1 = 40 − 12 + 1 = 29th
```

> **How to use this diagram:** Vritt me baithne ka sawaal dekhte hi **circle banao** aur kendra ki ore teer (arrow) lagao. Ranking me **line banao** aur dono taraf se gino.

### B. STORY-BASED EXPLANATION — gol ghare me dayein ulta kyun

Seating arrangement me log **gol ghare** (circle) me baithe hote hain aur sabka munh **kendra ki ore** hota hai. Yahi wajah hai ki yahan "dayein" ulta ho jata hai: jab tum kendra ki ore dekh rahe ho, tumhara dayein haath **ghadi ki vipreet** disha (anticlockwise) me jata hai. Ranking isse alag hai — wahan log **line** me khade hote hain, aur sthan upar se ya neeche se gina jata hai.

### C. WHY DOES IT HAPPEN? — dayein ulta kyun hota hai

- **Why is "right" reversed in a circle?** Kyunki "dayein" tumhare **shareer** ki disha hai, map ki nahi. Kendra ki ore munh karo to tumhara dayein haath ghadi ki vipreet disha me jata hai — khud karke dekho: kendra ki ore munh karke apna dayein haath uthao, woh anticlockwise jayega. Yeh **convention** nahi, shareer ka sach hai.
- **Why ranking formula works?** Kul 40 students me Ram upar se 12th hai — matlab uske upar 11 hain. Neeche se gino to: 40 − 12 = 28 uske neeche hain, aur Ram khud 1 — to neeche se 28 + 1 = **29th**. Formula "Kul − Upar + 1" yahi ginati hai.

### D. HOW DOES IT WORK? — seating aur ranking 4 steps me

1. **Vritt banao, kendra ki ore teer lagao** (seating) / **line banao** (ranking).
2. **Dayein = anticlockwise** (kendra ki ore munh ho to); bayein = clockwise.
3. **Ranking: Neeche se = Kul − Upar + 1**; Upar se = Kul − Neeche + 1.
4. **Ek shart se dusri jodo** — "na" wali shart ko pehle lagao.

### E. VISUAL MEMORY CONNECTION

Vritt me baithe logon ko **ghadi ke ulta** (anticlockwise) ghumte hue samjho — jaise ghadi ulta chal rahi ho. Ranking ko **seedhi** (ladder) samjho — upar se gino ya neeche se, kul seedhi ek hi hai.

### F. IMPORTANT FACTS

| Fact | Value |
|---|---|
| Circle, facing centre | Dayein = **anticlockwise**; bayein = **clockwise** |
| Circle, facing outside | Dayein = clockwise; bayein = anticlockwise (ulta) |
| Ranking formula | Neeche se = **Kul − Upar + 1** |
| Worked example (old notes, recomputed) | 40 students, Ram upar se 12th → neeche se 40 − 12 + 1 = **29th** |
| Bank convention question | Vritt me kendra ki ore munh karke baithe vyakti ka "dayein" **ghadi ki vipreet** (anticlockwise) disha hota hai |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| Kendra ki ore munh ho to dayein = clockwise | **Galat.** Kendra ki ore munh ho to dayein = **anticlockwise**. Clockwise tab hota hai jab munh **bahar** ki ore ho. |
| Neeche se = Kul − Upar (bina +1 ke) | **+1 zaroori hai** — khud ko bhi ginna hai. 40 − 12 = 28 galat; 40 − 12 + 1 = **29** sahi. |
| Upar se aur neeche se ko jodna | Upar se 12th + neeche se 29th = 41 — kul 40 + 1 (Ram khud dono me gina gaya). Yeh **check** hai, galti nahi. |
| Seating me "dayein" ko map ka purab samajhna | Seating me dayein/bayein **vyakti ke munh** par nirbhar karte hain, map ki disha par nahi. |

**⚠️ Mistakes box:** (1) Kendra ki ore munh ho to dayein clockwise likhna — sabse aam galti; hamesha pehle **munh ki disha** likho. (2) Ranking me +1 bhoolna. (3) "Upar se 12th" ka matlab "upar 12 log" samajhna — upar **11** log hain, 12th Ram khud hai.

### H. MEMORY TECHNIQUE (one only)

**"Kendra dekho to dayein ulta"** — ek hi vakya: kendra ki ore munh = dayein anticlockwise. Ranking ke liye: **"Kul − Upar + 1"** — khud ko ginna mat bhoolo.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** `08_REASONING-007` (40 students, 12th from top → 29th from bottom); `08_REASONING-021` (vritt me kendra ki ore munh — dayein = anticlockwise).
- **Actual PYQs (dataset subtopics):** **2024-P1 Q6** (Ranking — queue); **2024-P1 Q7** (Ranking — row); **2024-P2 Q7** (Seating arrangement).
- **Recurring exam angles:** kendra ki ore munh — dayein ulta; ranking formula (+1); queue/row me sthan.

### J. ACTIVE RECALL — answer from memory, then check

1. Vritt me kendra ki ore munh ho to "dayein" kis disha me hota hai?
2. Munh bahar ki ore ho to dayein kis disha me hota hai?
3. 40 students me Ram upar se 12th hai — neeche se kya sthan hai?
4. Ranking formula kya hai?
5. Upar se 12th + neeche se 29th = 41 kyun aata hai jab kul 40 hain?
6. Seating me "na" wali shart ko pehle kyun lagate hain?
7. 50 students me koi upar se 20th ho to neeche se kya hoga?

**Answers (check after attempting):** 1. Anticlockwise (ghadi ki vipreet). 2. Clockwise. 3. 29th. 4. Neeche se = Kul − Upar + 1. 5. Kyunki Ram dono ginatiyon me aata hai (40 + 1). 6. Kyunki woh sabse zyada possibilities khatm karti hai. 7. 50 − 20 + 1 = 31st.

### K. REVISION SUMMARY (one page — test yourself against it)

```
SEATING: kendra ki ore munh → dayein = ANTICLOCKWISE · munh bahar → dayein = clockwise
RANKING: Neeche se = Kul − Upar + 1 · 40 students, 12th from top → 29th from bottom
TRAPS: kendra me dayein clockwise likhna · +1 bhoolna · "upar 12 log" samajhna (11 hain)
MNEMONIC: "Kendra dekho to dayein ulta"
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (bank Reasoning-007, -021) → tomorrow (recall + circle redraw) → after 3 days (mixed with Chapter 4) → after 7 days (timed: bank set + PYQ 2024-P1 Q6/Q7, 2024-P2 Q7).

---

## Chapter 6 — Clock & Calendar

### A. VISUAL INTRODUCTION — the clock face

```
CLOCK — 3 baje: suiyon ke beech 90°

        12
         │
    9 ───┼─── 3        Minute wali sui 12 par,
         │             ghante wali sui 3 par
         │             → beech ka kon = 90°
         6

CALENDAR — 1 Jan 2026 = Thursday (verified)
  1 Jan (Thu) → 8 Jan (Thu) → 15 Jan (Thu) → 22 Jan (Thu) → 29 Jan (Thu)
  Har 7 din baad wahi din — 7 ka gunank hi niyam hai.
```

> **How to use this diagram:** Ghadi me **3 baje = 90°** ko yaad rakho — yahi ek tasveer kon, ghante aur minute teeno sikhati hai. Calendar me **7 din = wahi din** — bas yahi niyam hai.

### B. STORY-BASED EXPLANATION — ghadi aur calendar ka ganit

Ghadi aur calendar dono **chakr** (cycle) hain: ghadi ki suiyan har 12 ghante me wahi jagah laut aati hain; calendar har 7 din me wahi din lauta deta hai. Exam me inke 3 hi sawaal aate hain: **(1) kon kitna hai?** (2) **suiyan kab milengi?** (3) **kaun sa din hoga?** Teeno ka jawab ek hi tareeke se nikalta hai — chakr ko ginna.

### C. WHY DOES IT HAPPEN? — suiyan aur din kyun chakr me chalte hain

- **Why do the hands meet 11 times in 12 hours, not 12?** Kyunki minute wali sui ghante wali sui se **thodee tez** chalti hai — har ghante me woh ek baar usse aage nikal jati hai. 12 ghante me woh 12 baar aage nikalne ki koshish karti hai, lekin 12 baje wali mulaqat **donon ghante ki ek hi** hoti hai (shuru aur ant) — isliye kul **11** baar milti hain.
- **Why 90° at 3:00?** Ghadi ka poora chakr 360° hai, 12 ghanton me banta hai — har ghante ka kon = 360°/12 = **30°**. 3 baje suiyan 3 ghante door hain: 3 × 30° = **90°**.
- **Why does the same weekday repeat every 7 days?** Kyunki hafte me 7 din hote hain — 7 din baad wahi din laut aata hai. Yeh **convention** hai (7-din ka hafta), ganit nahi.
- **Why odd days?** 365 din = 52 hafte + **1 din** (1 odd day); leap year 366 din = 2 odd days. Agle saal ka 1 January isliye 1 din (ya 2 din) aage khisakta hai.

### D. HOW DOES IT WORK? — ghadi aur calendar 4 steps me

1. **Kon nikalo:** ghanton ka antar × 30° (minute wali sui ko bhoolo mat — woh bhi chalti hai: har minute 0.5°).
2. **Milne ka samay:** har ~1 ghanta 5.5 minute me ek baar (65 5/11 minute).
3. **Din nikalo:** dinon ka antar ÷ 7 — shesh (remainder) din aage badhao.
4. **Odd days:** saal ke din gin kar odd days nikalo (365 = 1; leap = 2).

### E. VISUAL MEMORY CONNECTION

Ghadi ko **pizza** samjho: 12 tukde, har tukda 30°. 3 baje = 3 tukde = 90°. Calendar ko **seedhi** samjho: har 7 seedhi chadhne par wahi din — 1 Jan Thursday to 8 Jan bhi Thursday.

### F. IMPORTANT FACTS

| Fact | Value |
|---|---|
| Har ghante ka kon | **30°** (360° ÷ 12) |
| 3:00 par kon | **90°** (3 × 30°) |
| Suiyan milti hain | **12 ghante me 11 baar** (lagbhag har 1 ghanta 5.5 minute me) |
| 90° (samkon) kitni baar | **12 ghante me 22 baar** (har ghante me 2 baar — lekin 2–3 aur 8–9 wale ghante me 1 baar; §G dekho) |
| 1 Jan 2026 | **Thursday** (calendar check se verified, 11 Nov 2026) |
| 8 Jan 2026 | **Thursday** (1 Jan + 7 din = wahi din) |
| Odd days | 365 din = **1** odd day; leap year 366 din = **2** odd days |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| "90° har ghante me 2 baar" — hamesha | **Sahi nahi hai.** 12 ghante me kul **22 baar** banta hai — 2–3 aur 8–9 wale ghante me sirf **1 baar** (kyunki 3:00 aur 9:00 par kon pehle se hi 90° hota hai). Purane notes me "1 ghante me 2 baar" likha tha — yah **sudhara gaya** hai (Preservation note dekho). |
| Suiyan milti hain 12 baar (12 ghante me) | **11 baar** — 12 baje wali mulaqat shuru aur ant dono me ek hi gini jati hai. |
| 1 Jan 2026 ko "verify" kiye bina yaad rakhna | Yeh **verified** hai (calendar check, 11 Nov 2026): 1 Jan 2026 = Thursday. |
| Kon nikalte samay minute wali sui ko bhoolna | Minute wali sui bhi chalti hai — 4:20 par kon sirf 4 × 30° = 120° nahi hota; minute sui 20 minute aage badh chuki hoti hai. (Syllabus me sirf basic kon aata hai — 3:00 jaisa — lekin yah jaanna zaroori hai.) |
| Leap year me odd days = 1 | Leap year = **2** odd days (366 din). |

**⚠️ Mistakes box:** (1) "12 baar milti hain" likhna — 11 sahi hai. (2) "Har ghante 90° 2 baar" — 2–3 aur 8–9 ghante me 1 baar; kul 22. (3) Calendar me 7 se bhag dena bhoolna — dinon ka antar ÷ 7, shesh aage badhao.

### H. MEMORY TECHNIQUE (one only)

**"30–11–22–7"** — har ghanta **30°** · suiyan **11** baar milti hain · 90° **22** baar · calendar **7** din ka chakr. Chaar sankhyaen, poora chapter.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** `08_REASONING-008` (3 baje = 90°); `08_REASONING-017` (1 Jan 2026 Thursday → 8 Jan 2026 Thursday); `08_REASONING-018` (12 ghante me suiyan 11 baar milti hain).
- **Actual PYQs:** is vishay par dataset ke 35 PYQs me **koi seedha PYQ nahi hai** — lekin clock/calendar official syllabus me hai aur bank me 3 MCQs hain, isliye padhna zaroori hai.
- **Recurring exam angles:** 3:00 par 90°; 11 baar milna; 7 din baad wahi din.

### J. ACTIVE RECALL — answer from memory, then check

1. 3 baje suiyon ke beech kitne degree ka kon banta hai, aur kyun?
2. Ghadi ki suiyan 12 ghante me kitni baar milti hain?
3. 90° (samkon) 12 ghante me kitni baar banta hai?
4. 1 Jan 2026 kaun sa din hai?
5. 8 Jan 2026 kaun sa din hoga, aur kyun?
6. 365 din me kitne odd days hote hain? Leap year me?
7. Har ghante ka kon kitna hota hai?
8. 2–3 wale ghante me 90° kitni baar banta hai?

**Answers (check after attempting):** 1. 90° — 3 ghante × 30°. 2. 11 baar. 3. 22 baar. 4. Thursday. 5. Thursday — 7 din baad wahi din. 6. 1; leap year me 2. 7. 30°. 8. 1 baar (3:00 par).

### K. REVISION SUMMARY (one page — test yourself against it)

```
CLOCK: har ghanta 30° · 3:00 = 90° · suiyan 12 ghante me 11 baar milti hain · 90° 12 ghante me 22 baar
CALENDAR: 1 Jan 2026 = Thursday · 7 din baad wahi din · 365 din = 1 odd day · leap = 2 odd days
TRAPS: "12 baar milti hain" (11 sahi) · "har ghante 90° 2 baar" (2–3 aur 8–9 me 1 baar) · minute sui bhoolna
MNEMONIC: "30–11–22–7"
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (bank Reasoning-008, -017, -018) → tomorrow (recall + clock face redraw) → after 3 days (mixed with Chapter 5) → after 7 days (timed: bank set).

---

## Chapter 7 — LCM & HCF + Number System

### A. VISUAL INTRODUCTION — the factor tree

```
252 ka gunankhand (factor tree):
         252
        /   \
       2    126
            /  \
           2    63
               /  \
              3    21
                  /  \
                 3    7
  252 = 2² × 3² × 7  →  7 ki ghat (power) = 1

LCM(12, 18):  12 = 2²×3 · 18 = 2×3² → LCM = 2²×3² = 36
HCF(12, 18) = 2×3 = 6 · Check: HCF × LCM = 6 × 36 = 216 = 12 × 18 ✓
```

> **How to use this diagram:** Har LCM/HCF sawaal me pehle **gunankhand** (prime factorisation) likho. Uske baad LCM/HCF nikalna bas chunna (choose) hai — LCM me badi ghat, HCF me chhoti ghat.

### B. STORY-BASED EXPLANATION — sankhyaon ko todna

LCM aur HCF ka kaam hai **sankhyaon ko unke sabse chhote tukdon (prime factors) me todna** aur phir un tukdon se nayi sankhya banana. LCM = woh sabse chhoti sankhya jo dono se vibhajya ho; HCF = woh sabse badi sankhya jo dono ko vibhajit kare. Jaise 12 aur 18: 12 = 2²×3, 18 = 2×3². LCM me har prime ki **badi** ghat lo (2²×3² = 36); HCF me **chhoti** ghat lo (2×3 = 6).

### C. WHY DOES IT HAPPEN? — HCF × LCM = gunafal kyun

- **Why does HCF × LCM = product of the two numbers?** Kyunki har prime factor ya to HCF me aata hai ya LCM me — dono me milakar uski kul ghat wahi hoti hai jo dono sankhyaon me milakar hai. Isliye HCF × LCM = pehli sankhya × dusri sankhya. Yeh **do sankhyaon** ke liye hai — teen sankhyaon par yah formula nahi chalta.
- **Why divisibility rules work?** 3 ka niyam (ankon ka yog 3 se vibhajya) isliye kaam karta hai kyunki 10 ≡ 1 (mod 3) — har sthan ka maan 3 se bhag dene par 1 bachta hai. Exam ke liye niyam yaad rakhna kaafi hai; wajah yah hai ki sthan-moolya (place value) 3 aur 9 ke niyam me ek jaisa bartav karta hai.
- **Why is 2 the only even prime?** Kyunki prime ka matlab hai sirf 1 aur khud se vibhajya. 2 ke alawa har sam sankhya 2 se bhi vibhajya hoti hai — isliye woh prime nahi ho sakti.

### D. HOW DOES IT WORK? — LCM/HCF 3 steps me

1. **Gunankhand karo** — dono sankhyaon ko prime factors me todo.
2. **LCM:** har prime ki **badi** ghat lo, guna karo.
3. **HCF:** har prime ki **chhoti** ghat lo, guna karo. Check: HCF × LCM = gunafal.

### E. VISUAL MEMORY CONNECTION

Gunankhand ko **ped** (tree) samjho: upar poori sankhya, neeche tukde-tukde. LCM = ped ke sabse bade tukde; HCF = dono pedon me **common** tukde.

### F. IMPORTANT FACTS

| Fact | Value |
|---|---|
| Sankhyaon ke prakar | Natural: 1, 2, 3…; Whole: 0, 1, 2…; Integer: …, −2, −1, 0, 1, 2…; Rational: p/q; Irrational: √2, π |
| Divisibility | 2: ant me sam · 3: ankon ka yog 3 se · 4: antim 2 ank 4 se · 5: ant 0/5 · 9: ankon ka yog 9 se · 11: (sam sthan − visham sthan) 0 ya 11 se |
| HCF × LCM | **Do sankhyaon ke liye:** HCF × LCM = sankhyaon ka gunafal |
| Primes | 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37…; **2 ekmatra sam prime**; **1 na prime na composite** |
| Worked examples (old notes, recomputed) | 252 = **2²×3²×7** (7 ki ghat = 1) · √144 = **12** · √625 = **25** · LCM(12, 18) = **36** · HCF(12, 18) = **6** |
| Sum of first n naturals | n(n+1)/2; 1+…+10 = **55** |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| HCF × LCM = gunafal — teen sankhyaon par | Yeh formula **sirf do sankhyaon** ke liye hai. Teen sankhyaon par nahi chalta. |
| LCM me chhoti ghat lena | LCM me **badi** ghat; HCF me **chhoti** ghat. Ulta karoge to jawab ulta aayega. |
| 1 ko prime samajhna | **1 na prime na composite** hai — prime ke liye do alag gunankhand (1 aur khud) chahiye, 1 ke paas sirf ek hai. |
| 9 ko prime samajhna | 9 = 3×3 — **composite** hai. |
| Divisibility by 4 vs by 8 | 4 ke liye **antim 2 ank**; 8 ke liye antim 3 ank. |

**⚠️ Mistakes box:** (1) LCM/HCF me gunankhand kiye bina guess karna — pehle factor tree banao. (2) HCF × LCM formula teen sankhyaon par lagana. (3) 1 ko prime ginnna — 1 kabhi prime nahi.

### H. MEMORY TECHNIQUE (one only)

**"LCM — Badi ghat; HCF — Chhoti ghat"** — ek hi vakya. "L" = Large (badi), "H" = Half/chhoti — yah shabd-khel nahi, seedha niyam hai.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** `08_MATHEMATICS-010` (LCM 12, 18 = 36); `08_MATHEMATICS-016` (252 = 2²×3²×7 — 7 ki ghat 1); `08_MATHEMATICS-021` (HCF × LCM = gunafal, do sankhyaon ke liye); `08_MATHEMATICS-022` (3 se vibhajyata); `08_REASONING-022` (pehli 10 prakritik sankhyaon ka yog = 55).
- **Actual PYQs:** is vishay par dataset ke 35 PYQs me **koi seedha PYQ nahi hai** — lekin LCM/HCF official syllabus me hai aur bank me 5 MCQs hain.
- **Recurring exam angles:** LCM/HCF; gunankhand; vibhajyata niyam; 1 na prime na composite.

### J. ACTIVE RECALL — answer from memory, then check

1. LCM(12, 18) kitna hai, aur kaise nikala?
2. HCF(12, 18) kitna hai?
3. HCF × LCM = gunafal — yah kab chalta hai?
4. 252 ka gunankhand kya hai? 7 ki ghat kitni hai?
5. 3 se vibhajyata ka niyam kya hai?
6. 2 ekmatra sam prime kyun hai?
7. 1 prime kyun nahi hai?
8. Pehli 10 prakritik sankhyaon ka yog kitna hai?

**Answers (check after attempting):** 1. 36 — 2²×3². 2. 6 — 2×3. 3. Sirf do sankhyaon ke liye. 4. 2²×3²×7; 7 ki ghat = 1. 5. Ankon ka yog 3 se vibhajya ho. 6. Baaki har sam sankhya 2 se vibhajya hoti hai. 7. Uske paas sirf ek gunankhand hai. 8. 55.

### K. REVISION SUMMARY (one page — test yourself against it)

```
FACTOR TREE: 252 = 2²×3²×7 · LCM = badi ghat (2²×3² = 36) · HCF = chhoti ghat (2×3 = 6)
FORMULA: HCF × LCM = gunafal (sirf 2 sankhyaon ke liye)
DIVISIBILITY: 2 sam · 3 ankon ka yog · 4 antim 2 ank · 5 ant 0/5 · 9 ankon ka yog · 11 sam−visham = 0/11
PRIMES: 2,3,5,7,11,13... · 2 ekmatra sam prime · 1 na prime na composite
TRAPS: LCM me chhoti ghat lena · formula teen sankhyaon par lagana · 1 ko prime samajhna
MNEMONIC: "LCM — Badi ghat; HCF — Chhoti ghat"
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (bank Maths-010, -016, -021, -022; Reasoning-022) → tomorrow (recall + factor tree redraw) → after 3 days (mixed with Chapter 6) → after 7 days (timed: bank set).

---

## Chapter 8 — Average (+ Median)

### A. VISUAL INTRODUCTION — the balancing point

```
5 sankhyaen, ausat 27 → kul yog = 5 × 27 = 135

  Pehli 4 ka ausat 25 → yog = 4 × 25 = 100
  5th sankhya = 135 − 100 = 35

  Ausat = santulan bindu (balancing point):
  ─────●──────●──────●───▲───●──────●─────
                          27 (ausat)
  Kul yog wahi rehta hai — ek sankhya badhao to doosri ghatani padegi.
```

> **How to use this diagram:** Ausat ka sawaal dekhte hi pehle **kul yog** nikalo (ausat × sankhya). Phir jo poochha hai use yog se nikalo — ausat se seedha nahi.

### B. STORY-BASED EXPLANATION — ausat ek santulan hai

Ausat (average) ka matlab hai: kul yog ko barabar baant do. 5 sankhyaon ka ausat 27 hai — matlab kul yog 135 hai. Pehli 4 ka ausat 25 hai — matlab unka yog 100 hai. To 5th sankhya = 135 − 100 = **35**. Ausat ko **santulan bindu** samjho: agar ek sankhya ausat se upar hai to koi doosri neeche hogi, tabhi santulan banta hai.

### C. WHY DOES IT HAPPEN? — ausat se kul yog kyun nikalta hai

- **Why average × count = total?** Kyunki ausat ki **paribhasha** hi yahi hai: Average = Yog / Sankhya. Isliye Yog = Average × Sankhya. Yeh koi trick nahi — paribhasha ko ulta likhna hai.
- **Why median?** Median (madhyika) woh sankhya hai jo **beech** me aati hai jab sankhyaon ko kram me lagao. Ausat sab sankhyaon ko barabar baant-ta hai; median beech wali sankhya batata hai. Dono "ausat" ke alag-alag matlab hain — isliye 2024-P1 Q18 me median poochha gaya.
- **Why does the "first/last difference" PYQ work?** 2024-P3 Q1 me pehli aur aakhri sankhya ka antar poochha gaya — yah ausat ke **santulan** par based hai: agar ausat badalta hai to kul yog badalta hai, aur antar se pata chalta hai kitna badla.

### D. HOW DOES IT WORK? — ausat 3 steps me

1. **Kul yog nikalo** — ausat × sankhya.
2. **Jo diya hai use ghatao/jodo** — pehli 4 ka yog, ya naya ausat.
3. **Bachi hui sankhya nikalo** — kul yog − diya hua yog.

### E. VISUAL MEMORY CONNECTION

Ausat ko **tarazu** (balance) samjho: beech me ausat ka bindu, dono taraf sankhyaen. Ek taraf bhaari ho to dusri taraf halka hona hi padega — nahi to tarazu santulit nahi hoga.

### F. IMPORTANT FACTS

| Fact | Formula / Value |
|---|---|
| Average | **Average = Yog / Sankhya** → Yog = Average × Sankhya |
| Worked example (old notes, recomputed) | 5 sankhyaon ka ausat 27 → yog 135; pehli 4 ka ausat 25 → yog 100; 5th = **35** |
| Median (madhyika) — odd n | Beech wali sankhya: ((n+1)/2)th pad (kram me lagane ke baad) |
| Median — even n | Beech ke **do padon ka ausat** |
| Median vs Average | Average = kul yog / sankhya; Median = beech wali sankhya — alag cheezen hain |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| Ausat se seedha 5th sankhya nikalna | Pehle **kul yog** nikalo (135), phir pehli 4 ka yog (100) ghatao — seedha ausat se nahi nikalta. |
| Median ko average samajhna | Median = **beech wali** sankhya; average = **yog/sankhya**. Dono alag hain. |
| Median nikalte samay kram na lagana | Median ke liye sankhyaon ko **chhote se bade** kram me lagana zaroori hai — bina kram ke beech wali sankhya galat hogi. |
| Even n me ek hi beech wali sankhya dhoondhna | Even n me beech me **do** sankhyaen hoti hain — unka **ausat** median hota hai. |

**⚠️ Mistakes box:** (1) Ausat × sankhya karna bhoolna — "ausat 27" ka matlab "yog 27" nahi, "yog 135" hai. (2) Median ke liye kram na lagana. (3) 5th sankhya nikalte samay pehli 4 ka **ausat** (25) ghata dena — yog (100) ghatao, ausat nahi.

### H. MEMORY TECHNIQUE (one only)

No mnemonic for this chapter — **"Pehle kul yog"** hi niyam hai. Har ausat sawaal pehle is vakya se shuru karo.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** `08_MATHEMATICS-005` (5 sankhyaon ka ausat 27, pehli 4 ka 25 → 5th = 35).
- **Actual PYQs (dataset subtopics):** **2024-P3 Q1** (Average — first/last difference); **2024-P1 Q18** (Median — find x).
- **Recurring exam angles:** kul yog se agyaat sankhya; pehli/aakhri ka antar; median vs average.

### J. ACTIVE RECALL — answer from memory, then check

1. Average ka formula kya hai?
2. 5 sankhyaon ka ausat 27 hai — kul yog kitna hai?
3. Pehli 4 ka ausat 25 ho to 5th sankhya kya hai?
4. Median kya hota hai?
5. Even sankhyaon me median kaise nikalte hain?
6. Median nikalne se pehle kya karna zaroori hai?
7. Ausat sawaal me pehla kadam kya hai?
8. 2024-P3 Q1 kis baat par based tha?

**Answers (check after attempting):** 1. Yog / Sankhya. 2. 135. 3. 35. 4. Kram me lagane par beech wali sankhya. 5. Beech ke do padon ka ausat. 6. Chhote se bade kram me lagana. 7. Kul yog nikalna. 8. Pehli aur aakhri sankhya ke antar par (ausat ka santulan).

### K. REVISION SUMMARY (one page — test yourself against it)

```
AVERAGE: Yog = Average × Sankhya · 5 sankhyaen, ausat 27 → yog 135 → 5th = 35
MEDIAN: kram lagao → beech wali (odd n) · beech ke do ka ausat (even n)
TRAPS: ausat se seedha nikalna · median ko average samajhna · kram na lagana
NO MNEMONIC — "Pehle kul yog" hi niyam hai
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (bank Maths-005) → tomorrow (recall + balance diagram redraw) → after 3 days (mixed with Chapter 7) → after 7 days (timed: bank set + PYQ 2024-P3 Q1, 2024-P1 Q18).

---

## Chapter 9 — Percentage

### A. VISUAL INTRODUCTION — 100 ka hissa

```
% = (Bhaag / Kul) × 100 — "prati-sau" (per hundred)

  240 ka 15%:  10% = 24 · 5% = 12 · 15% = 24 + 12 = 36
               (10% + 5% tod kar jodo — yahi shortcut hai)

  500 → 650:  badhotri = 150 · 150/500 × 100 = 30%

  SHORTCUTS: 10% = ÷10 · 5% = 10% ka aadha · 25% = ÷4 · 12.5% = ÷8
```

> **How to use this diagram:** Percentage me **10% nikalo pehle** — phir use tod-jod kar koi bhi % banao. 15% = 10% + 5%; 35% = 25% + 10%.

### B. STORY-BASED EXPLANATION — sau me se kitna

Percentage ka matlab hai **"sau me se kitna"**. 240 ka 15% matlab: 240 ko 100 hisso me baanto, unme se 15 hisse lo. Shortcut yeh hai ki 10% nikalna aasan hai (÷10), aur 5% uska aadha hai — isliye 15% = 24 + 12 = **36**. Badhotri % me hamesha **mool** (original) se bhag do — ₹500 se ₹650 hua to badhotri 150 hai, aur 150/500 = **30%**.

### C. WHY DOES IT HAPPEN? — successive % kyun −4% hota hai

- **Why +20% then −20% = −4%, not 0?** Kyunki dusri baar % **badli hui** sankhya par lagta hai. Pehle +20%: 100 → 120. Phir −20%: 120 ka 20% = 24, to 120 − 24 = **96**. Kul −4%. Dusra % pehle % ke **nateeje** par lagta hai, mool par nahi — isliye + aur − barabar nahi hote.
- **Why formula a+b+ab/100?** Pehle badhotri a%, phir b%: kul = (1 + a/100)(1 + b/100) − 1 = a + b + ab/100 (sab % me). a = +20, b = −20: 20 − 20 + (20×−20)/100 = **−4%**. Yeh **derivation** hai, ratne ki baat nahi.
- **Why divide by the original (mool)?** Kyunki "% badhotri" ka matlab hai "mool ke hisab se kitna badha". ₹500 se ₹650: badhotri 150 hai, aur mool 500 hai — 150/650 galat hoga, 150/500 sahi.

### D. HOW DOES IT WORK? — percentage 4 steps me

1. **10% nikalo** (÷10) — phir tod-jod kar koi bhi % banao.
2. **Badhotri %:** (Badhotri / Mool) × 100 — hamesha mool se bhag do.
3. **Kramik (successive):** a + b + ab/100 — chinh (sign) ka dhyaan rakho.
4. **125% jaisi sankhya:** 100% + 25% — 80 ka 125% = 80 + 20 = **100**.

### E. VISUAL MEMORY CONNECTION

Percentage ko **100 tukdon wali roti** samjho: 15% matlab 15 tukde. 10% = 10 tukde (aasaan), 5% = 5 tukde (aadha). Tukde jodkar koi bhi % banao.

### F. IMPORTANT FACTS

| Fact | Formula / Value |
|---|---|
| Percentage | **% = (Bhaag / Kul) × 100**; x% of y = (x/100) × y |
| Badhotri % | **(Badhotri / Mool) × 100** |
| Shortcuts | 10% = ÷10 · 5% = 10% ka aadha · 25% = ÷4 · 12.5% = ÷8 |
| Successive | **a + b + ab/100** (a, b % me; badhotri +, kami −) |
| Worked examples (old notes, recomputed) | 240 ka 15% = **36** (24+12) · 80 ka 125% = **100** · ₹500 → ₹650 = **30%** vriddhi · +20% phir −20% = **−4%** |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| +20% phir −20% = 0% | **−4%** — dusra % badli hui sankhya par lagta hai. |
| Badhotri % me nayi sankhya (650) se bhag dena | Hamesha **mool** (500) se bhag do — 150/500 = 30%. |
| 15% ko seedha guna karke nikalna (240 × 0.15) | Galat nahi, lekin **slow** hai — 10% + 5% todna tez aur surakshit hai. |
| Successive formula me ab/100 ka chinh bhoolna | a = +20, b = −20 ho to ab = −400; ab/100 = **−4** — chinh ke saath likho. |

**⚠️ Mistakes box:** (1) +x% phir −x% ko 0% samajhna — hamesha **negative** aata hai. (2) Badhotri % me galat sankhya se bhag dena — **mool** se bhag do. (3) 125% ko "125" samajhna — 125% = 100% + 25% = 1.25 guna.

### H. MEMORY TECHNIQUE (one only)

**"10% pehle, phir tod-jod"** — har % sawaal 10% se shuru karo. Yeh ek hi aadat percentage ke aadhe sawaal hal kar deti hai.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** `08_MATHEMATICS-001` (240 ka 15% = 36); `08_MATHEMATICS-013` (+20% phir −20% = −4%); `08_MATHEMATICS-024` (₹500 → ₹650 = 30%).
- **Actual PYQs:** is vishay par dataset ke 35 PYQs me **koi seedha PYQ nahi hai** (profit/loss wale PYQs Chapter 10 me hain) — lekin percentage official syllabus me hai aur bank me 3 MCQs hain.
- **Recurring exam angles:** 10% shortcut; successive %; badhotri % (mool se bhag).

### J. ACTIVE RECALL — answer from memory, then check

1. 240 ka 15% kitna hai, aur shortcut kya hai?
2. 80 ka 125% kitna hai?
3. ₹500 se ₹650 hone par vriddhi % kitni hai?
4. +20% phir −20% ka net parivartan kitna hai, aur kyun?
5. Successive % ka formula kya hai?
6. 25% nikalne ka shortcut kya hai?
7. Badhotri % me kis sankhya se bhag dete hain?
8. 60 ka 35% kitna hai? (10% shortcut se)

**Answers (check after attempting):** 1. 36 — 10% (24) + 5% (12). 2. 100. 3. 30%. 4. −4% — dusra % badli hui sankhya par lagta hai. 5. a + b + ab/100. 6. ÷4. 7. Mool (original) se. 8. 21 (10% = 6, 25% = 15, 15+6 = 21).

### K. REVISION SUMMARY (one page — test yourself against it)

```
% = (Bhaag/Kul) × 100 · 10% = ÷10 · 5% = aadha · 25% = ÷4 · 12.5% = ÷8
KEY: 240 ka 15% = 36 · 80 ka 125% = 100 · 500→650 = 30% · +20% −20% = −4%
SUCCESSIVE: a + b + ab/100 (chinh ke saath)
TRAPS: +x% −x% = 0 samajhna · nayi sankhya se bhag dena · ab/100 ka chinh bhoolna
MNEMONIC: "10% pehle, phir tod-jod"
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (bank Maths-001, -013, -024) → tomorrow (recall + roti diagram redraw) → after 3 days (mixed with Chapter 8) → after 7 days (timed: bank set).

---

## Chapter 10 — Profit & Loss (+ Discount)

### A. VISUAL INTRODUCTION — CP is the base

```
CP (Kray mulya) = khareedne ka daam — HAR % CP par lagta hai
SP (Vikray mulya) = bechne ka daam

  Labh = SP − CP · Hani = CP − SP
  Labh% = (Labh / CP) × 100  ← hamesha CP se bhag do!

  CP ₹800 → SP ₹920: Labh ₹120 → 120/800 × 100 = 15%
  CP ₹1,200, 10% hani → SP = 1200 × 0.9 = ₹1,080

  DISCOUNT: MP (Ankit mulya) par milta hai → SP = MP × (1 − d/100)
```

> **How to use this diagram:** Labh/hani ka sawaal dekhte hi pehle **CP likho** — kyunki har % CP par lagta hai. SP par % lagana sabse aam galti hai.

### B. STORY-BASED EXPLANATION — dukaan ka hisab

Dukaandar ne vastu **₹800 me khareedi** (CP) aur **₹920 me bechi** (SP). Labh = 920 − 800 = **₹120**. Labh% = 120/800 × 100 = **15%**. Agar 10% hani hui to SP = CP ka 90% — ₹1,200 ka 90% = **₹1,080**. Chhoot (discount) alag cheez hai: woh **MP** (ankit mulya, tag par likha daam) par milti hai, CP par nahi.

### C. WHY DOES IT HAPPEN? — % hamesha CP par kyun

- **Why is profit % always on CP?** Kyunki labh/hani **lagat** (investment) ke hisab se napi jati hai — dukaandar ne ₹800 lagaye, use ₹120 mile. 120/800 = 15% uske **lagaye hue paise** par return hai. SP se bhag doge to return galat niklega — SP me labh bhi shamil hai.
- **Why SP = CP × (1 ± %)?** Kyunki SP = CP + Labh (ya CP − Hani). Labh = CP × %/100, isliye SP = CP × (1 + %/100). Yeh **derivation** hai — formula ratne se behtar hai.
- **Why discount on MP, not CP?** Kyunki chhoot **grahak** ko dikhai jati hai — tag par jo daam likha hai (MP) us par. CP to dukaandar ka raaz hai, grahak ko nahi dikhta.

### D. HOW DOES IT WORK? — labh-hani 3 steps me

1. **CP likho** — khareedne ka daam.
2. **Labh/Hani nikalo** — SP − CP ya CP − SP.
3. **% nikalo** — (Labh/Hani ÷ CP) × 100. Hani ho to SP = CP × (1 − %/100).

### E. VISUAL MEMORY CONNECTION

CP ko **beej** (seed) samjho aur labh ko **fasal** (crop): fasal ki keemat hamesha beej ke hisab se napi jati hai — beej ₹800, fasal ₹120 zyada. Discount ko **tag** samjho — tag par jo daam hai usi par chhoot milti hai.

### F. IMPORTANT FACTS

| Fact | Formula / Value |
|---|---|
| Labh | SP − CP |
| Hani | CP − SP |
| Labh% / Hani% | **(Labh ya Hani / CP) × 100** — hamesha CP par |
| SP (labh par) | CP × (1 + %/100) |
| SP (hani par) | CP × (1 − %/100) |
| Discount | SP = MP × (1 − d/100) — MP par, CP par nahi |
| Worked examples (old notes, recomputed) | CP ₹800, SP ₹920 → Labh ₹120 → **15%** · CP ₹1,200, 10% hani → SP **₹1,080** |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| Labh% SP par nikalna | Labh% **hamesha CP par** — 120/920 galat, 120/800 = 15% sahi. |
| Discount CP par lagana | Discount **MP** par lagta hai — CP par nahi. |
| "10% hani" ka matlab SP = CP − 10 (₹) | 10% matlab CP ka 10% — ₹1,200 par ₹120, SP = **₹1,080**. |
| Labh aur labh% ko ek samajhna | Labh = **₹120** (rashi); Labh% = **15%** (dar). Alag cheezen hain. |

**⚠️ Mistakes box:** (1) Labh% SP par nikalna — sabse aam galti; pehle CP likho. (2) Discount aur hani ko ek samajhna — discount MP par, hani CP par. (3) % me ₹ jodna/ghataana — % hamesha CP ka % hota hai, seedha ₹ nahi.

### H. MEMORY TECHNIQUE (one only)

**"CP hi base hai"** — har labh/hani sawaal me pehle CP likho. Yeh ek hi aadat 90% galtiyan khatm kar deti hai.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** `08_MATHEMATICS-002` (CP ₹800, SP ₹920 → 15%); `08_MATHEMATICS-014` (CP ₹1,200, 10% hani → SP ₹1,080).
- **Actual PYQs (dataset subtopics):** **2024-P1 Q30** (Profit and loss); **2024-P3 Q2** (Loss and profit percent); **2023-11Feb-S2 Q11** (Loss percent — watch).
- **Recurring exam angles:** labh% CP par; hani par SP; discount MP par.

### J. ACTIVE RECALL — answer from memory, then check

1. Labh% ka formula kya hai, aur kis par lagta hai?
2. CP ₹800, SP ₹920 — labh% kitna hai?
3. CP ₹1,200 par 10% hani ho to SP kitna hai?
4. Discount kis par milta hai — CP ya MP?
5. Labh aur labh% me kya antar hai?
6. SP = CP × (1 + %/100) kaise banta hai?
7. 2024-P1 Q30 kis vishay par tha?

**Answers (check after attempting):** 1. (Labh/CP) × 100 — hamesha CP par. 2. 15%. 3. ₹1,080. 4. MP par. 5. Labh = ₹ (rashi); Labh% = % (dar). 6. SP = CP + Labh; Labh = CP × %/100. 7. Profit and loss.

### K. REVISION SUMMARY (one page — test yourself against it)

```
CP = base · Labh = SP − CP · Hani = CP − SP · Labh% = (Labh/CP) × 100
KEY: CP 800 → SP 920 = 15% labh · CP 1200, 10% hani → SP 1080
DISCOUNT: SP = MP × (1 − d/100) — MP par, CP par nahi
TRAPS: Labh% SP par nikalna · discount CP par lagana · % me ₹ jodna
MNEMONIC: "CP hi base hai"
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (bank Maths-002, -014) → tomorrow (recall + dukaan diagram redraw) → after 3 days (mixed with Chapter 9) → after 7 days (timed: bank set + PYQ 2024-P1 Q30, 2024-P3 Q2).

---

## Chapter 11 — Simple & Compound Interest

### A. VISUAL INTRODUCTION — SI grows straight, CI grows faster

```
P = ₹10,000 · R = 10% · T = 2 saal

  SI:  har saal ₹1,000 → 2 saal = ₹2,000
       ────────────── (seedha badhta hai)

  CI:  saal 1: ₹1,000 → saal 2: ₹1,100 (₹10,000 + ₹1,000 par byaj)
       ───────────╱ (dusre saal byaj par bhi byaj)
       CI = ₹2,100 · antar (CI − SI) = ₹100

  ANTAR FORMULA (2 saal): CI − SI = P × (R/100)² = 10000 × 0.01 = ₹100
```

> **How to use this diagram:** SI aur CI ka antar **dusre saal** se shuru hota hai — pehle saal dono barabar hote hain. Antar = pehle saal ke byaj par byaj.

### B. STORY-BASED EXPLANATION — byaj par byaj

Sadharan byaj (SI) me har saal **mool** (P) par byaj milta hai — ₹10,000 par 10% = har saal ₹1,000, 2 saal me ₹2,000. Chakravriddhi byaj (CI) me dusre saal byaj **mool + pehle saal ke byaj** par milta hai — ₹11,000 par 10% = ₹1,100. Kul CI = 1,000 + 1,100 = **₹2,100**. Antar = **₹100** — yah pehle saal ke ₹1,000 byaj par 10% byaj hai.

### C. WHY DOES IT HAPPEN? — CI zyada kyun hota hai

- **Why is CI more than SI?** Kyunki CI me byaj **byaj par bhi** milta hai. SI me har saal sirf mool par byaj milta hai; CI me dusre saal se byaj ki rashi bhi mool me jud jati hai. Isliye CI hamesha SI se zyada (ya barabar, jab T = 1 saal ho) hota hai.
- **Why does the difference formula work?** 2 saal me antar = pehle saal ke byaj (PR/100) par ek saal ka byaj (R%) = (PR/100) × (R/100) = **P(R/100)²**. Yeh derivation hai — 10000 × (10/100)² = 10000 × 0.01 = ₹100.
- **Why SI = PRT/100?** "Prati ₹100 par 1 saal ka byaj = R" — yahi paribhasha hai. P rupaye par T saal ka byaj = P × R × T / 100. Formula paribhasha se banta hai, ratne se nahi.

### D. HOW DOES IT WORK? — byaj 3 steps me

1. **SI nikalo:** P × R × T / 100.
2. **CI nikalo:** A = P(1 + R/100)ⁿ, phir CI = A − P.
3. **Antar (2 saal):** P(R/100)² — seedha formula, CI nikalne ki zaroorat nahi.

### E. VISUAL MEMORY CONNECTION

SI ko **seedhi sadak** samjho (har saal barabar), CI ko **chadhai wali sadak** — har saal thodi aur tez. Antar dusre saal se dikhne lagta hai — pehle saal dono sadaken ek hi hain.

### F. IMPORTANT FACTS

| Fact | Formula / Value |
|---|---|
| SI | **SI = (P × R × T)/100**; Amount A = P + SI |
| CI | **A = P(1 + R/100)ⁿ**; CI = A − P |
| Antar (2 saal) | **CI − SI = P(R/100)²** |
| Worked examples (old notes, recomputed) | P=₹10,000, R=10%, T=2 → SI **₹2,000** · CI **₹2,100** · antar **₹100** |
| 1 saal me | SI = CI (antar 0 — byaj par byaj ka samay hi nahi milta) |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| CI me har saal mool par byaj nikalna | CI me dusre saal se **mool + byaj** par byaj milta hai — yahi SI se antar hai. |
| Antar formula 3 saal par lagana | P(R/100)² sirf **2 saal** ke liye hai. 3 saal ka antar alag formula se nikalta hai. |
| R ko % ke bajaye seedha guna karna | R = 10% matlab **10/100 = 0.1** — 10 se guna karna galat hai. |
| SI aur CI me T ko saal ke bajaye mahina lena | T **saal** me hota hai — mahina diya ho to saal me badlo (mahina/12). |

**⚠️ Mistakes box:** (1) CI me dusre saal bhi mool par byaj nikalna — CI ka matlab hi "byaj par byaj" hai. (2) Antar formula 3 saal par lagana. (3) R/100 bhoolna — 10% = 0.1, 10 nahi.

### H. MEMORY TECHNIQUE (one only)

**"Pehla saal barabar, dusra saal antar"** — SI aur CI pehle saal ek jaise hote hain; antar dusre saal se shuru hota hai. Antar = pehle saal ke byaj par byaj.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** `08_MATHEMATICS-003` (SI ₹2,000); `08_MATHEMATICS-004` (CI − SI = ₹100).
- **Actual PYQs (dataset subtopics):** **2024-P1 Q19** (Simple/compound interest); **2024-P2 Q5** (Simple interest — date based); **2024-P3 Q28** (Simple interest — two investments); **2024-P4 Q16** (Compound interest — find sum).
- **Recurring exam angles:** SI vs CI; 2 saal ka antar formula; date-based SI (din gin kar samay nikalna).

### J. ACTIVE RECALL — answer from memory, then check

1. SI ka formula kya hai?
2. CI ka formula kya hai?
3. P=₹10,000, R=10%, T=2 saal — SI aur CI kitne hain?
4. 2 saal ka antar (CI − SI) ka formula kya hai?
5. CI, SI se zyada kyun hota hai?
6. 1 saal me SI aur CI barabar kyun hote hain?
7. 2024-P2 Q5 kis baat par based tha?

**Answers (check after attempting):** 1. (P×R×T)/100. 2. A = P(1+R/100)ⁿ; CI = A − P. 3. SI ₹2,000; CI ₹2,100. 4. P(R/100)². 5. Kyunki byaj par bhi byaj milta hai. 6. Byaj par byaj ka samay hi nahi milta. 7. Date-based simple interest.

### K. REVISION SUMMARY (one page — test yourself against it)

```
SI = PRT/100 · CI: A = P(1+R/100)ⁿ · CI = A − P
ANTAR (2 saal): CI − SI = P(R/100)² · 10000, 10%, 2y → SI 2000, CI 2100, antar 100
1 SAAL: SI = CI · R = 10% matlab 0.1
TRAPS: CI me mool par byaj · antar formula 3 saal par · R/100 bhoolna
MNEMONIC: "Pehla saal barabar, dusra saal antar"
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (bank Maths-003, -004) → tomorrow (recall + SI/CI diagram redraw) → after 3 days (mixed with Chapter 10) → after 7 days (timed: bank set + PYQ 2024-P1 Q19, 2024-P3 Q28).

---

## Chapter 12 — Ratio–Proportion & Age Problems

### A. VISUAL INTRODUCTION — ratio is sharing

```
A : B = 3 : 5, kul 64

  Kul bhaag = 3 + 5 = 8 · 1 bhaag = 64 ÷ 8 = 8
  A = 3 × 8 = 24 · B = 5 × 8 = 40

AGE — pita putra se 3 guna; 10 saal baad 2 guna:
  Ab: pita = 3x, putra = x
  10 saal baad: 3x + 10 = 2(x + 10) → 3x + 10 = 2x + 20 → x = 10
  Ab: pita 30, putra 10 · Check: 40 = 2 × 20 ✓
```

> **How to use this diagram:** Ratio me pehle **kul bhaag** nikalo, phir **ek bhaag** ka maan, phir jiska poochha hai use guna karo. Age me **x** maan kar samikaran banao — "baad" ka matlab dono me jodna hai.

### B. STORY-BASED EXPLANATION — baantna aur umar

Ratio ka matlab hai **baantna**: A:B = 3:5 ka matlab hai kul ko 8 hisso me baanto — A ko 3 hisse, B ko 5 hisse. Kul 64 hai to 1 hissa = 8, B = **40**. Age ka sawaal ek **samikaran** hai: pita putra se 3 guna hai (pita = 3x, putra = x). 10 saal baad dono ki umar 10 badhegi — pita 3x+10, putra x+10 — aur tab pita putra se 2 guna hoga: 3x+10 = 2(x+10). Hal karo: x = 10 — putra 10, pita **30**.

### C. WHY DOES IT HAPPEN? — ratio aur age ka ganit

- **Why total parts first?** Kyunki ratio **hisso** me baant-ta hai, rupayon me nahi. Kul bhaag nikale bina ek hisse ka maan nahi nikalta — aur bina ek hisse ke maan ke kisi ka hissa nahi nikalta.
- **Why does the age equation work?** Kyunki "10 saal baad" **dono** ki umar badhti hai — pita ki bhi, putra ki bhi. Sirf ek ki umar badhana sabse aam galti hai. Samikaran me dono taraf +10 likhna zaroori hai.
- **Why proportion ad = bc?** a/b = c/d ka matlab hai dono anupat barabar hain — tirchha guna (cross-multiplication) karne par ad = bc milta hai. Yeh anupat ki paribhasha hai.

### D. HOW DOES IT WORK? — ratio aur age 3 steps me

1. **Ratio:** kul bhaag nikalo → ek bhaag ka maan → jiska poochha hai use guna karo.
2. **Age:** chhoti umar = x maano → badi umar = guna × x → "baad/pehle" dono taraf jodo/ghatao → samikaran hal karo.
3. **Check karo:** jawab ko sawaal me wapas daal kar dekho (40 = 2 × 20 ✓).

### E. VISUAL MEMORY CONNECTION

Ratio ko **pizza ke tukde** samjho: 8 tukde, A ko 3, B ko 5. Age ko **dono taraf badhti seedhi** samjho — pita aur putra dono ek saath buddhe hote hain, isliye antar hamesha wahi rehta hai (yahan 20 saal).

### F. IMPORTANT FACTS

| Fact | Formula / Value |
|---|---|
| Ratio | a:b = a/b; kul bhaag = a + b |
| Proportion | a/b = c/d → **ad = bc** |
| Worked examples (old notes, recomputed) | A:B = 3:5, kul 64 → 1 bhaag 8 → B = **40** · Pita 3×, 10 saal baad 2× → pita **30**, putra **10** |
| Age rule | "Baad" = dono me jodo; "pehle" = dono me ghatao; **antar hamesha same** rehta hai |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| Kul bhaag nikale bina seedha guna karna | Pehle **kul bhaag** (8), phir ek bhaag (8), phir B (40) — kram mat todo. |
| Age me sirf ek ki umar badhana | "10 saal baad" **dono** ki umar badhti hai — pita ki bhi, putra ki bhi. |
| Ratio aur proportion ko ek samajhna | Ratio = **do sankhyaon ka tulna** (a:b); Proportion = **do ratio ki barabari** (a/b = c/d). |
| A:B = 3:5 me A = 3 samajhna | A = 3 **bhaag** — rashi nahi. Rashi = 3 × (ek bhaag ka maan) = 24. |

**⚠️ Mistakes box:** (1) Ek bhaag ka maan nikale bina seedha 3:5 se 64 baantna. (2) Age me ek taraf +10 bhoolna. (3) "Pita putra se 3 guna" ko "putra = 3x" likhna — pita = 3x, putra = x.

### H. MEMORY TECHNIQUE (one only)

**"Kul bhaag pehle"** (ratio) aur **"Dono ki umar badhegi"** (age) — do chhote vakya, dono chapter ka saar.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** `08_MATHEMATICS-011` (A:B = 3:5, kul 64 → B = 40); `08_MATHEMATICS-020` (pita 30, putra 10).
- **Actual PYQs (dataset subtopics):** **2024-P1 Q20** (Ratio); **2024-P4 Q17** (Gold biscuit — proportion).
- **Recurring exam angles:** kul bhaag se hissa; age samikaran (dono taraf +10); proportion (ad = bc).

### J. ACTIVE RECALL — answer from memory, then check

1. A:B = 3:5, kul 64 — B ka maan kitna hai?
2. Ratio me pehla kadam kya hai?
3. Pita putra se 3 guna hai; 10 saal baad 2 guna — ab pita kitne saal ka hai?
4. Age ke samikaran me "10 saal baad" ka matlab kya hai?
5. Proportion me ad = bc kaise banta hai?
6. A:B = 3:5 me A ki rashi kitni hai (kul 64 ho to)?
7. Pita aur putra ki umar ka antar 10 saal baad kitna hoga?

**Answers (check after attempting):** 1. 40. 2. Kul bhaag nikalna (8). 3. 30 saal (putra 10). 4. Dono ki umar me 10 jodna. 5. Tirchha guna (cross-multiplication) se. 6. 24 (3 × 8). 7. Wahi 20 saal — antar kabhi nahi badalta.

### K. REVISION SUMMARY (one page — test yourself against it)

```
RATIO: kul bhaag → ek bhaag → guna karo · 3:5, kul 64 → B = 40
AGE: chhoti = x · badi = guna × x · "baad" dono taraf jodo · pita 30, putra 10
PROPORTION: a/b = c/d → ad = bc · Antar hamesha same rehta hai
TRAPS: kul bhaag chhodna · ek taraf +10 bhoolna · ratio ko rashi samajhna
MNEMONIC: "Kul bhaag pehle" / "Dono ki umar badhegi"
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (bank Maths-011, -020) → tomorrow (recall + pizza diagram redraw) → after 3 days (mixed with Chapter 11) → after 7 days (timed: bank set + PYQ 2024-P1 Q20, 2024-P4 Q17).

---

## Chapter 13 — Time–Speed–Distance & Work–Time

### A. VISUAL INTRODUCTION — the triangle

```
SPEED TRIANGLE — ek hi tasveer, teen formula:

        Distance
       /    \
   Speed ── Time

  Speed = Distance / Time · Time = Distance / Speed · Distance = Speed × Time

  UNIT CHANGE: km/h → m/s: × 5/18 · m/s → km/h: × 18/5
  72 km/h = 72 × 5/18 = 20 m/s

  WORK: A 10 din, B 15 din → 1/10 + 1/15 = 5/30 = 1/6 → ek saath 6 din
  (Har din ka kaam jodo — din nahi, "kaam prati din" jodo!)
```

> **How to use this diagram:** Speed ka sawaal dekhte hi **triangle banao** — jo poochha hai use chhupao, baki do se formula mil jayega. Work me **din mat jodo, kaam-prati-din jodo**.

### B. STORY-BASED EXPLANATION — train aur platform

Train 300 m lambi hai aur 20 m/s ki gati se chal rahi hai — ek khambe (pole) ko paar karne me use **15 second** lagenge (300 ÷ 20). Lekin agar platform paar karna ho to doori **train + platform** hogi — kyunki train ka aakhri dibba bhi platform se guzarna hai. Kaam (work) me bhi wahi logic: A 10 din me kaam karta hai (roz 1/10 kaam), B 15 din me (roz 1/15 kaam) — dono milkar roz 1/10 + 1/15 = 1/6 kaam karte hain, isliye kul **6 din** lagenge.

### C. WHY DOES IT HAPPEN? — 5/18 aur 1/6 kyun

- **Why ×5/18?** 1 km = 1,000 m aur 1 ghanta = 3,600 second. Isliye 1 km/h = 1,000/3,600 m/s = **5/18 m/s**. Yeh unit badalna hai, formula nahi — 72 × 5/18 = 20 m/s.
- **Why add 1/10 + 1/15?** Kyunki kaam **rate** (prati din) se judta hai, din se nahi. A roz 1/10 kaam karta hai, B roz 1/15 — dono milkar roz 1/6 kaam. Din jodne se (10+15 = 25) galat jawab aayega — **rate jodo, din nahi**.
- **Why train + platform?** Kyunki "paar karna" ka matlab hai train ka **pehla hissa platform par chadhne se lekar aakhri hissa utarne tak** — kul doori = train ki lambaai + platform ki lambaai. Khamba (pole) ki lambaai nahi hoti, isliye wahan sirf train ki lambaai.

### D. HOW DOES IT WORK? — speed aur work 4 steps me

1. **Unit ek karo** — km/h ko m/s me badlo (×5/18) ya ulta (×18/5).
2. **Triangle se formula nikalo** — Speed = Distance/Time.
3. **Train:** khamba ho to sirf train ki lambaai; platform/pul ho to **train + platform**.
4. **Work:** har kaam karne wale ka **prati-din kaam** (1/din) jodo, phir ulta (reciprocal) lo.

### E. VISUAL MEMORY CONNECTION

Speed triangle ko **pahad** samjho: upar Distance, neeche Speed aur Time. Work ko **nal** (tap) samjho: ek nal tanki 10 ghante me bharta hai, dusra 15 me — dono kholo to tanki jaldi bharegi, kyunki **paani ki dhara** (rate) judti hai, ghante nahi.

### F. IMPORTANT FACTS

| Fact | Formula / Value |
|---|---|
| Speed | **Speed = Distance / Time** |
| Unit change | km/h → m/s: **× 5/18** · m/s → km/h: **× 18/5** |
| Work (together) | **1/T = 1/T₁ + 1/T₂** (prati-din kaam jodo) |
| Train + pole | Doori = **train ki lambaai** |
| Train + platform/bridge | Doori = **train + platform ki lambaai** |
| Relative speed | Ek disha me **antar**; vipreet disha me **yog** |
| Worked examples (old notes, recomputed) | 72 km/h = **20 m/s** · Train 300 m, 20 m/s → **15 sec** · A 10 din + B 15 din → ek saath **6 din** |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| Din jodna (10 + 15 = 25 din) | **Rate jodo:** 1/10 + 1/15 = 1/6 → **6 din**. Din jodne se galat jawab aayega. |
| Platform paar karte samay sirf train ki lambaai lena | Platform ho to doori = **train + platform**. Khamba ho to sirf train. |
| km/h ko seedha m/s samajhna | 72 km/h = **20 m/s**, 72 m/s nahi — ×5/18 zaroori hai. |
| Relative speed me ek disha me yog karna | Ek disha me **antar** (peeche wali tez ho to pakdegi); vipreet me **yog**. |

**⚠️ Mistakes box:** (1) Work me din jodna — rate jodo. (2) Platform ki lambaai bhoolna. (3) Unit badle bina guna/bhag karna — pehle km/h ko m/s me badlo ya ulta.

### H. MEMORY TECHNIQUE (one only)

**"5/18 aur 1/din"** — do hi sankhyaen: speed badalne ke liye **5/18**, kaam ke liye **1/din jodo**. In do ko yaad rakho, chapter yaad rahega.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** `08_MATHEMATICS-006` (A 10 din + B 15 din → 6 din); `08_MATHEMATICS-007` (72 km/h = 20 m/s); `08_MATHEMATICS-017` (train 300 m, 20 m/s → 15 sec).
- **Actual PYQs (dataset subtopics):** **2024-P2 Q30** (Work and time).
- **Recurring exam angles:** train + platform; unit change (×5/18); work together (rate jodo); relative speed.

### J. ACTIVE RECALL — answer from memory, then check

1. Speed ka formula kya hai?
2. 72 km/h kitne m/s hota hai?
3. km/h ko m/s me badalne ke liye kis se guna karte hain?
4. Train 300 m lambi hai, gati 20 m/s — khambe ko paar karne me kitna samay lagega?
5. Platform paar karte samay doori kya hoti hai?
6. A 10 din me aur B 15 din me kaam kare to dono milkar kitne din me karenge?
7. Work me din kyun nahi jodte?
8. Ek disha me relative speed kya hoti hai?

**Answers (check after attempting):** 1. Distance/Time. 2. 20 m/s. 3. 5/18 se. 4. 15 sec. 5. Train + platform ki lambaai. 6. 6 din. 7. Kyunki rate judta hai, din nahi. 8. Dono ki gati ka antar.

### K. REVISION SUMMARY (one page — test yourself against it)

```
TRIANGLE: Distance upar · Speed/Time neeche · Speed = Distance/Time
UNIT: km/h → m/s ×5/18 · m/s → km/h ×18/5 · 72 km/h = 20 m/s
WORK: 1/T = 1/T₁ + 1/T₂ · A 10 din + B 15 din → 6 din
TRAIN: khamba → sirf train · platform → train + platform · Relative: ek disha antar, vipreet yog
TRAPS: din jodna · platform bhoolna · unit na badalna
MNEMONIC: "5/18 aur 1/din"
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (bank Maths-006, -007, -017) → tomorrow (recall + triangle redraw) → after 3 days (mixed with Chapter 12) → after 7 days (timed: bank set + PYQ 2024-P2 Q30).

---

## Chapter 14 — Mensuration: Area & Volume

### A. VISUAL INTRODUCTION — shapes on one page

```
AREA (2D — satah)              VOLUME (3D — bharav)
  ■ Varg: a²                    ▣ Ghan (cube): a³
  ▭ Aayat: l × b                ▭ Ghanabh (cuboid): l × b × h
  △ Tribhuj: ½ × b × h          ▯ Belan (cylinder): πr²h
  ● Vritt: πr²                  ○ Gola (sphere): (4/3)πr³
  ⬭ Deergh-vritt (ellipse): πab  ▲ Shanku (cone): (1/3)πr²h  ← syllabus me hai, purane notes me nahi tha

  Vritt r = 7: kshetrafal = 22/7 × 49 = 154 cm² · paridhi = 2πr = 44 cm
  Belan r = 7, h = 10: aayatan = 22/7 × 49 × 10 = 1540 cm³
```

> **How to use this diagram:** Har aakriti ko **dekho aur chhoo kar** yaad karo: area = satah (flat), volume = bharav (bharna). π = 22/7 tabhi use karo jab trijya 7 se vibhajya ho.

### B. STORY-BASED EXPLANATION — jagah napna

Mensuration ka matlab hai **jagah napna**: zameen ka kshetrafal (area) aur bartan ka aayatan (volume). Khet ka kshetrafal nikalna ho to lambaai × chaudaai; kuan ka paani nikalna ho to belan (cylinder) ka aayatan — πr²h. Garden roller (2024-P3 Q3) belan hi hai: woh zameen par ghumta hai, aur uska **vakr satah** (2πrh) hi woh kshetra hai jo woh ek chakkar me dhakta hai.

### C. WHY DOES IT HAPPEN? — formula kyun wahi hai

- **Why circle area = πr²?** Kyunki vritt ko bahut chhote tukdon me kaat kar aayat banaya ja sakta hai — us aayat ki lambaai = aadhi paridhi (πr) aur chaudaai = trijya (r) — isliye kshetrafal = πr × r = **πr²**. Yeh derivation hai.
- **Why cylinder volume = πr²h?** Kyunki belan ek **vritt ko unchai tak khada** karna hai — neeche ka kshetrafal (πr²) × unchai (h). Volume = base area × height — yah niyam ghan, ghanabh aur belan teeno par lagta hai.
- **Why cone volume = (1/3)πr²h?** Kyunki shanku (cone) belan ka **ek-tihaai** hota hai — ek hi aadhar aur unchai wale belan me 3 shanku bharte hain. Yeh standard NCERT tathya hai (Class 10, Surface Areas and Volumes).
- **Why ellipse area = πab?** Vritt ka kshetrafal πr² hai; deergh-vritt (ellipse) ek **khincha hua vritt** hai — ek disha me aadha-aksh a, doosri me b — isliye πr² ki jagah **πab**. Yeh formula register §G12 aur handover checklist me diya gaya hai (neeche §G dekho).

### D. HOW DOES IT WORK? — mensuration 3 steps me

1. **Aakriti pehchano** — 2D (area) ya 3D (volume)?
2. **Formula lagao** — table se (neeche §F).
3. **Unit check karo** — kshetrafal cm² me, aayatan cm³ me; trijya 7 ho to π = 22/7.

### E. VISUAL MEMORY CONNECTION

Aakritiyon ko **bartan** samjho: vritt = thali (flat), belan = balti (bharav), gola = gend, shanku = kulfi-cone. Thali ka kshetrafal napo; balti ka paani napo.

### F. IMPORTANT FACTS

| Aakriti | Kshetrafal (Area) | Parimap / Satah |
|---|---|---|
| Varg (Square) | a² | Parimap 4a |
| Aayat (Rectangle) | l × b | Parimap 2(l+b) |
| Tribhuj (Triangle) | ½ × b × h | — |
| Vritt (Circle) | **πr²** | Paridhi 2πr |
| Samantar Chaturbhuj | b × h | — |
| **Deergh-vritt (Ellipse)** | **πab** (a, b = aadhe aksh) | — |

| Aakriti | Aayatan (Volume) | Satah |
|---|---|---|
| Ghan (Cube) | a³ | 6a² |
| Ghanabh (Cuboid) | l × b × h | 2(lb + bh + hl) |
| Belan (Cylinder) | **πr²h** | Vakr satah 2πrh |
| Gola (Sphere) | **(4/3)πr³** | 4πr² |
| Shanku (Cone) | **(1/3)πr²h** | Vakr satah πrl |

**Worked examples (old notes, recomputed):** Vritt r=7 cm → kshetrafal **154 cm²**, paridhi **44 cm** · Ghan a=5 → aayatan **125** · Belan r=7, h=10 → aayatan **1540 cm³** · Aayat 12×8 → **96 cm²** · Varg a=9 → parimap **36 cm**.

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| Area aur volume ko ek samajhna | Area = **satah** (cm²); Volume = **bharav** (cm³). Unit se pehchano. |
| Vritt ka kshetrafal (πr²) aur paridhi (2πr) | Kshetrafal me **r²**; paridhi me **2r**. r=7 ho to kshetrafal 154, paridhi 44. |
| Belan ka aayatan (πr²h) aur vakr satah (2πrh) | Aayatan me **r²h**; vakr satah me **rh**. Garden roller me vakr satah lagti hai (2024-P3 Q3). |
| Gola ka aayatan (4/3)πr³ aur satah 4πr² | Aayatan me **r³**; satah me **r²**. |
| ⚠️ **Ellipse (GAP — register §G12):** purane notes me ellipse ka formula **nahi tha** — yah syllabus ka ekmatra missing formula tha. Formula **πab** register §G12 aur handover §5.8 checklist me diya gaya hai; is file me use **verify-before-exam** ke roop me diya gaya hai — NCERT (Class 11, Conic Sections) se exam se pehle verify karo. a = aadha bada aksh (semi-major), b = aadha chhota aksh (semi-minor). | |
| Shanku (cone) purane notes me nahi tha | Syllabus me "volume (cone)" likha hai — isliye **(1/3)πr²h** yahan NCERT Class 10 Ch. 13 se joda gaya hai (standard formula, nayi khoj nahi). |

**⚠️ Mistakes box:** (1) π = 3.14 use karna jab trijya 7 se vibhajya ho — 22/7 se hisab saaf aata hai (154, 1540). (2) Area ka jawab cm³ me likhna — unit dekho. (3) Tribhuj me ½ bhoolna. (4) Belan ke aayatan aur vakr satah ko ek samajhna — roller wale sawaal me vakr satah lagti hai.

### H. MEMORY TECHNIQUE (one only)

**"2D = satah, 3D = bharav"** — aur π wale formula me **r ki ghat** dekho: area me r², volume me r³. Bas yahi do baaten poori table yaad dilati hain.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** `08_MATHEMATICS-008` (vritt r=7 → 154 cm²); `08_MATHEMATICS-009` (ghan a=5 → 125); `08_MATHEMATICS-018` (belan r=7, h=10 → 1540 cm³); `08_MATHEMATICS-019` (aayat 12×8 → 96); `08_MATHEMATICS-023` (varg a=9 → parimap 36).
- **Actual PYQs (dataset subtopics):** **2024-P3 Q3** (Garden roller — area covered; belan ki vakr satah); **2023-11Feb-S2 Q9** (Geometry — angle z, figure) — yah ek **aakriti (figure) se kon** nikalne wala sawaal tha. Syllabus me "area" likha hai, kon nahi — lekin figure wale sawaal aate hain, isliye 3 basic kon yaad rakho: seedha kon (straight line) = 180°; tribhuj ke teeno kon = 180°; samkon = 90°.
- **Recurring exam angles:** vritt (r=7, π=22/7); belan ka aayatan; vakr satah (roller); ghan/ghanabh; ellipse πab (GAP — verify karo).

### J. ACTIVE RECALL — answer from memory, then check

1. Vritt (r=7) ka kshetrafal aur paridhi kitni hai?
2. Belan (r=7, h=10) ka aayatan kitna hai?
3. Ghan (a=5) ka aayatan kitna hai?
4. Aayat (12×8) ka kshetrafal kitna hai?
5. Varg (a=9) ka parimap kitna hai?
6. Ellipse ka kshetrafal ka formula kya hai?
7. Shanku ka aayatan ka formula kya hai?
8. Garden roller wale sawaal me aayatan lagta hai ya vakr satah?

**Answers (check after attempting):** 1. 154 cm²; 44 cm. 2. 1540 cm³. 3. 125. 4. 96 cm². 5. 36 cm. 6. πab. 7. (1/3)πr²h. 8. Vakr satah (2πrh).

### K. REVISION SUMMARY (one page — test yourself against it)

```
AREA: varg a² · aayat l×b · tribhuj ½bh · vritt πr² · ellipse πab
VOLUME: ghan a³ · ghanabh lbh · belan πr²h · gola (4/3)πr³ · shanku (1/3)πr²h
KEY: r=7 → vritt 154, paridhi 44 · belan (7,10) → 1540 · ghan 5 → 125
TRAPS: area cm² / volume cm³ · πr² vs 2πr · aayatan vs vakr satah (roller) · tribhuj me ½ bhoolna
ELLIPSE: πab — GAP tha (register §G12), NCERT se verify karo
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (bank Maths-008, -009, -018, -019, -023) → tomorrow (recall + shapes diagram redraw) → after 3 days (mixed with Chapter 13) → after 7 days (timed: bank set + PYQ 2024-P3 Q3).

---

## Chapter 15 — Data Interpretation (Graphical Representation)

### A. VISUAL INTRODUCTION — pie chart

```
PIE CHART — 360° = 100%

  Kul 720 students, 25% Science:
  Science = 720 × 25/100 = 180 students
  Pie me Science ka kon = 25% × 360° = 90°

  RULE: pehle KUL nikalo, phir % nikalo.
  ────────────────┬───────────────
  Table: sankhya  │ Bar: tulna    │ Pie: hissa
  padho           │ unchai dekho  │ kon dekho
```

> **How to use this diagram:** DI me pehle **kul** (total) nikalo — bina kul ke % ka koi matlab nahi. Phir jo poochha hai use kul se nikalo.

### B. STORY-BASED EXPLANATION — graph padhna

Data Interpretation (DI) ka matlab hai **graph/table padh kar sawaal hal karna**. Teen tarah ke graph aate hain: **table** (sankhya padho), **bar chart** (unchai se tulna karo), **pie chart** (hissa dekho — 360° = 100%). Kul 720 students me 25% Science ke hain — matlab 720 × 25/100 = **180** students. Pie me Science ka kon = 25% × 360° = **90°**.

### C. WHY DOES IT HAPPEN? — 360° = 100% kyun

- **Why does a pie chart use 360°?** Kyunki poora vritt 360° ka hota hai — aur poora data 100% hota hai. Isliye 1% = 3.6°, 25% = 90°. Yeh **anupat** hai, convention nahi.
- **Why total first?** Kyunki % hamesha **kul ke hisab** se hota hai. Kul jaane bina 25% ka matlab nahi — 720 ka 25% = 180, lekin 800 ka 25% = 200. Kul badla to jawab badla.

### D. HOW DOES IT WORK? — DI 3 steps me

1. **Kul nikalo** — table/bar/pie se total padho.
2. **% ya hissa nikalo** — (bhaag/kul) × 100 ya kul × %/100.
3. **Option check karo** — % vs sankhya mix mat karo (option me 25% aur 180 dono ho sakte hain — poochha kya hai, yah dekho).

### E. VISUAL MEMORY CONNECTION

Pie chart ko **roti** samjho: poori roti = 100% = 360°. 25% matlab roti ka **chautha hissa** — 90° ka tukda.

### F. IMPORTANT FACTS

| Fact | Value |
|---|---|
| Pie chart | **360° = 100%**; 1% = 3.6° |
| Worked example (old notes, recomputed) | Kul 720 students, 25% Science → 720 × 25/100 = **180** students; kon = 90° |
| Table | Sankhya seedha padho; pehle kul nikalo |
| Bar chart | Unchai se tulna karo — sabse uncha = sabse zyada |
| % vs sankhya | Option me dhyaan do — poochha % hai ya sankhya |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| % aur sankhya ko ek samajhna | 25% = **hissa**; 180 = **sankhya**. Poochha kya hai — yah pehle dekho. |
| Bina kul nikale % nikalna | Pehle **kul** nikalo — bina kul ke % ka matlab nahi. |
| Pie me kon ko % samajhna | Kon = % × 3.6° — 25% ka kon **90°** hai, 25° nahi. |
| Bar chart me unchai ko seedha sankhya samajhna | Unchai **tulna** batati hai — asli sankhya axis par padho. |

**⚠️ Mistakes box:** (1) % poochha ho to sankhya likh dena (ya ulta). (2) Kul nikale bina hisab karna. (3) Pie me kon = % samajhna — kon = % × 3.6°.

### H. MEMORY TECHNIQUE (one only)

**"Pehle kul, phir hissa"** — DI ka ek hi niyam. Kul nikale bina koi hisab mat karo.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** `08_MATHEMATICS-012` (720 students, 25% Science → 180).
- **Actual PYQs:** is vishay par dataset ke 35 PYQs me **koi seedha PYQ nahi hai** — lekin "graphical representation of data" official syllabus me hai aur bank me 1 MCQ hai.
- **Recurring exam angles:** kul se hissa; pie me kon (360° = 100%); % vs sankhya.

### J. ACTIVE RECALL — answer from memory, then check

1. Pie chart me 360° kiske barabar hota hai?
2. Kul 720 students me 25% Science ke hon to kitne students hain?
3. 25% ka pie me kon kitna hota hai?
4. DI me pehla kadam kya hai?
5. % aur sankhya me kya antar hai?
6. Bar chart se kya pata chalta hai?

**Answers (check after attempting):** 1. 100%. 2. 180. 3. 90°. 4. Kul nikalna. 5. % = hissa; sankhya = ginti. 6. Unchai se tulna.

### K. REVISION SUMMARY (one page — test yourself against it)

```
PIE: 360° = 100% · 1% = 3.6° · 25% = 90°
KEY: kul 720, 25% Science → 180 students
RULE: Pehle KUL nikalo, phir % nikalo · % vs sankhya — poochha kya hai, dekho
TRAPS: % ko sankhya samajhna · bina kul ke hisab · kon = % samajhna
MNEMONIC: "Pehle kul, phir hissa"
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (bank Maths-012) → tomorrow (recall + pie diagram redraw) → after 3 days (mixed with Chapter 14) → after 7 days (timed: bank set).

---

## Chapter 16 — Analogy, Odd One Out & Classification

### A. VISUAL INTRODUCTION — the relationship map

```
ANALOGY — pehle rishta, phir jawab:

  Kitab : Padhna :: Kalam : LIKHNA
  (Kitab se padhte hain → Kalam se likhte hain)

  Delhi : Bharat :: Paris : FRANCE
  (Delhi Bharat ki rajdhani → Paris France ki rajdhani)

  Doctor : Hospital :: Teacher : SCHOOL
  (Doctor ka kaam-sthal Hospital → Teacher ka School)

ODD ONE OUT — jo alag hai use nikalo:
  2, 3, 5, 7, 9 → 9 (baki prime, 9 composite)
  Rose, Lotus, Marigold, Mango → MANGO (baki phool, Mango phal)
```

> **How to use this diagram:** Analogy me pehle **pehle jode ka rishta** likho — phir wahi rishta dusre jode par lagao. Odd one out me pehle **common baat** dhoondho — jo usme na ho, wahi odd hai.

### B. STORY-BASED EXPLANATION — rishta pehchanna

Analogy ka matlab hai **rishta**: "Kitab : Padhna" ka rishta hai "cheez : uska kaam" — kitab se padhte hain. To "Kalam : ?" me wahi rishta lagao — kalam se **likhte** hain. Odd one out iska ulta hai: 4 cheezon me 3 ki ek common baat hai, ek ki nahi — woh ek **odd** hai. 2, 3, 5, 7 prime hain, 9 composite hai — isliye 9 odd hai.

### C. WHY DOES IT HAPPEN? — rishta kyun kaam karta hai

- **Why does the first pair decide the answer?** Kyunki analogy me **rishta** hi sawaal hai, shabd nahi. Pehla joda rishta batata hai (rajdhani, kaam, kaam-sthal); dusra joda usi rishte ko dohrata hai. Rishta badla to jawab badal jayega.
- **Why is the odd one out the one that breaks the rule?** Kyunki 3 cheezen ek niyam manti hain (prime hona, phool hona) aur ek nahi manti. Niyam dhoondhna hi kaam hai — niyam mil gaya to odd mil gaya.
- **Why do number-group analogies exist?** 2023-S2 Q12 me sankhyaon ke samooh ka rishta poochha gaya — jaise 2, 3, 5, 7 ka rishta "prime" hai. Sankhyaon me bhi rishta hota hai: prime, varg, sam/visham, guna.

### D. HOW DOES IT WORK? — analogy aur odd one out 3 steps me

1. **Pehle jode ka rishta likho** — ek shabd me (rajdhani / kaam / kaam-sthal / prime).
2. **Wahi rishta dusre jode par lagao** — jo option rishta nibhaye, wahi jawab.
3. **Odd one out:** pehle **common baat** dhoondho (3 me kya same hai) — jo usme na ho, wahi odd.

### E. VISUAL MEMORY CONNECTION

Analogy ko **tarazu** samjho: pehla joda ek palda, dusra joda dusra palda — dono ka **rishta** barabar hona chahiye. Odd one out ko **4 me se 1 alag rang** samjho — 3 ek rang ke, 1 dusre rang ka.

### F. IMPORTANT FACTS

| Type | Rule | Example (old notes, recomputed) |
|---|---|---|
| Kaam (tool : work) | Cheez : uska kaam | Kitab : Padhna :: Kalam : **Likhna** |
| Rajdhani (capital) | Desh : rajdhani | Delhi : Bharat :: Paris : **France** |
| Kaam-sthal (worker : place) | Vyakti : uska sthal | Doctor : Hospital :: Teacher : **School** |
| Odd one — numbers | Common niyam todo | 2, 3, 5, 7, **9** (9 composite, baki prime) |
| Odd one — words | Shreni (category) dekho | Rose, Lotus, Marigold, **Mango** (Mango phal hai) |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| Pehla joda dekhe bina seedha option chunna | Pehle **rishta** likho — bina rishte ke guess karna galti hai. |
| Odd one out me "alag" ko "galat" samajhna | Odd ka matlab **alag shreni**, galat nahi — Mango galat nahi, bas phal hai. |
| Rajdhani wale me desh aur shahar ulta karna | Delhi : Bharat me **pehle shahar, phir desh** — Paris : France me bhi wahi kram. |
| 9 ko prime samajhna | 9 = 3 × 3 — **composite** hai. |

**⚠️ Mistakes box:** (1) Rishta likhe bina option dekhna — option dekhkar rishta badal jata hai. (2) Odd one out me pehli nazar me alag dikhne wali cheez chunna — common baat pehle dhoondho. (3) Kram ulta karna — A:B :: C:D me A↔C aur B↔D ka rishta same hota hai.

### H. MEMORY TECHNIQUE (one only)

**"Pehle rishta, phir jawab"** — analogy ka ek hi niyam. Rishta likhe bina option mat dekho.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** `08_REASONING-009` (Kitab : Padhna :: Kalam : Likhna); `08_REASONING-010` (Doctor : Hospital :: Teacher : School); `08_REASONING-011` (2, 3, 5, 7, 9 → 9); `08_REASONING-012` (Rose, Lotus, Marigold, Mango → Mango); `08_REASONING-016` (Delhi : Bharat :: Paris : France).
- **Actual PYQs (dataset subtopics):** **2023-11Feb-S2 Q12** (Number group analogy).
- **Recurring exam angles:** kaam/rajdhani/kaam-sthal ka rishta; prime vs composite; shreni (phool vs phal).

### J. ACTIVE RECALL — answer from memory, then check

1. Kitab : Padhna :: Kalam : ?
2. Delhi : Bharat :: Paris : ?
3. Doctor : Hospital :: Teacher : ?
4. 2, 3, 5, 7, 9 me odd kaun sa hai, aur kyun?
5. Rose, Lotus, Marigold, Mango me odd kaun sa hai?
6. Analogy me pehla kadam kya hai?
7. Odd one out me pehle kya dhoondhna chahiye?
8. 2023-S2 Q12 kis baat par tha?

**Answers (check after attempting):** 1. Likhna. 2. France. 3. School. 4. 9 — composite hai, baki prime. 5. Mango — phal hai, baki phool. 6. Pehle jode ka rishta likhna. 7. 3 cheezon ki common baat. 8. Number group analogy.

### K. REVISION SUMMARY (one page — test yourself against it)

```
ANALOGY: pehle rishta likho → wahi rishta lagao
KEY: Kitab:Padhna :: Kalam:Likhna · Delhi:Bharat :: Paris:France · Doctor:Hospital :: Teacher:School
ODD ONE: common baat dhoondho → jo usme na ho, wahi odd · 9 (composite) · Mango (phal)
TRAPS: rishta likhe bina option dekhna · kram ulta karna · 9 ko prime samajhna
MNEMONIC: "Pehle rishta, phir jawab"
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (bank Reasoning-009–012, -016) → tomorrow (recall + relationship map redraw) → after 3 days (mixed with Chapter 15) → after 7 days (timed: bank set + PYQ 2023-S2 Q12).

---

## Chapter 17 — Syllogism, Venn & Statement–Assumption/Conclusion

### A. VISUAL INTRODUCTION — circles inside circles

```
SYLLOGISM — Venn diagram banao, phir nishkarsh padho:

  "Sabhi kutte janwar hain; sabhi janwar jeevit hain"
       ┌───────────────────────┐
       │  JEEVIT (sabse bada)  │
       │   ┌───────────────┐   │
       │   │  JANWAR       │   │
       │   │   ┌───────┐   │   │
       │   │   │ KUTTE │   │   │
       │   │   └───────┘   │   │
       │   └───────────────┘   │
       └───────────────────────┘
  → "Sabhi kutte jeevit hain" — SAHI (kutte janwar ke andar, janwar jeevit ke andar)

  RULE: "Kuchh" se "Sabhi" kabhi nahi nikalta.
  "Sabhi A, B hain" se yah NAHI nikalta: "Sabhi B, A hain."
```

> **How to use this diagram:** Syllogism me pehle **Venn banao** — bada circle bahar, chhota andar. Phir nishkarsh ko diagram me dekho: woh circle ke andar hai ya bahar?

### B. STORY-BASED EXPLANATION — dabbe ke andar dabba

Syllogism ek **dabbe ke andar dabba** hai: "Sabhi kutte janwar hain" ka matlab hai kutte wala dabba, janwar wale dabbe ke **andar** hai. "Sabhi janwar jeevit hain" ka matlab hai janwar wala dabba, jeevit wale dabbe ke andar hai. To kutte wala dabba jeevit wale dabbe ke andar bhi hai — isliye "Sabhi kutte jeevit hain" **sahi** hai. Lekin "Kuchh" se "Sabhi" nahi nikalta: "Kuchh A, B hain" ka matlab sirf kuchh A, B ke andar hain — sabhi nahi.

### C. WHY DOES IT HAPPEN? — "Kuchh" se "Sabhi" kyun nahi

- **Why can't "some" give "all"?** Kyunki "kuchh" sirf **kuchh** ki baat karta hai — baaki ke baare me kuchh nahi kehta. "Kuchh kutte kaale hain" se yah nahi nikalta ki "sabhi kutte kaale hain" — baaki kutte safed bhi ho sakte hain. Yeh **tark** (logic) hai, yaad karne ki baat nahi.
- **Why is "Sabhi A, B hain" not reversible?** Kyunki A, B ke andar hai — lekin B, A ke andar nahi hai. "Sabhi kutte janwar hain" se "Sabhi janwar kutte hain" nahi nikalta — janwar me billi, ghoda bhi hain.
- **Why extreme words fail in assumptions?** "Sabhi", "kabhi nahi", "hamesha" jaise shabd **poori** baat karte hain — statement me itni badi baat likhi hi nahi hoti, isliye woh assumption aam taur par galat hota hai.

### D. HOW DOES IT WORK? — syllogism aur assumption 4 steps me

1. **Venn banao** — bada circle bahar, chhota andar; "kuchh" ho to circles **overlap** karo.
2. **Nishkarsh ko diagram me dekho** — andar hai to sahi, bahar hai to galat.
3. **Assumption:** sirf wahi assumption jo statement ke liye **zaroori** ho — extreme words (sabhi, hamesha, kabhi nahi) wale option aam taur par galat.
4. **Cause–effect:** samay kram dekho — pehle karan, phir prabhav.

### E. VISUAL MEMORY CONNECTION

Syllogism ko **dabbe ke andar dabba** samjho: sabse bada dabba bahar, chhota andar. Nishkarsh sahi hai ya galat — yah dabbe ko dekhkar pata chalta hai, yaad karke nahi.

### F. IMPORTANT FACTS

| Fact | Value |
|---|---|
| Syllogism — "Sabhi A, B" | A ka circle, B ke **andar** |
| Syllogism — "Kuchh A, B" | A aur B ke circles **overlap** karte hain |
| Rule 1 | **"Kuchh" se "Sabhi" nahi nikalta** |
| Rule 2 | "Sabhi A, B hain" se "Sabhi B, A hain" **nahi** nikalta |
| Worked example (old notes) | "Sabhi kutte janwar hain; sabhi janwar jeevit hain" → "Sabhi kutte jeevit hain" — **sahi** |
| Statement–assumption | Sirf **zaroori** assumption; extreme words (sabhi, hamesha, kabhi nahi) aam taur par galat |
| Venn — Doctor, Engineer, Male | Overlapping circles; **common region** dhyaan se padho |
| Grammar note (bank oddity) | `08_REASONING-019`: "Each of the students ___ present" — jawab D (**is**), kyunki "Each" singular hai. Yeh **English grammar** ka sawaal hai, reasoning ka nahi — bank me is sthan par hai, isliye yahan note kiya gaya hai. |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| "Kuchh A, B hain" se "Sabhi A, B hain" nikalna | **Galat.** Kuchh se sabhi nahi nikalta — baaki A ke baare me kuchh nahi kaha gaya. |
| "Sabhi A, B hain" ko ulta padhna | A, B ke andar hai; B, A ke andar **nahi** hai. |
| "Sabhi A, B hain" se "Kuchh B, A hain" na nikalna | **Yah nikalta hai:** agar sabhi A, B hain to kuchh B, A zaroor hain (wahi A wale). |
| Assumption me extreme words chunna | "Sabhi/hamesha/kabhi nahi" wale option aam taur par **galat** hote hain. |
| Venn me common region ko ignore karna | Common region hi sawaal hota hai — use dhyaan se padho. |

**⚠️ Mistakes box:** (1) "Kuchh" se "Sabhi" nikalna — sabse aam galti. (2) Ulta padhna — "Sabhi A, B" ≠ "Sabhi B, A". (3) Assumption me strong words chunna. (4) Venn banaye bina guess karna — hamesha diagram banao.

### H. MEMORY TECHNIQUE (one only)

**"Dabbe ke andar dabba"** — Venn diagram hi technique hai. "Kuchh se Sabhi nahi" — yah ek vakya yaad rakho.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** `08_REASONING-013` (syllogism — sabhi kutte jeevit hain); `08_REASONING-020` ("Sabhi A, B hain" se kya nahi nikalta); `08_REASONING-024` (statement–assumption — khel maidan); `08_REASONING-019` (grammar — "Each … is", §F dekho).
- **Actual PYQs:** is vishay par dataset ke 35 PYQs me **koi seedha PYQ nahi hai** — lekin syllogism/statement official syllabus ("mental & analytical ability") ka hissa hai aur bank me 4 MCQs hain.
- **Recurring exam angles:** "Kuchh" se "Sabhi" nahi; ulta padhna; extreme words wale assumption galat.

### J. ACTIVE RECALL — answer from memory, then check

1. "Sabhi kutte janwar hain; sabhi janwar jeevit hain" se kya nishkarsh nikalta hai?
2. "Kuchh" se "Sabhi" kyun nahi nikalta?
3. "Sabhi A, B hain" se "Sabhi B, A hain" kyun nahi nikalta?
4. "Sabhi A, B hain" se "Kuchh B, A hain" nikalta hai ya nahi?
5. Assumption me kaun se shabd wale option aam taur par galat hote hain?
6. Syllogism me pehla kadam kya hai?
7. "Each of the students ___ present" me sahi verb kya hai, aur kyun?

**Answers (check after attempting):** 1. "Sabhi kutte jeevit hain" — sahi. 2. Kyunki "kuchh" sirf kuchh ki baat karta hai. 3. Kyunki A, B ke andar hai; B, A ke andar nahi. 4. Nikalta hai — wahi A wale B me hain. 5. "Sabhi / hamesha / kabhi nahi" jaise extreme words. 6. Venn diagram banana. 7. "Is" — "Each" singular hai.

### K. REVISION SUMMARY (one page — test yourself against it)

```
VENN: bada bahar, chhota andar · "Kuchh" = overlap
RULES: "Kuchh" se "Sabhi" NAHI · "Sabhi A,B" ≠ "Sabhi B,A" · "Sabhi A,B" → "Kuchh B,A" SAHI
ASSUMPTION: sirf zaroori wala · extreme words (sabhi/hamesha) aam taur par galat
GRAMMAR NOTE: Each → singular verb ("is")
TRAPS: kuchh se sabhi nikalna · ulta padhna · Venn banaye bina guess
MNEMONIC: "Dabbe ke andar dabba"
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (bank Reasoning-013, -019, -020, -024) → tomorrow (recall + Venn redraw) → after 3 days (mixed with Chapter 16) → after 7 days (timed: bank set).

---

## Chapter 18 — Mental & Analytical Ability (Figures, Cubes, Puzzles)

### A. VISUAL INTRODUCTION — count by size, not by looking

```
PAINTED CUBE (4×4×4 = 64 chhote ghana):
  3 rang wale (kone): 8 · 2 rang wale (kinare): 12×(4−2) = 24
  1 rang wala (satah): 6×(4−2)² = 24 · 0 rang wala (andar): (4−2)³ = 8
  Check: 8 + 24 + 24 + 8 = 64 ✓

COUNT TRIANGLES: chhote → bade — pehle sabse chhote tribhuj gino,
  phir 2 chhote se bana bada, phir 3 se bana... — size ke hisab se gino,
  nazar se nahi.

PAPER FOLDING (box): aamne-saamne (opposite) wale phalak kabhi nahi milte.
  "1-4-1" net me beech ke 4 me pehla aur teesra aamne-saamne hote hain.
```

> **How to use this diagram:** Figure wale sawaal me **size ke hisab se gino** — pehle chhote, phir bade. Cube me **jagah** se gino — kone, kinare, satah, andar.

### B. STORY-BASED EXPLANATION — aakriti ko tod kar gino

Mental ability ke sawaal aakriti (figure) se poochhe jate hain: kitne tribhuj hain? Ghane (cube) ko rang kar kaata gaya — kitne tukdon par 2 rang hain? Kagaz ko mod kar dabba banaya — kaun se phalak aamne-saamne honge? In sabka ek hi tareeka hai: **aakriti ko tod kar gino**. Tribhuj ginte samay pehle sabse chhote gino, phir unse bane bade. Cube me tukde unki **jagah** se gino — kone par 3 rang, kinare par 2, satah par 1, andar 0.

### C. WHY DOES IT HAPPEN? — cube ke formula kyun kaam karte hain

- **Why 8 corners always have 3 faces painted?** Kyunki ghane ke **8 kone** hote hain — har kone par 3 satah milti hain. Kone ki jagah badalti nahi, isliye 3 rang wale tukde hamesha **8** hote hain — chahe cube kitna bhi bada ho.
- **Why 2-face pieces = 12(n−2)?** Kyunki ghane ke **12 kinare** hote hain, aur har kinare par (n−2) tukde hote hain (do kone wale tukde hata kar). n=4 ho to 12×2 = **24**.
- **Why 1-face pieces = 6(n−2)²?** Kyunki ghane ki **6 satah** hain, aur har satah par (n−2)² tukde hote hain (kinare hata kar). n=4 ho to 6×4 = **24**.
- **Why 0-face pieces = (n−2)³?** Kyunki andar ka hissa bhi ek chhota ghane hota hai — (n−2) side wala. n=4 ho to 2³ = **8**. Check: 8+24+24+8 = **64** = 4³ ✓.
- **Why opposite faces never meet in a folded box?** Kyunki kagaz ko modne par aamne-saamne wale phalak **ek dusre ke peeche** chale jate hain — woh kabhi ek kinare par nahi milte. Net me "1-4-1" pattern me beech ke 4 me pehla aur teesra aamne-saamne hote hain.

### D. HOW DOES IT WORK? — figure sawaal 4 steps me

1. **Tribhuj gino:** chhote se bade — size ke hisab se; har size ko alag gino, phir jodo.
2. **Cube:** n nikalo (kul tukde = n³) → kone 8, kinare 12(n−2), satah 6(n−2)², andar (n−2)³.
3. **Paper folding:** net me aamne-saamne wale phalak pehchano (1-4-1 me pehla↔teesra, dusra↔chautha); jo aamne-saamne hain woh kabhi ek saath nahi dikhenge.
4. **Sign interchange / missing number:** chinh badal kar **BODMAS** se hal karo; table me row/column ka rishta dhoondho (yog, guna, antar).

### E. VISUAL MEMORY CONNECTION

Cube ko **Rubik's cube** samjho: kone wale tukde 3 rang ke, kinare wale 2 rang ke, beech wale 1 rang ke, andar wala bina rang ke. Rubik's cube dekhkar hi formula yaad aa jayega.

### F. IMPORTANT FACTS

| Fact | Formula / Value |
|---|---|
| Painted cube (n×n×n) | 3 faces: **8** · 2 faces: **12(n−2)** · 1 face: **6(n−2)²** · 0 faces: **(n−2)³** |
| Worked example (2024-P2 Q21) | n=4 (64 tukde): 3-face **8**, 2-face **24**, 1-face **24**, 0-face **8** (check: 8+24+24+8 = 64) |
| Count triangles | Chhote → bade; size ke hisab se gino |
| Paper folding | Aamne-saamne wale phalak kabhi nahi milte; "1-4-1" net |
| Sign interchange | Chinh badlo, phir **BODMAS** (Bracket, Of, Division, Multiplication, Addition, Subtraction) |
| Missing number (table) | Row ya column ka rishta dhoondho — yog, guna, antar, varg |
| BODMAS order | Bracket → Of → Division → Multiplication → Addition → Subtraction |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| Cube me 3-face wale tukde n se badalte hain | **Nahi** — kone hamesha **8** hote hain, n kuchh bhi ho. |
| 2-face aur 1-face ke formula ulta lagana | 2-face: **12(n−2)** (kinare); 1-face: **6(n−2)²** (satah). |
| Tribhuj ginne me sirf chhote ginna | **Bade bhi gino** — 2-3 chhote se bane bade tribhuj bhi gine jate hain. |
| Paper folding me aamne-saamne wale ko ek saath dikhana | Aamne-saamne wale phalak **kabhi ek saath nahi dikhte** — option me dikhen to woh galat hai. |
| Sign interchange me BODMAS bhoolna | Chinh badalne ke **baad** BODMAS se hal karo — pehle guna/bhag, phir jod/ghata. |

**⚠️ Mistakes box:** (1) Cube me kone 8 ke bajaye n³ se nikalna. (2) Tribhuj ginne me bade chhoot jana — size ke hisab se gino. (3) BODMAS bhoolna — guna/bhag pehle. (4) Missing number me ek row ka rishta dusri row par na check karna — rishta **har** row/column par lagna chahiye.

### H. MEMORY TECHNIQUE (one only)

**"8–12–6–1"** — kone 8, kinare 12, satah 6, andar (n−2)³. Cube ka poora formula in 4 sankhyaon me hai.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** is vishay par bank me **koi MCQ nahi hai** — yah chapter sirf PYQs aur official syllabus ("mental & analytical ability") par based hai.
- **Actual PYQs (dataset subtopics):** **2024-P2 Q18** (Count triangles in figure); **2024-P2 Q21** (Painted cube — 64 pieces); **2024-P4 Q9** (Paper folding — box); **2024-P3 Q29** (Sign interchange); **2024-P3 Q12** (Missing number — table).
- **Recurring exam angles:** cube ke rang (8/24/24/8); tribhuj ginna; aamne-saamne wale phalak; BODMAS ke baad chinh badalna.

### J. ACTIVE RECALL — answer from memory, then check

1. 4×4×4 cube me 3 rang wale, 2 rang wale, 1 rang wale aur 0 rang wale tukde kitne hain?
2. 3 rang wale tukde hamesha kitne hote hain, aur kyun?
3. Tribhuj ginte samay kis kram me ginte hain?
4. Paper folding me aamne-saamne wale phalak ke baare me kya niyam hai?
5. Sign interchange ke baad kis niyam se hal karte hain?
6. Missing number wale sawaal me pehle kya dhoondhte hain?
7. 2-face wale tukdon ka formula kya hai?
8. BODMAS ka kram kya hai?

**Answers (check after attempting):** 1. 8, 24, 24, 8. 2. 8 — ghane ke 8 kone hote hain. 3. Chhote se bade, size ke hisab se. 4. Woh kabhi ek saath nahi dikhte. 5. BODMAS se. 6. Row/column ka rishta (yog, guna, antar). 7. 12(n−2). 8. Bracket, Of, Division, Multiplication, Addition, Subtraction.

### K. REVISION SUMMARY (one page — test yourself against it)

```
CUBE (n=4, 64 tukde): 3-face 8 · 2-face 24 · 1-face 24 · 0-face 8 (check: 8+24+24+8 = 64)
TRIANGLES: chhote → bade, size ke hisab se gino
BOX: aamne-saamne wale kabhi ek saath nahi dikhte
SIGNS: chinh badlo → BODMAS · MISSING NUMBER: row/column ka rishta dhoondho
TRAPS: kone 8 ke bajaye n³ · bade tribhuj chhootna · BODMAS bhoolna
MNEMONIC: "8–12–6–1"
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (cube formula + triangle counting practice) → tomorrow (recall + cube diagram redraw) → after 3 days (mixed with Chapter 17) → after 7 days (timed: PYQ 2024-P2 Q18/Q21, 2024-P4 Q9, 2024-P3 Q12/Q29).

---

## Preservation note (audit trail for this redesign)

**Old file:** `notes/08_reasoning_mathematics.md` (109 lines). **New file:** this file, 18 chapters, A–K structure.

**Every solved example from the old notes, recomputed by the author of this file (all correct):**
- A1: 252 = 2²×3²×7 ✓; √144 = 12 ✓; √625 = 25 ✓ → Chapter 7.
- A2: 240 ka 15% = 36 ✓; 80 ka 125% = 100 ✓; ₹500 → ₹650 = 30% ✓; +20% phir −20% = −4% ✓ → Chapter 9.
- A3: CP ₹800, SP ₹920 → 15% ✓; CP ₹1,200, 10% hani → SP ₹1,080 ✓ → Chapter 10.
- A4: SI ₹2,000, CI ₹2,100, antar ₹100 ✓ → Chapter 11.
- A5: 5th sankhya 35 ✓; pita 30, putra 10 ✓ → Chapters 8, 12.
- A6: A+B = 6 din ✓; 72 km/h = 20 m/s ✓; train 300 m → 15 sec ✓ → Chapter 13.
- A7: vritt r=7 → 154 cm², paridhi 44 cm ✓; ghan a=5 → 125 ✓ → Chapter 14.
- A8: LCM(12, 18) = 36 ✓; B = 40 ✓; belan 1540 cm³ ✓ → Chapters 7, 12, 14.
- A9: 720 students, 25% Science → 180 ✓ → Chapter 15.
- B1: CAT = 24, DOG = 26 ✓; CAT → DBU, DOG → EPH ✓ → Chapter 2.
- B2: 2, 6, 12, 20, 30 → 42 ✓; A, C, F, J, O → U ✓; 3, 9, 27, 81 → 243 ✓; 1, 4, 9, 16, 25 → 36 ✓ → Chapter 1.
- B3: "maa ki ikloti beti ki beti" = bhanji ✓ → Chapter 3.
- B4: Uttar 5 km → dayein 3 → dayein 4 → √10 km, Uttar-Purab ✓ → Chapter 4.
- B5: Kitab:Padhna :: Kalam:Likhna ✓; Doctor:Hospital :: Teacher:School ✓; 9 odd ✓; Mango odd ✓ → Chapter 16.
- B6: syllogism "sabhi kutte jeevit hain" ✓ → Chapter 17.
- B7: ranking 29th ✓; 1 Jan 2026 = Thursday (calendar check, 11 Nov 2026) ✓; 3:00 = 90° ✓ → Chapters 5, 6.
- B8: assumption/cause-effect/puzzle tricks → Chapters 17, 18.

**Facts dropped: none.**

**Two items re-framed (not dropped):**
1. **90° (samkon) frequency — CORRECTED.** Old notes said "Samkon (90°) — 1 ghante me 2 baar". Precisely: 12 ghante me kul **22 baar** banta hai, lekin 2–3 aur 8–9 wale ghante me sirf **1 baar** (kyunki 3:00 aur 9:00 par kon pehle se 90° hota hai). Chapter 6 §F/§G states the precise fact. The old wording is a common simplification, not an exam-trap fact.
2. **Out-of-syllabus warning preserved.** Old notes §A8 already marked Algebra/Trigonometry as OUT OF SYLLABUS (removed from the 12th level). This file keeps that warning in the header and adds the two 2024 PYQs that belong to the old syllabus (2024-P1 Q21 Trigonometry; 2024-P3 Q27 Quadratic roots) as do-not-study items.

**New material added (standard, sourced — not invented):**
- Cone volume (1/3)πr²h — syllabus lists "volume (cone)"; NCERT Class 10 Ch. 13 (Surface Areas and Volumes). Old notes had no cone formula.
- Ellipse area πab — syllabus lists it; formula as given in register §G12 and handover §5.8 checklist; marked **verify-before-exam** (NCERT Class 11, Conic Sections).
- Median (madhyika) — definition + method; linked to PYQ 2024-P1 Q18. Standard statistics.
- Painted-cube formulas 8 / 12(n−2) / 6(n−2)² / (n−2)³ — derived by counting positions (corners/edges/faces/interior); verified against 2024-P2 Q21 (n=4 → 8/24/24/8, sums to 64).
- Three basic angle facts (straight line 180°, triangle angles 180°, right angle 90°) — linked to PYQ 2023-S2 Q9 (angle from a figure); standard NCERT Class 9.
- BODMAS order — standard arithmetic convention.
- "1-4-1" cube-net rule — standard net reasoning.

**Bank MCQ coverage:** all 48 IDs appear in full form (Maths 001–024, Reasoning 001–024). Reasoning-019 (grammar) is noted in Chapter 17 §F/§I as a grammar item sitting in the Reasoning bank.

**PYQ coverage:** all 35 IDs appear in full form (33 linked to chapters by subtopic + 2 flagged out-of-syllabus in the header). No PYQ question text is invented anywhere.
