from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=20)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)