from django.db import models
<<<<<<< HEAD
=======
from django.contrib.auth.models import User
>>>>>>> 61f8d20b1749de51cae8f50bd2748639645c85df



class Register(models.Model):
<<<<<<< HEAD
    patientid= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    email = models.CharField(max_length=50)
    passwd = models.CharField(max_length=20)
    confirmpasswd = models.CharField(max_length=20)
    mobile = models.IntegerField()
    Add1 = models.CharField(max_length=30)
    Add2 = models.CharField(max_length=30)
    Add3 = models.CharField(max_length=30)
    city= models.CharField(max_length=30)
=======
    patientid= models.IntegerField(primary_key=True,)
    '''name = models.CharField(max_length=50)'''
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    '''email = models.ForeignKey(User, on_delete= models.CASCADE,)'''
    email = models.EmailField()
    '''passwd = models.CharField(max_length=15)'''
    confirmpasswd = models.CharField(max_length=15)
    mobile = models.BigIntegerField()
    Add1 = models.CharField(max_length=70)
    Add2 = models.CharField(max_length=65)
    Add3 = models.CharField(max_length=65)
    city = models.CharField(max_length=30)
>>>>>>> 61f8d20b1749de51cae8f50bd2748639645c85df
    state = models.CharField(max_length=30)
    pincode = models.IntegerField()




# Create your models here.
