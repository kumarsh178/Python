from django.urls import path
from .views import upload_patient_document

urlpatterns = [
    path("upload/documents", upload_patient_document)
]