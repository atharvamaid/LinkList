from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Register(UserCreationForm):
    email = forms.EmailField(label='email', widget=forms.TextInput(attrs={'placeholder':'Enter email'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.fields.TextInput(attrs={'placeholder': 'Enter Username'}),
            'email': forms.fields.TextInput(attrs={'placeholder': 'Enter email'}),
            'password1' : forms.fields.TextInput(attrs={'placeholder': 'Enter password'}),
            'password2' : forms.fields.TextInput(attrs={'placeholder': 'Re-enter password'}),
        }