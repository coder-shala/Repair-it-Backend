from django.db import models

# Create your models here.
class Customer(models.Model):
    CustomerID=models.AutoField(primary_key=True)
    CustomerName=models.CharField(max_length=50)
    MobileNo=models.IntegerField()
    City=models.CharField(max_length=30)