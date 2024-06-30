from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  # to display a message on login and logout
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request,"You have been sucessfully logged in !")
            return redirect('home')  
        else:
            messages.error(request, "Invalid username or password.")
    
    # Handle GET request (initial load of the login page or error in POST);
    return render(request, 'authentication/login.html', {})


def SignUp(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the form to create a new user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  # Use password1 to get the password
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')
        else:
            # If form is not valid, display errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserCreationForm()

    return render(request, 'authentication/signup.html', {'form': form})



def home(request):
    return render(request, 'authentication/home.html')

def landingpage(request):
    return render(request, 'authentication/landingpage.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully logged out!")
    return redirect('landingpage')
