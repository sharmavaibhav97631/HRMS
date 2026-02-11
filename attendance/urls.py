from django.urls import path
from .views import attendance_list, mark_attendance

urlpatterns = [
    path("", attendance_list, name="attendance_list"),
    path("mark/", mark_attendance, name="mark_attendance"),
]
