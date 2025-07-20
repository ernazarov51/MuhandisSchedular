from django.db import models


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Science(models.Model):
    name = models.CharField(max_length=255)


class Room(models.Model):
    name = models.CharField(max_length=255)


class Lesson(models.Model):
    start = models.DateField()
    end = models.DateField()
    science = models.ForeignKey(Science, on_delete=models.CASCADE, related_name='lessons')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='lessons')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='lessons')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='lessons')
