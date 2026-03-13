from django.core.management.base import BaseCommand
from sentence_transformers import SentenceTransformer
import faiss
import pickle
import os
from django.conf import settings
from patientsNew.models import Patient


class Command(BaseCommand):

    help = "Rebuild patient FAISS index"

    def handle(self, *args, **kwargs):

        print("Creating FAISS index file...")

        model = SentenceTransformer("all-MiniLM-L6-v2")

        patients = Patient.objects.all()

        texts = []

        for p in patients:
            text = f"Patient {p.name}, diagnosis {p.diagnosis}, doctor {p.doctor}"
            texts.append(text)

        embeddings = model.encode(texts)

        index = faiss.IndexFlatL2(len(embeddings[0]))
        index.add(embeddings) # type: ignore

        # File paths
        index_path = os.path.join(settings.BASE_DIR, "patient_index.faiss")
        texts_path = os.path.join(settings.BASE_DIR, "patient_texts.pkl")

        # Save files
        faiss.write_index(index, index_path)

        with open(texts_path, "wb") as f:
            pickle.dump(texts, f)

        print("Index file created successfully")
        print(f"Saved at: {index_path}")
        print(f"Total records indexed: {len(texts)}")