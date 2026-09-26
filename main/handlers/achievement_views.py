# Basic Libraries
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Achievement
from main.forms import AchievementForm 

# Achievements

def create_achievement(request):
   
    form = AchievementForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_main")

    return render(request, "achievement_form.html", {"form": form})

def update_achievement(request, achievement_id):
    achievement = get_object_or_404(Achievement,
        pk=achievement_id)

    form = AchievementForm(request.POST or None,
        instance=achievement)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_main")

    return render(request, "achievement_form.html", {"form": form})

def delete_achievement(request, achievement_id):
    achievement = get_object_or_404(Achievement,
        pk=achievement_id)

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