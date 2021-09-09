from django.urls import path
from . import views

app_name='blacklist'

urlpatterns = [
	path('', views.board, name='list-watch'),
	path('detail/<int:no>/',views.detail,name='list-detail'),
	path('detail/<int:no>/upload',views.upload,name='list-detail-upload')
]