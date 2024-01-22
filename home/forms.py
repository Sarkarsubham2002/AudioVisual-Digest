from django import forms

from .models import MediaFile




class MediaFileForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ['title', 'file']




############login#####
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

