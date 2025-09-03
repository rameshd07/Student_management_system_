# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Student
from .forms import StudentForm


def students_list(request):
    q = request.GET.get("q", "")
    if q:
        students = Student.objects.filter(Q(name__icontains=q))
    else:
        students = Student.objects.all().order_by("id")
    return render(request, "students/students_list.html", {"students": students, "q": q})


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("students_list")
    else:
        form = StudentForm()
    return render(request, "students/student_form.html", {"form": form, "title": "Add Student"})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("students_list")
    else:
        form = StudentForm(instance=student)
    return render(request, "students/student_form.html", {"form": form, "title": "Update Student"})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect("students_list")
    return render(request, "students/confirm_delete.html", {"student": student})
