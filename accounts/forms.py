# coding=utf-8

from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class UserAdminCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'ra']


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'ra', 'is_active', 'is_staff', 'is_superuser']
