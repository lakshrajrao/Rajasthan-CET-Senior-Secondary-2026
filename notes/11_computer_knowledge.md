# COMPUTER KNOWLEDGE — Rajasthan CET Senior Secondary 2026

**Redesigned 11 Nov 2026 under `LEARNING_METHODOLOGY.md` (A–K structure). Subject: Computer Knowledge | Syllabus head 11.**
**Sources:** previous notes `notes/11_computer_knowledge.md` (36 lines — every verified fact preserved, see "Preservation note" at the end); master notes §11; bank MCQs `11_COMPUTER_KNOWLEDGE-001..018` (all in the §4 explanation format); PYQ dataset (`research/pyq/pyq_dataset.csv`) + `research/pyq/pyq_analysis.md`.
**PYQ note (applies to the whole file):** the PYQ dataset classifies **5** Computer questions — **2024-P1 Q22, Q23; 2024-P2 Q1; 2024-P3 Q4, Q6** — and its **Subtopic column identifies them: Q22 = first Intel microprocessor transistor count (2,300); Q23 = Excel next-workbook shortcut (Ctrl+F6); Q1 = HTTP full form; Q4 = DigiLocker (Ministry of Electronics & IT); Q6 = Digital India key vision area — NOT "promotion of behavioural changes"**. They are listed by ID + subtopic only, never with invented question text.
**EXTRA warning:** the official 12th-level syllabus has **no Internet, E-mail, Cyber-security or AI** (Graduation-level only). Chapters 6, 7 and 8 are marked **⚠️ EXTRA** — low-priority PYQ-style awareness only. The only reason they appear at all is that the 2024 paper asked HTTP (2024-P2 Q1). Study Chapters 1–5 first; do the EXTRA chapters only if time remains.
**Gap (marked, NOT filled by invention):** the file-system topic (Chapter 3) is thin in the repo — it covers only the standard definitions. Deeper detail (FAT/NTFS) is NOT in the 12th syllabus and is not taught here.

## Chapter map (official syllabus order)

| Ch | Topic (official syllabus) | Bank MCQs (generated) | PYQs |
|---|---|---|---|
| 1 | Characteristics & applications of computers | 001 | — |
| 2 | Computer organisation — CPU, memory (RAM, ROM), software | 002, 003, 004, 018 | 2024-P1 Q22 |
| 3 | File system — ⚠️ thin (definitions only) | — | — |
| 4 | Input / output devices | 014 | — |
| 5 | MS Office — Word, Excel, PowerPoint | 005, 006 | 2024-P1 Q23 |
| 6 | ⚠️ EXTRA — Internet & E-mail | 007, 008 | 2024-P2 Q1 |
| 7 | ⚠️ EXTRA — Number system, networking, security | 009, 010, 011, 015, 016 | — |
| 8 | ⚠️ EXTRA — E-governance & Digital India (Rajasthan) | 012, 013, 017 | 2024-P3 Q4, Q6 |

---

## Chapter 1 — Computer kya hai? Characteristics & Applications

### A. VISUAL INTRODUCTION — the IPO machine

```
              ┌─────────────────────────────────┐
  INPUT  ───► │  PROCESS (CPU)                  │ ───►  OUTPUT
  Keyboard    │  sochna + ganana + niyantran    │       Monitor
  Mouse       │                                 │       Printer
  Scanner     │  STORAGE (memory / hard disk)   │       Speaker
              │  data + result ko sambhalna     │
              └─────────────────────────────────┘
  Computer = INPUT → PROCESS → OUTPUT (+ STORAGE)
  Har kaam isi chaar kadam me hota hai.
```

> **How to use this diagram:** Cover the labels and point at each box from memory: input kya deta hai? Process kahan hota hai? Output kya deta hai? That is retrieval practice, not reading.

### B. STORY-BASED EXPLANATION — Babbage ka sapna

1830s me England me **Charles Babbage** ne ek machine ka design banaya — **Analytical Engine**. Us samay aisi koi machine bani nahi thi, lekin uska design aaj ke computer jaisa tha: input, memory, processor, output. Isiliye Babbage ko **computer ka janak** kaha jata hai. Unke saath kaam karne wali **Ada Lovelace** ne is machine ke liye pehla algorithm likha — isiliye unhe **pehli programmer** mana jata hai.

Aaj computer har jagah hai: school me padhai, bank me khata, railway me ticket booking, hospital me report, kisan ke liye mandi bhav, sarkar ki sewayein. Ek hi machine — bas kaam badal jata hai. Yahi computer ki sabse badi pehchan hai: **ek machine, hazaron kaam**.

### C. WHY DOES IT HAPPEN? — computer tez aur sahi kyun hai?

- **Why is a computer fast?** Computer electronic circuits se kaam karta hai — bijli ki gati se. Ek second me lakhon gananayein kar sakta hai. Insan ko jo hisab ghanton me karna pade, computer use pal bhar me kar deta hai.
- **Why is a computer accurate?** Computer thakta nahi aur bhoolta nahi. Jo nirdesh (instruction) use diya gaya, use bilkul waisa hi karta hai — bina galti ke. Galti tab hoti hai jab nirdesh ya data hi galat ho — iska naam hai **GIGO: Garbage In, Garbage Out** (kachra dalo, kachra pao).
- **Why can't a computer think?** Computer ke paas apni buddhi (IQ) nahi hoti. Vah sirf diye gaye nirdeshon ka palan karta hai. Sochna, faisla lena, naya vichar — yah insan ka kaam hai; computer uska auzar hai.
- **Why is one machine useful everywhere?** Kyunki computer ka kaam program (software) se tay hota hai, machine se nahi. Program badlo — wahi machine ticket book karegi, wahi machine film chalayegi.

### D. HOW DOES IT WORK? — har kaam ke chaar kadam

1. **Input:** user data dalta hai — keyboard se type, mouse se click, scanner se photo.
2. **Process:** CPU data par kaam karta hai — ganana, tulna, nirdeshon ka palan.
3. **Storage:** jarurat padne par data memory ya hard disk me sambhala jata hai.
4. **Output:** result bahar aata hai — screen par dikhta hai, printer se chhapta hai, speaker se bajta hai.

**Example:** ek chhatra nibandh likhta hai — keyboard se type karta hai (input), computer shabdon ko process karta hai (process), file hard disk me save hoti hai (storage), nibandh screen par dikhta hai aur printer se chhapta hai (output).

### E. VISUAL MEMORY CONNECTION

Computer ko ek **bahut tez, kabhi na thakne wala clerk** samjho — jo likhit aadeshon ka aksharshah palan karta hai. Clerk ko aadesh sahi do to kaam sahi; aadesh galat do to kaam galat. Clerk khud nahi sochta — bas aadesh manta hai. Wahi computer hai.

### F. IMPORTANT FACTS

| Visheshta (Characteristic) | Matlab |
|---|---|
| **Speed (gati)** | Lakhon gananayein ek second me |
| **Accuracy (shuddhta)** | Bina galti ke kaam, agar data/nirdesh sahi hon |
| **Diligence (lagatar kaam)** | Thakta nahi, bore nahi hota — ghanton ek jaisa kaam |
| **Versatility (bahumukhi)** | Ek machine, hazaron kaam (program badlo, kaam badlo) |
| **Storage (smriti)** | Badi matra me data sambhal sakta hai |
| **Automation (swachalan)** | Ek baar nirdesh milne par khud kaam karta hai |
| **No IQ** | Apni buddhi nahi — sirf nirdeshon ka palan |

| Kshetra (Application) | Upyog |
|---|---|
| Shiksha | Online padhai, result, e-learning |
| Bank | Khata, ATM, online payment |
| Railway / Airlines | Ticket booking, reservation |
| Swasthya | Report, patient record |
| Sarkar / E-governance | e-Mitra, online sewayein |
| Krishi | Mandi bhav, mausam jankari |
| Manoranjan | Film, sangeet, khel |

| Vyakti | Pehchan |
|---|---|
| **Charles Babbage** | Computer ka janak — **Analytical Engine** |
| **Ada Lovelace** | Pehli programmer — Analytical Engine ke liye pehla algorithm |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| Computer vs Calculator | Calculator sirf ganana karta hai. Computer ganana + storage + niyantran + kai kaam karta hai. |
| "Computer sochta hai" vs "Computer nirdesh manta hai" | Computer **nahi sochta** — uske paas IQ nahi hai. Vah sirf diye gaye nirdeshon ka palan karta hai. |
| Babbage vs Berners-Lee vs Turing | Babbage = **computer** ka janak. Berners-Lee = **WWW** ka janak. Turing = computer **vigyan** ke janak mane jate hain. |
| GIGO | Galti computer ki nahi, **galat input** ki hoti hai — Garbage In, Garbage Out. |

### H. MEMORY TECHNIQUE (one only)

**"S-A-V-D"** — computer ki 4 pehchan: **S**peed (tez) – **A**ccuracy (sahi) – **V**ersatility (har kaam) – **D**iligence (thakta nahi). Inke saath yaad rakho: **Storage** (sambhalta hai) aur **No IQ** (sochta nahi).

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** `11_COMPUTER_KNOWLEDGE-001` (Babbage — computer ka janak).
- **Actual PYQs:** is chapter se juda koi PYQ classified sample me **nahi** hai. 5 Computer PYQs Chapters 2, 5, 6 aur 8 se jude hain (neeche dekho).
- **Recurring exam angles:** Babbage ↔ Analytical Engine; Ada Lovelace ↔ pehli programmer; computer ki visheshtayein (speed, accuracy, diligence, versatility); GIGO.

### J. ACTIVE RECALL — answer from memory, then check

