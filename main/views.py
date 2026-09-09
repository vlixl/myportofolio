from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Leow Vincent Vintizel",
        "brand": "VLIXL",
        "npm": "2506611856",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "CS Student @ UI, studying theoretical computer science. I’m someone who enjoys learning by making. "
            "Most of what I do starts with curiosity and turns into something creative."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Leow Vincent Vintizel",
        "brand": "VLIXL",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)
