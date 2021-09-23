from django.urls import path,include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view

schema_view=get_schema_view(title='Pastebin API')

urlpatterns =[
    path('',views.api_root),
    path('schema/',schema_view),
    path('snippets/',views.SnippetList.as_view(),name='snippet-list'),
    path('snippets/<int:pk>/',views.SnippetDetail.as_view(),name='snippet-detail'),
    path('snippets/<int:pk>/highlighted',views.SnippetHighlight.as_view(),name='snippet-highlighted'),
    path('user/',views.UserList.as_view(),name='user-list'),
    path('users/<int:pk>/',views.UserDetail.as_view(),name='user-detail'),
    path('api-auth/',include('rest_framework.urls')),
    
]
urlpatterns=format_suffix_patterns(urlpatterns)