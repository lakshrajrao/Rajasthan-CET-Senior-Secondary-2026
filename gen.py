#!/usr/bin/env python3
import random, csv, os, sys
random.seed(20261201)
OUT="/home/hatch/workspace/cet-2026"
def Q(q, opts4, ans, expl, topic, diff="Medium"):
    assert 0<=ans<4
    o=list(opts4); correct=o[ans]
    random.shuffle(o); idx=o.index(correct)
    o=o+["E. Unanswered / अनुत्तरित"]
    return {"q":q,"opts":o,"ans":idx,"expl":expl,"topic":topic,"diff":diff}
def fmt_opts(o):
    return "\n".join(f"   ({chr(65+i)}) {v}" for i,v in enumerate(o))

# ---------- PART 2: ALL OTHER SUBJECTS (balanced, not Raj-only) ----------
geo=[]
geo_data=[
 ("India's longest river is — / भारत की सबसे लंबी नदी है —",["Ganga","Yamuna","Godavari","Narmada"],0,"Ganga (~2,525 km) — longest river in India; Godavari is longest peninsular river.","Geo India","Easy"),
 ("The largest state of India by area is — / क्षेत्रफल में भारत का सबसे बड़ा राज्य है —",["Rajasthan","Madhya Pradesh","Maharashtra","Uttar Pradesh"],0,"Rajasthan (342,239 sq km) — largest; UP is most populous.","Geo India","Easy"),
 ("The Tropic of Cancer passes through how many Indian states? / कर्क रेखा भारत के कितने राज्यों से गुजरती है?",["8","6","7","9"],0,"8 states: Gujarat, Rajasthan, MP, Chhattisgarh, Jharkhand, West Bengal, Tripura, Mizoram.","Geo India","Medium"),
 ("Which is the highest peak in India? / भारत की सबसे ऊँची चोटी है —",["Kangchenjunga (K2 is in PoK, claimed)","Mount Everest","Nanda Devi","Anamudi"],0,"Kangchenjunga (8,586 m, Sikkim) — highest peak within India; K2 (8,611 m) is in PoK.","Geo India","Easy"),
 ("The Thar Desert lies mainly in — / थार मरुस्थल मुख्यतः किस राज्य में है?",["Rajasthan","Gujarat only","Punjab only","Haryana only"],0,"Thar — mainly Rajasthan (~60%), also Gujarat, Punjab, Haryana, Pakistan (Cholistan).","Geo India","Easy"),
 ("The Western Ghats are also known as — / पश्चिमी घाट को और किस नाम से जाना जाता है?",["Sahyadri","Vindhya","Satpura","Aravalli"],0,"Western Ghats = Sahyadri; UNESCO World Heritage (2012); Anamudi is highest peak (2,695 m).","Geo India","Easy"),
 ("Which river is called the 'Sorrow of Bihar'? / 'बिहार का शोक' किस नदी को कहा जाता है?",["Kosi","Ganga","Gandak","Son"],0,"Kosi — Sorrow of Bihar (frequent floods, shifting course). Damodar — Sorrow of Bengal.","Geo India","Easy"),
 ("Brahmaputra enters India through — / ब्रह्मपुत्र भारत में किस राज्य से प्रवेश करती है?",["Arunachal Pradesh","Assam","Sikkim","Nagaland"],0,"Brahmaputra (Tsangpo in Tibet) enters via Arunachal Pradesh; joins Ganga in Bangladesh as Jamuna/Padma.","Geo India","Medium"),
 ("The largest delta in the world is — / विश्व का सबसे बड़ा डेल्टा है —",["Sundarbans (Ganga-Brahmaputra)","Nile Delta","Mississippi Delta","Godavari Delta"],0,"Sundarbans — largest delta in world (Ganga-Brahmaputra-Meghna); mangrove forest, Royal Bengal Tiger.","Geo India","Easy"),
 ("Which state has the longest coastline in India? / भारत में सबसे लंबी तटरेखा वाला राज्य है —",["Gujarat","Tamil Nadu","Andhra Pradesh","Maharashtra"],0,"Gujarat (~1,600 km) — longest coastline; followed by Andhra Pradesh, Tamil Nadu.","Geo India","Easy"),
 ("The 'Deccan Trap' is known for — / दक्कन ट्रैप किसके लिए जाना जाता है?",["Basaltic lava / black soil (regur)","Sand dunes","Limestone caves","Granite hills"],0,"Deccan Trap — Cretaceous basalt lava flows; black cotton soil (regur), ideal for cotton.","Geo India","Medium"),
 ("Chilika Lake is in — / चिल्का झील कहाँ है?",["Odisha","West Bengal","Andhra Pradesh","Tamil Nadu"],0,"Chilika — Odisha; largest brackish-water lagoon in India; Ramsar site; Irrawaddy dolphins.","Geo India","Easy"),
 ("Wular Lake is in — / वुलर झील कहाँ है?",["Jammu & Kashmir","Himachal Pradesh","Uttarakhand","Ladakh"],0,"Wular — J&K; largest freshwater lake in India; fed by Jhelum.","Geo India","Medium"),
 ("The 'Green Revolution' was most successful in — / हरित क्रांति सर्वाधिक सफल रही —",["Punjab, Haryana, Western UP","Rajasthan desert","North-East","Kerala"],0,"Green Revolution (1960s, M.S. Swaminathan) — wheat & rice in Punjab, Haryana, western UP; HYV seeds, fertilisers, irrigation.","Geo India","Easy"),
 ("India's first nuclear power plant was — / भारत का प्रथम परमाणु ऊर्जा संयंत्र था —",["Tarapur (Maharashtra)","Kota","Kalpakkam","Narora"],0,"Tarapur Atomic Power Station (1969), Maharashtra — first nuclear plant in India.","Geo India","Medium"),
 ("The 'Bhakti' — no: Bhakra Dam is on which river? / भाखड़ा बांध किस नदी पर है?",["Sutlej","Beas","Ravi","Yamuna"],0,"Bhakra Dam — Sutlej, Himachal Pradesh; Govind Sagar reservoir; Bhakra-Nangal project.","Geo India","Easy"),
 ("Hirakud Dam is on — / हीराकुंड बांध किस नदी पर है?",["Mahanadi","Godavari","Krishna","Cauvery"],0,"Hirakud — Mahanadi, Odisha; longest earthen dam in world (main dam ~4.8 km).","Geo India","Easy"),
 ("Tehri Dam is on — / टिहरी बांध किस नदी पर है?",["Bhagirathi","Alaknanda","Yamuna","Ganga (main stream)"],0,"Tehri Dam — Bhagirathi, Uttarakhand; tallest dam in India (260.5 m).","Geo India","Medium"),
 ("Which is the largest river basin in India? / भारत का सबसे बड़ा नदी बेसिन है —",["Ganga","Godavari","Indus","Krishna"],0,"Ganga basin — largest in India (~25% of India's area).","Geo India","Easy"),
 ("The 'Western Disturbances' bring rain mainly to — / पश्चिमी विक्षोभ मुख्यतः किस क्षेत्र में वर्षा लाते हैं?",["North-west India in winter","South India in summer","North-East in monsoon","Central India in autumn"],0,"Western Disturbances — winter rain/snow in NW India (Punjab, Haryana, HP, J&K, Rajasthan); important for rabi crops.","Geo India","Medium"),
 ("The South-West Monsoon first hits — / दक्षिण-पश्चिम मानसून भारत में सर्वप्रथम कहाँ पहुँचता है?",["Kerala coast (1 June, normally)","Tamil Nadu","Gujarat","Odisha"],0,"SW Monsoon reaches Kerala ~1 June, then advances; retreats from Rajasthan (Sept). Mawsynram/Cherrapunji — wettest places.","Geo India","Easy"),
 ("Mawsynram is famous for — / मावसिनराम किसके लिए प्रसिद्ध है?",["Highest rainfall in the world","Lowest temperature","Highest peak","Largest desert"],0,"Mawsynram (Meghalaya) — wettest place on Earth (avg ~11,872 mm); Cherrapunji second.","Geo India","Easy"),
 ("Which soil is best for cotton? / कपास के लिए सर्वोत्तम मिट्टी है —",["Black soil (regur)","Alluvial soil","Red soil","Laterite soil"],0,"Black soil (regur) — retains moisture, rich in iron/lime; Deccan plateau; cotton, soybean.","Geo India","Easy"),
 ("Alluvial soil is found mainly in — / जलोढ़ मिट्टी मुख्यतः कहाँ पाई जाती है?",["Northern plains (Ganga-Brahmaputra)","Deccan plateau","Thar desert","Western Ghats"],0,"Alluvial soil — Indo-Gangetic plains; most fertile; rice, wheat, sugarcane.","Geo India","Easy"),
 ("The 'Golden Quadrilateral' connects — / स्वर्णिम चतुर्भुज किन शहरों को जोड़ता है?",["Delhi-Mumbai-Chennai-Kolkata","Delhi-Jaipur-Agra-Lucknow","Mumbai-Pune-Nagpur","Chennai-Bengaluru-Hyderabad"],0,"Golden Quadrilateral — Delhi, Mumbai, Chennai, Kolkata (5,846 km); NHDP, launched 2001.","Geo India","Medium"),
 ("Konkan Railway connects — / कोंकण रेलवे जोड़ती है —",["Roha (Maharashtra) to Mangaluru (Karnataka)","Delhi to Mumbai","Chennai to Bengaluru","Kolkata to Guwahati"],0,"Konkan Railway — Roha to Mangaluru (741 km) along west coast; tunnels/bridges.","Geo India","Medium"),
 ("The 'Silk Route' — no: India's largest port by cargo is — / भारत का सबसे बड़ा बंदरगाह (माल ढुलाई) है —",["Jawaharlal Nehru Port (Nhava Sheva) / Deendayal (Kandla) — varies by year","Kochi","Chennai","Paradip"],0,"By cargo volume, Deendayal (Kandla) and Paradip often lead among major ports; JNPT leads in container traffic. Wording matters — container vs total cargo. Treat JNPT as container leader.","Geo India","Hard"),
 ("Which state is the largest producer of rice in India? / चावल का सबसे बड़ा उत्पादक राज्य है —",["West Bengal","Punjab","Uttar Pradesh","Tamil Nadu"],0,"West Bengal — largest rice producer; Punjab — highest productivity/yield.","Geo India","Medium"),
 ("Which state is the largest producer of wheat? / गेहूँ का सबसे बड़ा उत्पादक राज्य है —",["Uttar Pradesh","Punjab","Haryana","Madhya Pradesh"],0,"Uttar Pradesh — largest wheat producer; Punjab second.","Geo India","Easy"),
 ("The 'Blue Revolution' relates to — / नीली क्रांति किससे संबंधित है?",["Fisheries","Milk production","Oilseeds","Horticulture"],0,"Blue Revolution — fisheries; White — milk; Green — foodgrains; Yellow — oilseeds; Golden — horticulture/honey.","Geo India","Easy"),
]
geo=[Q(q,o,a,e,t,d) for q,o,a,e,t,d in geo_data]

