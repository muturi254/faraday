from django.shortcuts import render
from rest_framework import viewsets

from apps.users.serializers import UserSerializer
from apps.users.models import User
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

