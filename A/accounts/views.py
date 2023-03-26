from django.shortcuts import (
    render,
    redirect
)
from .forms import (
    UserRegisterForm,
    UserLoginForm,
)
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from django.contrib import messages


# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username=cd["username"], password=cd["password"], email=cd["email"])
            messages.success(request, "create user successfully", 'success')
            return redirect("all_todo")

    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd["username"], password=cd["password"])
            if user is not None:
                login(request, user)
                messages.success(request, "user login successfully", 'success')
                return redirect("all_todo")
            else:
                messages.error(request, "user Not found", "danger")

    else:
        form = UserLoginForm()
    return render(request, 'login.html', {"form": form})


def logout_user(request):
    logout(request)
    messages.success(request, "logout user successfully", 'success')
    return redirect('all_todo')
