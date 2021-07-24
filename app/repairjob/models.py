from django.db import models

# Create your models here.
class Repairjob(models.Model):
    RJobID = models.CharField(max_length=50)
    CustomerID= models.ForeignKey(Customer, on_delete=models.CASCADE)   #FK--cs
    ProductName=models.CharField(max_length=50)
    ProducDescription=models.TextField()
    CreatedDate=models.DateField()
  