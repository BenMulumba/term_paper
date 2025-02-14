# import library for for form creation 
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# create the user registration form 
class user_registration_form (UserCreationForm):
    email = forms.EmailField()

    # configuiration of the userform 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

