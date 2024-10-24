from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserLoginForm


def register_view(request):
    if request.method == "POST":
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return redirect("jobs:index")
    else:
        register_form = UserRegisterForm()

    return render(request, "auth/register.html", {"register_form": register_form})


def login_view(request):
    if request.method == "POST":
        login_form = UserLoginForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            next_url = request.GET.get("next", "jobs:index")
            return redirect(next_url)
    else:
        login_form = UserLoginForm()

    return render(request, "auth/login.html", {"login_form": login_form})


@login_required
def logout_view(request):
    logout(request)
    return redirect("jobs:index")