sci=[]
sci_data=[
 ("The chemical formula of common salt is — / साधारण नमक का रासायनिक सूत्र है —",["NaCl","KCl","CaCO3","NaOH"],0,"NaCl — sodium chloride.","Science: Chemistry","Easy"),
 ("The pH of pure water at 25°C is — / 25°C पर शुद्ध जल का pH है —",["7","0","14","1"],0,"pH 7 — neutral; <7 acidic, >7 alkaline.","Science: Chemistry","Easy"),
 ("Which gas is used in balloons (safer than hydrogen)? / गुब्बारों में कौन-सी गैस भरी जाती है?",["Helium","Oxygen","Nitrogen","Carbon dioxide"],0,"Helium — light, non-flammable (hydrogen is flammable).","Science: Chemistry","Easy"),
 ("The SI unit of force is — / बल की SI इकाई है —",["Newton","Joule","Watt","Pascal"],0,"Newton (N); Joule = energy/work, Watt = power, Pascal = pressure.","Science: Physics","Easy"),
 ("Speed of light in vacuum is about — / निर्वात में प्रकाश की गति लगभग है —",["3 × 10^8 m/s","3 × 10^6 m/s","3 × 10^5 m/s","3 × 10^10 m/s"],0,"3×10^8 m/s (299,792,458 m/s).","Science: Physics","Easy"),
 ("Which organ purifies blood in the human body? / मानव शरीर में रक्त को शुद्ध करने वाला अंग है —",["Kidney","Liver","Heart","Lung"],0,"Kidney — filters blood, forms urine; liver detoxifies & makes bile; lungs oxygenate blood.","Science: Biology","Easy"),
 ("The powerhouse of the cell is — / कोशिका का ऊर्जा-गृह (पावरहाउस) है —",["Mitochondria","Nucleus","Ribosome","Golgi body"],0,"Mitochondria — ATP production (cellular respiration).","Science: Biology","Easy"),
 ("Photosynthesis takes place in — / प्रकाश-संश्लेषण कहाँ होता है?",["Chloroplast (leaves)","Mitochondria","Root","Flower"],0,"Chloroplast — chlorophyll captures sunlight; 6CO2+6H2O → C6H12O6+6O2.","Science: Biology","Easy"),
 ("The normal human body temperature is — / मानव शरीर का सामान्य तापमान है —",["37°C (98.6°F)","35°C","39°C","40°C"],0,"37°C / 98.6°F.","Science: Biology","Easy"),
 ("Which vitamin is produced in skin by sunlight? / सूर्य के प्रकाश से त्वचा में कौन-सा विटामिन बनता है?",["Vitamin D","Vitamin A","Vitamin C","Vitamin B12"],0,"Vitamin D — sunlight (UV) on skin; deficiency causes rickets.","Science: Biology","Easy"),
 ("Deficiency of Vitamin C causes — / विटामिन C की कमी से होता है —",["Scurvy","Rickets","Night blindness","Beriberi"],0,"Scurvy (Vit C); Rickets (Vit D); Night blindness (Vit A); Beriberi (Vit B1).","Science: Biology","Easy"),
 ("Deficiency of iodine causes — / आयोडीन की कमी से होता है —",["Goitre","Anaemia","Diabetes","Rickets"],0,"Goitre — thyroid enlargement; iodised salt prevents it.","Science: Biology","Easy"),
 ("The human heart has how many chambers? / मानव हृदय में कितने कक्ष होते हैं?",["4","2","3","5"],0,"4 chambers — 2 atria, 2 ventricles.","Science: Biology","Easy"),
 ("Red blood cells are formed in — / लाल रक्त कोशिकाएँ कहाँ बनती हैं?",["Bone marrow","Liver","Spleen","Heart"],0,"Bone marrow — RBCs (erythropoiesis); lifespan ~120 days.","Science: Biology","Medium"),
 ("The universal donor blood group is — / सर्वदाता रक्त समूह है —",["O negative","AB positive","A positive","B negative"],0,"O– — universal donor; AB+ — universal recipient.","Science: Biology","Easy"),
 ("The universal recipient blood group is — / सर्वग्राही रक्त समूह है —",["AB positive","O negative","A negative","B positive"],0,"AB+ — universal recipient (accepts all groups).","Science: Biology","Easy"),
 ("Which planet is known as the Red Planet? / लाल ग्रह किसे कहा जाता है?",["Mars","Venus","Jupiter","Mercury"],0,"Mars — iron oxide (rust) on surface.","Science: Physics","Easy"),
 ("Which planet is the largest in the Solar System? / सौरमंडल का सबसे बड़ा ग्रह है —",["Jupiter","Saturn","Neptune","Earth"],0,"Jupiter — largest; Saturn has prominent rings.","Science: Physics","Easy"),
 ("The nearest star to Earth is — / पृथ्वी के निकटतम तारा है —",["Sun","Proxima Centauri","Sirius","Alpha Centauri"],0,"Sun — nearest star; Proxima Centauri is nearest star beyond the Sun.","Science: Physics","Easy"),
 ("Acid rain is mainly caused by — / अम्लीय वर्षा मुख्यतः किससे होती है?",["Sulphur dioxide and nitrogen oxides","Carbon monoxide only","Oxygen","Methane only"],0,"SO2 + NOx → sulphuric/nitric acids in rain; from fossil-fuel burning.","Science: Chemistry","Medium"),
 ("Which acid is present in vinegar? / सिरके में कौन-सा अम्ल होता है?",["Acetic acid","Citric acid","Lactic acid","Formic acid"],0,"Acetic acid (CH3COOH); citric — lemon; lactic — curd; formic — ant sting.","Science: Chemistry","Easy"),
 ("Baking soda is — / बेकिंग सोडा है —",["Sodium bicarbonate (NaHCO3)","Sodium carbonate","Sodium chloride","Calcium carbonate"],0,"NaHCO3 — baking soda; Na2CO3 — washing soda; CaO — quicklime.","Science: Chemistry","Easy"),
 ("Washing soda is — / धावन सोडा है —",["Sodium carbonate (Na2CO3)","Sodium bicarbonate","Calcium hydroxide","Potassium chloride"],0,"Na2CO3·10H2O — washing soda.","Science: Chemistry","Medium"),
 ("The filament of an electric bulb is made of — / बिजली के बल्ब का तंतु किसका बना होता है?",["Tungsten","Copper","Aluminium","Iron"],0,"Tungsten — high melting point (3422°C); inert gas (argon/nitrogen) filled.","Science: Physics","Easy"),
 ("Which metal is liquid at room temperature? / कमरे के तापमान पर द्रव धातु है —",["Mercury","Iron","Copper","Aluminium"],0,"Mercury (Hg) — only metal liquid at room temp; bromine is liquid non-metal.","Science: Chemistry","Easy"),
 ("The unit of electric current is — / विद्युत धारा की इकाई है —",["Ampere","Volt","Ohm","Watt"],0,"Ampere (A); Volt = potential, Ohm = resistance, Watt = power.","Science: Physics","Easy"),
 ("Ohm's Law states — / ओम का नियम है —",["V = IR","P = VI only","F = ma","E = mc²"],0,"V = IR (voltage = current × resistance) at constant temperature.","Science: Physics","Medium"),
 ("Which instrument measures atmospheric pressure? / वायुमंडलीय दाब मापने का यंत्र है —",["Barometer","Thermometer","Ammeter","Hygrometer"],0,"Barometer; thermometer — temperature; hygrometer — humidity; ammeter — current.","Science: Physics","Easy"),
 ("Sound travels fastest in — / ध्वनि सबसे तेज़ किस माध्यम में चलती है?",["Solids (steel)","Vacuum","Air","Water only"],0,"Solids > liquids > gases; sound cannot travel in vacuum.","Science: Physics","Easy"),
 ("The colour of the sky is blue due to — / आकाश नीला किस कारण दिखता है?",["Scattering of light","Reflection only","Refraction only","Dispersion in clouds"],0,"Rayleigh scattering — blue light scatters most (short wavelength).","Science: Physics","Medium"),
 ("Which disease is caused by a virus? / विषाणु से होने वाला रोग है —",["Influenza (flu)","Tuberculosis","Cholera","Malaria"],0,"Influenza — virus; TB — bacterium; Cholera — bacterium (Vibrio); Malaria — protozoan (Plasmodium, via mosquito).","Science: Biology","Medium"),
 ("Malaria is caused by — / मलेरिया किससे होता है?",["Plasmodium (protozoan), transmitted by female Anopheles mosquito","Virus","Bacterium in water","Fungus"],0,"Plasmodium parasite; vector — female Anopheles mosquito.","Science: Biology","Easy"),
 ("Tuberculosis is caused by — / क्षय रोग (TB) किससे होता है?",["Mycobacterium tuberculosis (bacterium)","Virus","Fungus","Protozoan"],0,"Mycobacterium tuberculosis; BCG vaccine; DOTS treatment.","Science: Biology","Easy"),
 ("The BCG vaccine is given against — / BCG टीका किसके विरुद्ध दिया जाता है?",["Tuberculosis","Polio","Measles","Hepatitis B"],0,"BCG — TB (given at birth in India).","Science: Biology","Easy"),
 ("Which is the main source of Vitamin C? / विटामिन C का मुख्य स्रोत है —",["Amla / citrus fruits","Milk","Egg","Rice"],0,"Amla is richest source; citrus fruits, guava, capsicum also rich.","Science: Biology","Easy"),
 ("The chemical symbol for gold is — / सोने का रासायनिक प्रतीक है —",["Au","Ag","Gd","Go"],0,"Au (aurum); Ag — silver; Fe — iron; Pb — lead.","Science: Chemistry","Easy"),
 ("The hardest natural substance is — / सबसे कठोर प्राकृतिक पदार्थ है —",["Diamond","Gold","Iron","Quartz"],0,"Diamond (carbon allotrope); graphite is soft allotrope of carbon.","Science: Chemistry","Easy"),
 ("Which gas do plants absorb for photosynthesis? / प्रकाश-संश्लेषण में पौधे कौन-सी गैस लेते हैं?",["Carbon dioxide","Oxygen","Nitrogen","Hydrogen"],0,"CO2 absorbed, O2 released.","Science: Biology","Easy"),
 ("The SI unit of energy is — / ऊर्जा की SI इकाई है —",["Joule","Calorie","Watt","Newton"],0,"Joule (J); calorie is old unit (1 cal ≈ 4.184 J).","Science: Physics","Easy"),
 ("Which mirror is used in a vehicle's rear-view mirror? / वाहन के रियर-व्यू मिरर में कौन-सा दर्पण होता है?",["Convex mirror","Concave mirror","Plane mirror","Parabolic mirror"],0,"Convex mirror — wider field of view, diminished image; concave — shaving mirror / headlight reflector.","Science: Physics","Medium"),
 ("The human genome / DNA shape is — / DNA की आकृति है —",["Double helix","Single strand circle only","Triple helix","Flat sheet"],0,"Double helix (Watson & Crick, 1953).","Science: Biology","Medium"),
 ("Which blood cells fight infection? / संक्रमण से लड़ने वाली रक्त कोशिकाएँ हैं —",["White blood cells (WBC)","Red blood cells","Platelets","Plasma cells only"],0,"WBC (leucocytes) — immunity; platelets — clotting; RBC — oxygen transport.","Science: Biology","Easy"),
 ("The instrument used to measure body temperature is — / शरीर का तापमान मापने का यंत्र है —",["Clinical thermometer","Barometer","Stethoscope","Sphygmomanometer"],0,"Clinical thermometer (max ~35–42°C); sphygmomanometer — BP; stethoscope — heartbeat.","Science: Biology","Easy"),
 ("Which of the following is a greenhouse gas? / ग्रीनहाउस गैस है —",["Carbon dioxide","Oxygen","Nitrogen","Argon"],0,"CO2, CH4, N2O, water vapour are greenhouse gases; O2/N2 are not.","Science: Chemistry","Easy"),
 ("The ozone layer is in — / ओजोन परत किस मंडल में है?",["Stratosphere","Troposphere","Mesosphere","Thermosphere"],0,"Stratosphere (~15–35 km); protects from UV; depleted by CFCs.","Science: Chemistry","Medium"),
]
sci=[Q(q,o,a,e,t,d) for q,o,a,e,t,d in sci_data]