1. Computer ka janak kise kaha jata hai aur unki machine ka naam kya tha?
2. Pehli programmer kaun thi?
3. Computer ke kaam ke chaar kadam kya hain (kram se)?
4. GIGO ka matlab kya hai?
5. Computer tez aur sahi kyun hota hai?
6. Computer ki 4 mukhya visheshtayein (S-A-V-D) kya hain?

**Answers (check after attempting):** 1. Charles Babbage — Analytical Engine. 2. Ada Lovelace. 3. Input → Process → Storage → Output. 4. Garbage In, Garbage Out — galat input se galat output. 5. Electronic circuits (bijli ki gati) se kaam karta hai; thakta/bhoolta nahi, nirdesh ka aksharshah palan karta hai. 6. Speed, Accuracy, Versatility, Diligence (+ Storage, Automation, No IQ).

### K. REVISION SUMMARY (one page — test yourself against it)

```
IPO: INPUT → PROCESS → OUTPUT (+ STORAGE)
BABBAGE = computer ka janak (Analytical Engine) · ADA LOVELACE = pehli programmer
VISHESHTA: Speed · Accuracy · Versatility · Diligence · Storage · Automation · NO IQ
GIGO: Garbage In, Garbage Out — galti galat input ki hoti hai
TRAPS: Computer sochta NAHI (nirdesh manta hai) · Babbage (computer) ≠ Berners-Lee (WWW) ≠ Turing (vigyan)
MNEMONIC: S-A-V-D
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (redraw the IPO diagram from memory) → tomorrow (recall + bank 001) → after 3 days (mixed with Chapter 2) → after 7 days (timed: bank 001 + IPO flow).

---

## Chapter 2 — Computer Organisation: CPU, Memory, Software

### A. VISUAL INTRODUCTION — computer ke andar kya hai?

```
                    ┌───────────────────────────────┐
   INPUT ─────────► │  CPU — computer ka BRAIN       │ ─────────► OUTPUT
   Keyboard         │  ┌──────────┐  ┌───────────┐  │          Monitor
   Mouse            │  │  CU      │  │  ALU      │  │          Printer
   Scanner          │  │ niyantran│  │ ganana    │  │          Speaker
                    │  └──────────┘  └───────────┘  │
                    │  + MEMORY (registers)          │
                    └───────┬───────────────────────┘
                            │ data aata-jata hai
                    ┌───────▼───────────────────────┐
                    │  MEMORY                        │
                    │  RAM (kaam ki mez) — volatile │
                    │  ROM (recipe book) — non-vol. │
                    │  Hard Disk / SSD (almari)      │
                    └───────────────────────────────┘
  CPU = ALU + CU + Memory
```

> **How to use this diagram:** Cover the labels and point at each box from memory: CU kya karta hai? ALU kya karta hai? RAM kahan baithta hai? That is retrieval practice, not reading.

### B. STORY-BASED EXPLANATION — rasoi ki kahani

Ek rasoi socho. **CU (Control Unit)** head cook hai — vah batata hai kab kya karna hai, kis ko kya dena hai. **ALU (Arithmetic Logic Unit)** vahan ka karigar hai — vah ganana karta hai, jod-ghata karta hai, tulna karta hai. **Memory** vah counter hai jahan kaam ke samay samagri rakhi hoti hai.

- **RAM** kaam ki **mez** hai: jab tak rasoi chal rahi hai, samagri mez par hai. Rasoi band hote hi mez saaf ho jati hai — samagri (data) mit jati hai. Isiliye RAM **volatile** hai.
- **ROM** diwar par tangi **recipe book** hai: band hone par bhi vahi rehti hai. Isiliye ROM **non-volatile** hai.
- **Hard Disk / SSD** badi **almari** hai: sab kuch lambi samay ke liye sambhala rehta hai — chahe computer band ho.

Jab tum koi file kholte ho: file almari (hard disk) se mez (RAM) par aati hai, head cook (CU) aadesh deta hai, karigar (ALU) kaam karta hai, result screen par dikhta hai.

### C. WHY DOES IT HAPPEN? — RAM mit-ti kyun hai, ROM kyun nahi?

- **Why is RAM volatile?** RAM electronic memory hai — uska data bijli (electric charge) se tika rehta hai. Bijli band hote hi charge khatm, data gaya. Isiliye computer band karne par RAM ka data mit jata hai.
- **Why is ROM non-volatile?** ROM me data banate samay hi **sthayi roop se** likh diya jata hai (jaise chhapi hui kitab). Bijli ki jarurat nahi — isiliye band hone par bhi data bana rehta hai. ROM me computer ko start karne ke jaruri nirdesh hote hain.
- **Why is the CPU called the brain?** Kyunki vahi niyantran karta hai (CU) aur vahi ganana karta hai (ALU). Baki sab hisse — keyboard, screen, disk — uske aadesh par kaam karte hain.
- **Why do we need secondary memory at all?** RAM chhoti aur asthayi hai; hard disk badi aur sthayi hai. Bina hard disk ke har baar computer band karte hi sab kuch mit jata.

### D. HOW DOES IT WORK? — file kholne par kya hota hai (kram se)

1. **Tum file par double-click karte ho** (input — mouse).
2. **OS file ko hard disk se RAM me lata hai** (secondary → primary memory).
3. **CU nirdesh deta hai; ALU ganana karta hai** (CPU process karta hai).
4. **Result RAM me rakha jata hai, phir screen par dikhta hai** (output — monitor).
5. **Save karne par result wapas hard disk me likha jata hai** (permanent storage).

### E. VISUAL MEMORY CONNECTION

**RAM = kaam ki mez; Hard Disk = almari; ROM = diwar ki recipe book.** Mez band hote hi saaf (RAM volatile); almari band hone par bhi bhari rehti hai (hard disk permanent); recipe book hamesha diwar par (ROM non-volatile). Jab bhi RAM/ROM bhoolo, rasoi yaad karo.

### F. IMPORTANT FACTS

| CPU ka hissa | Kaam |
|---|---|
| **ALU** (Arithmetic Logic Unit) | Ganana (jod, ghata, guna, bhag) aur tulna |
| **CU** (Control Unit) | Niyantran — sabhi hisson ko aadesh dena |
| **Memory (registers)** | Kaam ke samay data aur nirdesh rakhna |
| **CPU = Brain of computer** | ALU + CU + Memory |

| Memory | Prakar | Visheshta |
|---|---|---|
| **RAM** | Primary (mukhy) | **Volatile** — band hone par data mit jata hai |
| **ROM** | Primary (mukhy) | **Non-volatile** — data bana rehta hai |
| **Hard Disk / SSD / Pen Drive / CD-DVD** | Secondary (gaun) | Sthayi storage — band hone par bhi data rehta hai |

| Memory unit | Maan |
|---|---|
| 1 Bit | 0 ya 1 (sabse chhoti ikai) |
| 1 Byte | **8 bit** |
| 1 KB | 1024 Byte |
| 1 MB | 1024 KB |
| 1 GB | 1024 MB |
| 1 TB | 1024 GB |
| 1 PB | 1024 TB |

| Software | Uddharan | Kaam |
|---|---|---|
| **System software — Operating System (OS)** | Windows, Linux, macOS | Computer ko chalana |
| **Application software** | MS Word, MS Excel, Browser | User ka kaam karna |

| OS ke kaam | Matlab |
|---|---|
| File prabandhan | Files ko sambhalna (banao, save karo, dhoondho) |
| Memory prabandhan | RAM ka batwara |
| Process prabandhan | Kaun sa program kab chalega |
| Device prabandhan | Keyboard, printer jaise devices ko chalana |
| **GUI** (Graphical User Interface) | Icons/windows se computer chalana (mouse se) |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| RAM vs ROM | RAM = **volatile** (mit jata hai), kaam ki mez. ROM = **non-volatile** (bana rehta hai), recipe book. |
| Primary vs Secondary memory | Primary (RAM/ROM) = CPU ke paas, tez, chhoti. Secondary (Hard Disk/SSD) = badi, sthayi, dheemi. |
| CPU vs Computer | CPU computer ka **ek hissa** (brain) hai — poora computer nahi. |
| System software vs Application software | System (OS) = computer chalata hai. Application (Word/Excel) = user ka kaam karta hai. |
| Windows vs Chrome vs Word | Windows = **OS** (system software). Chrome = **browser** (application). Word = **application**. |
| ALU vs CU | ALU = **ganana** karta hai. CU = **niyantran** karta hai. |
| Bit vs Byte | 1 Byte = **8 bit**. 1024 Byte = 1 KB (Byte ke baad har kadam 1024 guna). |

### H. MEMORY TECHNIQUE (one only)

**"CPU = A-C-M"** — **A**LU (ganana) + **C**U (niyantran) + **M**emory. Aur RAM ke liye: **"RAM = Rukega nahi, Aaj ka kaam, Mit jayega"** — band hote hi saaf.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** `11_COMPUTER_KNOWLEDGE-002` (CPU = Brain), `-003` (RAM volatile), `-004` (1 Byte = 8 bit), `-018` (Windows = OS).
- **Actual PYQs:** **2024-P1 Q22 — first Intel microprocessor transistor count = 2,300** (dataset Subtopic, key C). Intel 4004 (1971) pehla commercial microprocessor tha — CPU ka ek chip par aana. Isi liye yah sawal is chapter se juda hai.
- **Recurring exam angles:** CPU = ALU + CU + Memory; RAM volatile vs ROM non-volatile; 1 Byte = 8 bit; KB/MB/GB ka 1024 wala kram; OS vs application software.

### J. ACTIVE RECALL — answer from memory, then check

1. CPU ko kya kaha jata hai aur uske 3 hisse kaun se hain?
2. ALU aur CU me kya antar hai?
3. RAM volatile kyun hoti hai? ROM kyun nahi?
4. 1 Byte = kitne bit? 1 KB = kitne Byte? 1 PB = kitne TB?
5. Primary aur secondary memory me kya antar hai?
6. Windows, Chrome aur MS Word me se kaun sa OS hai — aur kyun?
7. OS ke 4 kaam kya hain?
8. Pehle Intel microprocessor me kitne transistor the (PYQ 2024-P1 Q22)?

**Answers (check after attempting):** 1. Brain of computer — ALU + CU + Memory. 2. ALU ganana karta hai; CU niyantran karta hai. 3. RAM ka data bijli (charge) se tika hai — bijli band hote hi mit jata hai; ROM me data sthayi roop se likha hota hai. 4. 1 Byte = 8 bit; 1 KB = 1024 Byte; 1 PB = 1024 TB. 5. Primary (RAM/ROM) tez aur chhoti, CPU ke paas; secondary (Hard Disk/SSD) badi aur sthayi. 6. Windows OS hai; Chrome browser aur Word application software hain. 7. File, memory, process, device prabandhan (+ GUI). 8. 2,300 (Intel 4004).

### K. REVISION SUMMARY (one page — test yourself against it)

```
CPU = BRAIN = ALU (ganana) + CU (niyantran) + Memory
RAM = mez — VOLATILE (band hote hi saaf) · ROM = recipe book — NON-VOLATILE (bani rehti hai)
SECONDARY = Hard Disk / SSD / Pen Drive / CD-DVD — sthayi storage
UNITS: Bit < Byte (8 bit) < KB < MB < GB < TB < PB — har kadam 1024 (Byte ke baad)
SOFTWARE: System (OS: Windows, Linux, macOS) vs Application (Word, Excel, Browser)
OS KE KAAM: file · memory · process · device prabandhan · GUI
PYQ: Intel 4004 — 2,300 transistors (2024-P1 Q22)
TRAPS: RAM ≠ ROM · ALU (ganana) ≠ CU (niyantran) · Windows (OS) ≠ Chrome (browser) ≠ Word (application)
MNEMONIC: CPU = A-C-M · RAM = band hote hi Mit jayega
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (redraw the CPU diagram from memory) → tomorrow (recall + bank 002, 003, 004, 018) → after 3 days (mixed with Chapter 1) → after 7 days (timed: bank 002–004, 018 + RAM/ROM table).

