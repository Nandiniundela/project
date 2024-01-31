import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from app1.models import bus_details
from apis.v1.serializer import bus_Serializer
@csrf_exempt
def all_buses(request):
    if request.method == "GET":
        result = bus_details.objects.all()
        serializedResult = bus_Serializer(result,many=True)
        if serializedResult.is_valid:
            return JsonResponse(serializedResult.data,safe=False)
        return HttpResponse("some error occured")
    return HttpResponse("invalid request type")
@csrf_exempt    
def add_bus(request):
    if request.method == "POST":
        incoming_data=JSONParser().parse(request)
        Serializerdata=bus_Serializer(data=incoming_data)
        if Serializerdata.is_valid():
            Serializerdata.save()
            return JsonResponse(Serializerdata.data,status=201)
        return JsonResponse(Serializerdata.errors , status=400)
    return HttpResponse("invalid request method")
@csrf_exempt    
def edit_bus(request):
    if request.method == "PATCH":
        incoming_data=JSONParser().parse(request)
        pk=incoming_data.get("id")
        obj=bus_details.objects.get(id=pk)
        Serializerdata=bus_Serializer(obj,data=incoming_data,partial=True)
        if Serializerdata.is_valid():
            Serializerdata.save()
            return JsonResponse(Serializerdata.data,status=201)
        return JsonResponse(Serializerdata.errors , status=400)
    return HttpResponse("invalid request method")
@csrf_exempt    
def put_bus(request):
    if request.method == "PUT":
        incoming_data=JSONParser().parse(request)
        pk=incoming_data.get("id")
        obj=bus_details.objects.get(id=pk)
        Serializerdata=bus_Serializer(obj,data=incoming_data)
        if Serializerdata.is_valid():
            Serializerdata.save()
            return JsonResponse(Serializerdata.data,status=201)
        return JsonResponse(Serializerdata.errors , status=400)
    return HttpResponse("invalid request method")
@csrf_exempt    
def delete_bus(request):
    if request.method == "DELETE":
        incoming_data=JSONParser().parse(request)
        pk=incoming_data.get("id")
        obj=bus_details.objects.get(id=pk)
        obj.delete()
        return HttpResponse("deleted successfully")
@csrf_exempt       
def one_busdetail(request,num):
    if request.method == "GET":
        result = bus_details.objects.get(bus_number=num)
        serializedResult = bus_Serializer(result)
        if serializedResult.is_valid:
            return JsonResponse(serializedResult.data,safe=False)
        return HttpResponse("some error occured")
    return HttpResponse("invalid request type")    
        