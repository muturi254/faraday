from rest_framework import serializers

from apps.lectures.models import Lecture
# serializers
class LectureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecture
        fields = ['id', 'title', 'lecturer_name', 'date', 'duration', 'slides_url', 'is_required']