from django.urls import path

from okmkapi import views
from okmkapi.views import GroupListAPIView, ScienceListAPIView, GroupUpdateDestroyAPIView, SciencesUpdateDestroyAPIView, \
    RoomUpdateDestroyAPIView, TeacherUpdateDestroyAPIView, LessonUpdateDestroyAPIView, LessonAllListAPIView

urlpatterns = [
    path('groups/<admin_id>', GroupListAPIView.as_view(), name='groups'),
    path('sciences/<admin_id>', ScienceListAPIView.as_view(), name='sciences'),
    path('rooms/<admin_id>', views.RoomListAPIView.as_view(), name='rooms'),
    path('teachers/<admin_id>', views.TeacherCreateListAPIView.as_view(), name='teachers'),
    path('lesson/<admin_id>',  views.LessonCreateAPIView.as_view(), name='lessons'),
    path('lesson-depth-one/<int:group_id>',  views.LessonListAPIView.as_view(), name='lessons'),
    path('<admin_id>/groups-update-delete/<pk>',GroupUpdateDestroyAPIView.as_view()),
    path('<admin_id>/sciences-update-delete/<pk>',SciencesUpdateDestroyAPIView.as_view()),
    path('<admin_id>/rooms-update-delete/<pk>',RoomUpdateDestroyAPIView.as_view()),
    path('<admin_id>/teachers-update-delete/<pk>',TeacherUpdateDestroyAPIView.as_view()),
    path('<admin_id>/lessons-update-delete/<pk>',LessonUpdateDestroyAPIView.as_view()),
    path('lessons/<admin_id>',LessonAllListAPIView.as_view())
]
