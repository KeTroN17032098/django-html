from django.shortcuts import render
from .serializer import UserSerializer
from .models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
# 회원가입
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[AllowAny]