# Hindi (23) + English (22) = 45
hindi=[]
hindi_data=[
 ("'विद्यालय' शब्द का संधि-विच्छेद है —",["विद्या + आलय","विद्य + आलय","विद्या + लय","वि + द्यालय"],0,"विद्या + आलय = विद्यालय (दीर्घ संधि, आ + आ = आ).","Hindi: Sandhi","Easy"),
 ("'राजा' का पर्यायवाची है —",["नृप","प्रजा","मंत्री","सेवक"],0,"राजा — नृप, भूप, नरेश, महीप.","Hindi: Paryayvachi","Easy"),
 ("'अंधकार' का विलोम है —",["प्रकाश","अंधेरा","रात्रि","काला"],0,"अंधकार — प्रकाश; अंधेरा is synonym, not antonym in standard lists.","Hindi: Vilom","Easy"),
 ("'जो कभी न मरे' के लिए एक शब्द है —",["अमर","अजर","अजेय","अनंत"],0,"अमर — जो कभी न मरे; अजर — जो कभी बूढ़ा न हो.","Hindi: Ek Shabda","Easy"),
 ("'कमल' का पर्यायवाची नहीं है —",["गुलाब","पंकज","जलज","नीरज"],0,"गुलाब is not a synonym of कमल; पंकज/जलज/नीरज are.","Hindi: Paryayvachi","Medium"),
 ("शुद्ध वर्तनी वाला शब्द है —",["विद्यालय","विध्यालय","विद्याल्य","विदयालय"],0,"विद्यालय is correct spelling.","Hindi: Shuddha Vartani","Easy"),
 ("'आँखों का तारा' मुहावरे का अर्थ है —",["बहुत प्रिय","आँख में दर्द","दूर देखना","अंधा होना"],0,"आँखों का तारा — अत्यंत प्रिय व्यक्ति.","Hindi: Muhavare","Easy"),
 ("'नौ दो ग्यारह होना' का अर्थ है —",["भाग जाना","गिनती करना","हार जाना","सो जाना"],0,"नौ दो ग्यारह होना — चुपचाप भाग जाना.","Hindi: Muhavare","Easy"),
 ("हिन्दी वर्णमाला में स्वरों की संख्या है —",["11","13","33","21"],0,"11 स्वर (अ आ इ ई उ ऊ ऋ ए ऐ ओ औ) — some count अं/अः separately; standard CET answer 11.","Hindi: Varnamala","Easy"),
 ("'मैंने पुस्तक पढ़ी।' में 'मैंने' कौन-सा कारक है? / कर्ता कारक का चिह्न है —",["ने (कर्ता कारक)","को","से","में"],0,"ने — कर्ता कारक (past transitive verb).","Hindi: Karak","Medium"),
 ("'राम ने रावण को मारा।' — वाच्य है —",["कर्तृवाच्य","कर्मवाच्य","भाववाच्य","इनमें से कोई नहीं"],0,"कर्तृवाच्य — subject (Ram) is doer.","Hindi: Vachya","Medium"),
 ("'जो पढ़ेगा, वह सफल होगा।' — सर्वनाम है —",["जो (संबंधवाचक सर्वनाम)","वह (पुरुषवाचक)","पढ़ेगा","सफल"],0,"जो — संबंधवाचक सर्वनाम (relative pronoun).","Hindi: Sarvanam","Medium"),
 ("'सूर्य' का पर्यायवाची है —",["दिनकर","चंद्रमा","तारा","अग्नि"],0,"सूर्य — दिनकर, भास्कर, रवि, आदित्य.","Hindi: Paryayvachi","Easy"),
 ("'उन्नति' का विलोम है —",["अवनति","प्रगति","विकास","उत्थान"],0,"उन्नति — अवनति.","Hindi: Vilom","Easy"),
 ("'पानी में आग लगाना' मुहावरे का अर्थ है —",["शांत स्थिति में झगड़ा कराना","पानी गरम करना","आग बुझाना","खाना बनाना"],0,"पानी में आग लगाना — शांत वातावरण में कलह पैदा करना.","Hindi: Muhavare","Medium"),
 ("'गंगा' का पर्यायवाची है —",["भागीरथी","यमुना","सरस्वती","नर्मदा"],0,"गंगा — भागीरथी, जाह्नवी, मंदाकिनी.","Hindi: Paryayvachi","Easy"),
 ("देवनागरी लिपि में लिखी जाने वाली भाषा है —",["हिन्दी","उर्दू","पंजाबी (गुरुमुखी)","बंगाली"],0,"हिन्दी — देवनागरी; पंजाबी — गुरुमुखी; बंगाली — बंगाली लिपि.","Hindi: Lipi","Easy"),
 ("'अतिथि' का अर्थ है —",["मेहमान","शत्रु","मित्र","पड़ोसी"],0,"अतिथि — मेहमान (guest).","Hindi: Shabdarth","Easy"),
 ("'विद्वान' का विलोम है —",["मूर्ख","ज्ञानी","पंडित","शिक्षित"],0,"विद्वान — मूर्ख.","Hindi: Vilom","Easy"),
 ("'चिड़िया' का बहुवचन है —",["चिड़ियाँ","चिड़िया","चिड़ियाएँ","चिड़ियों"],0,"चिड़ियाँ — plural of चिड़िया.","Hindi: Vachan","Medium"),
 ("'सत्य' का विलोम है —",["असत्य","झूठ (synonym of असत्य, but standard antonym is असत्य)","सही","न्याय"],0,"सत्य — असत्य (standard pair).","Hindi: Vilom","Easy"),
 ("'हाथी' का पर्यायवाची है —",["गज","घोड़ा","सिंह","ऊँट"],0,"हाथी — गज, कुंजर, हस्ती.","Hindi: Paryayvachi","Easy"),
 ("'जल' का पर्यायवाची है —",["नीर","अग्नि","वायु","पृथ्वी"],0,"जल — नीर, पानी, वारि, सलिल.","Hindi: Paryayvachi","Easy"),
]
hindi=[Q(q,o,a,e,t,d) for q,o,a,e,t,d in hindi_data]
eng=[]
eng_data=[
 ("Choose the correct synonym of 'Happy':",["Joyful","Sad","Angry","Tired"],0,"Happy — joyful, glad, delighted.","English: Synonym","Easy"),
 ("Choose the correct antonym of 'Brave':",["Cowardly","Bold","Strong","Heroic"],0,"Brave — cowardly, timid.","English: Antonym","Easy"),
 ("Choose the correctly spelt word:",["Occurrence","Occurence","Ocurrence","Occurrance"],0,"Occurrence — double 'c' + double 'r'.","English: Spelling","Medium"),
 ("Choose the correctly spelt word — (2):",["Separate","Seperate","Saperate","Seprate"],0,"Separate — 'se-par-ate'.","English: Spelling","Medium"),
 ("One who can use both hands equally well is a —",["Ambidextrous","Bilingual","Versatile","Ambiguous"],0,"Ambidextrous — both hands; bilingual — two languages.","English: One Word","Medium"),
 ("One who speaks many languages is a —",["Polyglot","Polygamist","Monolingual","Linguist only"],0,"Polyglot — speaks many languages.","English: One Word","Medium"),
 ("The passive voice of 'She writes a letter' is —",["A letter is written by her","A letter was written by her","She is written a letter","A letter writes her"],0,"Present simple passive: is + past participle (written).","English: Voice","Medium"),
 ("The active voice of 'The book was read by him' is —",["He read the book","He reads the book","He is reading the book","He has read the book"],0,"Past simple active: He read the book.","English: Voice","Medium"),
 ("Choose the correct article: ___ honest man",["An","A","The (only)","No article"],0,"An honest man — 'h' silent, vowel sound.","English: Articles","Easy"),
 ("Choose the correct preposition: He is good ___ mathematics.",["at","in","on","for"],0,"Good at — standard collocation.","English: Preposition","Easy"),
 ("'To bite the dust' means —",["To be defeated","To eat dust","To work hard","To run fast"],0,"Bite the dust — suffer defeat / fail.","English: Idioms","Medium"),
 ("'To break the ice' means —",["To start a conversation","To break a glass","To feel cold","To stop talking"],0,"Break the ice — ease initial awkwardness, start talking.","English: Idioms","Easy"),
 ("Choose the synonym of 'Abandon':",["Leave","Keep","Hold","Protect"],0,"Abandon — leave, forsake, desert.","English: Synonym","Easy"),
 ("Choose the antonym of 'Ancient':",["Modern","Old","Historic","Antique"],0,"Ancient — modern, new.","English: Antonym","Easy"),
 ("He ___ to school every day.",["goes","go","going","gone"],0,"Third person singular present: goes.","English: Tense","Easy"),
 ("I have lived here ___ 2015.",["since","for","from","at"],0,"Since + point of time (2015); for + duration.","English: Preposition","Medium"),
 ("Choose the correct sentence:",["Neither of the answers is correct.","Neither of the answers are correct.","Neither of the answer is correct.","Neither of answers is correct."],0,"Neither … is — singular verb with 'neither of'.","English: Grammar","Hard"),
 ("The plural of 'Child' is —",["Children","Childs","Childes","Childrens"],0,"Children — irregular plural.","English: Grammar","Easy"),
 ("The feminine of 'Lion' is —",["Lioness","Liones","She-lion (not standard)","Tigress"],0,"Lioness.","English: Gender","Easy"),
 ("'Rain' as a verb — Choose: It ___ heavily yesterday.",["rained","rains","rain","raining"],0,"Past: rained.","English: Tense","Easy"),
 ("Choose the synonym of 'Rapid':",["Quick","Slow","Lazy","Late"],0,"Rapid — quick, fast, swift.","English: Synonym","Easy"),
 ("Choose the antonym of 'Victory':",["Defeat","Success","Win","Triumph"],0,"Victory — defeat.","English: Antonym","Easy"),
]
eng=[Q(q,o,a,e,t,d) for q,o,a,e,t,d in eng_data]
lang=hindi+eng

