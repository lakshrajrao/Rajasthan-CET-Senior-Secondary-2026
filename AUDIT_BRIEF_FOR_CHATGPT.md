# Audit Brief — for ChatGPT (or any auditor)

## What this repo is

Complete exam-intelligence and preparation system for **Rajasthan CET Senior Secondary Level (12th Level) 2026**, built 11 November 2026 by the user's assistant (Muse) in one day. Exam: **1–3 December 2026 (tentative)**, conducting body **Rajasthan Staff Selection Board (RSSB), Jaipur**, Advertisement No. **08/2026** (23 June 2026, amended 25 June 2026).

## What you are asked to do

1. **Audit every file** in this repo for factual accuracy, internal consistency, syllabus coverage, and arithmetic (especially all marks/EV calculations).
2. **Explain the material to the user one thing at a time, in simple Hindi** (retaining English exam terms), starting with the exam pattern and OMR rules, then subject by subject. Do not dump everything at once. Ask the user which subject to explain next, or proceed in the order: Pattern → OMR → Rajasthan GK → Science → Maths → Reasoning → Hindi → English → Computer → Public Health → Current Affairs → Mocks.
3. **Flag every error you find** with file + line + correction. Do not silently fix and pretend it was always right.
4. **Do not invent** facts, PYQs, weightage, or sources. If something cannot be verified from the files or the official extract named below, say so.

## Verified facts (the ground truth — check everything against these)

- **Pattern (VERIFIED from the official notification extract, Adv. 08/2026, pp.15–22, RajKaj Ref No. 22979471):** 120 questions, 240 marks, 2 hours 30 minutes, all questions MCQ with equal marks (2 each). Negative marking: **one-third (1/3) of the question's marks per wrong answer = −2/3 (−0.667)**. Five options A–E; E = question deliberately not attempted. **Blank (no circle darkened) = also −2/3** (Rule 3: "one third (1/3) part of the marks of question shall be deducted"). **More than 10% blanks = disqualified** (Rule 5: >12 of 120 blanks = disqualified; ≤12 blanks = −2/3 each). Blue ball-point pen only, one circle per question mandatory, **+10 extra minutes after the paper for OMR verification**.
- **Exam dates:** originally 23–25 Oct 2026; revised to **1–3 Dec 2026 (tentative)**, two shifts/day, 38 districts — RSSB press notes 28 Sep 2026 and 14 Oct 2026. Application window 24 Jun–23 Jul 2026 (closed).
- **Qualifying marks: 40% (96/240), 35% (84/240) for SC/ST — REPORTED, not verified from the official extract.** Score valid 3 years (reported).
- **2022 cycle (held 4, 5, 11 Feb 2023) and 2024 cycle (held 22–24 Oct 2024): 150 questions, 300 marks, 3 hours, NO negative marking.** Never mix these patterns with 2026. 2024 date conflict resolved: no exam on 25/26 Oct 2024. 2024 keys: primary 5 Dec 2024, final 18 Feb 2025. 2022 key: primary 31 Mar 2023, final with result 17 May 2023.
- **Official scheme gives NO per-subject question split.** The split used for planning (Raj GK & Admin 50, Geo India 10, Science 15, Reasoning/Maths 15, Hindi+English 15, Computer 5, CA & Public Health 10 = 120) is **reported/derived only** (Adda247/Testbook), never RSSB weightage.
- **Syllabus:** 13 heads, verified line-by-line against the official extract (see `00_Official_Syllabus_Verification.md`). Graduation-only topics — Trigonometry, Algebra/quadratic equations, Logarithms, Internet/E-mail/Cyber-security/AI — are **NOT** in the 12th-level syllabus.
- **RSSB live-site check FAILED** 11 Nov 2026, 13:49–14:00 IST: rssb.rajasthan.gov.in timed out repeatedly (not a CAPTCHA/block). Nothing in this repo depends on the live site; verification rests on the uploaded official extract (SHA-256 below).

## Source for the official extract

The user uploaded `CET_Syllabus__12th_Level__2026.pdf` (Adv. 08/2026, pp.15–22). SHA-256: `9010141c9258b6a4c6414a742ef0b0fb9b4e03793140d9fbbad96946988c4a48`. The PDF itself is **not** in this repo (binary; see `BINARY_FILES_EXCLUDED.md`). Its full content is reproduced and cross-checked in `00_Official_Syllabus_Verification.md`.

## File map

