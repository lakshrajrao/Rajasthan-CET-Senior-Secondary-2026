#!/usr/bin/env python3
"""Apply audit corrections (11 Nov 2026 final QC) to CET repo text files.
Each replacement asserts the old string exists exactly once per file (or the
stated count). Question-bank and mock-paper corrections are NOT applied here
— they wait for the subagent content audits. Run from anywhere; paths absolute."""
import os

BASE = os.path.expanduser("~/workspace/cet-2026-upload")
applied = []

def fix(path, old, new, count=1):
    fp = os.path.join(BASE, path)
    s = open(fp, encoding="utf-8").read()
    n = s.count(old)
    assert n == count, f"{path}: expected {count}x {old[:70]!r}, found {n}x"
    s = s.replace(old, new)
    open(fp, "w", encoding="utf-8").write(s)
    applied.append(f"{path}: {old[:60]}... -> {new[:60]}...")

# --- 1. File 01: -1/3 -> -2/3 (two places) ---
fix("01_Official_Syllabus_and_Pattern.md",
    "Your pattern (120 questions / 240 marks / 150 minutes / −1/3) is **CONFIRMED CORRECT for 2026**.",
    "Your pattern (120 questions / 240 marks / 150 minutes / −2/3 per wrong answer) is **CONFIRMED CORRECT for 2026**.")
fix("01_Official_Syllabus_and_Pattern.md",
    "2. **Negative marking INTRODUCED (−1/3).**",
    "2. **Negative marking INTRODUCED (−2/3 per wrong answer — 1/3 of the question's 2 marks).**")

# --- 2. File 02: sources line ---
fix("02_Exam_Pattern_and_Marking_Strategy.md",
    "Sources: Adv. 08/2026 notes 1–2 (equal marks; −1/3 per wrong answer); p.22 OMR Rules 1–5 (E rule, blank = −1/3 of question marks, >10% blanks = disqualified, +10 min).",
    "Sources: Adv. 08/2026 notes 1–2 (equal marks; −2/3 per wrong answer = 1/3 of the question's 2 marks); p.22 OMR Rules 1–5 (E rule, blank = −2/3 of question marks, >10% blanks = disqualified, +10 min).")

# --- 3. README.md (upload): -1/3 -> -2/3 ---
fix("README.md",
    "- 2026 pattern is **120Q/240 marks/150 min with −1/3 negative marking**.",
    "- 2026 pattern is **120Q/240 marks/150 min with −2/3 negative marking (1/3 of the question's 2 marks)**.")

# --- 4. PYQ analysis: -1/3 -> -2/3 ---
fix("research/pyq/pyq_analysis.md",
    "**no negative marking → −1/3 per wrong answer**; 4 options (A–D in ShikshaNagari reproductions) → **5 options with E = not attempted, and a blank costs −1/3**;",
    "**no negative marking → −2/3 per wrong answer**; 4 options (A–D in ShikshaNagari reproductions) → **5 options with E = not attempted, and a blank costs −2/3**;")

# --- 5. performance_tracker.csv: two blank-penalty errors ---
fix("performance_tracker.csv",
    '"Example: same paper but 20 blanks instead of E => 120 - 20*0.333 = 113.33 AND 20 blanks > 12, so DISQUALIFIED under Rule 5 (more than 10% blanks)."',
    '"Example: same paper but 20 blanks instead of E => 140 - 20 - 20*0.667 = 106.67 AND 20 blanks > 12, so DISQUALIFIED under Rule 5 (more than 10% blanks)."')
fix("performance_tracker.csv",
    "blank EV = -0.333. Never leave a circle blank.",
    "blank EV = -0.667. Never leave a circle blank.")

# --- 6. Master notes header warning: superseded -> VERIFIED ---
fix("notes_hindi_english.md",
    "> ⚠️ **VERIFY BEFORE EXAM — Pattern discrepancy found (11 Nov 2026):** This pack follows the brief pattern 120Q/240 marks/150 min, which Testbook's summary of Advt 08/2026 also reports for Senior Secondary. BUT the 2024 Senior Secondary paper had **150Q/300 marks/3 hours**, and at least one secondary site (RojgarPulse) reports 150Q/300 for 2026 — it appears to conflate the Graduate-level pattern (150Q/300, 3 hrs) with Senior Secondary. **Check the official PDF on rssb.rajasthan.gov.in before the exam and adjust time strategy (120Q→75 sec/Q; 150Q→72 sec/Q).**",
    "> ✅ **Pattern VERIFIED 11 Nov 2026 (audit correction):** 120Q/240 marks/150 min, +2/−2/3, E=0, blank=−2/3 — confirmed from the user-uploaded official notification extract (Advt 08/2026, pp.15–22, RajKaj 22979471; see `00_Official_Syllabus_Verification.md`). The earlier warning about a possible 150Q pattern is **superseded**: the 2024 paper was 150Q/300/3h with no negative marking, and some secondary sites (e.g. RojgarPulse) wrongly copy that 150Q figure — or the Graduate-level pattern (150Q/300, 3 hrs) — onto 2026 Senior Secondary. Time strategy: 120Q → 75 sec/Q.")

