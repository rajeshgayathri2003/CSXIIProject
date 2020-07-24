from django.db import models

class Departments(models.Model):
    doctorID = models.IntegerField(primary_key=True)
    docname = models.CharField(max_length=50)
    specialisation = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100)
    post = models.CharField(max_length=70)

# Create your models here.
