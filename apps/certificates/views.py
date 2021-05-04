from django.shortcuts import render
from rest_framework import viewsets

from apps.certificates.models import Certificate
from apps.certificates.serializers import CertificateSerializer

# Create your views here.
class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer