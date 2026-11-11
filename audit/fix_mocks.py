#!/usr/bin/env python3
"""Apply mock-paper audit corrections (11 Nov 2026 final QC).
Splits mock_papers.md by paper, applies scoped replacements with assertions.
Wrong keys: P1 Q114, P2 Q47, P2 Q109, P3 Q4 (key B->A), P3 Q100.
Explanations rewritten: P1 Q13/Q50/Q60, P2 Q16/Q75/Q52/Q51/Q81/Q87/Q89, P3 Q50/Q57/Q85.
Ambiguity: P1 Q10/Q81, P2 Q46, P3 Q88. EXTRA tags: P1 Q52/Q56, P3 Q116.
Minor wording: P1 Q55/Q74/Q86/Q117, P2 Q7/Q50/Q77/Q100/Q37, P3 Q17/Q22 (+ '1 years' x3)."""
import re, os

BASE = os.path.expanduser("~/workspace/cet-2026-upload")
fp = os.path.join(BASE, "mock_papers.md")
txt = open(fp, encoding="utf-8").read()
parts = re.split(r"(?m)^(#{1,3}.*(?:mock\s*)?paper\s*[123IV]+.*)$", txt)
# Simpler: split on the three '# PAPER N' headings, keeping headings.
chunks = re.split(r"(?m)(^# PAPER [123] —.*$)", txt)
# chunks: [preamble, head1, body1, head2, body2, head3, body3]
assert len(chunks) == 7, f"unexpected split: {len(chunks)}"
pre, h1, b1, h2, b2, h3, b3 = chunks
applied = []

def fix(body, old, new, count=1, label=""):
    n = body.count(old)
    assert n == count, f"{label}: expected {count}x {old[:80]!r}, found {n}x"
    return body.replace(old, new)

# ---------------- PAPER 1 ----------------
# A1 Q114 duplicate options: (B) Bikaner -> Jodhpur (scoped to Q114 block)
m = re.search(r"(\*\*Q114\..*?)(?=\n\*\*Q115\.|\n## Answer Key)", b1, re.S)
assert m, "P1 Q114 block not found"
blk = m.group(1)
assert blk.count("(B) Bikaner") == 1
blk = blk.replace("(B) Bikaner", "(B) Jodhpur")
b1 = b1[:m.start()] + blk + b1[m.end():]
applied.append("P1 Q114: option (B) Bikaner -> Jodhpur (duplicate options fixed)")
# C1 Q10 stem
b1 = fix(b1, "'जो पढ़ेगा, वह सफल होगा।' — सर्वनाम है —",
        "'जो पढ़ेगा, वह सफल होगा।' — 'जो' किस प्रकार का सर्वनाम है? —", label="P1 Q10")
applied.append("P1 Q10: stem reworded so only (D) जो is uniquely correct")
# C2 Q81 stem + option
b1 = fix(b1, "Which is the highest peak in India? / भारत की सबसे ऊँची चोटी है —",
        "Which is the highest peak located within India's undisputed territory? / भारत की निर्विवाद सीमा के भीतर सबसे ऊँची चोटी है —", label="P1 Q81 stem")
b1 = fix(b1, "(B) Kangchenjunga (K2 is in PoK, claimed)",
        "(B) Kangchenjunga (8,586 m, Sikkim)", label="P1 Q81 opt")
applied.append("P1 Q81: 'highest peak in India' qualified (K2/PoK ambiguity removed)")
# D1 Q52 EXTRA tag
b1 = fix(b1, "**Q52. [Computer | Easy]** The full form of WWW is —",
        "**Q52. [Computer | Easy] [EXTRA — Internet topic, NOT in 2026 12th syllabus; PYQ-style awareness only]** The full form of WWW is —", label="P1 Q52")
b1 = fix(b1, "**Q52. Answer D** — WWW — World Wide Web (Tim Berners-Lee, 1989).",
        "**Q52. Answer D** — WWW — World Wide Web (Tim Berners-Lee, 1989). [EXTRA topic — see header tag.]", label="P1 Q52 expl")
