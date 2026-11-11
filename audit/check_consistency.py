#!/usr/bin/env python3
"""Automated consistency checks for CET 2026 repo (audit phase, 11 Nov 2026).
Reads ~/workspace/cet-2026-upload and prints a findings report.
No files are modified."""
import csv, json, os, re, sys
from collections import Counter, defaultdict

BASE = os.path.expanduser("~/workspace/cet-2026-upload")
def p(*a): return os.path.join(BASE, *a)
def norm(s): return re.sub(r"\s+", " ", (s or "").strip().lower())

report = []
def note(kind, msg): report.append(f"[{kind}] {msg}")

# ---------- 1. question_bank.csv ----------
qb = list(csv.DictReader(open(p("question_bank.csv"), encoding="utf-8")))
note("INFO", f"question_bank.csv rows = {len(qb)} (expect 300)")
cols = qb[0].keys() if qb else []
note("INFO", f"question_bank.csv columns = {list(cols)}")
ans = Counter(r.get("correct_answer","").strip().upper() for r in qb)
note("INFO", f"question_bank.csv answer distribution = {dict(sorted(ans.items()))}")
bad = [r for r in qb if r.get("correct_answer","").strip().upper() not in "ABCD"]
note("FAIL" if bad else "PASS", f"answers outside A-D: {len(bad)}" + (f" e.g. {bad[0]}" if bad else ""))
missing = [r for r in qb if not all((r.get(c) or "").strip() for c in ["question","option_a","option_b","option_c","option_d","correct_answer"])]
note("FAIL" if missing else "PASS", f"rows missing question/options/answer: {len(missing)}")
ids = [r.get("qid","") for r in qb]
dup_ids = [k for k,v in Counter(ids).items() if v>1]
note("FAIL" if dup_ids else "PASS", f"duplicate IDs in question_bank.csv: {dup_ids}")
qtexts = Counter(norm(r.get("question","")) for r in qb)
dups = [t for t,c in qtexts.items() if c>1]
note("FAIL" if dups else "PASS", f"duplicate question texts in question_bank.csv: {len(dups)}" + (f" e.g. {dups[:2]}" if dups else ""))
# E as an option?
e_opt = [r for r in qb if (r.get("option_e") or "").strip()]
note("INFO", f"rows with an option_e field filled: {len(e_opt)} (E must never be a correct answer option)")
prov = Counter(r.get("source","") for r in qb)
note("INFO", f"provenance values = {dict(prov)}")
# per-subject counts in combined file
subj = Counter(r.get("topic","") for r in qb)
note("INFO", f"combined bank per-subject counts = {dict(sorted(subj.items()))}")

# ---------- 2. per-subject CSVs ----------
total_sub = 0
for fn in sorted(os.listdir(p("question_bank"))):
    rows = list(csv.DictReader(open(p("question_bank",fn), encoding="utf-8")))
    total_sub += len(rows)
    a = Counter(r.get("correct_answer","").strip().upper() for r in rows)
    e_bad = [r for r in rows if r.get("correct_answer","").strip().upper() not in "ABCD"]
    qt = Counter(norm(r.get("question","")) for r in rows)
    d = [t for t,c in qt.items() if c>1]
    extra = [r for r in rows if "EXTRA" in (r.get("syllabus_status","") or r.get("notes","") or "")]
    note("INFO", f"{fn}: {len(rows)} rows, answers {dict(sorted(a.items()))}, E/bad answers {len(e_bad)}, dup texts {len(d)}, EXTRA-tagged {len(extra)}")
note("INFO", f"per-subject CSV total = {total_sub} (expect 300)")
# cross-check: combined vs per-subject question texts
sub_texts = Counter()
for fn in sorted(os.listdir(p("question_bank"))):
    for r in csv.DictReader(open(p("question_bank",fn), encoding="utf-8")):
        sub_texts[norm(r.get("question",""))] += 1
combined_texts = Counter(norm(r.get("question","")) for r in qb)
only_combined = [t for t in combined_texts if t not in sub_texts]
only_sub = [t for t in sub_texts if t not in combined_texts]
note("FAIL" if only_combined or only_sub else "PASS",
     f"combined vs per-subject text mismatch: only-combined {len(only_combined)}, only-subject {len(only_sub)}")
if only_combined: note("DETAIL", f"only-combined sample: {only_combined[:3]}")
if only_sub: note("DETAIL", f"only-subject sample: {only_sub[:3]}")

# ---------- 3. PYQ dataset ----------
pyq = list(csv.DictReader(open(p("research/pyq/pyq_dataset.csv"), encoding="utf-8")))
note("INFO", f"pyq_dataset.csv rows = {len(pyq)} (expect 139)")
note("INFO", f"pyq columns = {list(pyq[0].keys()) if pyq else []}")
note("INFO", f"PYQ per-subject = {dict(sorted(Counter(r.get('Subject','') for r in pyq).items()))}")
note("INFO", f"PYQ per-paper/shift = {dict(sorted(Counter(r.get('Shift','') for r in pyq).items()))}")
note("INFO", f"PYQ difficulty = {dict(sorted(Counter(r.get('Difficulty','') for r in pyq).items()))}")
pyq_ids = [(r.get("Year",""), r.get("Shift",""), r.get("Question_ID","")) for r in pyq]
note("FAIL" if len(set(pyq_ids))!=len(pyq_ids) else "PASS", f"duplicate PYQ IDs: {len(pyq_ids)-len(set(pyq_ids))}")
pyq_q = Counter()  # dataset has no question-text column; classification metadata only
note("INFO", f"duplicate PYQ question texts: {sum(1 for t,c in pyq_q.items() if c>1)}")
# any PYQ claiming full-paper coverage?
inv = open(p("research/pyq/pyq_inventory.md"), encoding="utf-8").read()
note("INFO", f"inventory mentions 'full paper' claim check: {'full-paper' in inv.lower() or 'complete paper' in inv.lower()}")

