from django.db import models

class Departments(models.Model):
    doctorID = models.IntegerField(primary_key=True)
    docname = models.CharField(max_length=50)
    specialisation = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100)
    post=models.CharField(max_length=70)
    Experience = models.CharField(max_length=20,default="no experience")

# Create your models here.
