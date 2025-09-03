

# Create your models here.
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    tamil = models.PositiveIntegerField()
    english = models.PositiveIntegerField()
    maths = models.PositiveIntegerField()
    science = models.PositiveIntegerField()
    social = models.PositiveIntegerField()
    grade = models.CharField(max_length=1, blank=True)

    def __str__(self):
        return f"{self.id} - {self.name}"

    def compute_grade(self) -> str:
        total = self.tamil + self.english + self.maths + self.science + self.social
        avg = total / 5
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        return "F"

    def save(self, *args, **kwargs):
        # compute grade automatically before saving
        self.grade = self.compute_grade()
        super().save(*args, **kwargs)