# D2 Q56 EXTRA tag
b1 = fix(b1, "**Q56. [Computer | Easy]** The full form of E-mail is —",
        "**Q56. [Computer | Easy] [EXTRA — E-mail topic, NOT in 2026 12th syllabus; PYQ-style awareness only]** The full form of E-mail is —", label="P1 Q56")
b1 = fix(b1, "**Q56. Answer A** — E-mail — Electronic Mail.",
        "**Q56. Answer A** — E-mail — Electronic Mail. [EXTRA topic — see header tag.]", label="P1 Q56 expl")
applied.append("P1 Q52/Q56: tagged EXTRA (Internet/E-mail out of 12th syllabus)")
# B1 Q13 explanation
b1 = fix(b1, "**Q13. Answer C** — Built by Anaji Chauhan (Arnoraj); Daulat Bagh by Jahangir",
        "**Q13. Answer C** — Ana Sagar Lake is in Ajmer (built by Anaji/Arnoraja Chauhan; Daulat Bagh added by Jahangir).", label="P1 Q13")
# B2 Q50 explanation
b1 = fix(b1, "**Q50. Answer A** — Living fort; golden sandstone; UNESCO Hill Forts",
        "**Q50. Answer A** — Jaisalmer Fort was founded by Rawal Jaisal in 1156; a living fort of golden sandstone, among the UNESCO Hill Forts of Rajasthan.", label="P1 Q50")
# B3 Q60 explanation
b1 = fix(b1, "**Q60. Answer A** — Second-longest wall in world after Great Wall (~36 km); birthplace of Maharana Pratap",
        "**Q60. Answer A** — Kumbhalgarh Fort was built by Maharana Kumbha in the 15th century (c. 1443–1458); its ~36 km wall is commonly described as the second-longest in the world after the Great Wall; Maharana Pratap was born there (1540).", label="P1 Q60")
applied.append("P1 Q13/Q50/Q60: copy-pasted explanations rewritten to justify the key")
# F2 P1 Q86 option, Q117 option, Q55 expl, Q74 expl
b1 = fix(b1, "   (B) The (only)", "   (B) The", label="P1 Q86")
b1 = fix(b1, "   (C) She-lion (not standard)", "   (C) She-lion", label="P1 Q117")
b1 = fix(b1, "**Q55. Answer B** — Chiranjeevi (2021) — ₹25 lakh cover; renamed Mukhyamantri Ayushman Arogya Yojana (2024). Verify current name/limit.",
        "**Q55. Answer B** — Chiranjeevi (2021) — cover raised to ₹25 lakh per family per year (2023); renamed Mukhyamantri Ayushman Arogya Yojana (2024). (Current limit — re-check before the exam; see audit register.)", label="P1 Q55")
b1 = fix(b1, "**Q74. Answer B** — Jaisalmer — largest by area (~38,401 sq km); Dholpur smallest (before 2023 changes).",
        "**Q74. Answer B** — Jaisalmer — largest by area (~38,401 sq km); Dholpur smallest (33 districts after the Dec 2024 reorganisation — re-check the current list before the exam).", label="P1 Q74")
applied.append("P1 Q55/Q74/Q86/Q117: wording/hedge fixes")

# ---------------- PAPER 2 ----------------
# A2 Q47: option C 22 -> 22.5 + explanation
m = re.search(r"(\*\*Q47\..*?)(?=\n\*\*Q48\.)", b2, re.S)
assert m, "P2 Q47 block not found"
blk = m.group(1)
assert blk.count("(C) 22\n") == 1
blk = blk.replace("(C) 22\n", "(C) 22.5\n")
b2 = b2[:m.start()] + blk + b2[m.end():]
b2 = fix(b2, "**Q47. Answer C** — Average = (18+27)/2 = 22.",
        "**Q47. Answer C** — Average = (18+27)/2 = 45/2 = 22.5.", label="P2 Q47")
