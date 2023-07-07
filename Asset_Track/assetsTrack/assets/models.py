from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# for company

class Company(models.Model):
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name
    
    
# for Employee

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# for device

class Device(models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    
    
# for device log

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    checkout_condition = models.CharField(max_length=100)
    return_condition = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.device} - {self.employee}"