---

## Chapter 3 — File System (⚠️ thin — sirf standard definitions)

> **Honest note:** official syllabus me "file system" ek topic hai, lekin repo me is par **koi bank MCQ aur koi PYQ nahi hai**, aur purane notes me bhi sirf OS ke "file prabandhan" ka ek shabd hai. Is chapter me sirf woh standard definitions hain jo har textbook me hoti hain — koi exam-specific data nahi. Gehra detail (jaise FAT/NTFS) 12th syllabus me nahi hai aur yahan nahi padhaya jata.

### A. VISUAL INTRODUCTION — almari ka ped (tree)

```
  C:  (drive — almari)
   │
   ├── 📁 School (folder)
   │     ├── 📄 nibandh.docx      ← file (kagaz)
   │     └── 📄 ganit.xlsx
   │
   ├── 📁 Photo (folder)
   │     ├── 📄 diwali.jpg
   │     └── 📁 2025 (sub-folder)
   │           └── 📄 mela.jpg
   │
   └── 📄 suchna.txt              ← file seedha drive par

  PATH (pata): C:\School\nibandh.docx
  = drive → folder → file — jaise ghar ka pata: sheher → mohalla → makan
```

> **How to use this diagram:** Cover the labels and draw the tree from memory: drive ke neeche folder, folder ke neeche file. Then say the path of `mela.jpg` aloud. That is retrieval practice, not reading.

### B. STORY-BASED EXPLANATION — library ka catalogue

Ek badi library socho: hazaron kitabein. Bina catalogue ke koi kitab nahi milegi. **File system wahi catalogue hai** — computer ka woh hissa jo batata hai ki har file kahan rakhi hai, uska naam kya hai, vah kis program ki hai.

- **File** = ek kagaz (nibandh.docx, ganit.xlsx, photo.jpg) — data ka ek tukda, ek naam ke saath.
- **Folder (directory)** = almari ka khana (shelf) — files ko samooh me rakhne ki jagah. Folder ke andar folder (sub-folder) bhi ho sakta hai.
- **Path** = file ka pura pata — jaise `C:\School\nibandh.docx`: pehle drive (C:), phir folder (School), phir file.
- **Extension** = naam ke baad ka hissa (.docx, .xlsx, .pptx, .txt) — jo batata hai ki file kis program ki hai.
- **Drive** = badi almari — jaise C: drive, D: drive, pen drive.

### C. WHY DOES IT HAPPEN? — folder kyun chahiye, extension kyun?

- **Why do folders exist?** Hazar files ek jagah padi hon to kuch nahi milega. Folder se files **vyavasthit** rehti hain — School ki files ek jagah, Photo ek jagah. Dhoondhna asan hota hai.
- **Why does a file need an extension?** Extension dekhkar OS jaanta hai ki file ko **kis program se kholna hai**: .docx → Word, .xlsx → Excel, .pptx → PowerPoint. Bina extension ke OS ko pata nahi chalega ki file kis ki hai.
- **Why does a file need a path?** Ek hi naam ki do files alag folder me ho sakti hain (jaise do `nibandh.docx`). Path batata hai **kaun si** file — drive + folder + naam milkar file ki pehchan banti hai.
- **Why is the file system managed by the OS?** Kyunki file banana, save karna, dhoondhna, delete karna — yah sab OS ka kaam hai (Chapter 2: file prabandhan). User sirf naam aur jagah batata hai; kaam OS karta hai.

### D. HOW DOES IT WORK? — file save karne ke kadam (kram se)

1. **Program me kaam karo** (jaise Word me nibandh likho).
2. **Save dabao** — OS poochhta hai: naam kya ho, kahan rakho?
3. **Naam + jagah chuno** — folder chuno, naam likho; extension program khud lagata hai (.docx).
4. **OS file ko hard disk me likhta hai** aur file system me uska pata (path) darj karta hai.
5. **Dobara kholna ho** to path se dhoondho — ya file par double-click karo; OS extension dekhkar sahi program kholta hai.

### E. VISUAL MEMORY CONNECTION

**File system = almari (cupboard) with labelled shelves.** Har shelf (folder) par label hai; har kagaz (file) par naam + extension. Kagaz dhoondhna ho to pehle almari (drive), phir shelf (folder), phir kagaz (file) — hamesha isi kram me.

### F. IMPORTANT FACTS

| Shabd | Matlab |
|---|---|
| **File** | Data ka ek tukda, ek naam ke saath (nibandh.docx) |
| **Folder / Directory** | Files rakhne ki jagah; folder ke andar folder (sub-folder) ho sakta hai |
| **Path** | File ka pura pata — drive → folder → file (C:\School\nibandh.docx) |
| **Extension** | Naam ke baad ka hissa — .docx (Word), .xlsx (Excel), .pptx (PowerPoint), .txt (text) |
| **Drive** | Storage ki ikai — C: drive, D: drive, pen drive |
| **Root** | Drive ki sabse upar ki jagah (C:\ ) — sab folder yahin se shuru hote hain |

| File par kaam (operations) | Matlab |
|---|---|
| Create (banana) | Nayi file banana |
| Rename | Naam badalna |
| Copy | Nakal banana |
| Move | Ek folder se doosre me le jana |
| Delete | Hatana |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| File vs Folder | File = **kagaz** (data). Folder = **khana/shelf** (files rakhne ki jagah). |
| File name vs Extension | Naam = tum dete ho (nibandh). Extension = program batata hai (.docx) — kis program ki file hai. |
| Drive vs Folder | Drive = **almari** (C:). Folder = almari ka **khana**. |
| Save vs Save As | Save = purani file ko wahi update karo. Save As = **naye naam/jagah** se save karo. |
| .docx vs .xlsx vs .pptx | .docx = **Word** (document), .xlsx = **Excel** (table), .pptx = **PowerPoint** (slides). |

### H. MEMORY TECHNIQUE

**No mnemonic for this chapter — and that is deliberate.** The tree diagram in §A is the memory aid: drive → folder → file. The terms are definitions to **use**, not a list to memorise. Draw the tree from memory instead.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** is topic par **koi bank MCQ nahi hai** — file system par repo me koi prashn nahi bana hai.
- **Actual PYQs:** is topic par classified sample me **koi PYQ nahi hai**. (Memory units wala 1 PB = 1024 TB ka item, P3 Q35, Chapter 2 se juda hai.)
- **Recurring exam angles:** file vs folder; extension ↔ program (.docx/.xlsx/.pptx); path ka kram (drive → folder → file). Syllabus topic hone ke karan definitions yaad rakho — lekin is par lamba samay mat lagao; exam evidence nahi hai.

### J. ACTIVE RECALL — answer from memory, then check

1. File, folder aur path me kya antar hai?
2. `C:\School\nibandh.docx` me drive, folder aur file kaun se hain?
3. Extension ka kya kaam hai? .xlsx kis program ki file hai?
4. File par 5 operations (kaam) kya hain?
5. Folder ke andar folder ko kya kehte hain?
6. File system kis ke dwara sambhala jata hai — user ya OS?

**Answers (check after attempting):** 1. File = data ka tukda; folder = files rakhne ki jagah; path = file ka pura pata. 2. Drive C:, folder School, file nibandh.docx. 3. Extension batata hai file kis program ki hai; .xlsx = Excel. 4. Create, Rename, Copy, Move, Delete. 5. Sub-folder. 6. OS (file prabandhan OS ka kaam hai).

### K. REVISION SUMMARY (one page — test yourself against it)

