from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "tamil", "english",
                    "maths", "science", "social", "grade")
    search_fields = ("name",)
