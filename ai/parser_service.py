import re
import uuid

def parse_patient(text):
    text = clean_ocr_text(text).lower()  # clean text first

    data = {
        "patient_id": None,
        "name": None,
        "age": None,
        "diagnosis": None,
        "doctor": None,
        "room": None
    }

    for line in text.splitlines():
        line = line.strip()
        # Patient ID
        if not data["patient_id"]:
            match = re.search(r'patient\s*id[:\s]*([a-z0-9]+)', line, re.IGNORECASE)
            if match:
                data["patient_id"] = match.group(1)
        # Name
        if not data["name"]:
            match = re.search(r'name[:\s]*([a-z\s]+)', line, re.IGNORECASE)
            if match:
                data["name"] = match.group(1)
        # Age
        if not data["age"]:
            match = re.search(r'age[:\s]*(\d+)', line, re.IGNORECASE)
            if match:
                data["age"] = match.group(1)
        # Diagnosis
        if not data["diagnosis"]:
            match = re.search(r'diagnosis[:\s]*([a-z\s]+)', line, re.IGNORECASE)
            if match:
                data["diagnosis"] = match.group(1)
        # Doctor (also allow typo 'Dector')
        if not data["doctor"]:
            match = re.search(r'(doctor|dector)[:\s]*([a-z\s\.]+)', line, re.IGNORECASE)
            if match:
                data["doctor"] = match.group(2).strip()
        # Room (also allow typo 'Oom')
        if not data["room"]:
            match = re.search(r'(room|oom)[:\s]*(\d+)', line, re.IGNORECASE)
            if match:
                data["room"] = match.group(2).strip()

    # Generate patient_id if missing
    if not data["patient_id"]:
        data["patient_id"] = "P" + str(uuid.uuid4())[:6]

    return data

def clean_ocr_text(text):
    # Replace multiple newlines with single newline
    text = re.sub(r'\n+', '\n', text)
    # Remove leading/trailing spaces on each line
    text = '\n'.join([line.strip() for line in text.splitlines()])
    return text