```
FILE SYSTEM = library ka catalogue
FILE = kagaz (data + naam) · FOLDER = shelf (files ki jagah) · PATH = drive → folder → file
EXTENSION: .docx = Word · .xlsx = Excel · .pptx = PowerPoint · .txt = text
OPERATIONS: Create · Rename · Copy · Move · Delete
MANAGED BY: OS (file prabandhan)
⚠️ THIN TOPIC: koi bank MCQ / PYQ nahi — definitions yaad rakho, lamba samay mat lagao
TRAPS: File ≠ Folder · Drive (almari) ≠ Folder (khana) · Extension program batata hai, naam tum dete ho
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (redraw the tree from memory) → tomorrow (recall + path likho) → after 3 days (mixed with Chapter 2) → after 7 days (timed: definitions + extensions).

---

## Chapter 4 — Input & Output Devices

### A. VISUAL INTRODUCTION — andar aur bahar

```
        ┌─────────────────────────────────┐
        │        COMPUTER (CPU)           │
        │                                 │
  INPUT │  Keyboard · Mouse · Scanner     │ OUTPUT
  ────► │  Microphone · Joystick · Webcam │ ────►
  ANDAR │                                 │ BAHAR
        │  Monitor · Printer · Speaker    │
        │  Plotter · Projector            │
        └─────────────────────────────────┘
  INPUT = andar jane wala (data dalna) · OUTPUT = bahar aane wala (result pana)
  Touchscreen = DONO (input bhi, output bhi)
```

> **How to use this diagram:** Cover the labels and point at each device from memory: yah andar jata hai ya bahar aata hai? That is retrieval practice, not reading.

### B. STORY-BASED EXPLANATION — paanch indriyan

Computer ke bhi "indriyan" hote hain — jaise insan ke:

- **Input devices** computer ki indriyan hain jo bahar se jankari **andar** lete hain: **Keyboard** (likhna), **Mouse** (chunna), **Scanner** (photo/kagaz ko digital banana), **Microphone** (awaz), **Joystick** (khel me disha), **Webcam** (tasveer/video).
- **Output devices** computer ki "awaz aur chehra" hain jo result **bahar** dete hain: **Monitor** (dikhan), **Printer** (chhapna), **Speaker** (bajana), **Plotter** (bade nakse/drawing banana), **Projector** (badi screen par dikhana).

Ek photo scan karo (scanner = input) → computer use process karta hai → photo screen par dikhti hai (monitor = output) ya chhapti hai (printer = output). Har kaam me input pehle, output baad me.

### C. WHY DOES IT HAPPEN? — yah input kyun, vah output kyun?

- **Why is a keyboard input and a monitor output?** Keyboard se data **andar** jata hai (tum type karte ho). Monitor par result **bahar** aata hai (tum dekhte ho). Disha hi pehchan hai: andar = input, bahar = output.
- **Why is a touchscreen both?** Touchscreen par tum **chhoote** ho (input — tap karna) aur vahi screen **dikhati** bhi hai (output). Ek hi device, do kaam — isiliye use input-output device kehte hain.
- **Why is a webcam input and a speaker output?** Webcam bahar ki tasveer **andar** leta hai. Speaker andar ka sound **bahar** deta hai. Dono ki disha ulta hai — isiliye ek input, doosra output.
- **Why is a plotter different from a printer?** Printer kagaz par text/photo chhapta hai. Plotter bade aakar ke drawing/nakse (jaise engineer ka blueprint) banata hai — pen se line kheenchkar. Kaam alag, isiliye device alag.

### D. HOW DOES IT WORK? — photo scan karke chhapna (kram se)

1. **Scanner photo ko digital data me badalta hai** (input).
2. **Data RAM me jata hai; CPU use process karta hai** (process).
3. **Result screen par dikhta hai** (output — monitor) — tum dekh kar jaanchte ho.
4. **Print dabate ho — printer kagaz par chhapta hai** (output — printer).

### E. VISUAL MEMORY CONNECTION

**Input = ghar ka pravesh dwar (andar aane wala); Output = nikasi dwar (bahar jane wala).** Keyboard, Mouse, Scanner dwar se andar aate hain; Monitor, Printer, Speaker dwar se bahar jate hain. Touchscreen = dono dwar ek saath.

### F. IMPORTANT FACTS

| Input device | Kaam |
|---|---|
| **Keyboard** | Type karna — akshar, sankhya dalna |
| **Mouse** | Chunna, click karna, khinchna |
| **Scanner** | Kagaz/photo ko digital banana |
| **Microphone** | Awaz andar lena |
| **Joystick** | Khel me disha niyantran |
| **Webcam** | Tasveer/video andar lena |

| Output device | Kaam |
|---|---|
| **Monitor** | Screen par dikhana |
| **Printer** | Kagaz par chhapna |
| **Speaker** | Awaz bahar dena |
| **Plotter** | Bade drawing/nakse banana |
| **Projector** | Badi screen (deewar/parde) par dikhana |

| Dono kaam | Kaam |
|---|---|
| **Touchscreen** | Chhune se input + dikhane se output |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| Monitor vs Webcam | Monitor = **output** (dikhta hai). Webcam = **input** (tasveer leta hai). |
| Printer vs Scanner | Printer = **output** (chhapta hai). Scanner = **input** (kagaz ko digital banata hai). |
| Speaker vs Microphone | Speaker = **output** (awaz bahar). Microphone = **input** (awaz andar). |
| Plotter vs Printer | Printer = kagaz par text/photo. Plotter = **bade drawing/nakse** (blueprint). |
| Keyboard vs Mouse | Dono **input** hain — keyboard type karta hai, mouse chunta hai. |
| Joystick | Input device hai (khel me) — output nahi. |

### H. MEMORY TECHNIQUE (one only)

**"Input: K-M-S · Output: M-P-S"** — Input ke bade teen: **K**eyboard – **M**ouse – **S**canner. Output ke bade teen: **M**onitor – **P**rinter – **S**peaker. Baki (microphone, joystick, webcam / plotter, projector) inke saath jod lo: awaz wale — microphone andar, speaker bahar.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** `11_COMPUTER_KNOWLEDGE-014` (Keyboard — input device).
- **Actual PYQs:** is chapter se juda classified sample me **koi PYQ nahi hai**. (Full 2024 paper me ek printer item hai — P3 Q41 — jo classified sample me nahi hai; isiliye use yahan sirf sanket ke roop me likha gaya hai, verified detail ke roop me nahi.)
- **Recurring exam angles:** input vs output ki pehchan; keyboard/mouse/scanner = input; monitor/printer/speaker = output; touchscreen = dono.

### J. ACTIVE RECALL — answer from memory, then check

1. Input aur output device me pehchan kya hai (ek shabd me)?
2. Keyboard, Mouse, Scanner, Webcam — inme se kaun sa output hai? (Koi nahi — sab input hain; jaanch lo.)
3. Plotter aur printer me kya antar hai?
4. Touchscreen ko input-output device kyun kehte hain?
5. Microphone aur speaker me disha ka antar kya hai?
6. Monitor output hai ya input — aur kyun?

**Answers (check after attempting):** 1. Disha — andar = input, bahar = output. 2. Koi nahi — charon input hain. 3. Printer kagaz par text/photo chhapta hai; plotter bade drawing/nakse banata hai. 4. Chhune se input leta hai aur dikhane se output deta hai — dono kaam. 5. Microphone awaz andar leta hai; speaker awaz bahar deta hai. 6. Output — result screen par bahar aata hai.

### K. REVISION SUMMARY (one page — test yourself against it)

```
INPUT (andar): Keyboard · Mouse · Scanner · Microphone · Joystick · Webcam
OUTPUT (bahar): Monitor · Printer · Speaker · Plotter · Projector
DONO: Touchscreen
PEHCHAN: disha — andar = input, bahar = output
TRAPS: Monitor (output) ≠ Webcam (input) · Printer (output) ≠ Scanner (input)
       Speaker (output) ≠ Microphone (input) · Plotter = bade nakse
MNEMONIC: Input K-M-S · Output M-P-S
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (devices ko input/output me baanto, bina dekhe) → tomorrow (recall + bank 014) → after 3 days (mixed with Chapter 2) → after 7 days (timed: bank 014 + device sorting).

---

## Chapter 5 — MS Office: Word, Excel, PowerPoint

### A. VISUAL INTRODUCTION — teen auzar, teen kaam

```
   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
   │  MS WORD     │  │  MS EXCEL    │  │  POWERPOINT  │
   │  🖊 pen      │  │  ▦ grid      │  │  ▣ screen    │
   │  .docx       │  │  .xlsx       │  │  .pptx       │
   │  nibandh,    │  │  table,      │  │  slides,     │
   │  patra,      │  │  hisab,      │  │  prastuti,   │
   │  report      │  │  formula     │  │  presentation│
   └──────────────┘  └──────────────┘  └──────────────┘
   WORD = likhna · EXCEL = ginna/hisab · POWERPOINT = dikhana
```

> **How to use this diagram:** Cover the labels and point at each icon from memory: iska extension kya hai? Iska kaam kya hai? That is retrieval practice, not reading.

### B. STORY-BASED EXPLANATION — school project ki kahani

Ek chhatra ko school project banana hai. **Word** me vah nibandh likhta hai — patra, report, essay. **Excel** me vah ankon ki table banata hai — kis vishay me kitne number, kul kitne, ausat kitna. **PowerPoint** me vah prastuti banata hai — slide par slide, class ke samne dikhane ke liye.

Teenon ek hi parivar (MS Office) ke hain, lekin kaam alag: Word **likhne** ke liye, Excel **ginne/hisab** ke liye, PowerPoint **dikhane** ke liye. Exam me inke extension aur kaam hi poochhe jate hain.

