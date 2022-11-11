from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','emp_no','age','salary','city']

admin.site.register(Employee,EmployeeAdmin)

