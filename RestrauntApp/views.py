from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from RestrauntApp.models import Restraunts,Employees, Menu
from RestrauntApp.serializers import RestrauntSerializer,EmployeeSerializer, MenuSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def menuApi(request,id=0):
    if request.method=='GET':
        menu = Menu.objects.all()
        menu_serializer=MenuSerializer(menu,many=True)
        return JsonResponse(menu_serializer.data,safe=False)
    elif request.method=='POST':
        menu_data=JSONParser().parse(request)
        menu_serializer=MenuSerializer(data=menu_data)
        if menu_serializer.is_valid():
            menu_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        menu_data=JSONParser().parse(request)
        menu=Menu.objects.get(MenuId=menu_data['MenuId'])
        menu_serializer=MenuSerializer(menu,data=menu)
        if menu_serializer.is_valid():
            menu_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        menu=Menu.objects.get(MenuId=id)
        menu.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def restrauntApi(request,id=0):
    if request.method=='GET':
        restraunts = Restraunts.objects.all()
        restraunts_serializer=RestrauntSerializer(restraunts,many=True)
        return JsonResponse(restraunts_serializer.data,safe=False)
    elif request.method=='POST':
        restraunt_data=JSONParser().parse(request)
        restraunts_serializer=RestrauntSerializer(data=restraunt_data)
        if restraunts_serializer.is_valid():
            restraunts_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        restraunt_data=JSONParser().parse(request)
        restraunt=Restraunts.objects.get(RestrauntsId=restraunt_data['RestrauntId'])
        restraunts_serializer=RestrauntSerializer(restraunt,data=restraunt_data)
        if restraunts_serializer.is_valid():
            restraunts_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        restraunt=Restraunts.objects.get(RestrauntId=id)
        restraunt.delete()
        return JsonResponse("Deleted Successfully",safe=False)

