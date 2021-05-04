from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.users import views

# urlaptterns 
router = DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]