
from rest_framework.permissions import BasePermission

class LessonTrainerOnly(BasePermission):

    def has_object_permission(self, request, view, obj):

        return request.user == obj.course.trainer

class LessonTrainerRUD(BasePermission):

    def has_object_permission(self, request, view, obj):

        return request.user == obj.module.course.trainer