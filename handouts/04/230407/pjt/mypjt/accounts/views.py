from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
#
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_POST, require_POST, require_safe, require_http_methods
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Create your views here.

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("accounts:index")
    else:
        form = AuthenticationForm()
    context = {
        "form":form,
    }
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("articles:index")


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("accounts:index")
    
    else:
        form = CustomUserCreationForm()
    context = {
            "form": form,
            }
    return render(request, "accounts/signup.html", context)


@require_http_methods(["POST"])
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("articles:index")


def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("articles:index")
    else:
        form = CustomUserChangeForm()
    context = {
        "user":user,
    }
    return render(request, "accounts/update.html", context)

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("accounts:index")
    else:
        form = PasswordChangeForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/change_password.html", context)