applied.append("P2 Q47: average 22 -> 22.5 (option + explanation; key C unchanged)")
# A3 Q109: option B 37 -> 37.5 + explanation
m = re.search(r"(\*\*Q109\..*?)(?=\n\*\*Q110\.)", b2, re.S)
assert m, "P2 Q109 block not found"
blk = m.group(1)
assert blk.count("(B) 37\n") == 1
blk = blk.replace("(B) 37\n", "(B) 37.5\n")
b2 = b2[:m.start()] + blk + b2[m.end():]
b2 = fix(b2, "**Q109. Answer B** — Average = (30+45)/2 = 37.",
        "**Q109. Answer B** — Average = (30+45)/2 = 75/2 = 37.5.", label="P2 Q109")
applied.append("P2 Q109: average 37 -> 37.5 (option + explanation; key B unchanged)")
# C3 Q46: option C -> unrelated word
b2 = fix(b2, "   (C) झूठ (synonym of असत्य, but standard antonym is असत्य)",
        "   (C) सुंदर", label="P2 Q46")
applied.append("P2 Q46: option (C) replaced — झूठ was a second valid antonym of सत्य")
# B4 Q16, B5 Q75, B6 Q52, B7 Q51, B8 Q81, B9 Q87, B13 Q89 explanations
b2 = fix(b2, "**Q16. Answer B** — Battle of Khanwa 1527 vs Babur; united Rajput confederacy",
        "**Q16. Answer B** — Rana Sanga ruled Mewar 1508–1528; he fought Babur at Khanwa (1527) leading a Rajput confederacy.", label="P2 Q16")
b2 = fix(b2, "**Q75. Answer B** — Founded Udaipur 1559; shifted capital from Chittorgarh after 1567 siege by Akbar",
        "**Q75. Answer B** — Udai Singh II ruled Mewar 1540–1572; he founded Udaipur (1559) and shifted the capital from Chittorgarh after Akbar's 1567–68 siege.", label="P2 Q75")
b2 = fix(b2, "**Q52. Answer A** — Sacred lake; Brahma temple nearby; Pushkar Fair (Kartik Purnima)",
        "**Q52. Answer A** — Pushkar Lake is in Ajmer district; sacred lake with the Brahma temple nearby and the Kartik Purnima Pushkar Fair.", label="P2 Q52")
b2 = fix(b2, "**Q51. Answer C** — Flows through Banswara/Dungarpur; Mahi Bajaj Sagar Dam",
        "**Q51. Answer C** — The Mahi flows through MP, Rajasthan and Gujarat and empties into the Gulf of Khambhat (an inlet of the Arabian Sea) — hence 'Gulf of Khambhat', not 'Arabian Sea directly'.", label="P2 Q51")
b2 = fix(b2, "**Q81. Answer A** — Flows through Gujarat; short course in Rajasthan",
        "**Q81. Answer A** — The Sabarmati (short course in Rajasthan, then Gujarat) empties into the Gulf of Khambhat — hence 'Gulf of Khambhat', not 'Arabian Sea directly'.", label="P2 Q81")
b2 = fix(b2, "**Q87. Answer B** — Flows through Jhalawar-Kota; Jhalrapatan",
        "**Q87. Answer B** — The Kali Sindh (origin Dewas, MP; flows through Jhalawar-Kota) joins the Chambal in Rajasthan.", label="P2 Q87")
b2 = fix(b2, "**Q89. Answer D** — Chittorgarh Fort is in Chittorgarh. Largest fort in India; Vijay Stambh; Jauhar of Rani Padmini (1303) & Rani Karnavati (1535)",
        "**Q89. Answer D** — Chittorgarh Fort is in Chittorgarh district; India's largest fort, site of the Vijay Stambh; jauhar of 1535 under Rani Karnavati. (The 1303 'Rani Padmini' story is from Jayasi's Padmavat legend, not verified history.)", label="P2 Q89")
applied.append("P2 Q16/Q75/Q52/Q51/Q81/Q87/Q89: explanations rewritten (copy-paste / missing terminus / Padmini legend)")
# F2 P2 Q7 stem, Q100 stem, Q37 option
b2 = fix(b2, "The 'Bhakti' — no: Bhakra Dam is on which river?",
        "Bhakra Dam is on which river?", label="P2 Q7")
