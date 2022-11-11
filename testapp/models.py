from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    emp_no = models.IntegerField()
    age = models.IntegerField()
    salary = models.IntegerField()
    city = models.CharField(max_length=20) 
