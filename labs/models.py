from django.db import models

# Create your models here.
class Labs(models.Model):
    testID = models.IntegerField(primary_key=True)
    testname = models.CharField(max_length=50)
    testprice = models.IntegerField()
