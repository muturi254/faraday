from django.shortcuts import render
from rest_framework import viewsets

from apps.lectures.models import Lecture
from apps.lectures.serializers import LectureSerializer
# Create your views here.
class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer