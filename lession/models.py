from django.db import models # type: ignore
from .models import Course

# Create your models here.
class Lession(models.Model):
    title=models.CharField(max_length=100)
    course=models.ForeignKey(Course, on_delete=models.SET_NULL,null=True)
    position=models.IntegerField()
    video_url=models.CharField(max_length=100)
    def __str__(self):
        return self.title
    class Meta:
        db_table="lession_lession"
        verbose_name="Manage Lession"