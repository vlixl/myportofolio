from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from main.models import Experience, Music, Education

GLOBAL_CONTEXT = {
    "name": "Leow Vincent Vintizel",
    "brand": "VLIXL",
}

def show_main(request):
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
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = GLOBAL_CONTEXT | {
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_music(request):
    context = GLOBAL_CONTEXT | {
        "music_list": Music.objects.all(),
    }
    return render(request, "music.html", context)

def show_education(request):
    context = GLOBAL_CONTEXT | {
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)
