from django import forms
from .models import Profile, Course


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['people', 'age', 'average_mark']
        labels = {
            'people': 'Student',
            'age': 'Age',
            'average_mark': 'Average mark',
        }
        widgets = {
            'people': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'average_mark': forms.TextInput(attrs={'class': 'form-control'})
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'title', 'class_teacher', 'code']
        labels = {
            'name': 'Назва',
            'title': 'Опис',
            'class_teacher': 'Класний керівник',
            'code': 'Код доступу',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'class_teacher': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
        }

