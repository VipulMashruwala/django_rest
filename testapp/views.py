from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
# from rest_framework.mixins import ListModelMixin, CreateModelMixin,RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
# from rest_framework.generics import GenericAPIView
# from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView,UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets

# Create your views here.
## ---------------------------- By Using Model Mixixn and Generic API View ------------------- ##
# class StudentListCreate(ListModelMixin,CreateModelMixin,GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class StudentRetriveUpdateDestroy(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin,GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         kwargs['partial'] = True
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

## ------------------------ API Views -------------------------- ##
# class EmployeeListCreateAPI(ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class EmployeeRetriveUpdateDelete(RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


## ------------------------- Viewsets ------------------------ ##
class EmployeeDataAPI(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
