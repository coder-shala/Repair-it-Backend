from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.
class Repairman(models.Model):
    repairmanID=models.AutoField(primary_key=True)  #pk
    repaiemanName=models.CharField(max_length=50)
    MobileNo=models.IntegerField()
    City=models.CharField(max_length=40)
    Address=models.TextField()
    Skills=models.JSONField()
    DateJoin=models.DateField()
class RepairmanSkill(models.Model):
    RepairManSkillID=models.AutoField(primary_key=True)
    SkillText=models.CharField(max_length=50)
