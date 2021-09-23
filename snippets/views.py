from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics,permissions,renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer,UserSerializer
from snippets.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
# Create your views here.

@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        'users':reverse('user-list',request=request,format=format),
        'snippets':reverse('snippet-list',request=request,format=format)
    })


class SnippetList(generics.ListCreateAPIView):
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    
class UserList(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
class SnippetHighlight(generics.GenericAPIView):
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer
    renderer_classes=(renderers.StaticHTMLRenderer,)
    
    def get(self, request, *args, **kwargs):
        snippets=self.get_object()
        return Response(snippets.highlighted)