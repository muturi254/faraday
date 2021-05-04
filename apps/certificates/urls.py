from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.certificates.views import CertificateViewSet
# urlpatterns
router = DefaultRouter()
router.register(r"", CertificateViewSet)

urlpatterns = [
    path("", include(router.urls))
]