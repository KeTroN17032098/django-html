from django.urls import path,include
from snippets import views
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register(r'snippets',views.SnippetViewSet)
router.register(r'user',views.UserViewSet)
schema_view=get_schema_view(title='Pastebin API')

urlpatterns =[
    path('',include(router.urls)),
    path('schema/',schema_view),
]