comp=[]
comp_data=[
 ("The full form of CPU is — / CPU का पूरा नाम है —",["Central Processing Unit","Central Program Unit","Computer Processing Unit","Central Peripheral Unit"],0,"CPU — Central Processing Unit; brain of computer.","Computer","Easy"),
 ("The full form of RAM is — / RAM का पूरा नाम है —",["Random Access Memory","Read Access Memory","Rapid Action Memory","Run Access Memory"],0,"RAM — Random Access Memory (volatile); ROM — Read Only Memory (non-volatile).","Computer","Easy"),
 ("1 GB equals — / 1 GB बराबर है —",["1024 MB","1000 KB","1024 KB","100 MB"],0,"1 GB = 1024 MB; 1 MB = 1024 KB; 1 KB = 1024 bytes.","Computer","Easy"),
 ("Which is an input device? / इनपुट डिवाइस कौन-सी है?",["Keyboard","Monitor","Printer","Speaker"],0,"Input: keyboard, mouse, scanner. Output: monitor, printer, speaker.","Computer","Easy"),
 ("Which is an output device? / आउटपुट डिवाइस कौन-सी है?",["Printer","Keyboard","Mouse","Scanner"],0,"Printer — output; keyboard/mouse/scanner — input.","Computer","Easy"),
 ("The full form of WWW is — / WWW का पूरा नाम है —",["World Wide Web","World Web Wide","Wide World Web","Web World Wide"],0,"WWW — World Wide Web (Tim Berners-Lee, 1989).","Computer","Easy"),
 ("The full form of HTTP is — / HTTP का पूरा नाम है —",["HyperText Transfer Protocol","High Transfer Text Protocol","HyperText Transmission Process","Home Text Transfer Protocol"],0,"HTTP — HyperText Transfer Protocol; HTTPS adds Secure (SSL/TLS).","Computer","Medium"),
 ("MS Word is mainly used for — / MS Word मुख्यतः किसके लिए प्रयोग होता है?",["Word processing (documents)","Spreadsheets","Presentations","Photo editing"],0,"MS Word — word processing; Excel — spreadsheets; PowerPoint — presentations.","Computer","Easy"),
 ("MS Excel is mainly used for — / MS Excel मुख्यतः किसके लिए प्रयोग होता है?",["Spreadsheets / data tables","Word documents","Presentations","Web browsing"],0,"Excel — spreadsheets; rows/columns, formulas.","Computer","Easy"),
 ("The shortcut for Copy is — / Copy का शॉर्टकट है —",["Ctrl + C","Ctrl + V","Ctrl + X","Ctrl + Z"],0,"Ctrl+C Copy, Ctrl+V Paste, Ctrl+X Cut, Ctrl+Z Undo.","Computer","Easy"),
 ("The shortcut for Paste is — / Paste का शॉर्टकट है —",["Ctrl + V","Ctrl + C","Ctrl + P","Ctrl + S"],0,"Ctrl+V Paste; Ctrl+P Print; Ctrl+S Save.","Computer","Easy"),
 ("Which is the brain of the computer? / कंप्यूटर का मस्तिष्क किसे कहा जाता है?",["CPU","Monitor","Keyboard","Hard Disk"],0,"CPU — brain; ALU + CU are its parts.","Computer","Easy"),
 ("The full form of PDF is — / PDF का पूरा नाम है —",["Portable Document Format","Personal Document File","Printed Document Format","Public Data Format"],0,"PDF — Portable Document Format (Adobe).","Computer","Medium"),
 ("An email address must contain — / ईमेल पते में क्या होना आवश्यक है?",["@ symbol","# symbol","$ symbol","% symbol"],0,"@ separates username and domain (e.g., name@example.com).","Computer","Easy"),
 ("Which of these is an operating system? / ऑपरेटिंग सिस्टम कौन-सा है?",["Windows","MS Word","Google Chrome","MS Excel"],0,"Windows — OS; Word/Excel are applications; Chrome is a browser.","Computer","Easy"),
 ("The full form of USB is — / USB का पूरा नाम है —",["Universal Serial Bus","United Serial Bus","Universal System Bus","Universal Storage Bus"],0,"USB — Universal Serial Bus.","Computer","Medium"),
 ("Which memory is volatile (data lost when power off)? / कौन-सी मेमोरी वोलेटाइल है?",["RAM","ROM","Hard Disk","Pen Drive"],0,"RAM is volatile; ROM/HDD/pen drive are non-volatile.","Computer","Medium"),
 ("The full form of E-mail is — / E-mail का पूरा नाम है —",["Electronic Mail","Electric Mail","Easy Mail","Express Mail"],0,"E-mail — Electronic Mail.","Computer","Easy"),
]
comp=[Q(q,o,a,e,t,d) for q,o,a,e,t,d in comp_data]

caph=[]
caph_data=[
 ("The VB-G RAM G Act, 2025 replaced which Act? / VB-G RAM G अधिनियम, 2025 ने किस अधिनियम को प्रतिस्थापित किया?",["MGNREGA, 2005","National Food Security Act","Right to Education Act","Factories Act"],0,"VB-G RAM G (Viksit Bharat – Guarantee for Rozgar and Ajeevika Mission, Gramin) Act, 2025 — replaces MGNREGA; guarantee raised to 125 days. Passed Dec 2025.","CA: Schemes","Hard"),
 ("Rajasthan's Unfair Means (Prevention) Act relates to — / राजस्थान अनुचित साधन निवारण अधिनियम किससे संबंधित है?",["Prevention of cheating / paper leaks in public exams","Traffic rules","Forest protection","Land records"],0,"Rajasthan Public Examination (Prevention of Unfair Means) Act, 2022 — anti-paper-leak law.","CA: Rajasthan","Hard"),
 ("Ayushman Bharat – PM-JAY provides health cover of — / PM-JAY में स्वास्थ्य बीमा कितने का है?",["₹5 lakh per family per year","₹1 lakh","₹25 lakh","₹50,000"],0,"PM-JAY — ₹5 lakh/family/year (secondary & tertiary care); Rajasthan's state scheme cover is higher (₹25 lakh) — do not confuse the two.","CA: Schemes","Medium"),
 ("The National Education Policy (NEP) was announced in — / राष्ट्रीय शिक्षा नीति कब घोषित हुई?",["2020","2015","2022","2019"],0,"NEP 2020 — 5+3+3+4 structure, replacing 10+2.","CA: Policy","Easy"),
 ("Digital India programme was launched in — / डिजिटल इंडिया कार्यक्रम कब शुरू हुआ?",["2015","2014","2016","2018"],0,"Digital India — 1 July 2015; Digital India, Make in India (2014), Swachh Bharat (2014).","CA: Policy","Easy"),
 ("Swachh Bharat Mission was launched on — / स्वच्छ भारत मिशन कब शुरू हुआ?",["2 October 2014","15 August 2014","26 January 2015","2 October 2015"],0,"Swachh Bharat Mission — 2 Oct 2014 (Gandhi Jayanti).","CA: Policy","Easy"),
 ("The headquarters of WHO is at — / WHO का मुख्यालय कहाँ है?",["Geneva, Switzerland","New York, USA","Paris, France","Vienna, Austria"],0,"WHO — Geneva; UNESCO — Paris; UN HQ — New York.","CA: International","Easy"),
 ("The headquarters of UNESCO is at — / UNESCO का मुख्यालय कहाँ है?",["Paris, France","Geneva, Switzerland","London, UK","Rome, Italy"],0,"UNESCO — Paris; FAO — Rome; ILO — Geneva.","CA: International","Easy"),
 ("Which disease was declared eradicated from India (polio)? — India was declared polio-free by WHO in — / भारत को पोलियो-मुक्त कब घोषित किया गया?",["2014","2011","2016","2020"],0,"India declared polio-free by WHO in March 2014 (last case Jan 2011, Howrah).","Public Health","Medium"),
 ("The National Health Mission (NHM) includes — / राष्ट्रीय स्वास्थ्य मिशन में शामिल है —",["NRHM + NUHM (rural + urban)","Only Ayushman Bharat","Only PM-JAY","Only Pulse Polio"],0,"NHM (2013) — National Rural Health Mission (2005) + National Urban Health Mission.","Public Health","Medium"),
 ("Mission Indradhanush relates to — / मिशन इंद्रधनुष किससे संबंधित है?",["Immunisation of children & pregnant women","Road construction","Digital literacy","Crop insurance"],0,"Mission Indradhanush (2014) — full immunisation for children & pregnant women; IMI 5.0 etc.","Public Health","Medium"),
 ("The Pulse Polio programme in India began in — / पल्स पोलियो कार्यक्रम भारत में कब शुरू हुआ?",["1995","2000","1990","2014"],0,"Pulse Polio Immunisation — Dec 1995.","Public Health","Medium"),
 ("ORS (Oral Rehydration Solution) is used for — / ORS किसके उपचार में प्रयोग होता है?",["Dehydration due to diarrhoea","Fever","Diabetes","Anaemia"],0,"ORS — dehydration from diarrhoea; WHO/UNICEF formula (salt + sugar + water).","Public Health","Easy"),
 ("Anaemia is mainly caused by deficiency of — / एनीमिया मुख्यतः किसकी कमी से होता है?",["Iron","Calcium","Vitamin C","Iodine"],0,"Iron-deficiency anaemia; Anaemia Mukt Bharat programme (2018).","Public Health","Easy"),
 ("The 'Fit India Movement' was launched in — / फिट इंडिया मूवमेंट कब शुरू हुआ?",["2019","2015","2020","2014"],0,"Fit India Movement — 29 Aug 2019 (National Sports Day).","Public Health","Easy"),
 ("International Yoga Day is observed on — / अंतर्राष्ट्रीय योग दिवस कब मनाया जाता है?",["21 June","21 May","5 June","1 July"],0,"International Yoga Day — 21 June (since 2015, UN resolution 2014).","CA: Days","Easy"),
 ("World Health Day is observed on — / विश्व स्वास्थ्य दिवस कब मनाया जाता है?",["7 April","7 May","1 December","10 October"],0,"World Health Day — 7 April (WHO founded 7 April 1948).","Public Health","Easy"),
 ("World AIDS Day is observed on — / विश्व एड्स दिवस कब मनाया जाता है?",["1 December","1 November","7 April","5 June"],0,"World AIDS Day — 1 December.","Public Health","Easy"),
 ("The 'Jal Jeevan Mission' aims to provide — / जल जीवन मिशन का उद्देश्य है —",["Tap water to every rural household","Free electricity","Irrigation to all farms","Flood control"],0,"Jal Jeevan Mission (2019) — Har Ghar Jal: tap water to rural households.","CA: Schemes","Medium"),
 ("PM Kisan Samman Nidhi provides — / PM-किसान योजना में कितनी राशि मिलती है?",["₹6,000 per year to farmers","₹12,000 per year","₹2,000 per month","₹10,000 one-time"],0,"PM-KISAN (2019) — ₹6,000/year in 3 instalments of ₹2,000 to eligible farmers.","CA: Schemes","Easy"),
 ("The 'One Nation One Ration Card' relates to — / 'एक राष्ट्र एक राशन कार्ड' किससे संबंधित है?",["Food security / portability of ration across states","One voter card","One health card","One bank account"],0,"ONORC — PDS portability under National Food Security Act.","CA: Schemes","Medium"),
 ("The G20 Summit 2023 was hosted by — / G20 शिखर सम्मेलन 2023 की अध्यक्षता किस देश ने की?",["India","Indonesia","Brazil","Italy"],0,"G20 2023 — India (New Delhi Summit, Sept 2023); theme 'Vasudhaiva Kutumbakam'; African Union became permanent member.","CA: International","Medium"),
 ("India's first Gaganyaan (human spaceflight) mission is by — / गगनयान मिशन किस संस्था का है?",["ISRO","DRDO","NASA","HAL"],0,"ISRO — Gaganyaan (human spaceflight; uncrewed test flights ongoing; crewed flight targeted mid-2020s, timeline revised).","CA: Science","Medium"),
 ("Chandrayaan-3 landed on the Moon on — / चंद्रयान-3 चंद्रमा पर कब उतरा?",["23 August 2023","14 July 2023","23 August 2022","20 August 2023"],0,"Chandrayaan-3 — Vikram lander touched down 23 Aug 2023 near south pole; India first to land there; landing site named Shiv Shakti Point.","CA: Science","Easy"),
 ("The 'Viksit Bharat @2047' vision relates to — / 'विकसित भारत @2047' का लक्ष्य है —",["India as a developed nation by 2047","100% literacy by 2030","Net-zero by 2030","$5 trillion by 2025 only"],0,"Viksit Bharat @2047 — developed-nation vision by centenary of Independence (2047).","CA: Policy","Medium"),
 ("Rajasthan's 'Mukhyamantri Nishulk Dava Yojana' started in — / निःशुल्क दवा योजना कब शुरू हुई?",["2011","2015","2018","2020"],0,"Mukhyamantri Nishulk Dava Yojana — Oct 2011 (Rajasthan).","Public Health: Rajasthan","Medium"),
 ("The National Deworming Day is observed on — / राष्ट्रीय कृमि-मुक्ति दिवस कब मनाया जाता है?",["10 February","10 January","5 June","14 November"],0,"National Deworming Day — 10 Feb (and 10 Aug round); albendazole for children 1–19 years.","Public Health","Hard"),
 ("Which vitamin is given in high dose to prevent blindness (Vit A programme)? / अंधता रोकने हेतु कौन-सा विटामिन दिया जाता है?",["Vitamin A","Vitamin B","Vitamin C","Vitamin D"],0,"Vitamin A supplementation — prevents xerophthalmia/blindness in children (9 months–5 years).","Public Health","Medium"),
 ("The 'Janani Suraksha Yojana' relates to — / जननी सुरक्षा योजना किससे संबंधित है?",["Promoting institutional delivery / safe motherhood","Girl child education","Free medicines only","Immunisation only"],0,"JSY (2005, under NRHM) — cash incentive for institutional delivery to reduce maternal & neonatal mortality.","Public Health","Medium"),
 ("The 'Poshan Abhiyaan' (National Nutrition Mission) was launched in — / पोषण अभियान कब शुरू हुआ?",["2018","2015","2020","2014"],0,"POSHAN Abhiyaan — March 2018 (Jhunjhunu, Rajasthan launch by PM); targets stunting, anaemia, under-nutrition.","Public Health","Medium"),
]
caph=[Q(q,o,a,e,t,d) for q,o,a,e,t,d in caph_data]

# ---------- REASONING / MATHS: computed, 45 distinct ----------
import math
reas=[]
def mcq_num(q, correct, distractors, expl, topic, diff="Medium"):
    opts=[correct]+distractors
    # ensure distinct strings
    seen=set(); u=[]
    for x in opts:
        if str(x) not in seen: seen.add(str(x)); u.append(str(x))
    while len(u)<4: u.append(str(int(correct)+len(u)*7+3))
    return Q(q, u[:4], 0, expl, topic, diff)
# 1-15: arithmetic / percentages / SI / averages (computed)
for i,(p,r,t) in enumerate([(1000,10,2),(2000,5,3),(1500,8,2),(5000,4,2),(1200,12,1),(3000,6,4),(800,15,2),(2500,8,3),(4000,10,1),(6000,5,2),(1800,10,3),(2200,6,2),(900,20,1),(3500,7,2),(4500,8,2)]):
    si=p*r*t//100
    reas.append(mcq_num(f"Simple Interest on ₹{p} at {r}% p.a. for {t} years is — / ₹{p} पर {r}% वार्षिक दर से {t} वर्ष का साधारण ब्याज है —", si, [si+50, si-40, si+120], f"SI = P×R×T/100 = {p}×{r}×{t}/100 = ₹{si}.","Maths: SI","Easy"))
for i,(a,b) in enumerate([(20,30),(15,25),(40,60),(12,18),(25,35),(30,45),(18,27),(50,75)]):
    avg=(a+b)//2
    reas.append(mcq_num(f"Average of {a} and {b} is — / {a} और {b} का औसत है —", avg, [avg+5, avg-3, avg+10], f"Average = ({a}+{b})/2 = {avg}.","Maths: Average","Easy"))
for i,(price,disc) in enumerate([(500,10),(800,25),(1000,20),(1200,15),(600,50)]):
    sp=int(price*(100-disc)/100)
    reas.append(mcq_num(f"A ₹{price} article sold at {disc}% discount costs — / ₹{price} की वस्तु {disc}% छूट पर कितने में मिलेगी?", sp, [sp+50, sp-40, sp+100], f"SP = {price} × (100−{disc})/100 = ₹{sp}.","Maths: Percentage","Easy"))
# Number series (hand-verified patterns)
series=[
 ("2, 4, 8, 16, 32, ? — next term:", "64", ["48","56","60"], "Each term ×2: 2,4,8,16,32,64.","Reasoning: Series","Easy"),
 ("3, 6, 11, 18, 27, ? — next term:", "38", ["36","40","34"], "Differences 3,5,7,9,11 → next 27+11=38.","Reasoning: Series","Medium"),
 ("1, 4, 9, 16, 25, ? — next term:", "36", ["30","35","49"], "Squares: 1²,2²,3²,4²,5²,6²=36.","Reasoning: Series","Easy"),
 ("5, 10, 20, 40, 80, ? — next term:", "160", ["100","120","140"], "Each term ×2.","Reasoning: Series","Easy"),
 ("100, 90, 81, 73, 66, ? — next term:", "60", ["58","62","59"], "Differences −10,−9,−8,−7,−6 → 66−6=60.","Reasoning: Series","Medium"),
 ("7, 14, 28, 56, 112, ? — next term:", "224", ["168","196","210"], "Each term ×2.","Reasoning: Series","Easy"),
 ("2, 3, 5, 8, 13, ? — next term (Fibonacci-like):", "21", ["18","20","17"], "Each term = sum of previous two: 8+13=21.","Reasoning: Series","Medium"),
 ("121, 144, 169, 196, ? — next term:", "225", ["216","220","230"], "Squares: 11²,12²,13²,14²,15²=225.","Reasoning: Series","Medium"),
 ("1, 8, 27, 64, ? — next term:", "125", ["100","81","216"], "Cubes: 1³,2³,3³,4³,5³=125.","Reasoning: Series","Medium"),
 ("90, 82, 74, 66, 58, ? — next term:", "50", ["48","52","46"], "Each term −8.","Reasoning: Series","Easy"),
]
for q,c,d,e,t,df in series:
    reas.append(mcq_num(q, c, d, e, t, df))
# Coding / odd-one / analogy / direction (hand-verified)
reas_extra=[
 ("If CAT = 24 (C=3,A=1,T=20; sum ×? — CAT letters sum=24), then DOG = ? (D=4,O=15,G=7)",["26","24","28","30"],0,"D+O+G = 4+15+7 = 26. (CAT: 3+1+20=24.)","Reasoning: Coding","Medium"),
 ("If 'MANGO' is coded as 'NBOHP' (each letter +1), then 'APPLE' is coded as —",["BQQMF","ZOOKD","BPPLE","AQQMF"],0,"Each letter +1: A→B, P→Q, P→Q, L→M, E→F = BQQMF.","Reasoning: Coding","Medium"),
 ("Odd one out: 121, 144, 169, 190, 225 —",["190","121","144","169"],0,"121,144,169,225 are perfect squares (11²,12²,13²,15²); 190 is not.","Reasoning: Odd One","Medium"),
 ("Odd one out: Apple, Mango, Banana, Potato —",["Potato","Apple","Mango","Banana"],0,"Potato is a vegetable (underground stem); others are fruits.","Reasoning: Odd One","Easy"),
 ("Book : Read :: Pen : ?",["Write","Ink","Paper","Draw"],0,"Book is read; pen is used to write. (Analogy: object : its use.)","Reasoning: Analogy","Easy"),
 ("Doctor : Hospital :: Teacher : ?",["School","Student","Book","Class"],0,"Doctor works in hospital; teacher works in school.","Reasoning: Analogy","Easy"),
 ("A man walks 5 km north, then 3 km east, then 5 km south. How far is he from start? / एक व्यक्ति 5 km उत्तर, 3 km पूर्व, 5 km दक्षिण चलता है। प्रारंभ से कितनी दूर है?",["3 km east","5 km","8 km","13 km"],0,"North 5 km and south 5 km cancel; only 3 km east remains.","Reasoning: Direction","Medium"),
 ("If today is Monday, what day will it be after 10 days? / आज सोमवार है, 10 दिन बाद कौन-सा दिन होगा?",["Thursday","Tuesday","Wednesday","Friday"],0,"10 mod 7 = 3 days after Monday → Thursday.","Reasoning: Calendar","Medium"),
 ("Find the missing number: 6, 12, 20, 30, 42, ? —",["56","48","52","60"],0,"Pattern n(n+1): 2×3=6, 3×4=12, 4×5=20, 5×6=30, 6×7=42, 7×8=56.","Reasoning: Series","Hard"),
 ("Ratio: If A:B = 2:3 and B:C = 4:5, then A:C = ?",["8:15","6:10","2:5","4:9"],0,"A:B=2:3=8:12; B:C=4:5=12:15 → A:C=8:15.","Maths: Ratio","Medium"),
 ("A train 200 m long crosses a pole in 10 s. Its speed (km/h) is — / 200 m लंबी ट्रेन 10 s में खंभा पार करती है। गति (km/h) है —",["72","60","80","36"],0,"Speed = 200/10 = 20 m/s = 20×18/5 = 72 km/h.","Maths: Speed","Medium"),
 ("The average of first 5 natural numbers is — / प्रथम 5 प्राकृतिक संख्याओं का औसत है —",["3","2.5","4","5"],0,"(1+2+3+4+5)/5 = 15/5 = 3.","Maths: Average","Easy"),
]
reas.extend([Q(q,o,a,e,t,d) for q,o,a,e,t,d in reas_extra])
print(f"GEO {len(geo)} SCI {len(sci)} LANG {len(lang)} (Hindi {len(hindi)}, Eng {len(eng)}) COMP {len(comp)} CA/PH {len(caph)} REAS {len(reas)}")

# ---------- PART 3: ASSEMBLY (balanced, disjoint, verified OMR rules) ----------
import sys
sys.path.insert(0, OUT)
from raj_pool import build_raj
raj = build_raj()
print(f"RAJ {len(raj)} GEO {len(geo)} SCI {len(sci)} LANG {len(lang)} COMP {len(comp)} CAPH {len(caph)} REAS {len(reas)}")

def partition(pool, n):
    # Paper 3 gets Hard questions first; Papers 1-2 share the rest. Disjoint slices.
    hard=[q for q in pool if q["diff"]=="Hard"]
    rest=[q for q in pool if q["diff"]!="Hard"]
    random.shuffle(hard); random.shuffle(rest)
    p3=(hard+rest)[:n]
    remaining=[q for q in pool if q not in p3]
    random.shuffle(remaining)
    p1=remaining[:n]; p2=remaining[n:2*n]
    assert len(p1)==n and len(p2)==n and len(p3)==n, (len(p1),len(p2),len(p3),len(pool))
    return p1,p2,p3

# Distribution per paper (REPORTED/DERIVED ONLY — official scheme gives NO per-subject split)
DIST=[("Raj GK & Admin", raj, 50),("Geography of India", geo, 10),("General Science", sci, 15),("Reasoning & Maths", reas, 15),("General Hindi & English", lang, 15),("Computer Knowledge", comp, 5),("Current Affairs & Public Health", caph, 10)]
papers=[[],[],[]]  # papers[0]=P1, [1]=P2, [2]=P3
for name,pool,n in DIST:
    a,b,c=partition(pool,n)
    papers[0].extend(a); papers[1].extend(b); papers[2].extend(c)
for i,p in enumerate(papers):
    assert len(p)==120, (i,len(p))
    qs=[x["q"] for x in p]
    assert len(set(qs))==120, f"dup within paper {i+1}"
allqs=[x["q"] for p in papers for x in p]
assert len(set(allqs))==360, f"cross-paper dup: {len(set(allqs))} unique of 360"
# Shuffle question order within each paper (keep subject mix interleaved like real paper)
for p in papers: random.shuffle(p)

