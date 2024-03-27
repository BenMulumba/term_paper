from django.shortcuts import render,redirect
from .forms import user_registration_form
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login 

# Create your views here.

def register (request):
    if request.method == 'POST':
        form  = user_registration_form (request.POST)

        # validate the user information 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get ('username')
            # create a flash message 
            messages.success (request, f'Account created for, {username}. You can now Loggin')
            # redirect the user to the loggin page
            return redirect ('login')
    else:
        form = user_registration_form()
    return render (request, 'user/Templates/user/register.html', {'form':form})

# login form
def login_view (request):
    if request.method == 'POST':
        form =AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect ('home')
    else:
        form = AuthenticationForm()
    return render (request, 'user/Templates/user/login.html', {'form': form})
    



