from rest_framework import serializers

from apps.certificates.models import Certificate
# derializers
class CertificateSerializer(serializers.ModelSerializer):
   
   class Meta:
        model = Certificate
        fields = ['id', 'name', 'description ', 'created_at', 'updated_at']