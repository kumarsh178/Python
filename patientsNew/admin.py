from django.contrib import admin
from .models import Patient, PatientDocument


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):

    list_display = ("patient_id","name","age","diagnosis","doctor","room")
    search_fields = ("name","diagnosis","doctor","age")
    list_per_page = 10


@admin.register(PatientDocument)
class PatientDocumentAdmin(admin.ModelAdmin):

    list_display = ("file", "uploaded_at")