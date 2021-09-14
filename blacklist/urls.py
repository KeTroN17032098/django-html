from django.urls import path
from . import views

app_name='blacklist'

urlpatterns = [
    path('',views.list,name='list'),
    path('<int:pk>/',views.detail,name='detail'),
    path('add/',views.add,name='add'),
]
