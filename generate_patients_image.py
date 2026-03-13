from PIL import Image, ImageDraw, ImageFont
from faker import Faker
import os
import random

fake = Faker()

# create folder
os.makedirs("patient_images", exist_ok=True)

def generate_patient_image(i):

    width = 800
    height = 500

    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    name = fake.name()
    age = random.randint(20, 80)
    gender = random.choice(["Male", "Female"])
    diagnosis = random.choice(["Diabetes", "Hypertension", "Asthma", "Fever"])
    doctor = random.choice(["Dr Sharma", "Dr Mehta", "Dr Rao"])
    room = random.randint(100, 400)

    text = f"""
Patient ID: P{i+1000}
Name: {name}
Age: {age}
Gender: {gender}
Diagnosis: {diagnosis}
Doctor: {doctor}
Room: {room}
"""

    draw.text((50, 50), text, fill="black")

    file_path = f"patient_images/patient_{i}.png"
    img.save(file_path)

    print("Created:", file_path)


for i in range(20):
    generate_patient_image(i)