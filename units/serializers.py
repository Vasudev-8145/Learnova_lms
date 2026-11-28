
from rest_framework import serializers

from units.models import Modules
from subject.models import Course
from chapters.models import Lessons
from chapters.serializers import LessonSerializer

from datetime import datetime

class ModuleSerializer(serializers.ModelSerializer):

    course = serializers.StringRelatedField(read_only=True)
    lessons = serializers.SerializerMethodField(read_only=True)
    lesson_count = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = Modules

        fields = "__all__"

        read_only_fields = ["id","course","created_at","updated_at","module_number"]

    def validate(self,validated_data):

        exam_date = validated_data.get("exam_date")

        if exam_date<datetime.today().date():

            raise serializers.ValidationError("Please enter a valid date")

        return validated_data

    def get_lessons(self,obj):

        lesson_object = Lessons.objects.filter(module=obj)

        serializer_instance = LessonSerializer(lesson_object,many=True)

        return serializer_instance.data

    def get_lesson_count(self,obj):

        return Lessons.objects.filter(module=obj).count()