### C. WHY DOES IT HAPPEN? — formula '=' se kyun shuru hoti hai?

- **Why does an Excel formula start with '='?** Kyunki Excel ko batana padta hai ki cell me **ganana** karni hai, text nahi likhna. `=SUM(A1:A5)` dekhkar Excel samajhta hai: A1 se A5 tak jodo. Bina '=' ke vah use sirf akshar samjhega.
- **Why do extensions matter?** Extension dekhkar OS jaanta hai ki file ko **kis program se kholna hai** — .docx dekhkar Word khulta hai, .xlsx dekhkar Excel. Bina extension ke OS confuse ho jayega.
- **Why is a cell named like B5?** Cell ka pata **column + row** se banta hai: B = column, 5 = row. Isiliye B5 matlab column B, row 5 ka cell — jaise shatranj ki chaal ka pata.
- **Why is Excel better than a calculator for tables?** Kyunki ek baar formula likh do to data badalne par result **khud** badal jata hai. Calculator me har baar dobara ginna padta hai.

### D. HOW DOES IT WORK? — Excel me formula lagana (kram se)

1. **Cell chuno** — jahan result chahiye (jaise B6).
2. **'=' type karo** — Excel ko batao ki ganana karni hai.
3. **Function likho** — jaise `SUM(A1:A5)` (A1 se A5 tak jodna).
4. **Enter dabao** — result cell me dikhega; formula upar formula bar me dikhega.
5. **Data badlo to result khud badlega** — dobara formula likhne ki jarurat nahi.

### E. VISUAL MEMORY CONNECTION

Teen auzar yaad rakho: **pen (Word), calculator-grid (Excel), screen (PowerPoint)**. Pen se likhte hain, grid par ginte hain, screen par dikhate hain. Extension bhi waise hi: **d**ocx = **d**ocument (likhna), **x**lsx = e**x**cel (hisab), **p**ptx = **p**resentation (dikhana).

### F. IMPORTANT FACTS

| Program | File | Extension | Mukhya kaam |
|---|---|---|---|
| **MS Word** | Document (nibandh, patra) | **.docx** | Likhna — text document |
| **MS Excel** | Spreadsheet (table, hisab) | **.xlsx** | Ginna — table + formula + calculation |
| **MS PowerPoint** | Presentation (slides) | **.pptx** | Dikhana — slides par prastuti |

| Excel ki baat | Tathya |
|---|---|
| **Cell** | Row + column ka milan — jaise **B5** (column B, row 5) |
| **Formula** | **'='** se shuru hoti hai — jaise `=SUM(A1:A5)` |
| **SUM** | Jodne ka function — `=SUM(A1:A5)` A1 se A5 tak jodta hai |
| **Next workbook shortcut (PYQ)** | **Ctrl+F6** — agle workbook par jao (2024-P1 Q23) |
| **Edit cell (standard shortcut)** | **F2** — cell ke andar edit karo (full 2024 paper P3 Q42 — classified sample me nahi, standard Excel shortcut ke roop me diya gaya) |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| .docx vs .xlsx vs .pptx | .docx = **Word** (document). .xlsx = **Excel** (table/hisab). .pptx = **PowerPoint** (slides). |
| Cell vs Range | Cell = **ek** khana (B5). Range = **kai** cells ka samooh (A1:A5). |
| Formula vs Function | Formula = '=' se shuru hone wali **ganana** (=SUM(A1:A5)). Function = pehle se bana **ganana ka niyam** (SUM, AVERAGE). |
| Word vs Excel vs PowerPoint | Word = **likhna**, Excel = **ginna**, PowerPoint = **dikhana**. |
| = vs +/− | '=' **formula ki shuruaat** batata hai; +/− ganana ke **chinh** hain. |

### H. MEMORY TECHNIQUE (one only)

**"d–x–p" (Word–Excel–PowerPoint ke kram me):** **d**ocx — **d**ocument (Word) · **x**lsx — e**x**cel (Excel) · **p**ptx — **p**resentation (PowerPoint). Teenon ka pehla akshar hi kaam batata hai.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated):** `11_COMPUTER_KNOWLEDGE-005` (Excel .xlsx), `-006` (formula '=' se shuru).
- **Actual PYQs:** **2024-P1 Q23 — Excel next-workbook shortcut = Ctrl+F6** (dataset Subtopic, key D).
- **Recurring exam angles:** extension ↔ program (.docx/.xlsx/.pptx); cell = row + column (B5); formula '=' se shuru; `=SUM(A1:A5)` ka matlab; Ctrl+F6.

### J. ACTIVE RECALL — answer from memory, then check

1. Word, Excel aur PowerPoint ke extension kya hain?
2. Cell B5 ka matlab kya hai?
3. Excel me formula kis chinh se shuru hoti hai — aur kyun?
4. `=SUM(A1:A5)` ka matlab kya hai?
5. Excel me agle workbook par jaane ka shortcut kya hai (PYQ 2024-P1 Q23)?
6. Word, Excel aur PowerPoint me se kaun sa hisab ke liye hai?
7. F2 ka kaam Excel me kya hai?

**Answers (check after attempting):** 1. Word .docx, Excel .xlsx, PowerPoint .pptx. 2. Column B, row 5 ka cell. 3. '=' se — taaki Excel samjhe ki ganana karni hai, text nahi. 4. A1 se A5 tak ke cells ko jodna. 5. Ctrl+F6. 6. Excel. 7. Cell ke andar edit karna.

### K. REVISION SUMMARY (one page — test yourself against it)

```
WORD (.docx) = likhna · EXCEL (.xlsx) = ginna · POWERPOINT (.pptx) = dikhana
CELL = column + row (B5) · FORMULA = '=' se shuru · =SUM(A1:A5) = A1 se A5 tak jodna
SHORTCUTS: Ctrl+F6 = agla workbook (PYQ 2024-P1 Q23) · F2 = cell edit karo
TRAPS: .docx ≠ .xlsx ≠ .pptx · Cell (ek) ≠ Range (kai) · '=' (shuruaat) ≠ +/− (chinh)
MNEMONIC: d–x–p (document – Excel – presentation)
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (extensions bina dekhe likho) → tomorrow (recall + bank 005, 006) → after 3 days (mixed with Chapter 2) → after 7 days (timed: bank 005–006 + Ctrl+F6).

---

## Chapter 6 — ⚠️ EXTRA: Internet & E-mail (2026 12th syllabus me NAHI)

> **EXTRA warning — low priority.** Yeh chapter official 12th syllabus me **nahi** hai (Graduation-level). Ise sirf isliye padho kyunki 2024 paper me HTTP puchha gaya tha (2024-P2 Q1). Pehle Chapters 1–5 pakke karo; yah chapter tabhi padho jab samay bache.

### A. VISUAL INTRODUCTION — jaal aur dak

```
   WEBSITE KHOLNA:                       EMAIL BHEJNA:
   Tumhara computer                      Tum ──► SMTP ──► uska inbox
        │  (URL type karo)                    (bhejna = SMTP)
        ▼
   Internet (jaal) ──► Web server
        │  (HTTP se page mango)
        ▼
   Page tumhari screen par

   EMAIL PANA: uska inbox ──► POP3 / IMAP ──► tum (pana = POP3/IMAP)
