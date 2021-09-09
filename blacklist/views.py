from django.shortcuts import render
from .models import *
from .forms import *
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.
def board(request):
    
    Persons=PersonModel.objects.all()

    try:
        j=Persons[0].key()
    except:
        j=[]
    return render(request,'board.html',{'persons':Persons,'keys':j})

def detail(request,no):
    Target=PersonModel.objects.filter(no=no)[0]
    filetype=Target.file.name.split('.')[-1]
    
    return render(request,'detail.html',{'person':Target,'filetype':filetype})

def upload(request,no):
    if request.method == 'POST':
        form=UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect('/blacklist/detail/'+no)