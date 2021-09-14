from django.urls import path
from . import views

app_name='help'

urlpatterns = [
    path('',views.pdf,name='pdf'),
    path('pdf/',views.file,name='file'),
]
