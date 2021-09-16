from django.shortcuts import render
from rest_framework.decorators import renderer_classes
from .models import *
from .serializers import *  
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import renderers
from .permissions import *
from rest_framework.response import Response
import datetime
# Create your views here.

class TransactionsTemplateHTMLRender(renderers.TemplateHTMLRenderer):
    def get_template_context(self, data, renderer_context):
        data = super().get_template_context(data, renderer_context)
        if not data:
            return {}
        else:
            return data

#Count의 목록/Detail 보기
class CountViewSet(viewsets.ModelViewSet):
     # authentication 추가
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrNotDelete]
    queryset = Count.objects.all()
    serializer_class=CountSerializer
   
        
    
    #serializer.save() 재정의
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class SectionViewSet(viewsets.ModelViewSet):
    # authentication 추가
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrNotDelete]
    queryset = Section.objects.all()
    serializer_class=SectionSerializer
    
    #serializer.save() 재정의
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
#Count의 목록/Detail 보기
class TodayCountViewSet(viewsets.ModelViewSet):
     # authentication 추가
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrNotDelete]
    queryset = Count.objects.filter(when=datetime.datetime.now().date())
    serializer_class=TodayCountSerializer
   
        
    
    #serializer.save() 재정의
    def perform_create(self, serializer):
        serializer.save(when=datetime.datetime.now().date())
        serializer.save(user=self.request.user)