# --- 7. EV line: 33% EV is +0.22, not ~0; attempt threshold is >=1 elimination ---
EV_OLD = "- **Negative-marking maths:** Sirf tab attempt karo jab kam se kam 2 options eliminate kar sako ya confidence ≥50% ho (EV: 50% par +2×0.5 − 0.667×0.5 = +0.667 > 0; 33% par EV ≈ 0; isse kam par E bharo). Bilkul andaza mat lagao."
EV_NEW = "- **Negative-marking maths (AUDIT-CORRECTED 11 Nov 2026):** Attempt karo jab kam se kam **1 option eliminate** kar sako — EV tab bhi positive hai (EV: 50% par +2×0.5 − 0.667×0.5 = **+0.667**; 33% par +2×0.33 − 0.667×0.67 = **+0.22**; sirf 25% (random guess, koi elimination nahi) par EV = 0 — tab E bharo). Bilkul andaza mat lagao; kabhi circle blank mat chhodo (blank EV = −0.667)."
fix("notes_hindi_english.md", EV_OLD, EV_NEW)
fix("notes/13_general_english.md", EV_OLD, EV_NEW)

# --- 8. Railway zones 16 -> 18 (master + Geo India split) ---
fix("notes_hindi_english.md",
    "- **Railway:** 16 zones (2026 tak); pehli rail 1853 Mumbai–Thane.",
    "- **Railway:** **18 zones** (South Coast Railway, Visakhapatnam — 18th zone, operational 1 June 2026, Gazette 4 May 2026); pehli rail 1853 Mumbai–Thane.")
fix("notes/03_geography_india.md",
    "- **Railway:** 16 zones (2026 tak); pehli rail 1853 Mumbai–Thane.",
    "- **Railway:** **18 zones** (South Coast Railway, Visakhapatnam — 18th zone, operational 1 June 2026, Gazette 4 May 2026); pehli rail 1853 Mumbai–Thane.")

# --- 9. Clock coincidence wording (master + Maths split) ---
CLK_OLD = "- **Clock:** Ghadi ki suiyan 1 ghante me 11 baar (lagbhag) milti hain; 12 ghante me **11 baar**;"
CLK_NEW = "- **Clock:** Ghadi ki suiyan **12 ghante me 11 baar** milti hain (lagbhag har 1 ghanta 5.5 minute me ek baar);"
fix("notes_hindi_english.md", CLK_OLD, CLK_NEW)
fix("notes/08_reasoning_mathematics.md", CLK_OLD, CLK_NEW)

# --- 10. INDEX.md: verified answer balance + scoring formula with blank term ---
fix("INDEX.md",
    "| 01 History of Rajasthan | 24 | A 73 / B 71 / C 76 / D 80 overall; E never correct |",
    "| 01 History of Rajasthan | 24 | A 74 / B 72 / C 75 / D 79 overall (audit-verified 11 Nov 2026); E never correct |")
fix("INDEX.md",
    "2. Score with: Score = (Correct×2) − (Incorrect×2/3); E = 0.",
    "2. Score with: Score = (Correct×2) − (Incorrect×2/3) − (Blank×2/3); E = 0.")

# --- 11. Hindi notes §12.6 Ras/Chhand/Alankar: label EXTRA (not in 12th syllabus) ---
fix("notes/12_general_hindi.md",
    "## 12.6 Ras, Chhand, Alankar (short)",
    "## 12.6 Ras, Chhand, Alankar (short) — ⚠️ EXTRA, 2026 12th-level syllabus me NAHI (Graduation-level / general awareness only; priority mat do)")
fix("notes_hindi_english.md",
    "## 12.6 Ras, Chhand, Alankar (short)",
    "## 12.6 Ras, Chhand, Alankar (short) — ⚠️ EXTRA, 2026 12th-level syllabus me NAHI (Graduation-level / general awareness only; priority mat do)")

