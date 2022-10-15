from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Restraunts(models.Model):
    RestrauntId = models.AutoField(primary_key=True)
    RestrauntName = models.CharField(max_length=500)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Vote = models.IntegerField(blank=True, null=True)

class Menu(models.Model):
    MenuId = models.ForeignKey('Restraunts', on_delete=models.PROTECT, null=True)
    Dish1 = models.CharField(max_length=500)
    Dish2 = models.CharField(max_length=500)
    Drink = models.CharField(max_length=500)