```

> **How to use this diagram:** Cover the labels and trace both flows from memory: website kaise khulti hai? Email kaise jata hai, kaise aata hai? That is retrieval practice, not reading.

### B. STORY-BASED EXPLANATION — library aur dak-khana

**WWW (World Wide Web)** ek bahut badi library hai — duniya bhar ke web pages ek jaal (web) me jude hue. Is jaal ko **Tim Berners-Lee** ne banaya tha (1989 me prastav). Tum **browser** (Chrome, Firefox, Edge) se is library me jate ho; har page ka **URL** uska pata hai.

**Email** dak-khana hai: tum patra likhte ho, **SMTP** use le jata hai (bhejne wala postman), dusre ka inbox use pa leta hai. Jab tum apna email dekhte ho, **POP3/IMAP** use tumhare inbox se tum tak lata hai (pane wala postman). **@** ka matlab "at the rate" — jaise ram@example.com matlab "ram, example.com par".

### C. WHY DOES IT HAPPEN? — HTTP kyun, SMTP/POP3 alag kyun?

- **Why HTTP/HTTPS?** Browser aur server alag-alag jagah hain — unhe baat karne ke liye ek **common bhasha** chahiye. HTTP (Hyper Text Transfer Protocol) wahi bhasha hai. **HTTPS** me 'S' = Secure — bhasha wahi, lekin baat-cheet **encrypted** (surakshit) hoti hai.
- **Why is SMTP for sending and POP3/IMAP for receiving?** Bhejna aur pana **alag kaam** hain: SMTP patra ko tumhare paas se dusre ke server tak le jata hai; POP3/IMAP dusre ke server se patra tumhare paas lata hai. Ek hi protocol dono kaam nahi karta — isiliye do naam.
- **Why is the Internet different from the WWW?** **Internet** = network (taar/wireless se jude computers). **WWW** = us network par chalne wale **web pages ka jaal**. Internet sadak hai, WWW us par chalne wali gaadiyan.
- **Why does a computer need an IP address?** Jaise har ghar ka pata hota hai, vaise har computer ki **pehchan** hoti hai — IP address. Bina pata ke data kahan jayega, pata nahi chalega.

### D. HOW DOES IT WORK? — website kholna (kram se)

1. **Browser me URL type karo** (jaise www.example.com).
2. **Browser server se HTTP se page mangta hai** (request).
3. **Server page bhejta hai** (response).
4. **Browser page ko screen par dikhata hai.**

**Email bhejna (kram se):** 1. Email likho → 2. **SMTP** use dusre ke mail server tak le jata hai → 3. Vah uske inbox me rakha jata hai → 4. Vah **POP3/IMAP** se use padhta hai.

### E. VISUAL MEMORY CONNECTION

**SMTP = bhejne wala postman; POP3/IMAP = pane wala postman.** Postman patra le jata hai (SMTP), aur dakiya tumhare post box se patra lata hai (POP3/IMAP). Dono postman hain — disha alag hai.

### F. IMPORTANT FACTS

| Shabd | Matlab |
|---|---|
| **WWW** | World Wide Web — web pages ka jaal; **Tim Berners-Lee** ne banaya |
| **HTTP / HTTPS** | Web protocol — browser aur server ki bhasha; HTTPS = Secure (encrypted) |
| **URL** | Web page ka pata (address) |
| **IP address** | Computer ki pehchan (address) |
| **Browser** | Web dekhne ka program — Chrome, Firefox, Edge |
| **Search Engine** | Dhoondhne ka auzar — Google, Bing |
| **Cloud** | Online storage — Google Drive, OneDrive |
| **Social media** | X, Facebook, Instagram |

| Email ki baat | Tathya |
|---|---|
| **SMTP** | **Bhejne** ke liye (Simple Mail Transfer Protocol) |
| **POP3 / IMAP** | **Pane** ke liye |
| **@** | "At the rate" — ram@example.com |
| **CC** | Carbon Copy — nakal dusre ko bhi |
| **BCC** | Blind Carbon Copy — nakal, bina bataye |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| Internet vs WWW | Internet = **network** (sadak). WWW = **web pages ka jaal** (gaadiyan). |
| HTTP vs HTTPS | HTTP = web bhasha. HTTPS = wahi bhasha + **Secure (encrypted)**. |
| SMTP vs POP3/IMAP | SMTP = **bhejna**. POP3/IMAP = **pana**. |
| CC vs BCC | CC = nakal, sabko **dikhai** deti hai. BCC = nakal, **bina bataye** (blind). |
| Browser vs Search Engine | Browser = **program** (Chrome). Search Engine = **website/auzar** (Google). |
| Berners-Lee vs Babbage | Berners-Lee = **WWW** ka janak. Babbage = **computer** ka janak. |

### H. MEMORY TECHNIQUE (one only)

**"SMTP = Send; POP3/IMAP = Paana."** S se **S**end (bhejna), P se **P**aana. Disha hi pehchan hai.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated, ⚠️ EXTRA):** `11_COMPUTER_KNOWLEDGE-007` (WWW), `-008` (SMTP) — dono EXTRA, low priority.
- **Actual PYQs:** **2024-P2 Q1 — HTTP = Hyper Text Transfer Protocol** (dataset Subtopic, key D). Yahi ekmatra karan hai ki yah chapter yahan hai.
- **Mock questions (generated, ⚠️ EXTRA):** P1 Q52 (WWW), P1 Q56 (E-mail), P3 Q116 (E-mail) — teeno EXTRA tagged hain.
- **Recurring exam angles:** WWW ka pura naam; HTTP ka pura naam; SMTP = bhejna, POP3/IMAP = pana; CC vs BCC.

### J. ACTIVE RECALL — answer from memory, then check

1. WWW ka pura naam kya hai aur use kisne banaya?
2. HTTP ka pura naam kya hai (PYQ 2024-P2 Q1)?
3. Email bhejne ke liye kaun sa protocol hai? Pane ke liye kaun se?
4. Internet aur WWW me kya antar hai?
5. CC aur BCC me kya antar hai?
6. Browser aur search engine me kya antar hai?

**Answers (check after attempting):** 1. World Wide Web — Tim Berners-Lee. 2. Hyper Text Transfer Protocol. 3. Bhejne ke liye SMTP; pane ke liye POP3/IMAP. 4. Internet = network; WWW = web pages ka jaal. 5. CC ki nakal sabko dikhti hai; BCC ki nakal bina bataye jati hai. 6. Browser = program (Chrome); search engine = auzar/website (Google).

### K. REVISION SUMMARY (one page — test yourself against it)

```
⚠️ EXTRA — low priority (2026 12th syllabus me NAHI)
WWW = World Wide Web (Tim Berners-Lee) · HTTP = Hyper Text Transfer Protocol (PYQ 2024-P2 Q1)
HTTPS = HTTP + Secure · URL = pata · IP = pehchan · Browser = Chrome/Firefox/Edge
EMAIL: SMTP = BHEJNA · POP3/IMAP = PAANA · @ = at the rate · CC (dikhti nakal) vs BCC (blind nakal)
TRAPS: Internet (network) ≠ WWW (jaal) · SMTP (bhejna) ≠ POP3/IMAP (pana) · Browser ≠ Search Engine
MNEMONIC: SMTP = Send · POP3/IMAP = Paana
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (flows bina dekhe banao) → tomorrow (recall + bank 007, 008) → after 3 days (mixed with Chapter 5) → after 7 days (timed: bank 007–008 + HTTP/WWW).

---

## Chapter 7 — ⚠️ EXTRA: Number System, Networking & Security (2026 12th syllabus me NAHI)

> **EXTRA warning — low priority.** Yeh chapter official 12th syllabus me **nahi** hai (Graduation-level / general awareness). Sirf PYQ-style awareness ke liye padho — pehle Chapters 1–5 pakke karo.

### A. VISUAL INTRODUCTION — switch, ghere aur deewar

```
  BINARY (switch):                 NETWORK (ghere):
  8   4   2   1  ← sthan ka maan        ┌─────────────┐
  1   0   1   0  = 8+0+2+0 = 10         │    WAN      │  desh/duniya
  (on/off = 1/0)                       │  ┌───────┐  │
                                       │  │  MAN  │  │  shahar
                                       │  │ ┌───┐ │  │
                                       │  │ │LAN│ │  │  office/school
                                       │  │ └───┘ │  │
                                       │  └───────┘  │
                                       └─────────────┘
  FIREWALL = deewar: sirf ijazat wala traffic andar aata hai.
```

> **How to use this diagram:** Cover the numbers and convert 1010 to decimal from memory. Then draw the three circles and label LAN/MAN/WAN. That is retrieval practice, not reading.

### B. STORY-BASED EXPLANATION — switch, mohalla aur chaukidar

**Binary:** Computer ke andar sirf do halat hain — bijli hai (1) ya nahi (0). Jaise light ka switch: on = 1, off = 0. Saari sankhya, akshar, photo — sab isi 0/1 se bante hain.

**Network:** Ek building ke computers jude hon to **LAN** (Local Area Network — chhota, office/school). Pure shahar ke jude hon to **MAN** (Metropolitan Area Network). Desh-duniya ke jude hon to **WAN** (Wide Area Network — Internet hi sabse bada WAN hai). **Wi-Fi** bina taar wala LAN hai. **Modem** digital ko analog me badalta hai (aur ulta) — taar wali line par bhejne ke liye. **Router** alag-alag networks ko jodta hai.

**Security:** **Virus** hanikarak program hai — computer ko nuksan pahunchata hai. **Antivirus** use dhoondh kar hatata hai. **Firewall** suraksha deewar hai — bina ijazat kisi ko andar aane nahi deta. **Phishing** nakli email/website se dhokha dekar password ya jankari lena hai. **OTP** (One Time Password) ek baar ka password hai — har baar naya.

### C. WHY DOES IT HAPPEN? — binary kyun, firewall kyun?

- **Why does a computer use binary (0/1)?** Kyunki circuit ke paas sirf do halat hain — current hai ya nahi. Do halat = do ank (0 aur 1). Isiliye computer ki bhasha binary hai.
- **Why do LAN, MAN and WAN differ?** Sirf **aakar** (size) se: LAN ek jagah, MAN ek shahar, WAN desh/duniya. Bada network = zyada computers = zyada taar/upkaran.
- **Why is a firewall different from an antivirus?** Firewall **rokta** hai — bina ijazat traffic ko andar aane nahi deta (deewar). Antivirus **hatata** hai — jo virus andar aa gaya, use dhoondh kar mita deta hai (dawai). Ek deewar hai, doosra ilaj.
- **Why is phishing dangerous even without a virus?** Kyunki phishing me koi program nahi — **insan ko dhokha** diya jata hai. Nakli email asal jaisa dikhta hai; user khud password de deta hai. Isiliye pehchan mushkil hoti hai.

### D. HOW DOES IT WORK? — decimal se binary (kram se)

**Decimal 10 → Binary:**
1. 10 ÷ 2 = 5, shesh **0** (neeche se upar likhna hai — shesh ulta kram me).
2. 5 ÷ 2 = 2, shesh **1**.
3. 2 ÷ 2 = 1, shesh **0**.
4. 1 ÷ 2 = 0, shesh **1**.
5. Shesh ulta kram me: **1010**. Isiliye decimal 10 = binary **1010**.

**Binary 101 → Decimal (sthan ka maan 4, 2, 1):**
1×4 + 0×2 + 1×1 = 4 + 0 + 1 = **5**.

### E. VISUAL MEMORY CONNECTION

**Binary = light ke switch; Network = teen ghere (LAN chhota, MAN beech, WAN bada); Firewall = ghar ki deewar.** Switch on/off yaad karo to binary yaad; ghere yaad karo to LAN/MAN/WAN yaad; deewar yaad karo to firewall yaad.

### F. IMPORTANT FACTS

| Binary conversion | Maan |
|---|---|
| Decimal 10 | Binary **1010** (8 + 2) |
| Decimal 13 | Binary **1101** (8 + 4 + 1) |
| Binary 101 | Decimal **5** (4 + 0 + 1) |
| Sthan ka maan | Daayein se: 1, 2, 4, 8, 16 … (2 ki ghat) |

