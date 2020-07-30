from django.db import models

class Departments(models.Model):
    doctorID=models.IntegerField(primary_key=True)
    docname= models.CharField(max_length=50)
    specialisation=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    post=models.CharField(max_length=30)





