from django import forms
from .models import Profile


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

