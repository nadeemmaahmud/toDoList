from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import models

class CreateForm(forms.ModelForm):
    class Meta:
        model = models.Task
        exclude = ('user', 'status',)

        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'datetime-local'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = models.Task
        exclude = ('user',)

        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserLogin(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')