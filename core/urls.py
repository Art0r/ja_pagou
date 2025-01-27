from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core.views import PaymentViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'payments', PaymentViewSet)


urlpatterns = [
    path('', include(router.urls))
]
