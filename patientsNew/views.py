from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import PatientDocument, Patient
from ai.document_processor import process_document
from ai.parser_service import parse_patient


@api_view(["POST"])
def upload_patient_document(request):

    files = request.FILES.getlist("files")

    for file in files:

        # Save uploaded file
        doc = PatientDocument.objects.create(file=file)

        file_path = doc.file.path

        # OCR
        text = process_document(file_path)

        print("OCR TEXT:", text)

        # Parse patient fields
        data = parse_patient(text)

        print("PARSED DATA:", data)

        if data["name"]:

            # Save patient in MySQL
            patient = Patient.objects.create(**data)

    return Response({"message": "Files processed successfully"})
