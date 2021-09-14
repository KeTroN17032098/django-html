from django.urls import path
from . import views

app_name='blacklist'

urlpatterns = [
    path('',views.list,name='list'),
]
