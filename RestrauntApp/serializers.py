from rest_framework import serializers
from RestrauntApp.models import Restraunts,Employees

class RestrauntSerializer(serializers.ModelSerializer):
    class Meta:
        model=Restraunts
        fields=('RestrauntId','RestrauntName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('EmployeeId','EmployeeName','Vote')

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('MenuId','Dish1','Dish2', 'Drink')