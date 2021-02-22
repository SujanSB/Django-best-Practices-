from django.shortcuts import render,redirect
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.
def homepage(request):
    return render(request,'main/home.html',{"tutorials":Tutorial.objects.all })
    # return render (request,) 

def register(request):
    if request.method == "POST":
        form =UserCreationForm(request.POST)
        if form.is_valid():
            user =form.save()
            username =form.cleaned_data.get('username')
            messages.success(request,f"New Account Created:{username}")
            login(request,user)
            return redirect('/')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            # return redirect('/')
    form = UserCreationForm
    return render (request,'main/register.html',context={'form':form})

def logout_request(request):
    logout(request)
    return redirect('/')

def login_request(request):
    if request.method == "POST":
        form =AuthenticationForm(request,data =request.POST)
        if form.is_valid():
            username =form.cleaned_data.get('username')
            password =form.cleaned_data.get('password')
            user =authenticate(username =username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f'You are now logged in as {username}')
                return redirect("/")
            else:
                messages.error(request,"invalid username or password")
        else:
            messages.error(request,"invalid username or password")

    form =AuthenticationForm()
    # login(request)
    return render(request,'main/login.html',{"form": form})
