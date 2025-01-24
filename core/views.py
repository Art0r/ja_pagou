from django.shortcuts import render

from core.models import User
from core.serializers import UserSerializer
from rest_framework import routers, serializers, viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