| Network | Pura naam | Aakar |
|---|---|---|
| **LAN** | Local Area Network | Chhota — office, school |
| **MAN** | Metropolitan Area Network | Shahar |
| **WAN** | Wide Area Network | Desh / duniya — Internet |
| **Wi-Fi** | Wireless LAN | Bina taar ka LAN |
| **Modem** | Modulator-Demodulator | Digital ↔ Analog badalta hai |
| **Router** | — | Alag networks ko jodta hai |

| Suraksha (Security) | Matlab |
|---|---|
| **Virus** | Hanikarak program — nuksan pahunchata hai |
| **Antivirus** | Virus ko dhoondh kar hatane wala program |
| **Firewall** | Suraksha deewar — bina ijazat access rokta hai |
| **Phishing** | Nakli email/website se dhokha dekar jankari lena |
| **Strong password** | Letters + numbers + symbols ka majboot password |
| **OTP** | One Time Password — ek baar ka password |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| Binary vs Decimal | Binary = **0/1** (computer ki bhasha). Decimal = **0–9** (hamari bhasha). |
| LAN vs MAN vs WAN | Sirf **aakar**: LAN (office) < MAN (shahar) < WAN (desh/duniya). |
| Modem vs Router | Modem = **digital ↔ analog** badalta hai. Router = **networks ko jodta** hai. |
| Virus vs Antivirus | Virus = **hanikarak program**. Antivirus = **use hatane wala** program. |
| Firewall vs Antivirus | Firewall = **rokta** hai (deewar). Antivirus = **hatata** hai (ilaj). |
| Phishing vs Virus | Phishing = **dhokha** (nakli email). Virus = **hanikarak program**. |

### H. MEMORY TECHNIQUE (one only)

**"L-M-W: Local–Metro–World"** — LAN = **L**ocal (paas ka), MAN = **M**etro (shahar ka), WAN = **W**orld (duniya ka). Aakar badhta jata hai: office → shahar → duniya.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated, ⚠️ EXTRA):** `11_COMPUTER_KNOWLEDGE-009` (decimal 10 → 1010), `-010` (LAN), `-011` (phishing), `-015` (binary 101 → 5), `-016` (firewall) — sab EXTRA, low priority.
- **Actual PYQs:** is chapter se juda classified sample me **koi PYQ nahi hai**.
- **Recurring exam angles:** binary conversion (10 → 1010; 101 → 5); LAN/MAN/WAN ka kram; modem vs router; phishing ka matlab; firewall ka kaam.

### J. ACTIVE RECALL — answer from memory, then check

1. Decimal 10 ka binary kya hai? Steps ke saath batao.
2. Binary 101 ka decimal maan kya hai?
3. LAN, MAN aur WAN me aakar ka kram kya hai?
4. Modem aur router me kya antar hai?
5. Firewall aur antivirus me kya antar hai?
6. Phishing kya hai?
7. Computer binary kyun use karta hai?

**Answers (check after attempting):** 1. 1010 (10 ÷ 2 ke shesh ulta kram me: 0, 1, 0, 1 → 1010). 2. 5 (1×4 + 0×2 + 1×1). 3. LAN (office) < MAN (shahar) < WAN (desh/duniya). 4. Modem digital ↔ analog badalta hai; router networks ko jodta hai. 5. Firewall rokta hai (deewar); antivirus hatata hai (ilaj). 6. Nakli email/website se dhokha dekar jankari lena. 7. Circuit ke paas sirf do halat hain — current hai (1) ya nahi (0).

### K. REVISION SUMMARY (one page — test yourself against it)

```
⚠️ EXTRA — low priority (2026 12th syllabus me NAHI)
BINARY: 10 = 1010 · 13 = 1101 · 101 = 5 · sthan ka maan 1, 2, 4, 8 (2 ki ghat)
NETWORK: LAN (Local, office) < MAN (Metro, shahar) < WAN (Wide, duniya)
Wi-Fi = wireless LAN · Modem = digital ↔ analog · Router = networks jodta hai
SECURITY: Virus (hanikarak) · Antivirus (hatata hai) · Firewall (rokta hai — deewar)
Phishing = nakli email se dhokha · OTP = One Time Password
TRAPS: Firewall (rokna) ≠ Antivirus (hatana) · Modem (badalna) ≠ Router (jodna) · Phishing (dhokha) ≠ Virus (program)
MNEMONIC: L-M-W (Local–Metro–World)
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (binary conversions bina dekhe karo) → tomorrow (recall + bank 009, 010, 011, 015, 016) → after 3 days (mixed with Chapter 6) → after 7 days (timed: bank 009–011, 015–016 + conversions).

---

## Chapter 8 — ⚠️ EXTRA: E-Governance & Digital India (Rajasthan)

> **EXTRA warning — low priority.** Yeh chapter official 12th syllabus me **nahi** hai (Graduation-level / general awareness). Sirf isliye padho kyunki 2024 paper me DigiLocker aur Digital India puchhe gaye the (2024-P3 Q4, Q6). Pehle Chapters 1–5 pakke karo.

### A. VISUAL INTRODUCTION — ek khidki, kai sewayein

```
   ┌─────────────────────────────────────────────────┐
   │  e-MITRA KIOSK / PORTAL — "ek khidki"          │
   │                                                 │
   │   Nagrik ──► [e-Mitra] ──► Bijli · Pani ·       │
   │              [SSO login] ──► Certificate ·      │
   │              [Jan Aadhaar] ──► Sarkari yojana   │
   │                                                 │
   │   Shikayat ho to ──► RajSampark                │
   │   Payment ho to ──► UPI / BHIM                 │
   │   Kagaz ho to ──► DigiLocker                   │
   └─────────────────────────────────────────────────┘
   Ek number, ek login, ek khidki — yahi e-governance hai.
