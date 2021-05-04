from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from apps.users.models import User, UserProfile

# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'is_staff', 'is_admin']
    list_filter = ['is_admin']
    fieldsets  = [
        (None, {'fields': ('email', 'password')}),
        ('Permisiions', {'fields': ('is_admin', 'is_staff')})
    ]

    add_fieldsets = [
        (None, {
            'class': ('wide'),
            'fields': ('email', 'password1', 'password2')
        }),
    ]

    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = []


admin.site.register(User, UserAdmin)