def render_paper(idx, title, subtitle):
    p=papers[idx]
    L=[]
    L.append(f"# {title}\n")
    L.append(f"**{subtitle}**\n")
    L.append("**⚠️ ALL 120 questions below are PREDICTED / GENERATED — NOT actual PYQs. No question is reproduced from a real CET paper. Use for practice only.**\n")
    L.append("**Exam conditions:** 120 questions • 240 marks • 150 minutes answering + **10 minutes extra after the paper for OMR verification** (official) • +2 correct • −2/3 wrong • **E = 0** (deliberate skip) • **Blank (no circle darkened) = −2/3 mark each if 12 or fewer blanks; MORE THAN 10% blanks (13+ of 120) = DISQUALIFIED** (Adv 08/2026 Rule 5, pp.15–22) • **Blue ball-point pen only** • One circle per question mandatory — darken E if you do not know the answer; **never leave a circle blank** (a blank costs −2/3 and counts toward disqualification, while E costs 0 and a random guess has EV 0.0 — see §12). Qualifying: 40% = 96/240 (35% = 84/240 for SC/ST) — reported; verify against the official notification.\n")
    L.append("**Subject mix used (REPORTED/DERIVED ONLY — the official scheme gives NO per-subject question split):** Raj GK & Admin 50 • Geo India 10 • Science 15 • Reasoning/Maths 15 • Hindi+English 15 • Computer 5 • Current Affairs & Public Health 10 = 120.\n")
    L.append("## Questions\n")
    for i,q in enumerate(p,1):
        L.append(f"**Q{i}. [{q['topic']} | {q['diff']}]** {q['q']}\n")
        L.append(fmt_opts(q['opts'])+"\n")
    L.append("## Answer Key\n")
    L.append("| Q | Ans | Q | Ans | Q | Ans | Q | Ans |")
    L.append("|---|---|---|---|---|---|---|---|")
    for r in range(0,120,4):
        cells=[]
        for k in range(4):
            j=r+k
            cells.append(f"{j+1} | **{chr(65+papers[idx][j]['ans'])}**")
        L.append("| "+" | ".join(cells)+" |")
    L.append("\n## Brief Explanations (in question order)\n")
    for i,q in enumerate(p,1):
        L.append(f"**Q{i}. Answer {chr(65+q['ans'])}** — {q['expl']}\n")
    return "\n".join(L)

header="""# RAJASTHAN CET SENIOR SECONDARY LEVEL 2026 — THREE FULL-LENGTH MOCK PAPERS

**Advt 08/2026 • RSSB • Exam 1–3 Dec 2026 (revised from 23–25 Oct 2026) • 120 Q / 240 marks / 150 min + 10 min OMR verification**
**Marking: +2 correct, −2/3 wrong, E = 0, blank = −2/3 each (≤12 blanks); 13+ blanks = DISQUALIFIED (Rule 5). Blue ball-point pen only.**
**Qualifying: 40% = 96/240; 35% = 84/240 for SC/ST (reported — verify in official notification).**

> **ALL 360 questions are PREDICTED / GENERATED for practice — NOT actual PYQs.** No question is claimed to be from a real CET paper. No question is repeated across the three papers (verified: 360 unique questions). The subject split below is **reported/derived only; the official scheme gives NO per-subject split** — do not treat it as official weightage.
>
> **How to use:** Sit each paper in one 150-minute sitting, use a printed OMR-style sheet, darken **E** for every question you deliberately skip, **never leave a circle blank**, then score with Score = (Correct×2) − (Incorrect×2/3) − (Blank×1/3). E responses count as neither correct nor incorrect. Log the result in `performance_tracker.csv`.

## Contents
- Paper 1 — Historical-trend oriented (Raj GK heavy in style, but ALL subjects covered)
- Paper 2 — Balanced syllabus coverage
- Paper 3 — Challenging / unexpected (conceptual, statement-based, matching, assertion-reason, new areas: Public Health, VB-G RAM G, Unfair Means Act 2022)

---
"""
body=header
body+="\n"+render_paper(0,"PAPER 1 — HISTORICAL-TREND ORIENTED","Raj GK in PYQ style (forts, rulers, rivers, fairs, polity) + full coverage of Science, Maths/Reasoning, Hindi, English, Computer, Public Health & Current Affairs. Difficulty: mostly Easy–Medium.")
body+="\n---\n"+render_paper(1,"PAPER 2 — BALANCED SYLLABUS COVERAGE","Even coverage of all 13 syllabus heads: Raj GK, India Geo, Science, Reasoning/Maths, Hindi, English, Computer, Public Health, Current Affairs. Difficulty: mixed Easy–Medium–Hard.")
body+="\n---\n"+render_paper(2,"PAPER 3 — CHALLENGING / UNEXPECTED","Conceptual, statement-based, matching-style and assertion-type questions; Hard questions prioritised; new syllabus areas (Public Health, VB-G RAM G 2025, Unfair Means Act 2022, 2023-district changes). Difficulty: mostly Medium–Hard.")
with open(f"{OUT}/mock_papers.md","w",encoding="utf-8") as f: f.write(body)
print("mock_papers.md written:", len(body), "chars; unique Qs:", len(set(allqs)))

