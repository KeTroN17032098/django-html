from django.shortcuts import render

# Create your views here.
def pdf(request):
    return render(request,'help.html',{})