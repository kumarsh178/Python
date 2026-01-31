from django.db import models

# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=150)
    coursesChoice = [("bca","BCA"),("mca","MCA"),("mba","MBA")]
    courses=models.CharField(choices=coursesChoice, max_length=50)
    video_url=models.CharField(max_length=100)
    def __str__(self):
        return self.title
    class Meta:
        db_table="courses_courses"
        verbose_name="Manage Courses"