| File | What it is |
|---|---|
| `00_Official_Syllabus_Verification.md` | Cross-check of every syllabus head + OMR rules vs the official extract |
| `01_Official_Syllabus_and_Pattern.md` | Full syllabus (13 heads, hierarchical), pattern, what changed vs 2024 |
| `02_Exam_Pattern_and_Marking_Strategy.md` | EV maths, OMR rules, 150-min time plan, worked examples |
| `INDEX.md` | File map, counts, per-subject coverage checklist (official subtopic → covered Y/N) |
| `notes_hindi_english.md` | Master notes, all 13 areas, Hindi+English mix (767 lines) |
| `notes/01_…_13_*.md` | Per-subject notes (13 files) |
| `question_bank.csv` | 300 original MCQs (5 options, answer, explanation, topic, difficulty, provenance) |
| `question_bank/*.csv` | Per-subject question banks (14 files; area 8 split into Maths + Reasoning) |
| `research/pyq/pyq_inventory.md` | 2022 + 2024 paper inventory (12 shifts), gaps |
| `research/pyq/pyq_dataset.csv` | 139 classified PYQs (sample only — 7.7% of 1,800; never extrapolate) |
| `research/pyq/pyq_analysis.md` | Per-subject PYQ analysis + coverage checklist |
| `mock_papers.md` | 3 full mock papers × 120Q = 360 unique questions, keys + explanations. ALL labelled PREDICTED/GENERATED, never PYQs |
| `study_plan_20day.md` | 20-day plan, 12 Nov–1 Dec 2026, 5–6 hrs/day |
| `performance_tracker.csv` | 13-subject tracker + mock log; Score = (Correct×2) − (Incorrect×2/3) − (Blank×2/3), E = 0 |
| `gen.py`, `gen_qb.py`, `raj_pool.py` | Generator scripts (reproducibility) |

## Corrections already made during the build (audit these especially)

1. **Blank penalty:** first written as −1/3 in mock/plan/tracker files; corrected to **−2/3** (1/3 of the question's 2 marks, Rule 3). Worked example corrected: 70C/30W/20E = 120.0; same with 20 blanks = 106.7 **and disqualified**.
2. **Maths out-of-syllabus:** 3 questions on Algebra (x+1/x) and Trigonometry (sin²+cos², tan45+sin30) were **removed** and replaced with in-syllabus LCM/HCF, Ratio, Cylinder Volume. Notes §A8 rewritten the same way.
3. **Computer out-of-syllabus:** 10 questions (WWW, SMTP, Binary, LAN, Phishing, Firewall, e-Mitra, UPI, Jan Aadhaar) are **retagged "EXTRA — not in 2026 12th syllabus"** and kept only as low-priority general awareness (the 2024 paper did ask HTTP). Notes §11.2/11.3 carry the same EXTRA label.
4. **150Q error:** several websites show 150Q/300 marks for 2026 — that is the **2024 pattern**, wrong for 2026. This repo uses 120Q/240 throughout.
5. **2024 dates:** "23–26 Oct 2024" listings are stale; the exam was 22–24 Oct 2024.

## Known gaps and flags (do not fill by invention)

- PYQ classification covers only **139 of 1,800** questions; Q31–150 of every shift unclassified; 2024 P5/P6 (24 Oct) not classified; no official RSSB key PDF was downloaded (2024 answers via ShikshaNagari "as per official key", 2023 via Examzy unofficial key).
- **Public Health has ZERO PYQ evidence** (new 2026 head) — covered from syllabus + national programmes only.
- **Current Affairs after 11 Nov 2026** is not in this pack — needs a pre-exam update.
- Flagged ambiguities (kept, not resolved by guessing): district count after 2023–24 reorganisation; Rajya Pashu Chinkara vs Unt (2014); Jaisamand "Asia's largest artificial lake" (source-dependent); Panchayat women-reservation % ("verify current"); Rajasthan state animal dual listing; largest port by cargo vs containers (wording-dependent).
- Two mock-paper explanations flag ambiguities deliberately (see mock file caveats).
- EV maths: random guess (p=0.25) EV = 0.00; 1 option eliminated (p=1/3) EV = +0.222; 2 eliminated (p=0.5) EV = +0.667; certain EV ≈ +2.00; blank EV = −0.667. Check the arithmetic.
- The notes' Current Affairs items are web-verified events Dec 2025–Nov 2026 only; re-verify any event you repeat to the user.

## What the user wants from the audit

The user (preparing from 11 Nov 2026, 5–6 hrs/day, 20 days left) asked that this work be put on GitHub **so ChatGPT can audit it and explain each thing one by one**. Explain in **simple Hindi** with English exam terms retained. Start with the pattern and OMR rules — those decide the score — then go subject by subject. Keep each explanation short, check understanding, and point to the exact file/line for anything the user wants to read themselves.
