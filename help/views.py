from django.shortcuts import render
from django.http import FileResponse, Http404
from django.contrib.staticfiles.storage import staticfiles_storage
import os

# Create your views here.
def pdf(request):
    return render(request, 'pdfviewer.html',{'link':'help:file'})

def file(request):
    try:
        return FileResponse(open(staticfiles_storage.path('documents/help.pdf'),'rb'),content_type='application/pdf')
    except FileNotFoundError:
        raise Http404('not found')
    