import random
def Q(q, opts4, ans, expl, topic, diff="Medium"):
    assert 0<=ans<4
    o=list(opts4); correct=o[ans]
    random.shuffle(o); idx=o.index(correct)
    o=o+["E. Unanswered / अनुत्तरित"]
    return {"q":q,"opts":o,"ans":idx,"expl":expl,"topic":topic,"diff":diff}
forts=[
 ("Chittorgarh Fort","Chittorgarh","Maurya / Mewar — Maharana Kumbha era expansion","Largest fort in India; Vijay Stambh; Jauhar of Rani Padmini (1303) & Rani Karnavati (1535)"),
 ("Kumbhalgarh Fort","Rajsamand","Maharana Kumbha (15th c.)","Second-longest wall in world after Great Wall (~36 km); birthplace of Maharana Pratap"),
 ("Mehrangarh Fort","Jodhpur","Rao Jodha (1459)","On Bhakurcheeria hill; Rao Jodha founded Jodhpur; Chamunda Devi temple"),
 ("Amber (Amer) Fort","Jaipur","Raja Man Singh I (1592)","Sheesh Mahal; Maota Lake; UNESCO Hill Forts of Rajasthan"),
 ("Junagarh Fort","Bikaner","Raja Rai Singh (1589-94)","Never conquered; Anup Mahal; not built on a hill"),
 ("Jaisalmer Fort (Sonar Quila)","Jaisalmer","Rawal Jaisal (1156)","Living fort; golden sandstone; UNESCO Hill Forts"),
 ("Ranthambore Fort","Sawai Madhopur","Chauhan (10th c., Hammir Dev)","Inside Ranthambore Tiger Reserve; UNESCO Hill Forts; Trinetra Ganesh temple"),
 ("Gagron Fort","Jhalawar","Dodal / Khinchi Chauhan","Water fort — Ahu & Kali Sindh rivers; UNESCO Hill Forts; only water fort in Rajasthan"),
]
rivers=[
 ("Chambal","Janapav (Mhow, MP)","Yamuna (U.P.)","Longest river of Rajasthan; Kota, Rawatbhata atomic power, Chambal ravines"),
 ("Banas","Khamnor hills, Rajsamand","Chambal near Rameshwar","Longest river flowing entirely within Rajasthan (~512 km); Bisalpur Dam"),
 ("Luni","Nag Pahar, Ajmer","Rann of Kutch","Only major west-flowing river of Rajasthan; saline downstream; Balotra"),
 ("Sabarmati","Aravalli, Udaipur","Gulf of Khambhat","Flows through Gujarat; short course in Rajasthan"),
 ("Mahi","Madhya Pradesh (Vindhyas)","Gulf of Khambhat","Flows through Banswara/Dungarpur; Mahi Bajaj Sagar Dam"),
 ("Ghaggar","Shivalik, Himachal","dies in Thar / Hakra","Seasonal; Saraswati identification debated; Hanumangarh-Ganganagar"),
 ("Banganga","Bairath hills, Jaipur","Yamuna (via Gambhir)","Also called Arjun ki Ganga; Ramgarh Dam on it"),
 ("Kali Sindh","Dewas, MP","Chambal","Flows through Jhalawar-Kota; Jhalrapatan"),
]
lakes=[
 ("Sambhar Lake","Jaipur / Nagaur / Ajmer border","India's largest inland saline lake; salt production; Ramsar site"),
 ("Pichola Lake","Udaipur","Built by Banjara in 1362, expanded by Maharana Udai Singh; Lake Palace, Jag Mandir"),
 ("Fateh Sagar Lake","Udaipur","Built by Maharana Jai Singh (1687), rebuilt by Maharana Fateh Singh; Nehru Park island"),
 ("Pushkar Lake","Ajmer","Sacred lake; Brahma temple nearby; Pushkar Fair (Kartik Purnima)"),
 ("Ana Sagar Lake","Ajmer","Built by Anaji Chauhan (Arnoraj); Daulat Bagh by Jahangir"),
 ("Nakki Lake","Mount Abu (Sirohi)","Only natural lake in Aravalli region, Mount Abu; believed dug by gods' nails"),
 ("Rajsamand Lake","Rajsamand","Built by Maharana Raj Singh (1662-76); Raj Prashasti — longest Sanskrit inscription"),
 ("Jaisamand Lake","Udaipur (Salumbar)","Built by Maharana Jai Singh (1685-91); second-largest artificial lake in Asia (then); Dhebar Lake"),
]
dances=[
 ("Ghoomar","Marwar / Mewar — women, festive","State dance of Rajasthan; graceful swirling ghaghra"),
 ("Kalbeliya","Kalbeliya (snake-charmer) community","UNESCO Intangible Heritage 2010; 'Sapera' dance; Gulabo Sapera"),
 ("Terah Taali","Ramdevra (Pabuji devotees, Kamad caste)","13 manjiras tied to body; performed sitting, to Pabuji's tales"),
 ("Chang Dhap","Shekhawati — Holi","Chang (daff) instrument, men dance at Holi"),
 ("Bhavai","Rajasthan — balancing pots","Balancing pots on head; famous in Nagaur, Jodhpur"),
 ("Kathputli","Marwar / Nagaur (Bhat community)","Puppet dance; Nat Bhat community"),
 ("Kachchhi Ghodi","Shekhawati","Dummy horse dance; men at weddings/fairs"),
 ("Fire Dance (Agni Nritya)","Bikaner — Jasnathi sect","Dancing on burning embers; Jasnath sect devotees"),
]
rulers=[
 ("Maharana Pratap","Mewar (Udaipur)","1572–1597","Battle of Haldighati 18 June 1576 vs Akbar's army (Man Singh); Chetak horse"),
 ("Maharana Kumbha","Mewar","1433–1468","Built 32 forts incl. Kumbhalgarh; Vijay Stambh (1440-48) vs Mahmud Khilji; wrote Sangeet Raj"),
 ("Rana Sanga","Mewar","1508–1528","Battle of Khanwa 1527 vs Babur; united Rajput confederacy"),
 ("Rao Jodha","Marwar","1438–1489","Founded Jodhpur 1459; built Mehrangarh"),
 ("Maharaja Ganga Singh","Bikaner","1888–1943","Built Ganga Canal (1927, from Sutlej); represented India at Versailles 1919"),
 ("Prithviraj Chauhan III","Ajmer-Delhi","1178–1192","Second Battle of Tarain 1192 vs Muhammad Ghori; First Tarain 1191 — Prithviraj won; Chand Bardai"),
 ("Maharaja Man Singh I","Amber (Jaipur)","1589–1614","Navratna of Akbar; built Amber Fort; Mughal general"),
 ("Maharana Udai Singh II","Mewar","1540–1572","Founded Udaipur 1559; shifted capital from Chittorgarh after 1567 siege by Akbar"),
]
def build_raj():
    raj=[]
    for name,dist,builder,note in forts:
        raj.append(Q(f"Which district is {name} located in? / {name} किस जिले में स्थित है?",[dist,"Udaipur","Kota","Bikaner"],0,f"{name} is in {dist}. {note}","Raj: Forts","Easy"))
        raj.append(Q(f"Who built / is chiefly associated with {name}? / {name} का निर्माण किससे संबंधित है?",[builder,"Maharaja Ranjit Singh","Maharana Sanga","Raja Bhoj"],0,note,"Raj: Forts","Medium"))
        raj.append(Q(f"{name} is famous for — / {name} किसके लिए प्रसिद्ध है?",[note.split(';')[0],"Tea gardens","Iron mines","A sea port"],0,note,"Raj: Forts","Medium"))
    for name,src,mouth,note in rivers:
        raj.append(Q(f"Where does the {name} river originate? / {name} नदी का उद्गम कहाँ है?",[src,"Mount Abu","Guru Shikhar","Pachpadra"],0,f"{name}: {src} → {mouth}. {note}","Raj: Rivers","Medium"))
        raj.append(Q(f"The {name} river finally joins / ends in — / {name} नदी अंत में कहाँ मिलती है?",[mouth,"Arabian Sea directly","Bay of Bengal","Lake Pichola"],0,note,"Raj: Rivers","Medium"))
        raj.append(Q(f"Which statement about the {name} river is correct? / {name} नदी के बारे में सही कथन है —",[note,"It originates in the Himalayas and forms a delta","It is a tributary of the Narmada","It flows only in Gujarat"],0,note,"Raj: Rivers","Hard"))
    for name,dist,note in lakes:
        raj.append(Q(f"{name} is located in which district/place? / {name} कहाँ स्थित है?",[dist,"Kota","Bikaner","Jhalawar"],0,note,"Raj: Lakes","Easy"))
        raj.append(Q(f"{name} is known for — / {name} किसके लिए जाना जाता है?",[note,"A hydroelectric dam of 1000 MW","A coal mine","A tea estate"],0,note,"Raj: Lakes","Medium"))
    for name,comm,note in dances:
        raj.append(Q(f"{name} dance is associated with — / {name} नृत्य किससे संबंधित है?",[comm,"Bhil tribe only, Banswara","Kathak gharana, Delhi","Bharatanatyam, Tamil Nadu"],0,note,"Raj: Folk Dance","Medium"))
        raj.append(Q(f"Which fact about {name} is correct? / {name} के बारे में सही तथ्य है —",[note,"It is a classical dance of Kerala","It is performed only in Punjab","It originated in Bengal"],0,note,"Raj: Folk Dance","Hard"))
    for name,state,period,note in rulers:
        raj.append(Q(f"{name} is associated with which state/kingdom and period? / {name} किस राज्य/काल से संबंधित हैं?",[f"{state}, {period}","Marwar, 1700–1750","Delhi Sultanate, 1206–1290","Gujarat, 1400–1450"],0,note,"Raj: History","Medium"))
        raj.append(Q(f"Which event is associated with {name}? / {name} से कौन-सी घटना संबंधित है?",[note,"Battle of Plassey 1757","Third Battle of Panipat 1761","Revolt of 1857 at Delhi only"],0,note,"Raj: History","Medium"))
    extra=[
     ("Rajasthan was formed (unification completed) on — / राजस्थान का एकीकरण कब पूर्ण हुआ?",["1 November 1956","15 August 1947","26 January 1950","1 November 2000"],0,"Final unification 1 Nov 1956 (Ajmer-Merwara merged). First stage 18 Mar 1948 (Matsya Sangh).","Raj: Polity","Easy"),
     ("The first Chief Minister of Rajasthan was — / राजस्थान के प्रथम मुख्यमंत्री कौन थे?",["Heera Lal Shastri","Mohan Lal Sukhadia","Tika Ram Paliwal","Bhairon Singh Shekhawat"],0,"Heera Lal Shastri (1949–1951). Mohan Lal Sukhadia was longest-serving CM.","Raj: Polity","Easy"),
     ("Rajasthan's State Bird is — / राजस्थान का राज्य पक्षी है —",["Great Indian Bustard (Godawan)","Peacock","Sarus Crane","Indian Roller"],0,"Godawan — critically endangered, Desert National Park (Jaisalmer).","Raj: Symbols","Easy"),
     ("Rajasthan's State Tree is — / राजस्थान का राज्य वृक्ष है —",["Khejri","Banyan","Neem","Teak"],0,"Khejri (Prosopis cineraria) — sacred in Bishnoi tradition (Khejarli 1730, Amrita Devi).","Raj: Symbols","Easy"),
     ("Rajasthan's State Flower is — / राजस्थान का राज्य पुष्प है —",["Rohida","Lotus","Marigold","Rose"],0,"Rohida (Tecomella undulata) — also called Marwar teak.","Raj: Symbols","Easy"),
     ("The Thar Desert is also known as — / थार मरुस्थल को और किस नाम से जाना जाता है?",["Marusthali","Malwa Plateau","Deccan Trap","Terai"],0,"Thar = Marusthali, ~60% in Rajasthan; Luni is its main river.","Raj: Geography","Easy"),
     ("Guru Shikhar is — / गुरु शिखर क्या है?",["Highest peak of Aravalli in Rajasthan (1,722 m, Mount Abu, Sirohi)","Highest peak of India","A river in Mewar","A fort in Jodhpur"],0,"Guru Shikhar 1,722 m, Mount Abu — highest point of Aravalli and Rajasthan.","Raj: Geography","Easy"),
     ("The Aravalli range runs in which direction in Rajasthan? / अरावली श्रृंखला किस दिशा में फैली है?",["South-west to north-east","North-west to south-east","East to west","North to south"],0,"Aravalli runs SW–NE, dividing Rajasthan into eastern (fertile) and western (arid) parts.","Raj: Geography","Easy"),
     ("Which city is known as the 'Blue City'? / 'नीला शहर' किसे कहा जाता है?",["Jodhpur","Jaipur","Udaipur","Bikaner"],0,"Jodhpur — Blue City. Jaipur — Pink City; Udaipur — Lake City; Jaisalmer — Golden City.","Raj: Geography","Easy"),
     ("Which city is known as the 'Pink City'? / 'गुलाबी शहर' किसे कहा जाता है?",["Jaipur","Jodhpur","Kota","Ajmer"],0,"Jaipur — Pink City (painted pink 1876 for Prince of Wales visit, Maharaja Ram Singh II).","Raj: Geography","Easy"),
     ("Pushkar Fair is held in which month? / पुष्कर मेला किस माह में लगता है?",["Kartik (Oct–Nov)","Chaitra","Shravan","Magh"],0,"Pushkar Fair — Kartik Purnima (Oct–Nov), Ajmer; famous camel fair.","Raj: Fairs","Easy"),
     ("The Desert Festival is held at — / मरु महोत्सव कहाँ मनाया जाता है?",["Jaisalmer","Barmer","Bikaner","Jodhpur"],0,"Desert Festival — Jaisalmer (Jan–Feb); Camel Festival — Bikaner (Jan).","Raj: Fairs","Easy"),
     ("Kalbeliya dance was inscribed by UNESCO in — / कालबेलिया नृत्य UNESCO सूची में कब शामिल हुआ?",["2010","2005","2015","2020"],0,"Kalbeliya — UNESCO Intangible Heritage, 2010.","Raj: Culture","Medium"),
     ("Vijay Stambh at Chittorgarh was built by — / विजय स्तंभ किसने बनवाया?",["Maharana Kumbha","Maharana Pratap","Rana Sanga","Maharana Udai Singh"],0,"Vijay Stambh (1440–48) by Kumbha for victory over Mahmud Khilji; 9 storeys.","Raj: History","Easy"),
     ("Battle of Haldighati was fought in — / हल्दीघाटी का युद्ध कब हुआ?",["1576","1527","1192","1761"],0,"Haldighati — 18 June 1576, Maharana Pratap vs Mughal army led by Man Singh.","Raj: History","Easy"),
     ("Battle of Khanwa was fought between Babur and — / खानवा का युद्ध बाबर और किसके बीच हुआ?",["Rana Sanga","Maharana Pratap","Prithviraj Chauhan","Rao Jodha"],0,"Khanwa 1527 — Babur vs Rana Sanga's Rajput confederacy.","Raj: History","Easy"),
     ("The Matsya Sangh (first stage of unification) included — / मत्स्य संघ में कौन-से राज्य थे?",["Alwar, Bharatpur, Dholpur, Karauli","Jaipur, Jodhpur, Udaipur, Bikaner","Kota, Bundi, Jhalawar","Ajmer, Kishangarh"],0,"Matsya Sangh 18 Mar 1948 — Alwar, Bharatpur, Dholpur, Karauli.","Raj: Polity","Medium"),
     ("Rajasthan Legislative Assembly has how many seats? / विधानसभा में कितनी सीटें हैं?",["200","250","180","150"],0,"Vidhan Sabha — 200 seats. Lok Sabha — 25; Rajya Sabha — 10.","Raj: Polity","Easy"),
     ("Rajasthan sends how many members to Lok Sabha? / लोकसभा में कितने सदस्य?",["25","20","29","33"],0,"Lok Sabha 25, Rajya Sabha 10.","Raj: Polity","Easy"),
     ("The High Court of Rajasthan is located at — / राजस्थान उच्च न्यायालय कहाँ है?",["Jodhpur (principal seat); Jaipur bench","Jaipur only","Udaipur","Kota"],0,"Principal seat Jodhpur (estd. 1949), bench at Jaipur.","Raj: Polity","Easy"),
     ("Indira Gandhi Canal originates from — / इंदिरा गांधी नहर कहाँ से निकलती है?",["Harike Barrage (Sutlej-Beas, Punjab)","Bhakra Dam","Bisalpur Dam","Tehri Dam"],0,"Indira Gandhi Canal — from Harike Barrage; longest canal in India (~649 km main).","Raj: Economy","Medium"),
     ("Bisalpur Dam is built on which river? / बीसलपुर बांध किस नदी पर है?",["Banas","Chambal","Luni","Mahi"],0,"Bisalpur — Banas, Tonk; drinking water to Jaipur, Ajmer, Tonk.","Raj: Economy","Easy"),
     ("Rana Pratap Sagar Dam is on — / राणा प्रताप सागर बांध किस नदी पर है?",["Chambal","Banas","Mahi","Sabarmati"],0,"Rana Pratap Sagar — Chambal, Rawatbhata; Chambal Valley Project.","Raj: Economy","Medium"),
     ("Rajasthan's largest district by area is — / क्षेत्रफल में सबसे बड़ा जिला है —",["Jaisalmer","Bikaner","Barmer","Jodhpur"],0,"Jaisalmer — largest by area (~38,401 sq km); Dholpur smallest (before 2023 changes).","Raj: Geography","Easy"),
     ("Rajasthan is India's largest producer of — / राजस्थान किसके उत्पादन में प्रथम है?",["Mustard (also bajra, guar, wool)","Rice","Tea","Coffee"],0,"Rajasthan leads in mustard, bajra, guar, moth, wool; also marble, zinc, lead.","Raj: Economy","Medium"),
     ("Zawar mines (Udaipur) are famous for — / जावर खानें किसके लिए प्रसिद्ध हैं?",["Zinc and lead","Coal","Iron ore","Gold"],0,"Zawar — zinc-lead; Rampura Agucha (Bhilwara) — large zinc-lead deposit.","Raj: Economy","Medium"),
     ("Rajasthan's famous marble comes mainly from — / प्रसिद्ध संगमरमर मुख्यतः कहाँ से आता है?",["Makrana (Nagaur)","Kota","Jaisalmer","Bikaner"],0,"Makrana marble — used in Taj Mahal.","Raj: Economy","Easy"),
     ("Blue Pottery is associated with — / ब्लू पॉटरी किससे संबंधित है?",["Jaipur","Jodhpur","Udaipur","Bikaner"],0,"Blue Pottery — Jaipur (Persian origin, quartz/frit, no clay).","Raj: Art","Easy"),
     ("Pichwai painting is associated with — / पिछवाई चित्रकला किससे संबंधित है?",["Nathdwara (Rajsamand)","Kota","Bundi","Bikaner"],0,"Pichwai — Nathdwara, Shrinathji temple cloth paintings; Mewar school.","Raj: Art","Medium"),
     ("Phad painting is associated with — / फड़ चित्रकला किससे संबंधित है?",["Shahpura (Bhilwara) — Pabuji & Devnarayan tales","Jaipur court","Kota-Bundi","Jaisalmer"],0,"Phad — Shahpura; scroll paintings of Pabuji/Devnarayan, Joshi family.","Raj: Art","Medium"),
     ("The Khejarli massacre (1730) is associated with — / खेजड़ली बलिदान (1730) किससे संबंधित है?",["Bishnoi community protecting Khejri trees (Amrita Devi)","Rajput revolt vs Mughals","Peasant revolt in Shekhawati","1857 revolt"],0,"Khejarli 1730 — 363 Bishnois led by Amrita Devi saved Khejri trees; origin of Chipko ethos.","Raj: History","Medium"),
     ("Desert National Park is in — / मरु राष्ट्रीय उद्यान कहाँ है?",["Jaisalmer-Barmer","Udaipur","Kota","Bharatpur"],0,"Desert National Park — Jaisalmer-Barmer; Great Indian Bustard habitat.","Raj: Environment","Easy"),
     ("Keoladeo National Park is in — / केवलादेव राष्ट्रीय उद्यान कहाँ है?",["Bharatpur","Alwar","Sawai Madhopur","Kota"],0,"Keoladeo (Bharatpur) — UNESCO World Heritage, Ramsar; Siberian cranes in winter.","Raj: Environment","Easy"),
     ("Ranthambore National Park is famous for — / रणथंभौर किसके लिए प्रसिद्ध है?",["Tigers","Lions","Rhinos","Elephants"],0,"Ranthambore — tigers; Project Tiger reserve (1973). Sariska (Alwar) also tiger reserve.","Raj: Environment","Easy"),
     ("Sariska Tiger Reserve is in — / सरिस्का बाघ अभयारण्य कहाँ है?",["Alwar","Jaipur","Bharatpur","Dausa"],0,"Sariska — Alwar; tigers reintroduced 2008 after local extinction.","Raj: Environment","Easy"),
     ("Dhundhari dialect is spoken mainly in — / ढूँढाड़ी बोली मुख्यतः कहाँ बोली जाती है?",["Jaipur region","Jodhpur region","Udaipur region","Bikaner region"],0,"Dhundhari — Jaipur (Dhundhar); Marwari — Jodhpur; Mewari — Udaipur; Harauti — Kota-Bundi.","Raj: Language","Medium"),
     ("Which is the official language of Rajasthan? / राजस्थान की राजभाषा है —",["Hindi","Rajasthani","Marwari","English"],0,"Hindi is official language (1956 Act); Rajasthani is not in 8th Schedule (demand pending).","Raj: Polity","Easy"),
     ("Panchayati Raj was first introduced in India at — / पंचायती राज सर्वप्रथम कहाँ से शुरू हुआ?",["Nagaur (2 Oct 1959, by Nehru)","Jaipur","Jodhpur","Udaipur"],0,"Panchayati Raj inaugurated 2 Oct 1959 at Nagaur by PM Nehru (Balwant Rai Mehta Committee).","Raj: Polity","Medium"),
     ("The 73rd Constitutional Amendment relates to — / 73वाँ संशोधन किससे संबंधित है?",["Panchayati Raj","Municipalities","Fundamental Rights","Centre-State relations"],0,"73rd (1992/93) — Panchayati Raj; 74th — Municipalities.","Raj: Polity","Easy"),
     ("RPSC is headquartered at — / RPSC का मुख्यालय कहाँ है?",["Ajmer","Jaipur","Jodhpur","Udaipur"],0,"RPSC — Ajmer (estd. 1949). RSSB — Jaipur.","Raj: Polity","Easy"),
     ("RSSB is headquartered at — / RSSB का मुख्यालय कहाँ है?",["Jaipur","Ajmer","Jodhpur","Kota"],0,"RSSB — Jaipur (formed 2014).","Raj: Polity","Easy"),
     ("Which Rajasthan scheme provides free medicines? / निःशुल्क दवा योजना कौन-सी है?",["Mukhyamantri Nishulk Dava Yojana (2011)","Ayushman Bharat only","Janani Suraksha Yojana","PM-JAY only"],0,"Nishulk Dava Yojana (Oct 2011) — free essential medicines at govt hospitals.","Raj: Schemes","Medium"),
     ("Chiranjeevi / Mukhyamantri Ayushman Arogya Yojana provides health cover of — / चिरंजीवी योजना में बीमा कितने का है?",["₹25 lakh per family per year","₹5 lakh","₹10 lakh","₹1 lakh"],0,"Chiranjeevi (2021) — ₹25 lakh cover; renamed Mukhyamantri Ayushman Arogya Yojana (2024). Verify current name/limit.","Raj: Schemes","Medium"),
     ("The VB-G RAM G Act, 2025 relates to — / VB-G RAM G अधिनियम, 2025 किससे संबंधित है?",["Rural employment guarantee replacing MGNREGA","Urban housing","Crop insurance","Skill development only"],0,"VB-G RAM G Act, 2025 — replaces MGNREGA (2005); 125 days' guarantee (up from 100), passed Dec 2025.","Raj: CA/Schemes","Hard"),
     ("Rajasthan's Unfair Means (Prevention) Act was passed in — / अनुचित साधन निवारण अधिनियम कब पारित हुआ?",["2022","2019","2024","2016"],0,"Rajasthan Public Examination (Prevention of Unfair Means) Act, 2022 — anti-paper-leak law.","Raj: Polity","Hard"),
     ("Dilwara Temples are located at — / दिलवाड़ा मंदिर कहाँ हैं?",["Mount Abu (Sirohi)","Udaipur","Chittorgarh","Ajmer"],0,"Dilwara Jain temples — Mount Abu; Vimal Vasahi (1031), Luna Vasahi; marble carving.","Raj: Culture","Easy"),
     ("Karni Mata Temple (Rat Temple) is at — / करणी माता मंदिर कहाँ है?",["Deshnoke (Bikaner)","Nagaur","Jaisalmer","Barmer"],0,"Karni Mata — Deshnoke, Bikaner; rats (kabbas) sacred.","Raj: Culture","Easy"),
     ("The famous 'Kota Doria' is — / कोटा डोरिया क्या है?",["A lightweight cotton fabric (saree) from Kota","A dance","A fort","A sweet"],0,"Kota Doria — GI-tagged lightweight cotton-silk fabric from Kota/Kaithoon.","Raj: Art","Medium"),
     ("Bikaneri Bhujia has — / बीकानेरी भुजिया को क्या मिला है?",["GI tag","UNESCO tag","National award only","Patent"],0,"Bikaneri Bhujia — GI tag; also Kota Doria, Blue Pottery, Kathputli, Molela, Sanganeri, Bagru have GI tags.","Raj: Art","Medium"),
     ("Rajasthan's largest solar park is at — / सबसे बड़ा सोलर पार्क कहाँ है?",["Bhadla (Jodhpur district)","Jaisalmer city","Barmer","Bikaner"],0,"Bhadla Solar Park — Phalodi/Jodhpur; one of world's largest (~2,245 MW).","Raj: Economy","Medium"),
     ("Rajasthan's sex ratio (Census 2011) is — / लिंगानुपात (2011) है —",["928 females per 1000 males","943","919","987"],0,"Sex ratio 2011 — 928; child sex ratio 888; literacy 66.1%.","Raj: Census","Medium"),
     ("Rajasthan's literacy rate (Census 2011) is — / साक्षरता दर (2011) है —",["66.1%","74.0%","61.4%","69.7%"],0,"Literacy 2011 — 66.1% (India 73.0%); Kota highest, Jalore lowest district.","Raj: Census","Medium"),
     ("Rajasthan's population (2011 Census) was about — / जनसंख्या (2011) लगभग —",["6.85 crore","5.65 crore","7.85 crore","4.85 crore"],0,"Population 2011 — 6.85 crore; largest state by area (342,239 sq km).","Raj: Census","Easy"),
     ("Rajasthan is the largest state of India by — / राजस्थान भारत का सबसे बड़ा राज्य है —",["Area","Population","GDP","Forest cover"],0,"Largest by area (342,239 sq km, ~10.4% of India); 7th by population (2011).","Raj: Geography","Easy"),
     ("Tejaji Fair is held at — / तेजाजी मेला कहाँ लगता है?",["Parbatsar (Nagaur)","Pushkar","Deshnoke","Salasar"],0,"Tejaji Fair — Parbatsar, Nagaur; Tejaji is folk deity, protector from snakebite.","Raj: Fairs","Medium"),
     ("Ramdevra Fair is held at — / रामदेवरा मेला कहाँ लगता है?",["Ramdevra (Jaisalmer district)","Nagaur","Bikaner","Barmer"],0,"Ramdevra Fair — Ramdevra, Jaisalmer; Baba Ramdev — Hindu-Muslim folk deity.","Raj: Fairs","Medium"),
     ("Pabuji is worshipped as — / पाबूजी किस रूप में पूजे जाते हैं?",["Folk deity (Lok Devta), protector of camels","King of Mewar","Saint of Ajmer","Mughal general"],0,"Pabuji — Lok Devta, camel protector; Phad painting narrates his tale.","Raj: Culture","Medium"),
     ("Gogaji is worshipped as — / गोगाजी किस रूप में पूजे जाते हैं?",["Snake god (Nag Devta)","Rain god","War god","Sun god"],0,"Gogaji (Jaharveer) — snake god; Gogamedi fair (Hanumangarh).","Raj: Culture","Medium"),
     ("The 'Bhamashah Yojana' relates to — / भामाशाह योजना किससे संबंधित है?",["Direct benefit transfer to women heads of family","Free housing","Crop loan waiver","Student scholarship only"],0,"Bhamashah Yojana (2014) — DBT to bank accounts of women family heads.","Raj: Schemes","Medium"),
     ("Which is Rajasthan's first UNESCO World Heritage Site? / प्रथम UNESCO स्थल —",["Keoladeo National Park (1985)","Jantar Mantar, Jaipur","Hill Forts of Rajasthan","Jaipur City"],0,"Keoladeo (1985) — first; Jantar Mantar (2010), Hill Forts (2013), Jaipur City (2019).","Raj: Culture","Medium"),
     ("Jantar Mantar, Jaipur was built by — / जंतर-मंतर किसने बनवाया?",["Maharaja Sawai Jai Singh II","Maharana Kumbha","Raja Man Singh","Maharaja Ram Singh II"],0,"Jantar Mantar Jaipur (1734) — Sawai Jai Singh II; Samrat Yantra; UNESCO 2010.","Raj: History","Easy"),
     ("Jaipur city was founded in — / जयपुर की स्थापना कब हुई?",["1727","1592","1459","1559"],0,"Jaipur founded 1727 by Sawai Jai Singh II; designed by Vidyadhar Bhattacharya.","Raj: History","Easy"),
     ("Hawa Mahal was built by — / हवा महल किसने बनवाया?",["Maharaja Sawai Pratap Singh (1799)","Sawai Jai Singh II","Man Singh I","Ram Singh II"],0,"Hawa Mahal (1799) — Sawai Pratap Singh; 953 windows, 5 storeys.","Raj: History","Easy"),
     ("The 'Shekhawati' region is known for — / शेखावाटी किसके लिए प्रसिद्ध है?",["Painted havelis / frescoes","Desert dunes only","Tea gardens","Iron mines"],0,"Shekhawati (Sikar-Jhunjhunu-Churu) — painted havelis; 'open-air art gallery'.","Raj: Culture","Medium"),
     ("Which river is called the 'Lifeline of Marwar'? / 'मारवाड़ की जीवनरेखा' किस नदी को कहा जाता है?",["Luni","Chambal","Banas","Mahi"],0,"Luni — lifeline of Marwar (western Rajasthan); saline downstream.","Raj: Rivers","Medium"),
     ("Rajasthan's only hill station is — / राजस्थान का एकमात्र पर्वतीय स्थल है —",["Mount Abu","Udaipur","Kota","Alwar"],0,"Mount Abu (Sirohi) — only hill station; Dilwara, Nakki Lake, Guru Shikhar.","Raj: Geography","Easy"),
     ("The 'Hadoti' region comprises — / हाड़ौती क्षेत्र में कौन-से जिले आते हैं?",["Kota, Bundi, Baran, Jhalawar","Jaipur, Alwar, Bharatpur","Jodhpur, Nagaur, Pali","Udaipur, Rajsamand, Dungarpur"],0,"Hadoti — Kota, Bundi, Baran, Jhalawar (Hada Chauhan region).","Raj: Geography","Medium"),
     ("Rajasthan's first woman Governor was — / प्रथम महिला राज्यपाल कौन थीं?",["Pratibha Patil","Kamla Beniwal","Margaret Alva","Draupadi Murmu"],0,"Pratibha Patil — first woman Governor of Rajasthan (2004–2007); later President (2007–12).","Raj: Polity","Medium"),
     ("Kotputli-Behror district was created in which year (2023 new districts)? / कोटपूतली-बहरोड़ जिला किस वर्ष बना?",["2023","2019","2021","2025"],0,"Created 2023. NOTE: In Dec 2024 Rajasthan govt abolished 9 of 17 new 2023 districts; Kotputli-Behror retained — verify current list before exam.","Raj: Polity","Hard"),
     ("Deeg district was created in which year? / डीग जिला किस वर्ष बना?",["2023","2019","2021","2025"],0,"Deeg — new district 2023, retained; Deeg palaces (Bharatpur rulers). Verify current list.","Raj: Polity","Hard"),
     ("Khairthal-Tijara district was created in which year? / खैरथल-तिजारा जिला किस वर्ष बना?",["2023","2019","2021","2025"],0,"Khairthal-Tijara — new district 2023, retained (Alwar region). Verify current list.","Raj: Polity","Hard"),
     ("Phalodi district was created in which year? / फलोदी जिला किस वर्ष बना?",["2023","2019","2021","2025"],0,"Phalodi — new district 2023, retained (Jodhpur region). Verify current list.","Raj: Polity","Hard"),
    ]
    raj.extend([Q(q,o,a,e,t,d) for q,o,a,e,t,d in extra])
    random.shuffle(raj)
    return raj
