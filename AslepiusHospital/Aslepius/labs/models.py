from django.db import models

# Create your models here.
class Labs(models.Model):
    testID = models.IntegerField(primary_key=True)
    testname = models.CharField(max_length=50)
    testprice = models.IntegerField()

class Labs_payment(models.Model):
    fname = models.CharField(max_length=50)
    patientID = models.IntegerField(primary_key=True)
    email = models.EmailField()
    Add = models.CharField(max_length=70)
    city = models.CharField(max_length=30)
    testname = models.CharField(max_length=30)
    price = models.IntegerField()
    state = models.CharField(max_length=30)
    pincode = models.IntegerField()
    cardname = models.CharField(max_length=30)
    cardnumber = models.IntegerField()
    exp_month = models.CharField(max_length=30)
    exp_year = models.IntegerField()
    cvv = models.IntegerField()
