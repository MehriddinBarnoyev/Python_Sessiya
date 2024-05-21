from django.shortcuts import render
from .models import *
from PIL import Image

# Create your views here.
def home(request):
    return render(
        request=request,
        template_name='../templates/home.html'
    )

def get_services(request):
    services = Services.objects.all()
    context = {
        'services': services,
    }

    return render(
        request=request,
        template_name='../templates/services.html',
        context = context
    )

def get_staffs(request):
    staffs = Staff.objects.all()
    context = {
        'staffs': staffs,
    }

    return render(
        request=request,
        template_name='../templates/staffs.html',
        context = context
    )