
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

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

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = GLOBAL_CONTEXT | {
        "form": form,
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
    }
    return render(request, "project.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

# Achievements

def verify_achievement_request(request, type, achievement_id):

    # Future Verification System Setup


    
    match type:
        case 'create_achievement':
            return create_achievement_verified(request)
        case 'update_achievement':
            return update_achievement_verified(request, achievement_id)
        case 'delete_achievement':
            return delete_achievement_verified(request, achievement_id)

def create_achievement(request):
    return verify_achievement_request(
        request, 'create_achievement', 0)

def update_achievement(request, achievement_id):
    return verify_achievement_request(
        request, 'update_achievement', achievement_id)

def delete_achievement(request, achievement_id):
    return verify_achievement_request(
        request, 'delete_achievement', achievement_id)

def create_achievement_verified(request):
   
    form = AchievementForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_main")

    context = GLOBAL_CONTEXT | {
        "form": form,
    }

    return render(request, "achievement_form.html", context)

def update_achievement_verified(request, achievement_id):
    achievement = get_object_or_404(
        Achievement,
        pk=achievement_id
    )

    form = AchievementForm(
        request.POST or None,
        instance=achievement
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_main")

    context = GLOBAL_CONTEXT | {
        "form": form,
    }

    return render(
        request,
        "achievement_form.html",
        context
    )

def delete_achievement_verified(request, achievement_id):
    achievement = get_object_or_404(
        Achievement,
        pk=achievement_id
    )

    if request.method == "POST":
        achievement.delete()
        return redirect("main:show_main")

    return redirect("main:show_main")

def get_achievements_json(request):
    achievements = Achievement.objects.all()

    achievements_json = serializers.serialize(
        "json", achievements)

    return HttpResponse(
        achievements_json,
        content_type="application/json"
    )