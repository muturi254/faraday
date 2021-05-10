from django.contrib import admin

from apps.waitlist.models import WaitListEntry

# Register your models here.
class WaitlistEntryAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'updated_at']
    search_fields = ['first_name', 'last_name']


admin.site.register(WaitListEntry, WaitlistEntryAdmin)