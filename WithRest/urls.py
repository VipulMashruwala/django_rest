from django.contrib import admin
from django.urls import path, include
from testapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('emp',views.EmployeeDataAPI, basename='employee')
### It automatically finds the corrects urls for base & id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
