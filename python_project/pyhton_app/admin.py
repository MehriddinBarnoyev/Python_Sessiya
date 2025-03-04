from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'position', 'staff_image']

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'image']


