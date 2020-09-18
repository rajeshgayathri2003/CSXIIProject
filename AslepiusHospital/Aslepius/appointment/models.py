from django.db import models
from dept import models as deptmodels
from django.contrib.auth.models import User



class Availability(models.Model):
    sno = models.IntegerField(primary_key = True)
    doctorID = models.ForeignKey(deptmodels.Departments, on_delete = models.CASCADE, )
    timeslot1 = models.CharField(max_length = 15)
    timeslot2 = models.CharField(max_length = 15)
    timeslot3 = models.CharField(max_length = 15)
    timeslot4 = models.CharField(max_length = 15)
    timeslot5 = models.CharField(max_length = 15)
    dayunavailable1 = models.CharField(max_length = 10)
    dayunavailable2 = models.CharField(max_length = 10)

class Appointment(models.Model):
    aptid = models.AutoField(primary_key = True,)
    doctorID = models.ForeignKey(deptmodels.Departments, on_delete = models.CASCADE, )
    patientID = models.ForeignKey(User, on_delete = models.CASCADE, )
    time = models.CharField(max_length = 15)
    date = models.DateField()
    status = models.BooleanField(default = 0)



# Create your models here.
