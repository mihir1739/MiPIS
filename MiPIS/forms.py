from django import forms
from django.contrib.auth.forms import UserCreationForm
import random, string
from MiPIS.models import User,Data

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    firstname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    lastname =  forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('firstname','lastname','username', 'email', 'password1', 'password2', 'is_admin', 'is_staff', 'is_user')

class DataForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    class Meta:
        model = Data
        fields = ('name','picture','age')

class EditForm(forms.ModelForm):
    similiar = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    class Meta:
        model = Data
        fields = ('similiar','location')