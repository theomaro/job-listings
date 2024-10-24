from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control rounded-1"}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control rounded-1"}),
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]

        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control rounded-1", "autofocus": ""}
            ),
            "last_name": forms.TextInput(attrs={"class": "form-control rounded-1"}),
            "email": forms.EmailInput(attrs={"class": "form-control rounded-1"}),
            "username": forms.TextInput(attrs={"class": "form-control rounded-1"}),
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control rounded-1", "autofocus": ""}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control rounded-1"})
    )  #
