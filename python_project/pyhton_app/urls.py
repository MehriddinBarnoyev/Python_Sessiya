from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('services/', get_services, name='services'),
    path('staffs/', get_staffs, name='staffs'),
]
