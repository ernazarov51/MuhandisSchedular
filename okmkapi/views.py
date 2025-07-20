from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView

from okmkapi.models import Group, Science, Room, Teacher, Lesson
from okmkapi.serializers import GroupModelSerializer, ScienceModelSerializer, RoomModelSerializer, \
    TeacherModelSerializer, LessonModelSerializer


# Create your views here.
@extend_schema(tags=['API'])
class GroupListAPIView(ListCreateAPIView):
    serializer_class = GroupModelSerializer
    queryset = Group.objects.all()

@extend_schema(tags=['API'])
class ScienceListAPIView(ListCreateAPIView):
    serializer_class = ScienceModelSerializer
    queryset = Science.objects.all()

@extend_schema(tags=['API'])
class RoomListAPIView(ListCreateAPIView):
    serializer_class = RoomModelSerializer
    queryset = Room.objects.all()

@extend_schema(tags=['API'])
class TeacherCreateListAPIView(ListCreateAPIView):
    serializer_class = TeacherModelSerializer
    queryset = Teacher.objects.all()


@extend_schema(tags=['API'])
class LessonCreateAPIView(ListCreateAPIView):
    serializer_class = LessonModelSerializer
    queryset = Lesson.objects.all()
