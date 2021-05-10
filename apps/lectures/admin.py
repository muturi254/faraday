from django.contrib import admin

from apps.lectures.models import Lecture

# Register your models here.
class LectureAdmin(admin.ModelAdmin):
    list_display = ['title', 'lecturer_name', 'date', 'is_required']
    search_fields = ['title', 'lecturer_name']

admin.site.register(Lecture, LectureAdmin)