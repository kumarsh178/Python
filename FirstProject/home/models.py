from django.db import models
from django.template.defaultfilters import slugify
from home.utils import generateNewSlug
from django.db.models import CheckConstraint, Q
# Create your models here.
class Student(models.Model):
    gender_choices = (('Male', 'Male') , ('Female' , 'Female'))
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=12)
    email = models. EmailField()
    gender = models.CharField(max_length=10 ,choices=gender_choices , default = "Male")
    age = models. IntegerField(null = True , blank=True)
    date_of_birth = models. DateField()
    profile_image = models. ImageField(null=True , blank=True, upload_to="student/")
    file = models. FileField(upload_to="files/")
    student_bio = models.TextField()
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True)
#author
class Author(models.Model):
    author_name = models.CharField(max_length=100)
    class Meta:
        db_table = "Author3"
        verbose_name = "Manage Books"
        verbose_name_plural = "Manage Books 2"
class Book(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100, default=None)
    brand = models.CharField(max_length=100, null=True, blank=True)
class Products(models.Model):
    name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to="product_images/")
    product_slug = models.SlugField(max_length=200,null=True, blank=True)

    def save(self, *args, **kwargs) -> None:
        if not self.id:
            self.product_slug = generateNewSlug(self.name, Products)
        return super().save(*args, **kwargs)
class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    age=models.IntegerField(null=True,blank=True)
    class Meta:
        constraints = [
                CheckConstraint(check = Q(age__gte = 18), name='age')
        ]
class StudentCollege(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

