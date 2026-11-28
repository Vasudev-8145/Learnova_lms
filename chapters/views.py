from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import serializers
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView

from chapters.serializers import LessonSerializer
from chapters.permissions import LessonTrainerOnly,LessonTrainerRUD
from chapters.models import Lessons

from units.models import Modules

class LessonCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [LessonTrainerOnly]

    def post(self,request,pk=None):

        module_object = Modules.objects.filter(id=pk).first()

        form_data = request.data

        # validation start

        if module_object is None:

            raise serializers.ValidationError("No such module exists")

        # validation ends

        self.check_object_permissions(request,module_object)

        serializer_instance = LessonSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(module=module_object)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

class LessonRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [LessonTrainerRUD]

    serializer_class = LessonSerializer
    queryset = Lessons.objects.all()
