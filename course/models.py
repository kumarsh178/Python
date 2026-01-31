from django.db import models

# Create your models here.
class Course(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    publish_date=models.DateTimeField()
    price=models.FloatField()
    author = models.CharField(max_length=100)
    statusChoice = [("draft","Draft"),("published","Published")]
    status=models.CharField(choices=statusChoice,max_length=100)
    def __str__(self):
        return self.title
    class Meta:
        db_table="course_course"
        verbose_name="Manage Course"