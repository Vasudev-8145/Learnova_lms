
from rest_framework import serializers

from chapters.models import Lessons

class LessonSerializer(serializers.ModelSerializer):

    module = serializers.StringRelatedField(read_only=True)

    class Meta:

        model = Lessons

        fields = "__all__"

        read_only_fields = ["id","module","lesson_number","created_at","updated_at"]
        