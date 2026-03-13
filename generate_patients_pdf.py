from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import random
import os

names = [
"Rahul Sharma","Anita Singh","Mohit Verma","Priya Nair","Amit Gupta",
"Neha Kapoor","Rohit Yadav","Pooja Mehta","Sanjay Patel","Kavita Joshi",
"Arjun Nair","Sneha Reddy","Rajesh Kumar","Simran Kaur","Deepak Mishra"
]

diagnosis_list = [
"Fever","Diabetes","Asthma","Hypertension",
"Migraine","Covid-19","Heart Disease","Fracture"
]

doctors = [
"Dr. Sharma","Dr. Mehta","Dr. Gupta","Dr. Reddy","Dr. Kapoor"
]

os.makedirs("patient_pdfs", exist_ok=True)

for i in range(1,51):

    patient_id = f"P{3000+i}"
    name = random.choice(names)
    age = random.randint(20,70)
    diagnosis = random.choice(diagnosis_list)
    doctor = random.choice(doctors)
    room = random.randint(100,500)

    file_name = f"patient_pdfs/patient_{i}.pdf"

    c = canvas.Canvas(file_name, pagesize=letter)

    text = c.beginText(50,700)
    text.setFont("Helvetica", 14)

    text.textLine(f"Patient ID: {patient_id}")
    text.textLine(f"Name: {name}")
    text.textLine(f"Age: {age}")
    text.textLine(f"Diagnosis: {diagnosis}")
    text.textLine(f"Doctor: {doctor}")
    text.textLine(f"Room: {room}")

    c.drawText(text)
    c.save()

print("50 patient PDFs created successfully!")