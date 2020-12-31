from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vaccines(models.Model):
    VaccineID = models.CharField(max_length = 10, primary_key = True)
    Vaccine_Name = models.CharField(max_length = 150)
    Age = models.IntegerField()
    Dosage = models.CharField(max_length = 100)
    Cost = models.IntegerField()
    #checked = models.BooleanField(default = False)

class Availability(models.Model):
    sno = models.IntegerField(primary_key = True)
    VaccineID = models.ForeignKey(Vaccines, on_delete = models.CASCADE, )
    timeslot1 = models.CharField(max_length = 15)
    timeslot2 = models.CharField(max_length = 15)
    timeslot3 = models.CharField(max_length = 15)
    timeslot4 = models.CharField(max_length = 15)
    timeslot5 = models.CharField(max_length = 15)
    dayunavailable1 = models.CharField(max_length = 10)
    dayunavailable2 = models.CharField(max_length = 10)

# class Appointment(models.Model):
#     aptid = models.AutoField(primary_key = True,)
#     VaccineID = models.ForeignKey(Vaccines, on_delete = models.CASCADE, )
#     patientID = models.ForeignKey(User, on_delete = models.CASCADE, )
#     time = models.CharField(max_length = 15)
#     date = models.DateField()
#     status = models.BooleanField(default = 0)

class Vaccines_payment(models.Model):
    bookingID = models.AutoField(primary_key = True,)
    patientID = models.ForeignKey(User, on_delete = models.CASCADE, )
    fname = models.CharField(max_length=50)
    email = models.EmailField()
    Add = models.CharField(max_length=70)
    city = models.CharField(max_length=30)
    Vaccinename = models.CharField(max_length=100)
    price = models.IntegerField()
    state = models.CharField(max_length=30)
    pincode = models.IntegerField()
    cardname = models.CharField(max_length=30)
    cardnumber = models.BigIntegerField()
    exp_month = models.CharField(max_length=30)
    exp_year = models.IntegerField()
    cvv = models.IntegerField()