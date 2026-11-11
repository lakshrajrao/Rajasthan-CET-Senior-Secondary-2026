#!/usr/bin/env python3
"""Generate study_progress_tracker.csv (topic level, File 00 syllabus sequence).
Values are honest: nothing is marked complete without evidence.
- Research verified / Notes verified: Yes = topic covered in notes + audit 11 Nov 2026
  found no error in the spot-checked material; Partial = covered but thin or with an
  open ambiguity; No = coverage gap (see AUDIT_CORRECTION_REGISTER.md §G).
- Explained by ChatGPT / PDF prepared: No for every row (teaching has not started).
- Questions completed: 0 for every row. Test accuracy: blank until a test is taken.
- Revision required: Yes = audit-identified gap/thin coverage that needs new verified
  material before or during teaching; No = material ready to teach.
"""
import csv, os

BASE = os.path.expanduser("~/workspace/cet-2026-upload")
# (Subject, Topic, Research, Notes, Revision)
ROWS = [
    # 1. History of Rajasthan
    ("History of Rajasthan", "Ancient civilisations & archaeological sites (Kalibangan, Ahar, Bairat, Ganeshwar)", "Yes", "Yes", "No"),
    ("History of Rajasthan", "Prominent rulers & achievements (Guhila, Chauhan, Rathore, Kachhwaha)", "Yes", "Yes", "No"),
    ("History of Rajasthan", "Revolt of 1857 in Rajasthan", "Yes", "Yes", "No"),
    ("History of Rajasthan", "Peasant movements", "Yes", "Yes", "No"),
    ("History of Rajasthan", "Tribal movements (detail)", "Partial", "Partial", "Yes"),
    ("History of Rajasthan", "Praja Mandal movements", "Yes", "Yes", "No"),
    ("History of Rajasthan", "Integration of Rajasthan (1948–1956)", "Yes", "Yes", "No"),
    ("History of Rajasthan", "Prominent historical personalities", "Yes", "Yes", "No"),
    # 2. Art & Culture of Rajasthan
    ("Art & Culture of Rajasthan", "Architecture & painting (forts, palaces, schools)", "Yes", "Yes", "No"),
    ("Art & Culture of Rajasthan", "Folk music, musical instruments, dance & theatre", "Partial", "Partial", "Yes"),
    ("Art & Culture of Rajasthan", "Major religious sects & folk deities", "Yes", "Yes", "No"),
    ("Art & Culture of Rajasthan", "Social life: dresses, ornaments, fairs, festivals, customs, traditions", "No", "No", "Yes"),
    ("Art & Culture of Rajasthan", "Language, dialects & literature", "Yes", "Yes", "No"),
    ("Art & Culture of Rajasthan", "Prominent personalities in art & culture", "Yes", "Yes", "No"),
    # 3. Geography of India
    ("Geography of India", "Physical features: mountains, plateaus, deserts, plains", "Yes", "Yes", "No"),
    ("Geography of India", "Major rivers, dams, lakes & oceans", "No", "No", "Yes"),
    ("Geography of India", "Wildlife & sanctuaries", "No", "No", "Yes"),
    ("Geography of India", "Disaster management & climate change (NEW 2026)", "No", "No", "Yes"),
    # 4. Geography of Rajasthan
    ("Geography of Rajasthan", "Major physical features & climatic conditions", "Yes", "Yes", "No"),
    ("Geography of Rajasthan", "Natural vegetation & major soils", "Yes", "Yes", "No"),
    ("Geography of Rajasthan", "Rivers, dams & lakes", "Yes", "Yes", "No"),
    ("Geography of Rajasthan", "Natural resources: mineral, forest, water", "Yes", "Yes", "No"),
    ("Geography of Rajasthan", "Livestock", "No", "No", "Yes"),
    ("Geography of Rajasthan", "Wildlife, sanctuaries & conservation", "Yes", "Yes", "No"),
    ("Geography of Rajasthan", "Population: distribution, growth, density, literacy, sex ratio", "Yes", "Yes", "No"),
    ("Geography of Rajasthan", "Major tribes (Bhil, Meena, Garasia)", "No", "No", "Yes"),
    ("Geography of Rajasthan", "Tourism", "No", "No", "Yes"),
    # 5. Indian Political System (Rajasthan ref.)
    ("Indian Political System (Rajasthan ref.)", "Nature of Constitution, Preamble, Fundamental Rights, DPSP", "Yes", "Yes", "No"),
    ("Indian Political System (Rajasthan ref.)", "President, PM & Council of Ministers, Parliament", "Yes", "Yes", "No"),
    ("Indian Political System (Rajasthan ref.)", "Supreme Court (detail)", "Partial", "Partial", "Yes"),
    ("Indian Political System (Rajasthan ref.)", "Election Commission (detail)", "Partial", "Partial", "Yes"),
    ("Indian Political System (Rajasthan ref.)", "Governor, CM, Legislative Assembly, High Court, RPSC", "Yes", "Yes", "No"),
    ("Indian Political System (Rajasthan ref.)", "State Election Commission, State Information Commission, State Human Rights Commission, Chief Secretary, District Administration", "No", "No", "Yes"),
    ("Indian Political System (Rajasthan ref.)", "Local self-government & Panchayati Raj", "Yes", "Yes", "No"),
    # 6. Economy of Rajasthan
    ("Economy of Rajasthan", "Role of industry, agriculture, animal husbandry & mineral sector", "Partial", "Partial", "Yes"),
    ("Economy of Rajasthan", "Features & issues of Rajasthan economy", "Yes", "Yes", "No"),
    ("Economy of Rajasthan", "Concepts of state income & budget", "Yes", "Yes", "No"),
    ("Economy of Rajasthan", "Handicraft industry & small enterprises", "Yes", "Yes", "No"),
    ("Economy of Rajasthan", "Unemployment", "No", "No", "Yes"),
    ("Economy of Rajasthan", "Drought & famine", "No", "No", "Yes"),
    ("Economy of Rajasthan", "Welfare schemes & Acts", "Yes", "Yes", "No"),
    ("Economy of Rajasthan", "Development institutions & financial institutions", "No", "No", "Yes"),
    ("Economy of Rajasthan", "PRI role in rural development", "No", "No", "Yes"),
    ("Economy of Rajasthan", "MGNREGA", "Yes", "Yes", "No"),
    ("Economy of Rajasthan", "VB-G RAM G (Viksit Bharat Guarantee for Rozgar and Aajeevika Mission – Gramin) (NEW 2026)", "No", "No", "Yes"),
    # 7. Everyday Science
    ("Everyday Science", "Physical & chemical changes; oxidation/reduction; catalyst", "No", "No", "Yes"),
    ("Everyday Science", "Metals, non-metals & important compounds", "Yes", "Yes", "No"),
    ("Everyday Science", "Carbon & compounds, hydrocarbons, allotropes, CFC/Freons, CNG, polymers, soap & detergents", "No", "No", "Yes"),
    ("Everyday Science", "Reflection of light, laws, dispersion, lenses, vision defects", "Yes", "Yes", "No"),
    ("Everyday Science", "Space & IT; Indian space programme / ISRO", "No", "No", "Yes"),
    ("Everyday Science", "Genetics: terminology, Mendel's laws, chromosomes, nucleic acids, central dogma, sex determination", "No", "No", "Yes"),
    ("Everyday Science", "Environmental study: ecosystem structure, biotic factors, energy flow, biogeochemical cycles", "Yes", "Yes", "No"),
    ("Everyday Science", "Biotechnology: general info, bio-patent, new plant varieties, transgenic organisms", "No", "No", "Yes"),
    ("Everyday Science", "Economic importance of animals & plants", "No", "No", "Yes"),
    ("Everyday Science", "Blood groups, transfusion, Rh factor, pathogens, human health, malnutrition, human diseases — causes & cures", "Yes", "Yes", "No"),
    # 8. Logical Reasoning & Mathematics
    ("Logical Reasoning & Mathematics", "Blood relation", "Yes", "Yes", "No"),
    ("Logical Reasoning & Mathematics", "Number series & alphabet series", "Yes", "Yes", "No"),
    ("Logical Reasoning & Mathematics", "Clock & calendar", "Yes", "Yes", "No"),
    ("Logical Reasoning & Mathematics", "LCM & HCF", "Yes", "Yes", "No"),
    ("Logical Reasoning & Mathematics", "Average, profit & loss, percentage", "Yes", "Yes", "No"),
    ("Logical Reasoning & Mathematics", "Simple interest & compound interest", "Yes", "Yes", "No"),
    ("Logical Reasoning & Mathematics", "Ratio-proportion, time-speed-distance, work & time", "Yes", "Yes", "No"),
    ("Logical Reasoning & Mathematics", "Area (triangle, circle, ellipse, rectangle, sphere, cylinder) — ellipse formula missing", "Partial", "Partial", "Yes"),
    ("Logical Reasoning & Mathematics", "Volume (sphere, cylinder, cube, cone)", "Yes", "Yes", "No"),
    ("Logical Reasoning & Mathematics", "Graphical representation of data", "Yes", "Yes", "No"),
    ("Logical Reasoning & Mathematics", "Code & decode; sitting arrangement; mental & analytical ability", "Yes", "Yes", "No"),
    # 9. Current Affairs
    ("Current Affairs", "Major contemporary events — state & national (politics, economy, society, culture, technology, geography, ecology, sports) to Nov 2026", "Yes", "Yes", "No"),
    ("Current Affairs", "Major contemporary events after 11 Nov 2026 (needs pre-exam update)", "No", "No", "Yes"),
    ("Current Affairs", "Famous personalities", "Yes", "Yes", "No"),
    ("Current Affairs", "State & national programmes & policies", "Yes", "Yes", "No"),
    ("Current Affairs", "Civic duties: Fundamental Duties, moral values", "Yes", "Yes", "No"),
    ("Current Affairs", "Rajasthan Public Examination (Prevention of Unfair Means) Act, 2022", "Yes", "Yes", "No"),
    # 10. Public Health
    ("Public Health", "Basics of first aid", "No", "No", "Yes"),
    ("Public Health", "CPR (steps, 30:2 ratio, 100–120 compressions/min)", "No", "No", "Yes"),
    ("Public Health", "Types of drug abuse & prevention", "No", "No", "Yes"),
    ("Public Health", "Physical & mental fitness of youth", "No", "No", "Yes"),
    ("Public Health", "Health risks of social-media addiction & prevention", "No", "No", "Yes"),
    ("Public Health", "Health programmes, schemes & indicators (PM-JAY, ASHA, JSY, IMR, BMI, nutrition)", "Yes", "Yes", "No"),
    # 11. Computer Knowledge
    ("Computer Knowledge", "Characteristics & applications of computers", "Yes", "Yes", "No"),
    ("Computer Knowledge", "Computer organisation incl. memory (RAM, ROM)", "Yes", "Yes", "No"),
    ("Computer Knowledge", "File system (thin coverage)", "Partial", "Partial", "Yes"),
    ("Computer Knowledge", "Input/output devices", "Yes", "Yes", "No"),
    ("Computer Knowledge", "MS Office: Word, Excel/Spreadsheet, PowerPoint", "Yes", "Yes", "No"),
    # 12. General Hindi
    ("General Hindi", "Sangya, sarvanam, visheshan, avyaya, kriya (detail)", "Partial", "Partial", "Yes"),
    ("General Hindi", "Sandhi & sandhi-vichhed", "Yes", "Yes", "No"),
    ("General Hindi", "Samas & samas-vigrah", "Yes", "Yes", "No"),
    ("General Hindi", "Upsarg & pratyaya", "Yes", "Yes", "No"),
    ("General Hindi", "Paryayvachi, vilom, anekarthak", "Yes", "Yes", "No"),
    ("General Hindi", "Shabd-yugm", "No", "No", "Yes"),
    ("General Hindi", "Shabd-shuddhi & vakya-shuddhi", "No", "No", "Yes"),
    ("General Hindi", "Vakyaansh ke liye ek shabd; muhavare & lokoktiyaan", "Yes", "Yes", "No"),
    ("General Hindi", "Hindi equivalents of English technical terms", "No", "No", "Yes"),
    ("General Hindi", "Office letters (aadesh, paripatra, adhisoochna, ardh-shaskiya patra, nivida, press vigyapti)", "No", "No", "Yes"),
    # 13. General English
    ("General English", "Tenses / sequence of tenses", "Yes", "Yes", "No"),
    ("General English", "Active & passive voice", "Yes", "Yes", "No"),
    ("General English", "Direct & indirect narration", "Yes", "Yes", "No"),
    ("General English", "Articles & determiners (detail)", "Partial", "Partial", "Yes"),
    ("General English", "Prepositions", "Yes", "Yes", "No"),
    ("General English", "Translation (Hindi ↔ English)", "No", "No", "Yes"),
    ("General English", "Official & technical terms (with Hindi versions)", "No", "No", "Yes"),
    ("General English", "Synonyms & antonyms", "Yes", "Yes", "No"),
    ("General English", "One-word substitution", "Yes", "Yes", "No"),
    ("General English", "Unseen passage comprehension", "Yes", "Yes", "No"),
    ("General English", "Letter writing (official, demi-official, informal)", "No", "No", "Yes"),
]

FIELDS = ["Subject", "Topic", "Research verified", "Notes verified",
          "Explained by ChatGPT", "PDF prepared", "Questions completed",
          "Test accuracy", "Revision required"]
out = os.path.join(BASE, "study_progress_tracker.csv")
with open(out, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    for subj, topic, res, notes, rev in ROWS:
        w.writerow({"Subject": subj, "Topic": topic,
                    "Research verified": res, "Notes verified": notes,
                    "Explained by ChatGPT": "No", "PDF prepared": "No",
                    "Questions completed": 0, "Test accuracy": "",
                    "Revision required": rev})
print(f"wrote {out}: {len(ROWS)} topic rows")
from collections import Counter
print("by subject:", dict(Counter(s for s, *_ in ROWS)))
print("Research verified:", Counter(r[2] for r in ROWS))
print("Notes verified:", Counter(r[3] for r in ROWS))
print("Revision required Yes:", sum(1 for r in ROWS if r[4] == "Yes"))
