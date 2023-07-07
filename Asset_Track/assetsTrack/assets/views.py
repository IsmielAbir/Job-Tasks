from django.shortcuts import render

from rest_framework import viewsets
from assets.models import Company, Device, Employee, DeviceLog
from assets.serializers import CompanySerializer, DeviceSerializer, EmployeeSerializer, DeviceLogSerializer

# Create your views here.
def test(request):
    return render(request, 'index.html')



class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DeviceLogViewSet(viewsets.ModelViewSet):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer

