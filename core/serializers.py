from django.urls import path, include
from core.models import User
from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 
                  'username', 
                  'email', 
                  'is_staff', 
                  'is_superuser',
                  'first_name',
                  'last_name']
