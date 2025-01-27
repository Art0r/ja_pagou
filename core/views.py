from django.shortcuts import render

from core.models import User, Payment
from core.serializers import PaymentSerializer, UserSerializer
from rest_framework import routers, serializers, viewsets


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
