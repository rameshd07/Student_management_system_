from django.urls import path
from . import views

urlpatterns = [
    path("", views.students_list, name="students_list"),
    path("add/", views.student_create, name="student_create"),
    path("edit/<int:pk>/", views.student_update, name="student_update"),
    path("delete/<int:pk>/", views.student_delete, name="student_delete"),
]