# ---------- 4. mock papers ----------
mock = open(p("mock_papers.md"), encoding="utf-8").read()
# count question headings: lines starting with **Q or 'Q1.' patterns
qheads = re.findall(r"(?m)^#{0,3}\s*(?:\*\*)?Q(\d+)[\.\):]", mock)
note("INFO", f"mock_papers.md Q-heading matches = {len(qheads)} (expect 360)")
papers = re.split(r"(?m)^#{1,3}\s+.*(?:Paper|MOCK).*(\d)", mock)
# simpler: find paper sections
paper_heads = re.findall(r"(?mi)^(#{1,3}.*(?:mock\s*)?paper\s*[123IV]+.*)$", mock)
note("INFO", f"mock paper section headings found: {paper_heads}")
# answer keys: lines like 'Q1. B' in key sections
key_lines = re.findall(r"(?m)^\s*Q?(\d+)[\.\)]\s*([A-E])\b", mock)
note("INFO", f"answer-key style lines found = {len(key_lines)}")
# count per-paper by splitting on 'Paper 1/2/3' headings
parts = re.split(r"(?mi)^#{1,3}\s+.*paper\s*([123])\b", mock)
# parts[0] preamble, then alternating number, body
for i in range(1, len(parts)-1, 2):
    body = parts[i+1]
    qs = re.findall(r"(?m)^#{0,3}\s*(?:\*\*)?Q(\d+)[\.\):]", body)
    note("INFO", f"Mock Paper {parts[i]}: Q headings = {len(qs)}, max Q no = {max((int(x) for x in qs), default=0)}")
# duplicate question texts across mocks — question lines only (tag bracket after Q no.);
# explanation lines ('**Q12. Answer A** — ...') are excluded so identical explanation
# fragments are not misreported as duplicate questions.
mq = re.findall(r"(?m)^\*\*Q\d+\.\s*\[.*?\]\s*(.+)$", mock)
mqn = [norm(x) for x in mq if x.strip()]
mqc = Counter(mqn)
mqd = [t for t,c in mqc.items() if c>1]
note("FAIL" if mqd else "PASS", f"duplicate mock question stems: {len(mqd)}" + (f" e.g. {mqd[:2]}" if mqd else ""))
# overlap between mock stems and question bank stems
bank_stems = set(norm(r.get("question","")) for r in qb)
overlap = [t for t in mqn if t in bank_stems]
note("FAIL" if overlap else "PASS", f"mock stems also in question bank: {len(overlap)}" + (f" e.g. {overlap[:2]}" if overlap else ""))

# ---------- 5. performance_tracker.csv ----------
trk = open(p("performance_tracker.csv"), encoding="utf-8").read()
for pat in ["-1/3", "-0.33", "1/3", "-2/3", "-0.667", "0.667"]:
    n = trk.count(pat)
    if n: note("INFO", f"performance_tracker.csv contains '{pat}' x{n}")
trk_rows = list(csv.DictReader(open(p("performance_tracker.csv"), encoding="utf-8")))
note("INFO", f"performance_tracker.csv rows = {len(trk_rows)}, cols = {list(trk_rows[0].keys()) if trk_rows else []}")

# ---------- 6. stale-pattern / weightage wording scan ----------
scan_files = ["notes_hindi_english.md","01_Official_Syllabus_and_Pattern.md","02_Exam_Pattern_and_Marking_Strategy.md",
              "study_plan_20day.md","mock_papers.md","INDEX.md","README.md","AUDIT_BRIEF_FOR_CHATGPT.md",
              "00_Official_Syllabus_Verification.md"] + [f"notes/{f}" for f in sorted(os.listdir(p("notes")))]
pats = {
  "150 questions": r"150\s*(?:questions|Q\b)",
  "300 marks": r"300\s*marks",
  "no negative marking (2026 context)": r"no negative marking",
  "blank -1/3": r"-1/3|minus 1/3|–1/3",
  "blank -0.33": r"-0\.33",
  "weightage as official?": r"(?:50|15|10|5)\s*(?:questions|marks)\b.{0,40}(?:official|weightage)",
  "official weightage": r"official\s+(?:weightage|distribution|split)",
  "150Q": r"150\s*Q",
}
for fn in scan_files:
    try: txt = open(p(fn), encoding="utf-8").read()
    except FileNotFoundError: note("FAIL", f"missing file {fn}"); continue
    for label, pat in pats.items():
        hits = re.findall(pat, txt, flags=re.I)
        if hits:
            # show line numbers
            lines = [i+1 for i,l in enumerate(txt.splitlines()) if re.search(pat, l, flags=re.I)]
            note("CHECK", f"{fn} :: '{label}' x{len(hits)} lines {lines[:8]}")

print("\n".join(report))
with open(os.path.expanduser("~/workspace/cet-2026/audit/automated_checks_report.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(report) + "\n")
print("\n--- report saved to ~/workspace/cet-2026/audit/automated_checks_report.txt ---")
