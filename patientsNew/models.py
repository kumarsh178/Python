from django.db import models

class Patient(models.Model):

    patient_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    diagnosis = models.TextField(null=True, blank=True)
    doctor = models.CharField(max_length=100, null=True, blank=True)
    room = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name


class PatientDocument(models.Model):

    file = models.FileField(upload_to="patient_docs/")
    uploaded_at = models.DateTimeField(auto_now_add=True)