from django.contrib import admin
from assets.models import Company, Device, Employee, DeviceLog

# Register your models here.

admin.site.register(Company)
admin.site.register(Device)
admin.site.register(Employee)
admin.site.register(DeviceLog)
