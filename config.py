import os

TOTAL_IMAGES = 10000        # Total number of images to generate
IMAGES_PER_BATCH = 1000     # Number of images to generate per batch folder
OUTPUT_DIR = "dataset_prescriptions"
NUM_WORKERS = os.cpu_count() or 4

#TTF handwritings 
FONT_URLS = {
    "Zeyada": "https://github.com/google/fonts/raw/main/ofl/zeyada/Zeyada.ttf",
    "HerrVonMuellerhoff": "https://github.com/google/fonts/raw/main/ofl/herrvonmuellerhoff/HerrVonMuellerhoff-Regular.ttf",
    "Nanum_Pen_Script": "https://github.com/google/fonts/raw/main/ofl/nanumpenscript/NanumPenScript-Regular.ttf",
    "Dancing_Script": "https://github.com/google/fonts/raw/main/ofl/dancingscript/DancingScript%5Bwght%5D.ttf",
    "Liu_Jian_Mao_Cao": "https://github.com/google/fonts/raw/main/ofl/liujianmaocao/LiuJianMaoCao-Regular.ttf"
}

HOSPITALS = [
    ("ST. JUDE MEMORIAL HOSPITAL", "Department of Internal Medicine"),
    ("METRO HEALTHCARE CLINIC", "General Medicine & Cardiology"),
    ("CITY CARE MEDICAL CENTER", "Outpatient Department (OPD)"),
    ("APEX SPECIALTY CLINIC", "Consultant Physician & Diabetologist"),
    ("GRACE COMMUNITY HOSPITAL", "Family Medicine & Urgent Care"),
    ("APOLLO SPECTRA HOSPITAL", "Multi-Specialty Care Unit"),
    ("FORTIS ESCORTS HEART INSTITUTE", "Department of Cardiology"),
    ("AIIMS ANNEXE CLINIC", "General Outpatient Services"),
    ("MEDANTA CITY HOSPITAL", "Department of Internal Medicine"),
    ("KOKILABEN DHIRUBHAI MEDICAL CENTER", "Endocrinology & Diabetes Care"),
    ("NARAYANA MULTISPECIALITY HOSPITAL", "Department of Nephrology"),
    ("MAX SUPER SPECIALITY HOSPITAL", "Department of Pulmonology"),
    ("RUBY GENERAL HOSPITAL", "Department of Gastroenterology"),
    ("SUSHRUTA NURSING HOME", "General Physician & Consultant"),
    ("SANJEEVANI POLYCLINIC", "Family Medicine Practice"),
    ("LILAVATI HOSPITAL & RESEARCH CENTRE", "Department of Neurology"),
    ("VIDYASAGAR HEALTH CENTER", "General Medicine & Pediatrics"),
    ("ASHIRWAD MEDICAL COLLEGE HOSPITAL", "Department of Orthopedics")
]

DOCTORS = [
    ("Dr. Arthur Vance, M.D.", "Reg No: MED-884920"),
    ("Dr. Sarah Jenkins, M.S.", "Reg No: REG-441029"),
    ("Dr. Robert Chen, M.B.B.S", "Reg No: DOC-992184"),
    ("Dr. Maria Garcia, M.D.", "Reg No: MED-110293"),
    ("Dr. James Wilson, M.D.", "Reg No: REG-773012"),
    ("Dr. Rajesh Sharma, M.B.B.S., M.D.", "Reg No: MCI-556812"),
    ("Dr. Anita Deshmukh, M.D. (Medicine)", "Reg No: MCI-778234"),
    ("Dr. Vikram Nair, M.S. (Ortho)", "Reg No: KMC-991823"),
    ("Dr. Priya Iyer, M.D. (Pediatrics)", "Reg No: TNMC-234871"),
    ("Dr. Suresh Reddy, M.D. (Cardiology)", "Reg No: APMC-664521"),
    ("Dr. Kavita Menon, M.D. (Endocrinology)", "Reg No: KSMC-118732"),
    ("Dr. Arvind Chatterjee, M.B.B.S., D.M.", "Reg No: WBMC-559012"),
    ("Dr. Neha Kapoor, M.D. (Dermatology)", "Reg No: DMC-773455"),
    ("Dr. Mohammed Iqbal, M.S. (General Surgery)", "Reg No: MCI-902341"),
    ("Dr. Ritu Bhatia, M.D. (Gynaecology)", "Reg No: PMC-441982"),
    ("Dr. Sanjay Gupta, M.D. (Nephrology)", "Reg No: DMC-227845"),
    ("Dr. Lakshmi Venkatesh, M.D. (Pulmonology)", "Reg No: KMC-338291"),
    ("Dr. Amitav Bose, M.B.B.S., M.D.", "Reg No: WBMC-664918")
]

PATIENTS = [
    "John Doe", "Jane Smith", "Robert Miller", "Emily Davis",
    "Michael Brown", "David Wilson", "Sarah Conor", "Alex Thorne",
    "Rahul Verma", "Priya Nair", "Amitabh Sinha", "Sneha Reddy",
    "Arjun Kapoor", "Divya Menon", "Rohit Sharma", "Ananya Iyer",
    "Vikas Gupta", "Pooja Chatterjee", "Karan Malhotra", "Neha Joshi",
    "Suresh Pillai", "Meera Krishnan", "Aditya Bose", "Kavya Rao",
    "Manoj Tiwari", "Ritika Desai", "Sandeep Yadav", "Shalini Agarwal",
    "Gaurav Mehta", "Anjali Bhatt", "Deepak Choudhury", "Swati Bansal",
    "Imran Khan", "Fatima Sheikh", "Rajesh Patel", "Nandini Rao"
]

