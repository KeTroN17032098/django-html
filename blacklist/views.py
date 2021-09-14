from django.shortcuts import render
from .models import *

# Create your views here.
def list(request):
    people =Person.objects.all()
    
    return render(request,'datatable.html',{'people':people,'keys':Person.keys(),'places':PLACE_NAME})

def detail(request,pk):
    return render(request,'datatable.html',{'detail':pk})

def add(request):
    return render(request,'pdfviewer.html',{'link':'help:file'})