b2 = fix(b2, "If CAT = 24 (C=3,A=1,T=20; sum ×? — CAT letters sum=24), then DOG = ? (D=4,O=15,G=7)",
        "If CAT = 24 (C=3,A=1,T=20; letters sum to 24), then DOG = ? (D=4,O=15,G=7)", label="P2 Q100")
b2 = fix(b2, "   (C) Udaipur (Salumbar)",
        "   (C) Salumbar (formerly Udaipur district)", label="P2 Q37")
applied.append("P2 Q7/Q100/Q37: garbled stems and confusing district option fixed")

# ---------------- PAPER 3 ----------------
# A4 Q4: stem, option B, key table, explanation
b3 = fix(b3, "The 'Silk Route' — no: India's largest port by cargo is —",
        "India's largest major port by cargo handled is —", label="P3 Q4 stem")
b3 = fix(b3, "   (B) Jawaharlal Nehru Port (Nhava Sheva) / Deendayal (Kandla) — varies by year",
        "   (B) Jawaharlal Nehru Port (Nhava Sheva)", label="P3 Q4 opt")
# key table (scoped to Paper 3 key section)
km = re.search(r"(## Answer Key\n.*?)(## Brief Explanations)", b3, re.S)
assert km, "P3 key section not found"
ksec = km.group(1)
assert ksec.count("| 4 | **B** |") == 1, f"P3 key Q4 pattern count: {ksec.count('| 4 | **B** |')}"
ksec = ksec.replace("| 4 | **B** |", "| 4 | **A** |")
b3 = b3[:km.start(1)] + ksec + b3[km.end(1):]
b3 = fix(b3, "**Q4. Answer B** — By cargo volume, Deendayal (Kandla) and Paradip often lead among major ports; JNPT leads in container traffic. Wording matters — container vs total cargo. Treat JNPT as container leader.",
        "**Q4. Answer A** — Paradip is the largest major port by cargo: FY 2024-25 Paradip 150.41 MMT vs Deendayal (Kandla) 150.16 MMT; JNPT (92.12 MMT) leads only in container traffic. (Private port Mundra handles more overall, so the question is about major ports.)", label="P3 Q4 expl")
applied.append("P3 Q4: key B->A (Paradip, largest major port by cargo); stem/option/explanation rewritten")
# A5 Q100: option A 62 -> 62.5 + explanation
m = re.search(r"(\*\*Q100\..*?)(?=\n\*\*Q101\.)", b3, re.S)
assert m, "P3 Q100 block not found"
blk = m.group(1)
assert blk.count("(A) 62\n") == 1
blk = blk.replace("(A) 62\n", "(A) 62.5\n")
b3 = b3[:m.start()] + blk + b3[m.end():]
b3 = fix(b3, "**Q100. Answer A** — Average = (50+75)/2 = 62.",
        "**Q100. Answer A** — Average = (50+75)/2 = 125/2 = 62.5.", label="P3 Q100")
applied.append("P3 Q100: average 62 -> 62.5 (option + explanation; key A unchanged)")
# C4 Q88 option D qualifier
b3 = fix(b3, "   (D) Longest river of Rajasthan; Kota, Rawatbhata atomic power, Chambal ravines",
        "   (D) Longest river (by total course) of Rajasthan; Kota, Rawatbhata atomic power, Chambal ravines", label="P3 Q88")
b3 = fix(b3, "**Q88. Answer D** — Longest river of Rajasthan; Kota, Rawatbhata atomic power, Chambal ravines",
        "**Q88. Answer D** — Chambal is the longest river (by total course, ~1,024 km) associated with Rajasthan; Kota, Rawatbhata atomic power, Chambal ravines. (Banas, ~512 km, is the longest river flowing *entirely within* Rajasthan — see Q7.)", label="P3 Q88 expl")
applied.append("P3 Q88: Chambal 'longest river' qualified (vs Q7 Banas)")
# D3 Q116 EXTRA tag
b3 = fix(b3, "**Q116. [Computer | Easy]** An email address must contain —",
        "**Q116. [Computer | Easy] [EXTRA — E-mail topic, NOT in 2026 12th syllabus; PYQ-style awareness only]** An email address must contain —", label="P3 Q116")
