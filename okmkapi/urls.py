from django.urls import path

from okmkapi import views
from okmkapi.views import GroupListAPIView, ScienceListAPIView

urlpatterns = [
    path('groups', GroupListAPIView.as_view(), name='groups'),
    path('sciences', ScienceListAPIView.as_view(), name='sciences'),
    path('rooms', views.RoomListAPIView.as_view(), name='rooms'),
    path('teachers', views.TeacherCreateListAPIView.as_view(), name='teachers'),
    path('lesson',  views.LessonCreateAPIView.as_view(), name='lessons'),
]
