from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'firstname', 'name': 'firstname', 'id': 'floatingInput',
               'type': 'text'}))

    last_name = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'lastname', 'name': 'lastname', 'id': 'floatingInput', 'type': 'text'}))

    username = forms.CharField(label="Username", widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'username', 'name': 'username', 'id': 'floatingInput', 'type': 'text'}))

    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'email', 'name': 'email', 'id': 'floatingInput', 'type': 'email'}))

    password1 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control','placeholder': 'password1', 'name': 'password1', 'id': 'floatingInput', 'type': 'password'}))

    password2 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control','placeholder': 'password2', 'name': 'password2', 'id': 'floatingInput', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': False})
