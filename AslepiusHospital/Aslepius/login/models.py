from django.db import models



class Register(models.Model):
    patientid= models.CharField(primary_key=True)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    email = models.CharField()
    passwd = models.CharField()
    confirmpasswd = models.CharField()
    mobile = models.IntegerField()
    Add1 = models.CharField(max_length=30)
    Add2 = models.CharField(max_length=30)
    Add3 = models.CharField(max_length=30)
    city= models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.IntegerField()




# Create your models here.
