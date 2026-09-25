
from django.conf import settings
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

# Register and Sign Up Form
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render

# Bookkeeping
import datetime

# Authorization
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from main.models import (
    Music, 
    Education, 
    Achievement, 
    Photo, 
    Project 
    )

# Form Libraries
from main.forms import (
    ProjectForm, 
    AchievementForm 
    )


def is_gate_password_correct(request):
    """Checks the confirmation password submitted alongside an
    add/edit/delete action against the configured gate password."""
    return request.POST.get("gate_password", "") == settings.GATE_PASSWORD


GLOBAL_CONTEXT = {
    "name": "Leow Vincent Vintizel",
    "brand": "VLIXL",
}

def show_main(request):
    json_response = get_achievements_json(request)

    achievements = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    achievements = [
        achievement.object
        for achievement in achievements
    ]

    last_login = request.COOKIES.get(
        'last_login', 
        'Belum ada sesi login / Cookie tidak ditemukan'
        )

    context = GLOBAL_CONTEXT | {
        "first_name": "Leow",
        "middle_name": "Vincent",
        "last_name": "Vintizel",
        "npm": "2506611856",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "CS Student @ UI, studying theoretical computer science. I’m someone who enjoys learning by making. "
            "Most of what I do starts with curiosity and turns into something creative."
        ),
        "achievement_list": achievements,
        "wrong_password_achievement": request.GET.get("wrong_password_achievement", ""),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

def show_art(request):
    context = GLOBAL_CONTEXT | {
        "music_list": Music.objects.all(),
        "photo_tracks":[
            Photo.objects.filter(track=number).order_by("position")
            for number in range(1, 4)
        ],
    }
    return render(request, "art.html", context)

def show_education(request):
    context = GLOBAL_CONTEXT | {
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)

# PROJECTS
@login_required(login_url="/login/")
def create_project(request):

    if not request.user.is_superuser:
        raise PermissionDenied

    form = ProjectForm(request.POST or None)
    password_error = None

    if request.method == "POST" and form.is_valid():
        if is_gate_password_correct(request):
            form.save()
            messages.success(request, "Proyek baru berhasil ditambahkan!")
            return redirect("main:show_projects")
        password_error = "Password salah. Silakan coba lagi."

    context = GLOBAL_CONTEXT | {
        "form": form,
        "password_error": password_error,
    }
    return render(request, "projects_form.html", context)

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = GLOBAL_CONTEXT | {
        "project_list": projects,
        "title_query": title_query,
        "wrong_password_project": request.GET.get("wrong_password_project", ""),
    }
    return render(request, "project.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize(
        "json", projects, use_natural_foreign_keys=True
    )
    return HttpResponse(projects_json, content_type="application/json")

@login_required(login_url="/login/")
def delete_project(request, project_id):

    if not request.user.is_superuser:
        raise PermissionDenied
    
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if is_gate_password_correct(request):
            project.delete()
            messages.success(request, "Project berhasil dihapus!")
            return redirect("main:show_projects")

        messages.error(request, "Password salah. Project tidak dihapus.")
        return redirect(f"{reverse('main:show_projects')}?wrong_password_project={project_id}")

    return redirect("main:show_projects")

# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

# Achievements

def create_achievement(request):

    form = AchievementForm(request.POST or None)
    password_error = None

    if request.method == "POST" and form.is_valid():
        if is_gate_password_correct(request):
            form.save()
            return redirect("main:show_main")
        password_error = "Password salah. Silakan coba lagi."

    context = GLOBAL_CONTEXT | {
        "form": form,
        "password_error": password_error,
    }

    return render(request, "achievement_form.html", context)

def update_achievement(request, achievement_id):
    achievement = get_object_or_404(
        Achievement,
        pk=achievement_id
    )

    form = AchievementForm(
        request.POST or None,
        instance=achievement
    )
    password_error = None

    if request.method == "POST" and form.is_valid():
        if is_gate_password_correct(request):
            form.save()
            return redirect("main:show_main")
        password_error = "Password salah. Silakan coba lagi."

    context = GLOBAL_CONTEXT | {
        "form": form,
        "password_error": password_error,
    }

    return render(
        request,
        "achievement_form.html",
        context
    )

def delete_achievement(request, achievement_id):
    achievement = get_object_or_404(
        Achievement,
        pk=achievement_id
    )

    if request.method == "POST":
        if is_gate_password_correct(request):
            achievement.delete()
            return redirect("main:show_main")

        messages.error(request, "Password salah. Achievement tidak dihapus.")
        return redirect(f"{reverse('main:show_main')}?wrong_password_achievement={achievement_id}#achievements")

    return redirect("main:show_main")

def get_achievements_json(request):
    achievements = Achievement.objects.all()

    achievements_json = serializers.serialize(
        "json", achievements)

    return HttpResponse(
        achievements_json,
        content_type="application/json"
    )

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = GLOBAL_CONTEXT | {
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = GLOBAL_CONTEXT | {
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response