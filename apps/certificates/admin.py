from django.contrib import admin

from apps.certificates.models import Certificate
# Register your models here.

class CertficateAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_field = ['name']
    list_filter = ['name']



admin.site.register(Certificate, CertficateAdmin)