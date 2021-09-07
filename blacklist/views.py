from django.shortcuts import render
from .models import *

# Create your views here.
def board(request):
    
    Persons=PersonModel.objects.all()

    return render(request,'board.html',{'persons':Persons,'keys':Persons[0].key()})