from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            messages.success(request, "")
            return redirect('home')  # Ensure 'home' exists in urls.py
        else:
            messages.error(request, "")
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect after successful login
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # Ensure 'login' exists in urls.py


@login_required
def home(request):
    return render(request, "users/home.html")


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page after update
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})


def home1(request):
    """Main home page accessible to all users"""
    return render(request, "users/home1.html")


from django.contrib import messages


@login_required
def delete_profile(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        logout(request)
        messages.success(request, "")
        return redirect("home")  # Redirect to homepage after deletion

    return redirect("profile")  # Redirect back to profile page if accessed via GET
