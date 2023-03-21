from django.http import HttpResponse
from .models import Driver
from django.http import JsonResponse
from .serializers import DriverSerializer, DriverSerializer0
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status , filters , generics

@api_view(['GET', 'PUT', 'DELETE'])
def api_view_details(request, id):
    try:
        driver = Driver.objects.get(id=id)
    except Driver.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DriverSerializer(driver)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DriverSerializer(driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_driver(request):
    if request.method == 'POST':
        serializer = DriverSerializer0(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_view0(request):
    if request.method == 'GET':
        driver = Driver.objects.all().exclude(truck=1)
        serializer = DriverSerializer(driver, many=True)
        return JsonResponse({'drivers': serializer.data}, safe=False)
        # return Response(serializer.data)

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /',
        'GET /domain/driver',
        'POST /domain/driver/',
        'GET /domain/driver/id'
    ]
    return Response(routes)

class ListView(generics.ListAPIView):
    queryset = Driver.objects.all().exclude(truck=1)
    serializer_class = DriverSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'mobile_number', 'language', 'name', 'truck__number_plate'] 

# py manage.py runserver