from rest_framework.serializers import ModelSerializer

from okmkapi.models import Group, Science, Room, Teacher, Lesson


class GroupModelSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']
        extra_kwargs = {
            'id': {'read_only': True}
        }


class ScienceModelSerializer(ModelSerializer):
    class Meta:
        model = Science
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }


class RoomModelSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class TeacherModelSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class LessonModelSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


from rest_framework.serializers import ModelSerializer

class LessonSerializerDepthOne(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'start', 'end', 'science', 'room', 'teacher', 'group']
        depth = 1


