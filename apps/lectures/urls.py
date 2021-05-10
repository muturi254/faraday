from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.lectures.views import LectureViewSet
# urlpatterns
router = DefaultRouter()
router.register(r'', LectureViewSet)

urlpatterns = [
    path('', include(router.urls))
]