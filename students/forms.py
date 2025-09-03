from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "tamil", "english", "maths", "science", "social"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "tamil": forms.NumberInput(attrs={"class": "form-control", "min": 0, "max": 100}),
            "english": forms.NumberInput(attrs={"class": "form-control", "min": 0, "max": 100}),
            "maths": forms.NumberInput(attrs={"class": "form-control", "min": 0, "max": 100}),
            "science": forms.NumberInput(attrs={"class": "form-control", "min": 0, "max": 100}),
            "social": forms.NumberInput(attrs={"class": "form-control", "min": 0, "max": 100}),
        }

    def clean(self):
        cleaned = super().clean()
        for f in ["tamil", "english", "maths", "science", "social"]:
            val = cleaned.get(f)
            if val is not None and not (0 <= val <= 100):
                self.add_error(f, "Marks must be between 0 and 100.")
        return cleaned
