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

def search(request):
    if request.method =='POST':
        Form=SearchForm(request.POST)
        context={}
        
        if Form.is_valid():
            print(Form.cleaned_data)
            tmp=PersonModel.objects.filter(Q(name__icontains=Form.cleaned_data['person_info'])|Q(kolasid__icontains=Form.cleaned_data['person_info'])).distinct()

            context['object_list']=tmp
            context['search_keyword']=Form.cleaned_data['person_info']
            context['keys']=PersonModel.objects.all()[0].key()
        
            
        return render(request, 'search.html',context)
    else:
        return HttpResponseRedirect(reverse('blacklist:list-watch'))