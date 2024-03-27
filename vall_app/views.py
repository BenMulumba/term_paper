from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    return render(request, 'vall_app/templates/vall_app/main.html' )

def about (request):
    return render (request, 'vall_app/templates/vall_app/about.html')

def donate (request):
    return render (request, 'vall_app/templates/vall_app/donate.html')

def cause (request):
    return render (request, 'vall_app/templates/vall_app/cause.html')

# adding parameter for loggin and register
def register (request):
    if request.method =="POST":
        pass
    else:
        pass
    return render (request=request, template_name='vall_app/templates/vall_app/sign_up.html')

def login (request):
    return render (request, "vall_app/templates/vall_app/login.html")

