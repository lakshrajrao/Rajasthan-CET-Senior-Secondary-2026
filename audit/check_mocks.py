#!/usr/bin/env python3
"""Mock-paper structural audit: per paper, count questions (1-120), parse
answer-key tables, parse explanations, cross-check key vs explanation,
check option counts, duplicate stems, and answer distribution.
Writes findings to stdout and to audit/mock_audit_report.txt."""
import re, os
from collections import Counter

BASE = os.path.expanduser("~/workspace/cet-2026-upload")
txt = open(os.path.join(BASE, "mock_papers.md"), encoding="utf-8").read()
out = []
def note(k, m): out.append(f"[{k}] {m}")

papers = re.split(r"(?m)^# PAPER ([123]) ", txt)
# papers[0] preamble; then n, body alternating
for i in range(1, len(papers) - 1, 2):
    n = papers[i]; body = papers[i + 1]
    qsec = re.search(r"## Questions\n(.*?)\n## Answer Key\n", body, re.S)
    ksec = re.search(r"## Answer Key\n(.*?)\n## Brief Explanations", body, re.S)
    esec = re.search(r"## Brief Explanations.*?\n(.*)$", body, re.S)
    note("INFO", f"--- PAPER {n} ---")
    if not (qsec and ksec and esec):
        note("FAIL", f"Paper {n}: missing section(s) q={bool(qsec)} k={bool(ksec)} e={bool(esec)}")
        continue
    qtext, ktext, etext = qsec.group(1), ksec.group(1), esec.group(1)
    # questions
    qheads = re.findall(r"(?m)^\*\*Q(\d+)\.\s*\[([^\]]+)\]\s*(.+?)$", qtext)
    qnums = [int(x[0]) for x in qheads]
    note("INFO" if len(qheads) == 120 and qnums == list(range(1, 121)) else "FAIL",
         f"Paper {n}: questions = {len(qheads)}, numbering 1..120 sequential: {qnums == list(range(1, 121))}" +
         ("" if qnums == list(range(1, 121)) else f" (missing {sorted(set(range(1,121))-set(qnums))[:10]}, extra {sorted(set(qnums)-set(range(1,121)))[:10]})"))
    # options per question: count (A)..(E) blocks between Q heads
    qblocks = re.split(r"(?m)^\*\*Q\d+\.\s*\[[^\]]+\]", qtext)[1:]
    opt_bad = []
    for j, b in enumerate(qblocks, 1):
        opts = re.findall(r"^\s*\(([A-E])\)", b, re.M)
        if opts != ["A", "B", "C", "D", "E"]:
            opt_bad.append((j, opts))
    note("FAIL" if opt_bad else "PASS", f"Paper {n}: questions without exactly A-E options: {len(opt_bad)} {opt_bad[:5]}")
    # tags / difficulty
    tags = Counter(x[1].split("|")[0].strip() for x in qheads)
    diffs = Counter(x[1].split("|")[-1].strip() for x in qheads)
    note("INFO", f"Paper {n}: subject tags = {dict(tags)}")
    note("INFO", f"Paper {n}: difficulty = {dict(diffs)}")
    # duplicate stems within paper
    stems = [re.sub(r"\s+", " ", x[2]).strip().lower() for x in qheads]
    dups = [t for t, c in Counter(stems).items() if c > 1]
    note("FAIL" if dups else "PASS", f"Paper {n}: duplicate stems = {len(dups)} {dups[:3]}")
    # answer key table
    pairs = re.findall(r"\|\s*(\d+)\s*\|\s*\*\*([A-E])\*\*", ktext)
    key = {int(a): b for a, b in pairs}
    note("INFO" if len(key) == 120 and sorted(key) == list(range(1, 121)) else "FAIL",
         f"Paper {n}: key entries = {len(key)}, covers 1..120: {sorted(key) == list(range(1, 121))}")
    kdist = Counter(key.values())
    note("INFO", f"Paper {n}: key distribution = {dict(sorted(kdist.items()))}")
    # explanations
    expl = re.findall(r"(?m)^\*\*Q(\d+)\.\s*Answer\s+([A-E])\*\*\s*—\s*(.+)$", etext)
    edict = {int(a): (b, c) for a, b, c in expl}
    note("INFO" if len(edict) == 120 and sorted(edict) == list(range(1, 121)) else "FAIL",
         f"Paper {n}: explanations = {len(edict)}, covers 1..120: {sorted(edict) == list(range(1, 121))}")
    # key vs explanation mismatch
    mism = [(q, key[q], edict[q][0]) for q in range(1, 121) if q in key and q in edict and key[q] != edict[q][0]]
    note("FAIL" if mism else "PASS", f"Paper {n}: key-vs-explanation mismatches = {len(mism)} {mism[:10]}")
    # explanation vs option text: does the keyed option exist? (spot: explanation letter must be A-D)
    # scoring arithmetic sanity: max score 240
    note("INFO", f"Paper {n}: max score = 120 x 2 = 240; key dist sums to {sum(kdist.values())}")

# cross-paper duplicate stems
allstems = []
for i in range(1, len(papers) - 1, 2):
    body = papers[i + 1]
    qsec = re.search(r"## Questions\n(.*?)\n## Answer Key\n", body, re.S)
    heads = re.findall(r"(?m)^\*\*Q(\d+)\.\s*\[[^\]]+\]\s*(.+?)$", qsec.group(1))
    allstems += [re.sub(r"\s+", " ", h[1]).strip().lower() for h in heads]
xd = [t for t, c in Counter(allstems).items() if c > 1]
note("FAIL" if xd else "PASS", f"ALL PAPERS: duplicate stems across papers = {len(xd)}")
for t in xd[:10]:
    note("DETAIL", f"  dup stem: {t[:160]}")

print("\n".join(out))
open(os.path.expanduser("~/workspace/cet-2026/audit/mock_audit_report.txt"), "w", encoding="utf-8").write("\n".join(out) + "\n")