# --- 12. Study plan: Day 6 'internet' -> EXTRA; checkpoint '10 subject areas' -> 13 heads ---
fix("study_plan_20day.md",
    "| Day 6 — Tue 17 Nov | **Logical Reasoning** — series, coding, odd-one, analogy, direction, calendar | **Computer Knowledge** — CPU/RAM, MS Office, shortcuts, internet, full forms | 60 | 30Q Reasoning | Days 3–5 |",
    "| Day 6 — Tue 17 Nov | **Logical Reasoning** — series, coding, odd-one, analogy, direction, calendar | **Computer Knowledge** — CPU/RAM, MS Office, shortcuts, full forms (internet = EXTRA, 12th syllabus me nahi — low priority) | 60 | 30Q Reasoning | Days 3–5 |")
fix("study_plan_20day.md",
    "- **After Day 7:** all 10 subject areas touched at least once; tracker filled for Days 1–7.",
    "- **After Day 7:** all 13 syllabus heads touched at least once; tracker filled for Days 1–7.")

# --- 13. gen.py: fix the generator so the errors cannot regenerate ---
g = os.path.join(BASE, "gen.py")
s = open(g, encoding="utf-8").read()
gen_fixes = [
    ("**Blank (no circle darkened) = −1/3 mark each if 12 or fewer blanks; MORE THAN 10% blanks (13+ of 120) = DISQUALIFIED** (Adv 08/2026 Rule 5, pp.15–22) • **Blue ball-point pen only** • One circle per question mandatory — darken E if you do not know the answer; **never leave a circle blank** (a blank costs −1/3 and counts toward disqualification, while E costs 0 and a random guess has EV 0.0 — see §12).",
     "**Blank (no circle darkened) = −2/3 mark each if 12 or fewer blanks; MORE THAN 10% blanks (13+ of 120) = DISQUALIFIED** (Adv 08/2026 Rule 5, pp.15–22) • **Blue ball-point pen only** • One circle per question mandatory — darken E if you do not know the answer; **never leave a circle blank** (a blank costs −2/3 and counts toward disqualification, while E costs 0 and a random guess has EV 0.0 — see §12)."),
    ("**Marking: +2 correct, −2/3 wrong, E = 0, blank = −1/3 each (≤12 blanks); 13+ blanks = DISQUALIFIED (Rule 5). Blue ball-point pen only.**",
     "**Marking: +2 correct, −2/3 wrong, E = 0, blank = −2/3 each (≤12 blanks); 13+ blanks = DISQUALIFIED (Rule 5). Blue ball-point pen only.**"),
    ("• **Blank (no circle) = −1/3 each if ≤12 blanks; 13+ blanks (more than 10% of 120) = DISQUALIFIED.**",
     "• **Blank (no circle) = −2/3 each if ≤12 blanks; 13+ blanks (more than 10% of 120) = DISQUALIFIED.**"),
    ("- **NEVER leave a circle blank.** A blank costs −0.333 and counts toward disqualification; E costs 0.",
     "- **NEVER leave a circle blank.** A blank costs −0.667 and counts toward disqualification; E costs 0."),
    ("(blank EV = −0.333, worse than both).",
     "(blank EV = −0.667, worse than both)."),
    ("→ 120 − 20×0.333 = **113.3**, plus disqualification risk if blanks rise to 13+ (here 20 blanks = disqualified outright). **E vs blank is a 6.7-mark swing and a disqualification risk — never blank.**",
     "→ 140 − 20 − 20×0.667 = **106.7**, plus disqualification outright (here 20 blanks = disqualified). **E vs blank is a 13.3-mark swing and a disqualification risk — never blank.**"),
    ('"Example: same paper but 20 blanks instead of E => 120 - 20*0.333 = 113.33 AND 20 blanks > 12, so DISQUALIFIED under Rule 5 (more than 10% blanks)."',
     '"Example: same paper but 20 blanks instead of E => 140 - 20 - 20*0.667 = 106.67 AND 20 blanks > 12, so DISQUALIFIED under Rule 5 (more than 10% blanks)."'),
    ('"OMR RULE: more than 10% blanks (13+ of 120) = DISQUALIFIED. 12 or fewer blanks = -1/3 mark each.',
     '"OMR RULE: more than 10% blanks (13+ of 120) = DISQUALIFIED. 12 or fewer blanks = -2/3 mark each.'),
    ("blank EV = -0.333. Never leave a circle blank.",
     "blank EV = -0.667. Never leave a circle blank."),
]
for old, new in gen_fixes:
    n = s.count(old)
    assert n == 1, f"gen.py: expected 1x {old[:70]!r}, found {n}x"
    s = s.replace(old, new)
    applied.append(f"gen.py: {old[:60]}... -> fixed")
open(g, "w", encoding="utf-8").write(s)

print(f"Applied {len(applied)} corrections:")
for a in applied:
    print(" -", a)
