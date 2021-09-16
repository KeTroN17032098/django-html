from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('count',CountViewSet,'list')

router.register('section',SectionViewSet,'section')

router.register('today-count',TodayCountViewSet,'today-count')

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
