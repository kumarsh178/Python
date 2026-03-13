import faiss
import pickle
import os
from django.conf import settings
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index_path = os.path.join(settings.BASE_DIR, "patient_index.faiss")
texts_path = os.path.join(settings.BASE_DIR, "patient_texts.pkl")

index = None
texts = None

# Load index only if file exists
if os.path.exists(index_path):

    index = faiss.read_index(index_path)

    with open(texts_path, "rb") as f:
        texts = pickle.load(f)


def search(query):

    global index, texts

    if index is None:
        raise Exception("Index not found. Run: python manage.py reindex_patients")

    query_vector = model.encode([query])

    D, I = index.search(query_vector, k=3)

    return [texts[i] for i in I[0]]