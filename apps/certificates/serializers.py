from rest_framework import serializers

from apps.certificates.models import Certificate
# derializers
class CertificateSerializer(serializer.ModelSerializer):
   
   class Meta:
        model = Certificate
        fields = ['id', 'name']