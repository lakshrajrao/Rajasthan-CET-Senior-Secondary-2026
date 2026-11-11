#!/usr/bin/env python3
"""Apply question-bank audit corrections (11 Nov 2026 final QC).
Edits question_bank.csv AND the matching per-subject CSV in question_bank/.
Both files must stay in sync; the script asserts that at the end.
QB audit: qb_audit_findings.md (agent 7d3a83c9)."""
import csv, os

BASE = os.path.expanduser("~/workspace/cet-2026-upload")
COMBINED = os.path.join(BASE, "question_bank.csv")
SUBJ = {
    "12_GENERAL_HINDI-015": "12_general_hindi.csv",
    "13_GENERAL_ENGLISH-005": "13_general_english.csv",
    "13_GENERAL_ENGLISH-020": "13_general_english.csv",
    "08_REASONING-021": "08_reasoning.csv",
    "08_REASONING-020": "08_reasoning.csv",
    "08_REASONING-024": "08_reasoning.csv",
    "06_ECONOMY_RAJASTHAN-004": "06_economy_rajasthan.csv",
}

FIXES = {
    # 1. Wrong key: Neelkanth is Bahuvrihi, not Karmadharaya. Replace distractor D.
    "12_GENERAL_HINDI-015": {
        "option_d": "Bahuvrihi",
        "explanation": "Neelkanth (neela kanth wala — Shiv) — samas kisi teesre (Shiv) ko darshata hai, isliye Bahuvrihi samas hai. (Dashanan, Lambodar bhi isi prakar Bahuvrihi hain.)",
    },
    # 2. Ambiguous: 'loves himself' matches Egoist; reword stem so Narcissist is unique.
    #    Also removes the unverified '(2024 PYQ)' tag from the stem (bank is generated).
    "13_GENERAL_ENGLISH-005": {
        "question": "'A person who admires himself excessively' — one word kya hai?",
        "explanation": "A person who admires himself excessively — Narcissist. (Egoist = one who loves himself / self-centred; Narcissist = excessive self-admiration.)",
    },
    # 3. Ambiguous/unsolvable: no arrangement given; rewrite as a convention question.
    "08_REASONING-021": {
        "question": "Vritt me kendra ki ore munh karke baithe vyakti ka 'dayein' kis disha me hota hai?",
        "difficulty": "Medium",
    },
    # 4. Ambiguous: 'Textile City of India' also describes Bhilwara; replace with 'Sun City' (Jodhpur).
    "06_ECONOMY_RAJASTHAN-004": {
        "option_b": "Sun City",
    },
    # 5. Minor wording: meta-commentary inside option C.
    "08_REASONING-020": {
        "option_c": "Koi A, B nahi hai",
    },
    # 6. Non-test content: exam tip as a question; replace with a real assumption item.
    "08_REASONING-024": {
        "question": "Kathn: 'Rajasthan ke sabhi jilon me khel maidan banaye jayenge.' — Is kathn me kaun si purvadharana (assumption) antarnit hai?",
        "option_a": "Khel maidan banane se khel pratibha badhegi",
        "option_b": "Rajasthan me abhi koi khel maidan nahi hai",
        "option_c": "Sabhi jile khel maidan chahte hain",
        "option_d": "Khel maidan banana sasta hai",
        "correct_answer": "A",
        "explanation": "Khel maidan banane ke peeche yahi mana jata hai ki isse khel pratibha badhegi. B galat hai (maidan pehle se hain), C aur D kathn se nahi nikalte.",
    },
    # 7. Non-test content: study advice as a question; replace with a real comprehension item.
    "13_GENERAL_ENGLISH-020": {
        "question": "Passage: 'The camel is called the ship of the desert. It can walk for many days in the hot desert without water. It carries people and heavy loads across the sand.' — Camel ko 'ship of the desert' kyun kaha jata hai?",
        "option_a": "It carries people and loads across the desert",
        "option_b": "It can live without water for many days",
        "option_c": "It is the fastest animal in the desert",
        "option_d": "It lives only in Rajasthan",
        "correct_answer": "A",
        "explanation": "Passage ke anusar camel desert me logon aur bojh ko le jata hai, jaise jahaz samudra me — isiliye 'ship of the desert'.",
    },
}


def load(path):
    with open(path, encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def save(path, fields, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def apply(path, label):
    fields, rows = load(path)
    by_qid = {r["qid"]: r for r in rows}
    n = 0
    for qid, changes in FIXES.items():
        if qid not in by_qid:
            continue
        r = by_qid[qid]
        for k, v in changes.items():
            assert k in fields, f"{label}: unknown column {k}"
            r[k] = v
        n += 1
    save(path, fields, rows)
    return n


n_comb = apply(COMBINED, "combined")
print(f"combined question_bank.csv: {n_comb} rows edited (expected 7)")
assert n_comb == 7
for qid, fname in SUBJ.items():
    p = os.path.join(BASE, "question_bank", fname)
    fields, rows = load(p)
    assert qid in {r["qid"] for r in rows}, f"{fname}: {qid} missing"
    n = apply(p, fname)
    print(f"  {fname}: {n} row(s) edited")

# verify sync: combined vs per-subject union
_, comb = load(COMBINED)
subj_rows = []
for fname in sorted(set(SUBJ.values())):
    _, rows = load(os.path.join(BASE, "question_bank", fname))
    subj_rows += rows
# full union check needs all 14 files
import glob
all_subj = []
for p in sorted(glob.glob(os.path.join(BASE, "question_bank", "*.csv"))):
    _, rows = load(p)
    all_subj += rows
comb_by = {r["qid"]: r for r in comb}
subj_by = {r["qid"]: r for r in all_subj}
assert set(comb_by) == set(subj_by), "qid sets differ"
diffs = [q for q in comb_by if comb_by[q] != subj_by[q]]
assert not diffs, f"rows differ between combined and per-subject: {diffs}"
print(f"SYNC OK: {len(comb)} combined rows == {len(all_subj)} per-subject rows, 0 differing rows")
