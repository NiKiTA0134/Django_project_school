from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):

    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': "Прізвище, ім'я, по батькові"}))

    email = forms.EmailField(widget=forms.EmailInput)

    POSITION_CHOICES = [
        ('Учень', 'Учень'),
        ('Вчитель', 'Вчитель'),
    ]
    position = forms.ChoiceField(choices=POSITION_CHOICES)

    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Номер телефону *+380..*'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'position', 'phone_number']
