from .models import Employee
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','name','emp_no','age','salary','city']
        extra_kwargs = {
            'name' : {
                'required' : True
            },
            'emp_no' : {
                'required' : True
            },
            'age' : {
                'required' : True
            },
            'salary' : {
                'required' : True
            },
            'city' : {
                'required' : True
            }
        }