# ---------- STUDY PLAN (balanced across ALL subjects) ----------
plan = """# 20-DAY STUDY PLAN — RAJASTHAN CET SENIOR SECONDARY 2026
**12 Nov – 1 Dec 2026 • 5–6 hours/day • Exam 1–3 Dec 2026 • 120Q / 240 marks / 150 min + 10 min OMR verification**

> **Balance rule (user correction, 11 Nov):** NO subject is Raj-GK-only. Every day covers 2–3 subjects; each of Science, Maths, Reasoning, Hindi, English, Computer, Public Health, Indian GK, Rajasthan GK and Current Affairs gets dedicated days AND daily revision blocks. The subject split in the mocks (Raj 50 / Geo 10 / Science 15 / Reasoning-Maths 15 / Hindi+English 15 / Computer 5 / CA+PH 10) is **reported/derived only — the official scheme gives NO per-subject split**.

## OMR & NEGATIVE-MARKING STRATEGY (verified, Adv 08/2026 Rule 5, pp.15–22)
- **+2** correct • **−2/3 (−0.667)** wrong • **E = 0** (deliberate skip, darken the E circle) • **Blank (no circle) = −2/3 each if ≤12 blanks; 13+ blanks (more than 10% of 120) = DISQUALIFIED.** Blue ball-point pen only; one circle per question mandatory; **10 extra minutes after the paper for OMR verification** — use them to check every row has exactly one circle darkened.
- **NEVER leave a circle blank.** A blank costs −0.667 and counts toward disqualification; E costs 0. If you truly do not know, darken E.
- **Expected Value (EV) per attempt, per question (correct +2, wrong −2/3):**
  - Random guess, p=0.25: EV = 0.25×2 − 0.75×0.667 = 0.50 − 0.50 = **0.00** (neutral — same as E).
  - 1 option eliminated (p=1/3): EV = 0.333×2 − 0.667×0.667 = 0.667 − 0.444 = **+0.222** → **ATTEMPT**.
  - 2 options eliminated (p=0.50): EV = 0.50×2 − 0.50×0.667 = 1.00 − 0.333 = **+0.667** → **ATTEMPT**.
  - 3 eliminated / certain (p≈1): EV ≈ **+2.00** → **ATTEMPT**.
  - No elimination at all: EV = 0.00 = E — **darken E, do NOT leave blank** (blank EV = −0.667, worse than both).
  - Rule of thumb: **attempt if you can eliminate ≥1 option; otherwise mark E.** Over 120Q, attempting all 1-elimination questions at EV +0.222 each is worth real marks; blind guessing adds nothing on average but adds variance.
- **Qualifying target:** 96/240 (40%; SC/ST 84/240 = 35%) — reported, verify officially. Aim in mocks for **≥120/240** to have a safety margin, not just 96.
- **Worked example:** 70 correct, 30 wrong, 20 E, 0 blank → Score = 70×2 − 30×0.667 = 140 − 20 = **120**. The same paper with 20 blanks instead of E → 140 − 20 − 20×0.667 = **106.7**, plus disqualification outright (here 20 blanks = disqualified). **E vs blank is a 13.3-mark swing and a disqualification risk — never blank.**
- **Time plan (150 min / 120Q = 75 sec/Q):** Pass 1 (0–90 min): answer all Easy/certain questions, mark E provisionally for unsure ones, circle Q-nos to revisit — do not spend >90 sec on any one question. Pass 2 (90–130 min): revisit marked questions, apply elimination, attempt if ≥1 eliminated else confirm E. Pass 3 (130–150 min): fill every remaining circle (E if unsure), check numbering. **+10 min OMR verification:** verify every row has exactly one darkened circle, no blanks, no double-marks, roll no. and booklet code correct.
- **Daily test scoring:** always use Score = (Correct×2) − (Incorrect×2/3) − (Blank×1/3); E = 0. Log Correct / Incorrect / E / Blank separately in the tracker. A day with any blank is a failed OMR day — fix the habit, not just the score.

## DAILY TEMPLATE (5–6 hrs)
| Block | Time | What |
|---|---|---|
| 1 | 90 min | Main subject — notes + facts (see day table) |
| 2 | 60 min | Second subject — notes / PYQ-style practice |
| 3 | 60 min | MCQ practice (target in day table) + error-notebook entry |
| 4 | 45 min | Daily test (25–30Q mixed, timed, with E/blank discipline) |
| 5 | 45 min | Cumulative revision (previous days' weak areas first) + end-of-day evaluation |

**End-of-day evaluation (every day):** Score today's test with the formula above; list top 3 weak topics; copy them into tomorrow's Block 5; update `performance_tracker.csv` (Accuracy, Weak_Areas, Revision_Status). If accuracy <50% in a subject, that subject gets an extra 30 min the next day.

## DAY-BY-DAY PLAN (12 Nov – 1 Dec 2026)

| Day / Date | Main subject (Block 1) | Second subject (Block 2) | MCQ target | Daily test | Revision focus |
|---|---|---|---|---|---|
| Day 1 — Thu 12 Nov | **Rajasthan History** — rulers, battles (Haldighati 1576, Khanwa 1527, Tarain 1191/1192), unification 1948–56 | **General Hindi** — sandhi, paryayvachi, vilom, muhavare | 60 | 30Q mixed | — |
| Day 2 — Fri 13 Nov | **Rajasthan Geography** — Aravalli, Thar, rivers (Chambal/Banas/Luni), lakes, districts | **General Science: Biology** — human body, vitamins, diseases | 60 | 30Q | Day 1 History |
| Day 3 — Sat 14 Nov | **Rajasthan Art & Culture** — forts, paintings (Phad/Pichwai/Kota-Bundi), dances, fairs, GI tags | **Mathematics** — SI, %, average, ratio, speed (formula sheet) | 60 | 30Q | Days 1–2 |
| Day 4 — Sun 15 Nov | **Indian Polity (Raj focus)** — Assembly 200, LS 25/RS 10, HC Jodhpur, Panchayati Raj (Nagaur 1959), 73rd/74th | **General English** — synonym/antonym, spelling, voice, prepositions | 60 | 30Q | Days 1–3 weak areas |
| Day 5 — Mon 16 Nov | **Rajasthan Economy** — agriculture (bajra/mustard), minerals (zinc-lead, marble), irrigation (IGC, Bisalpur, Rana Pratap Sagar), solar (Bhadla) | **General Science: Physics** — units, light, sound, electricity | 60 | 30Q | Days 1–4 |
| Day 6 — Tue 17 Nov | **Logical Reasoning** — series, coding, odd-one, analogy, direction, calendar | **Computer Knowledge** — CPU/RAM, MS Office, shortcuts, internet, full forms | 60 | 30Q Reasoning | Days 3–5 |
| Day 7 — Wed 18 Nov | **Geography of India** — rivers, soils, monsoon, dams, coastline, Green/Blue revolutions | **Public Health** — NHM, Mission Indradhanush, Pulse Polio, ORS, anaemia, JSY, Poshan | 60 | 30Q | Week 1 full revision (Days 1–6) |
| Day 8 — Thu 19 Nov | **Current Affairs (last 12 months)** — schemes (VB-G RAM G 2025, PM-JAY, Jal Jeevan, PM-KISAN), Chandrayaan-3, G20 2023, NEP 2020 | **General Hindi** — karak, vachya, sarvanam, shuddha vartani | 60 | 30Q CA | Days 1–7 weakest subject |
| Day 9 — Fri 20 Nov | **Rajasthan History + Culture — consolidation** — forts × rulers × fairs × temples (timed recall, no notes first) | **General Science: Chemistry** — acids, salts, metals, pH, greenhouse gases | 60 | 30Q | Days 1–8 |
| Day 10 — Sat 21 Nov | **Mathematics + Reasoning — consolidation** — 40 mixed numericals timed (75 sec/Q) | **General English** — idioms, one-word, tense, articles | 60 | 30Q Maths/Reasoning | Days 1–9 |
| Day 11 — Sun 22 Nov | **MOCK PAPER 1** (full 150 min + 10 min OMR check, exam conditions) | — (post-mock analysis in Block 3) | 120 (mock) | Mock 1 | Full error notebook from Mock 1 |
| Day 12 — Mon 23 Nov | **Rajasthan Polity + Schemes** — CM/Governor firsts, RPSC/RSSB, Bhamashah, Chiranjeevi/Ayushman Arogya, Nishulk Dava, Unfair Means Act 2022 | **Computer + Public Health** — mixed revision | 60 | 30Q | Mock 1 weak topics |
| Day 13 — Tue 24 Nov | **Science — consolidation** — Physics + Chemistry + Biology mixed (45Q timed) | **Geography of India + Rajasthan Geo** — map-based recall | 60 | 30Q Science | Days 1–12 |
| Day 14 — Wed 25 Nov | **Hindi + English — consolidation** — 45Q mixed language timed | **Current Affairs refresh** — new items since Day 8 + Rajasthan CA | 60 | 30Q Language | Mock 1 + Days 12–13 |
| Day 15 — Thu 26 Nov | **MOCK PAPER 2** (full 150 min + 10 min OMR check, exam conditions) | — (post-mock analysis) | 120 (mock) | Mock 2 | Full error notebook from Mock 2 |
| Day 16 — Fri 27 Nov | **Weak-area day** — top 3 weakest subjects from Mocks 1–2 (from tracker, not guesswork) | **Reasoning + Maths** — only error types seen in mocks | 80 | 30Q weak subjects | Mocks 1–2 errors |
| Day 17 — Sat 28 Nov | **Rajasthan GK — rapid revision** — 1-page fact sheets: forts, rivers, lakes, dances, fairs, symbols, census 2011 | **Science + Computer** — formula & full-form rapid recall | 80 | 30Q | All weak areas |
| Day 18 — Sun 29 Nov | **MOCK PAPER 3** (full 150 min + 10 min OMR check, exam conditions — hardest paper) | — (post-mock analysis) | 120 (mock) | Mock 3 | Full error notebook from Mock 3 |
| Day 19 — Mon 30 Nov | **Full-syllabus rapid revision** — all subjects, 30 min each: Raj GK, Science, Maths/Reasoning, Hindi, English, Computer, PH, CA, India Geo | **OMR drill** — 30Q in 35 min with strict E/blank discipline | 60 | 30Q mixed | Mock 3 errors only |
| Day 20 — Tue 1 Dec | **FULL MOCK + OMR PRACTICE** — re-attempt your lowest-scoring mock paper (or Mock 1) under exam conditions; final OMR check drill; light revision only after lunch; **no new topics**; sleep early | **Exam kit check** — admit card, blue ball-point pens (×3), ID, reporting time | 120 (mock re-attempt) | Full mock | Error notebook — read only, do not start new material |

## WEEKLY CHECKPOINTS
- **After Day 7:** all 10 subject areas touched at least once; tracker filled for Days 1–7.
- **After Day 11 (Mock 1):** target ≥96/240 (qualifying); if below, Days 12–14 shift 30 min/day to the two weakest subjects.
- **After Day 15 (Mock 2):** target ≥110/240; error notebook must show repeated-mistake patterns, not just scores.
- **After Day 18 (Mock 3):** target ≥110/240 on the hardest paper; if any mock had ≥1 blank, do an extra OMR drill on Day 19.
- **Day 20:** no new topics. A calm, OMR-clean re-attempt beats a new chapter.

## SOURCES & CAVEATS
- Pattern/marking/OMR: RSSB Adv 08/2026 (pp.15–22, RajKaj 22979471) via user-uploaded extract — Rule 5 disqualification, blue pen, +10 min OMR time, E/blank rules as stated above. Qualifying 40%/35% — reported; verify in the official notification before the exam.
- Subject split in mocks: reported/derived only; official scheme gives NO per-subject split.
- Current Affairs in mocks is generated/predicted practice material — refresh it from a newspaper / PIB / Rajasthan Patrika in the last week; do not rely on any single mock for CA.
"""
with open(f"{OUT}/study_plan_20day.md","w",encoding="utf-8") as f: f.write(plan)
print("study_plan_20day.md written")

# ---------- TRACKER ----------
subjects=["Rajasthan GK & History","Rajasthan Art & Culture","Rajasthan Geography","Rajasthan Polity & Economy","Geography of India","General Science","Mathematics","Logical Reasoning","General Hindi","General English","Computer Knowledge","Public Health","Current Affairs"]
with open(f"{OUT}/performance_tracker.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f)
    w.writerow(["Subject","Topics_Completed","PYQs_Solved","MCQs_Solved","Accuracy","Weak_Areas","Revision_Status"])
    for s in subjects:
        w.writerow([s,0,0,0,"","","Not started"])
    w.writerow([])
    w.writerow(["MOCK TEST LOG — fill one row per mock / daily test"])
    w.writerow(["Date","Paper","Correct","Incorrect","E_Unattempted","Blank","Score","Accuracy_pct","Notes"])
    w.writerow(["2026-11-22","Mock Paper 1","","","","","","",""])
    w.writerow(["2026-11-26","Mock Paper 2","","","","","","",""])
    w.writerow(["2026-11-29","Mock Paper 3","","","","","","",""])
    w.writerow(["2026-12-01","Mock re-attempt (Day 20)","","","","","","",""])
    w.writerow([])
    w.writerow(["SCORE CALCULATOR — Score = (Correct x 2) - (Incorrect x 2/3) - (Blank x 1/3). E responses are NOT counted as incorrect and score 0."])
    w.writerow(["Example: 70 correct, 30 wrong, 20 E, 0 blank => 70*2 - 30*0.667 - 0 = 120.00"])
    w.writerow(["Example: same paper but 20 blanks instead of E => 140 - 20 - 20*0.667 = 106.67 AND 20 blanks > 12, so DISQUALIFIED under Rule 5 (more than 10% blanks)."])
    w.writerow(["Qualifying: 96/240 (40%); SC/ST 84/240 (35%) — reported, verify officially. Aim >=120/240 in mocks."])
    w.writerow(["OMR RULE: more than 10% blanks (13+ of 120) = DISQUALIFIED. 12 or fewer blanks = -2/3 mark each. Blue ball-point pen only. One circle per question; darken E for deliberate skips. +10 min OMR verification after the paper."])
    w.writerow(["EV RULE: attempt if you can eliminate >=1 option (EV +0.222 with 1 eliminated, +0.667 with 2 eliminated); random guess EV = 0.00 = E; blank EV = -0.667. Never leave a circle blank."])
print("performance_tracker.csv written")
