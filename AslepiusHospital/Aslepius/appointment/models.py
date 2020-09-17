from django.db import models
from dept import models as deptmodels
from django.contrib.auth.models import User



class Availability(models.Model):
    sno = models.IntegerField(primary_key = True)
    doctorID = models.ForeignKey(deptmodels.Departments, on_delete = models.CASCADE, )
    timeslot1 = models.TimeField(null = False)
    timeslot2 = models.TimeField(null = False)
    timeslot3 = models.TimeField(null = False)
    timeslot4 = models.TimeField(null = False)
    timeslot5 = models.TimeField(null = False)
    dayunavailable1 = models.CharField(max_length = 10)
    dayunavailable2 = models.CharField(max_length = 10)

class Appointment(models.Model):
    aptid = models.AutoField(primary_key = True,)
    doctorID = models.ForeignKey(deptmodels.Departments, on_delete = models.CASCADE, )
    patientID = models.ForeignKey(User, on_delete = models.CASCADE, )
    time = models.CharField(max_length = 15)
    date = models.DateField()



# Create your models here.
