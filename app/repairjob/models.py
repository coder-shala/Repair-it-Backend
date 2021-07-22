from django.db import models

# Create your models here.
class Repairjob(models.Model):
    RJobID = models.CharField(max_length=50)
    CustomerID=models.IntegerField()
    ProductName=models.CharField(max_length=50)
    ProducDescription=models.CharField(max_length=50)
    CreatedDate=models.DateField()
    statusForCustomer=models.CharField