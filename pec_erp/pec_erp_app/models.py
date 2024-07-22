from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('hod', 'HOD'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=20)
    batch = models.CharField(max_length=10)
    mode = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    father = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='pics')

class Faculty(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    staff_id = models.CharField(max_length=20)
    dept = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='pics')

class HOD(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    staff_id = models.CharField(max_length=20)
    dept = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='pics')