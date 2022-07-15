from django.shortcuts import render, get_object_or_404
from . models import Service, Category

# Create your views here.

    

def Service_details(request, slug):
    services = get_object_or_404(Service, slug=slug)
    return render(request, 'service.html', {'services':services})
