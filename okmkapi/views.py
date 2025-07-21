from datetime import datetime, timedelta

from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, ListCreateAPIView

from okmkapi.models import Group, Science, Room, Teacher, Lesson
from okmkapi.serializers import GroupModelSerializer, ScienceModelSerializer, RoomModelSerializer, \
    TeacherModelSerializer, LessonModelSerializer, LessonSerializerDepthOne


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

@extend_schema(tags=['API'])
class LessonListAPIView(ListAPIView):
    serializer_class = LessonSerializerDepthOne
    queryset = Lesson.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        group_id = self.kwargs['group_id']

        today = datetime.today()
        start_of_week = today - timedelta(days=today.weekday())  # Dushanba
        start_of_week = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)

        end_of_week = start_of_week + timedelta(days=6, hours=23, minutes=59, seconds=59)

        return queryset.filter(
            group_id=group_id,
            start__range=(start_of_week, end_of_week)
        )