b3 = fix(b3, "**Q116. Answer B** — @ separates username and domain (e.g., name@example.com).",
        "**Q116. Answer B** — @ separates username and domain (e.g., name@example.com). [EXTRA topic — see header tag.]", label="P3 Q116 expl")
applied.append("P3 Q116: tagged EXTRA (E-mail out of 12th syllabus)")
# B10 Q50, B11 Q57, B12 Q85 explanations
b3 = fix(b3, "**Q50. Answer B** — Never conquered; Anup Mahal; not built on a hill",
        "**Q50. Answer B** — Junagarh Fort was built by Raja Rai Singh of Bikaner, 1589–94; a ground-level fort (not on a hill), never conquered; Anup Mahal inside.", label="P3 Q50")
b3 = fix(b3, "**Q57. Answer D** — Built Ganga Canal (1927, from Sutlej); represented India at Versailles 1919",
        "**Q57. Answer D** — Maharaja Ganga Singh ruled Bikaner 1888–1943; built the Ganga Canal (1927, from the Sutlej) and represented India at Versailles (1919).", label="P3 Q57")
b3 = fix(b3, "**Q85. Answer A** — Largest fort in India; Vijay Stambh; Jauhar of Rani Padmini (1303) & Rani Karnavati (1535)",
        "**Q85. Answer A** — Largest fort in India (~700 acres); Vijay Stambh; jauhar of 1303 (Alauddin Khalji's siege) and of 1535 under Rani Karnavati. ('Rani Padmini' is the Padmavat legend, not verified history.)", label="P3 Q85")
applied.append("P3 Q50/Q57/Q85: explanations rewritten (missing builder / copy-paste / Padmini legend)")
# F2 P3 Q17 stem — numbered (1) because P3 Q93 has the identical stem (see below)
b3 = fix(b3, "Choose the correctly spelt word — (2):",
        "Choose the correctly spelt word — (1):", label="P3 Q17")
assert b3.count("**Q93. [English: Spelling | Medium]** Choose the correctly spelt word:") == 1
b3 = b3.replace("**Q93. [English: Spelling | Medium]** Choose the correctly spelt word:",
                "**Q93. [English: Spelling | Medium]** Choose the correctly spelt word — (2):")
applied.append("P3 Q17: stray '(2)' removed")

# ---------------- global: '1 years' -> '1 year' (P2 Q50, Q77; P3 Q22) ----------------
for body_name in ["b1", "b2", "b3"]:
    pass
combined = pre + h1 + b1 + h2 + b2 + h3 + b3
n = combined.count("for 1 years is")
assert n == 3, f"'for 1 years is' count: {n}"
combined = combined.replace("for 1 years is", "for 1 year is")
applied.append("'for 1 years' -> 'for 1 year' (3 occurrences)")

# ---------------- header: audit note ----------------
old_hdr = "> **How to use:** Sit each paper in one 150-minute sitting, use a printed OMR-style sheet, darken **E** for every question you deliberately skip, **never leave a circle blank**, then score with Score = (Correct×2) − (Incorrect×2/3) − (Blank×2/3). E responses count as neither correct nor incorrect. Log the result in `performance_tracker.csv`."
new_hdr = old_hdr + "\n>\n> **Audit 11 Nov 2026 (final QC):** 5 wrong keys, 13 wrong explanations, 4 ambiguous wordings and 3 out-of-syllabus questions were found and corrected in this file — see `AUDIT_CORRECTION_REGISTER.md`. Questions tagged **[EXTRA]** are Graduation-level / PYQ-awareness only, not 12th-level syllabus. Note: ~39 mock questions test the same facts as the 300-MCQ question bank — kept deliberately as revision overlap (same fact, usually a different angle); the full list is in `audit/mock_audit_findings.md`."
assert combined.count(old_hdr) == 1
combined = combined.replace(old_hdr, new_hdr)
applied.append("Mock header: audit-correction + overlap disclosure added")

open(fp, "w", encoding="utf-8").write(combined)
print(f"Applied {len(applied)} mock-paper correction groups:")
for a in applied:
    print(" -", a)
