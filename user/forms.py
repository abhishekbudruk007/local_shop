from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import CustomUsers
from django import forms
class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUsers
        fields ="__all__"

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Username', 'maxlength':'20','pattern':'[A-Za-z]+',
               'title':'Enter Chracters only','required':'true'}))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'autofocus':'autofocus', 'placeholder':'Email', 'class':'form-control',
                   'required': 'true'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'password', 'maxlength':'50', 'required':'true'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'confirm password', 'maxlength': '50', 'required': 'true'}))
    user_photo = forms.ImageField(required=False,widget=forms.ClearableFileInput(attrs={'class': 'form-control','accept':'image/*', 'placeholder':'Email'}))
    class Meta:
        model = CustomUsers
        fields = ('username', 'email', 'password1', 'password2', 'user_photo')

class ChangePassForm(PasswordChangeForm):
    # pass1 = forms.CharField(widget=forms.PasswordInput(
    #     attrs={'class': 'form-control', 'placeholder': 'old password', 'maxlength': '50', 'required': 'true'}))
    # pass2 = forms.CharField(widget=forms.PasswordInput(
    #     attrs={'class': 'form-control', 'placeholder': 'new password', 'maxlength': '50', 'required': 'true'}))
    # pass3 = forms.CharField(widget=forms.PasswordInput(
    #     attrs={'class': 'form-control', 'placeholder': 'confirm password', 'maxlength': '50', 'required': 'true'}))
    class Meta:
        model = CustomUsers
        fields = ('password1', 'password2', 'password3')