DIAGNOSES = [
    "Acute Pharyngitis", "Type 2 Diabetes Control",
    "Upper Respiratory Tract Infection", "Essential Hypertension",
    "Mild Gastritis", "Acute Bronchitis", "Allergic Rhinitis",
    "Chronic Kidney Disease Stage 3", "Acute Myocardial Infarction (post-op follow-up)",
    "Community Acquired Pneumonia", "Congestive Heart Failure (NYHA II)",
    "Chronic Obstructive Pulmonary Disease (COPD)", "Dengue Fever (recovering)",
    "Typhoid Fever", "Acute Appendicitis (post-surgical review)",
    "Rheumatoid Arthritis Flare", "Migraine with Aura",
    "Hypothyroidism", "Hyperlipidemia", "Peptic Ulcer Disease",
    "Urinary Tract Infection", "Viral Hepatitis A", "Anemia (Iron Deficiency)",
    "Bronchial Asthma - Exacerbation", "Acute Gastroenteritis",
    "Cellulitis - Lower Limb", "Sciatica / Lumbar Radiculopathy",
    "Generalized Anxiety Disorder", "Osteoarthritis - Knee",
    "Chikungunya - Post Fever Arthralgia", "Tuberculosis (on ATT, Month 3 review)"
]

MEDICINES_POOL = [
    "Amoxicillin 500mg --- 1 cap t.i.d. x 7d",
    "Paracetamol 650mg -- 1 tab p.r.n. (fever)",
    "Pantoprazole 40mg -- 1 tab o.d. b.f. x 14d",
    "Cetirizine 10mg ---- 1 tab h.s. x 5d",
    "Metformin 500mg ---- 1 tab b.d. with meal",
    "Atorvastatin 10mg -- 1 tab h.s.",
    "Azithromycin 500mg - 1 tab o.d. x 3d",
    "Omeprazole 20mg ---- 1 cap b.d. b.f.",
    "Ibuprofen 400mg ---- 1 tab t.i.d. p.c.",
    "Doxycycline 100mg -- 1 cap b.d. x 7d",
    "Montelukast 10mg --- 1 tab h.s.",
    "Levothyroxine 50mcg - 1 tab o.d. empty stomach",
    "Amlodipine 5mg ------ 1 tab o.d. morning",
    "Losartan 50mg ------- 1 tab o.d.",
    "Clopidogrel 75mg ---- 1 tab o.d. x 30d",
    "Aspirin 75mg -------- 1 tab o.d. h.s.",
    "Furosemide 40mg ----- 1 tab o.d. morning",
    "Insulin Glargine 10U - s.c. inj. o.d. h.s.",
    "Salbutamol Inhaler -- 2 puffs p.r.n. (breathlessness)",
    "Budesonide + Formoterol -- 1 puff b.d.",
    "Rifampicin + Isoniazid + Pyrazinamide -- as per ATT chart",
    "Ceftriaxone 1g ------ IV b.d. x 5d",
    "Ondansetron 4mg ----- 1 tab sos (vomiting)",
    "Ranitidine 150mg ---- 1 tab b.d.",
    "Diclofenac 50mg ----- 1 tab b.d. p.c. x 3d",
    "Tramadol 50mg ------- 1 tab sos (severe pain)",
    "Prednisolone 10mg --- 1 tab o.d. tapering x 5d",
    "Hydroxychloroquine 200mg -- 1 tab b.d.",
    "Folic Acid 5mg ------ 1 tab o.d.",
    "Iron + Folic Acid --- 1 tab o.d. p.c.",
    "Sertraline 50mg ----- 1 tab o.d. morning",
    "Alprazolam 0.25mg --- 1 tab h.s. sos",
    "Multivitamin Syrup -- 10ml o.d. x 15d",
    "ORS Sachet ---------- 1 packet in 1L water, sos",
    "Vitamin D3 60000 IU - 1 sachet weekly x 8 wks",
    "Calcium + Vitamin D3 - 1 tab o.d."
]

SIDE_NOTES_MARGIN = [
    "NKA (No Known Allergies)",
    "Allergy: Sulfa drugs",
    "Allergy: Penicillin!",
    "B.P. Check weekly",
    "Weight: 68 kg",
    "Weight: 82 kg | BMI: 27.4",
    "FBS: 142 mg/dL",
    "PPBS: 210 mg/dL",
    "HbA1c: 8.2%",
    "SpO2 room air: 97%",
    "S. Creatinine: 1.1",
    "TC/HDL: Normal"
]

ADVICE_NOTES = [
    "Advised low salt, low fat diet",
    "Strict bed rest x 3 days",
    "Avoid oily/spicy foods & caffeine",
    "Plenty of fluids (3-4L daily)",
    "Avoid NSAIDs / Painkillers",
    "Steam inhalation b.d.",
    "Warm saline gargle t.i.d.",
    "Monitor blood sugar logs daily",
    "Review with USG Abdomen reports"
]