from app.repairman.models import Repairman
from django.db import models

# Create your models here.
class Review(models.Model):
    rmReviewID=models.AutoField(primary_key=True)
    repairmanID=models.ForeignKey(Repairman,on_delete=models.CASCADE)   #FK --rm
    #reviewby=models.IntegerField()   FK--cs
    rating=models.DecimalField()
    reviewDate=models.DateField()
    reviewText=models.TextField()

