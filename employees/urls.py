from django.urls import path
from .views import employee_list, employee_create, employee_delete

urlpatterns = [
    path("", employee_list, name="employee_list"),
    path("add/", employee_create, name="employee_create"),
    path("delete/<int:pk>/", employee_delete, name="employee_delete"),
]
