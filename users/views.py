from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.db.models import Q
from .forms import UserRegistrationForm, TeamForm
from .models import Team


def home(request):
    teams = Team.objects.all()

    context = {"teams": teams}
    return render(request, "home.html", context)


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(
                request, f"Your account has been created. You can log in now!"
            )
            return redirect("login")
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "register.html", context)


def create_team(request):
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            team_name = form.cleaned_data["name"]

            if Team.objects.filter(Q(name__iexact=team_name)).exists():
                form.add_error("name", "A team with this name already exists.")
            else:
                form.save()
                return redirect("home")
    else:
        form = TeamForm()
    return render(request, "home.html", {"form": form})


def show_teams(request):
    teams = Team.objects.all()

    context = {"teams": teams}
    return render(request, home.html, context)
