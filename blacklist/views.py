from django.shortcuts import render
from .models import *

# Create your views here.
def board(request):
    
    Persons=PersonModel.objects.all()

    try:
        j=Persons[0].key()
    except:
        j=[]
    return render(request,'board.html',{'persons':Persons,'keys':j})

def search(request,text):
    if request.method =='post':
        tmp=PersonModel.objects.all().filter(name=text)
        tmp2=PersonModel.objects.all().filter(kolasid=text)