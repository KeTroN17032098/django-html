from django.urls import path
from . import views

app_name='blacklist'

urlpatterns = [
	path('', views.board, name='list-watch'),
	path('search/',views.search,name='list-search'),
]