```

> **How to use this diagram:** Cover the labels and say from memory: e-Mitra kya hai? SSO kya karta hai? Shikayat kahan hoti hai? That is retrieval practice, not reading.

### B. STORY-BASED EXPLANATION — gaon se jila mukhyalaya tak

Pehle ek praman-patra ke liye gaon se jila mukhyalaya jana padta tha — din bhar ki yatra. Ab gaon ke **e-Mitra kiosk** par wahi kaam hota hai: bijli ka bill, praman-patra, yojana ka form — ek hi khidki se. **SSO Rajasthan** (Single Sign-On) ek login hai — ek baar login karo, kai sarkari sewayein khul jati hain. **Jan Aadhaar Yojana** Rajasthan ka parivar pehchan patra hai — ek parivar, ek number, sab yojanaon ke liye. Shikayat ho to **RajSampark** portal par darj karo.

Desh bhar me **Digital India (2015)** karyakram ne yahi kaam kiya: sarkari sewayein digital banao, har nagrik tak pahuchao. **UPI** (Unified Payments Interface, NPCI) se mobile se turant payment hota hai — **BHIM** usi par bana ek app hai. **Aadhaar** vyakti ki pehchan hai; **DigiLocker** kagazon ko online sambhalne ki seva hai.

### C. WHY DOES IT HAPPEN? — e-governance kyun?

- **Why e-governance?** Taaki nagrik ko sarkari kaam ke liye **yatra na karni pade, line me na khada hona pade, bicholiye par nirbhar na raho**. Sewa gaon tak pahunche, samay bache, pardarshita badhe.
- **Why one family ID (Jan Aadhaar)?** Kyunki har yojana ke liye alag-alag kagaz dena mushkil hai. Ek parivar ki **ek pehchan** se sab yojanaon me usi parivar ko pehchana ja sakta hai.
- **Why one login (SSO)?** Har seva ke liye alag password yaad rakhna mushkil hai. Ek login se kai sewayein khul jayein to kaam asan hota hai.
- **Why UPI?** Nagad (cash) le jaane aur badle ki samasya se chhutkara. Mobile se seedha bank-to-bank payment — turant, bina bicholiye.

### D. HOW DOES IT WORK? — e-Mitra se seva pana (kram se)

1. **Nagrik e-Mitra kiosk/portal par jata hai** (ya SSO se login karta hai).
2. **Seva chunta hai** — jaise janm praman-patra, bijli bill.
3. **Jankari aur shulk deta hai** — UPI se payment ho sakta hai.
4. **Receipt milti hai; seva poori hone par praman-patra milta hai** — kagaz DigiLocker me bhi sambhala ja sakta hai.

### E. VISUAL MEMORY CONNECTION

**e-Mitra = Rajasthan ka "Mitra" (friend)** — ek dost jo sarkari kaam ke liye tumhare gaon me baitha hai. **SSO = ek chabi, kai taale** — ek login se kai sewayein khulti hain. **Jan Aadhaar = parivar ka ek number** — jaise ghar ka ek pata.

### F. IMPORTANT FACTS

| Seva / Yojana | Kya hai |
|---|---|
| **SSO Rajasthan** | Single Sign-On portal — ek login se kai sarkari sewayein |
| **e-Mitra** | Rajasthan ki e-governance seva — kiosk/portal se sarkari sewayein |
| **Jan Aadhaar Yojana** | Rajasthan ka parivar pehchan patra — ek parivar, ek number |
| **RajSampark** | Shikayat portal — shikayat darj karo |

| Rashtriya karyakram | Tathya |
|---|---|
| **Digital India (2015)** | Bharat sarkar ka digital karyakram — 3 key vision areas (neeche) |
| **UPI** | Unified Payments Interface — **NPCI** dwara; mobile se turant bank-to-bank payment |
| **BHIM** | UPI par bana payment app |
| **Aadhaar** | Vyakti ki pehchan (UIDAI) |
| **DigiLocker** | Kagazon ko online sambhalne ki seva — **Ministry of Electronics & IT (MeitY)** ke antargat |

| Digital India — 3 key vision areas | Matlab |
|---|---|
| 1. Digital Infrastructure as a Core Utility to Every Citizen | Har nagrik tak digital buniyadi suvidha |
| 2. Governance and Services on Demand | Mang par shasan aur sewayein |
| 3. Digital Empowerment of Citizens | Nagrikon ka digital sashaktikaran |

### G. COMMON CONFUSIONS

| Confusion | Correct difference |
|---|---|
| e-Mitra vs SSO | e-Mitra = **sewa dene** ka kendra/portal. SSO = **ek login** se kai sewayein kholna. |
| Jan Aadhaar vs Aadhaar | Jan Aadhaar = **parivar** ki pehchan (Rajasthan). Aadhaar = **vyakti** ki pehchan (desh bhar). |
| UPI vs BHIM | UPI = **system** (NPCI). BHIM = UPI par bana **app**. |
| DigiLocker vs UPI | DigiLocker = **kagaz** sambhalna (MeitY). UPI = **payment** karna (NPCI). |
| RajSampark vs e-Mitra | RajSampark = **shikayat** darj karna. e-Mitra = **sewa** pana. |

### H. MEMORY TECHNIQUE (one only)

**"e-Mitra = Rajasthan ka Mitra; SSO = ek chabi, kai taale."** Mitra gaon me baitha dost hai; SSO ek chabi hai jo kai sewaon ke taale kholti hai.

### I. CET EXAM CONNECTION

- **Bank MCQs (generated, ⚠️ EXTRA):** `11_COMPUTER_KNOWLEDGE-012` (e-Mitra), `-013` (UPI), `-017` (Jan Aadhaar) — sab EXTRA, low priority.
- **Actual PYQs:** **2024-P3 Q4 — DigiLocker = Ministry of Electronics & IT** (dataset Subtopic, key C). **2024-P3 Q6 — Digital India key vision area NOT "promotion of behavioural changes"** (dataset Subtopic, key D) — matlab: upar wale 3 vision areas me "promotion of behavioural changes" **nahi** hai.
- **Recurring exam angles:** e-Mitra ↔ Rajasthan; UPI ↔ NPCI; Jan Aadhaar ↔ Rajasthan parivar pehchan; DigiLocker ↔ MeitY; Digital India ke 3 vision areas (aur kaun sa nahi hai).

### J. ACTIVE RECALL — answer from memory, then check

1. e-Mitra kya hai aur vah kis rajya ki seva hai?
2. SSO ka pura naam aur kaam kya hai?
3. Jan Aadhaar aur Aadhaar me kya antar hai?
4. UPI ka pura naam kya hai aur use kisne banaya (NPCI)?
5. DigiLocker kis mantralaya ke antargat hai (PYQ 2024-P3 Q4)?
6. Digital India ke 3 key vision areas kya hain — aur kaun sa ek unme nahi hai (PYQ 2024-P3 Q6)?

**Answers (check after attempting):** 1. Rajasthan ki e-governance seva — kiosk/portal se sarkari sewayein. 2. Single Sign-On — ek login se kai sarkari sewayein. 3. Jan Aadhaar = parivar ki pehchan (Rajasthan); Aadhaar = vyakti ki pehchan. 4. Unified Payments Interface — NPCI. 5. Ministry of Electronics & Information Technology (MeitY). 6. (1) Digital Infrastructure as Core Utility, (2) Governance and Services on Demand, (3) Digital Empowerment of Citizens — "promotion of behavioural changes" inme nahi hai.

### K. REVISION SUMMARY (one page — test yourself against it)

```
⚠️ EXTRA — low priority (2026 12th syllabus me NAHI)
e-MITRA = Rajasthan ki seva (ek khidki) · SSO = Single Sign-On (ek login)
JAN AADHAAR = parivar ki pehchan (Rajasthan) · AADHAAR = vyakti ki pehchan
RAJSAMPARK = shikayat portal
DIGITAL INDIA (2015): 3 vision areas — Infrastructure · Governance on Demand · Digital Empowerment
UPI = Unified Payments Interface (NPCI) · BHIM = UPI app · DigiLocker = MeitY
PYQ: DigiLocker — MeitY (2024-P3 Q4) · Vision area NOT "promotion of behavioural changes" (2024-P3 Q6)
TRAPS: e-Mitra (sewa) ≠ SSO (login) · Jan Aadhaar (parivar) ≠ Aadhaar (vyakti) · UPI (system) ≠ BHIM (app)
MNEMONIC: e-Mitra = Rajasthan ka Mitra · SSO = ek chabi, kai taale
```
**Revision schedule for this topic:** today (recall Qs above) → same day evening (seva ↔ naam matching bina dekhe) → tomorrow (recall + bank 012, 013, 017) → after 3 days (mixed with Chapter 6) → after 7 days (timed: bank 012–013, 017 + PYQ Q4/Q6).

---

## Preservation note (audit trail for this redesign)

Every fact in the old notes file (`notes/11_computer_knowledge.md`, 36 lines) is preserved below. **Facts dropped: none.**

| Old notes fact | Where it now lives |
|---|---|
| Babbage — computer ka janak (Analytical Engine); Ada Lovelace — pehli programmer | Ch 1 §B, §F |
| CPU = Brain; ALU + CU + Memory; ALU ganana, CU niyantran | Ch 2 §A, §B, §F, §G |
| Input devices: Keyboard, Mouse, Scanner, Microphone, Joystick, Webcam | Ch 4 §B, §F |
| Output devices: Monitor, Printer, Speaker, Plotter, Projector | Ch 4 §B, §F |
| RAM volatile; ROM non-volatile | Ch 2 §B, §C, §F, §G |
| Secondary: Hard Disk, SSD, Pen Drive, CD/DVD | Ch 2 §B, §F |
| Memory units: Bit < Byte (8 bit) < KB (1024 B) < MB < GB < TB < PB | Ch 2 §F (1 PB = 1024 TB added — verified via `pyq_analysis.md` P3 Q35) |
| System software OS (Windows, Linux, macOS); Application software (Word, Excel, Browser) | Ch 2 §F |
| OS ke kaam: file, memory, process, device prabandhan; GUI | Ch 2 §F |
| MS Word .docx; Excel .xlsx, cell = row + column (B5), formula '=' se (=SUM(A1:A5)); PowerPoint .pptx slide | Ch 5 §B, §D, §F |
| WWW — World Wide Web (Tim Berners-Lee); HTTP/HTTPS; URL; IP address; Browser (Chrome, Firefox, Edge) | Ch 6 §B, §F |
| Email: SMTP bhejne, POP3/IMAP pane; @; CC; BCC | Ch 6 §B, §F |
| Search Engine: Google, Bing; Social media: X, Facebook, Instagram | Ch 6 §F |
| Cloud: Google Drive, OneDrive | Ch 6 §F |
| Binary: 0/1; Decimal 10 → 1010; Decimal 13 = 1101; Binary 101 = 5 | Ch 7 §B, §D, §F |
| LAN (office), MAN (shahar), WAN (desh/duniya — Internet); Wi-Fi wireless LAN; Modem digital↔analog; Router networks jodta hai | Ch 7 §B, §F |
| Virus; Antivirus; Firewall; Phishing; strong password (letters+numbers+symbols); OTP | Ch 7 §B, §F |
| SSO Rajasthan; e-Mitra; Jan Aadhaar Yojana; RajSampark | Ch 8 §B, §F |
| Digital India (2015); UPI (NPCI); BHIM, Aadhaar, DigiLocker | Ch 8 §B, §F |
| High-priority line (in syllabus): Babbage, CPU=Brain, RAM volatile, 1 Byte=8 bit, .docx/.xlsx/.pptx, input/output devices, file system, RAM/ROM | Ch 1–5 §F/§I |
| EXTRA line (low priority): Binary, LAN/MAN/WAN, Phishing, SSO/e-Mitra, UPI | Ch 6–8 (all marked ⚠️ EXTRA) |

**New facts added (all standard textbook / verified repo facts, each labelled where used):**
- GIGO (Garbage In, Garbage Out) — Ch 1 §C/§G (standard computing concept).
- Intel 4004 (1971), 2,300 transistors — Ch 2 §I (verified: PYQ 2024-P1 Q22, `pyq_analysis.md`).
- Ctrl+F6 next workbook; F2 edit cell — Ch 5 §F (Ctrl+F6 verified: PYQ 2024-P1 Q23; F2 standard Excel shortcut, full-paper P3 Q42 read not classified — flagged in the text).
- Tim Berners-Lee, WWW prastav 1989 — Ch 6 §B (standard fact).
- Digital India 3 key vision areas — Ch 8 §F (standard Digital India programme fact; PYQ 2024-P3 Q6 tests the NOT item).
- Touchscreen = input + output — Ch 4 §A/§F (standard fact).
- Plotter = bade drawing/nakse — Ch 4 §C/§F (standard fact).
- File-system definitions (file, folder, path, extension, drive, root, operations) — Ch 3 (standard definitions; chapter honestly flagged as thin, no bank MCQ/PYQ).
- Computer characteristics (speed, accuracy, diligence, versatility, storage, automation, no IQ) — Ch 1 §F (standard textbook characteristics).

**Could not verify / flagged in the file:**
- File system: no exam evidence (no bank MCQ, no PYQ) — chapter marked thin; FAT/NTFS explicitly NOT taught (beyond 12th syllabus).
- F2 shortcut: standard Excel shortcut; the full-paper P3 Q42 reference is "read, not classified" in the repo analysis — flagged in Ch 5 §F.
- Printer item P3 Q41: mentioned in Ch 4 §I only as "read, not in the classified sample" — not presented as a verified PYQ.
- P3 Q35 (1 PB = 1024 TB): "read, not in sample" in the repo analysis; included in the memory-units table as standard fact, flagged here.
