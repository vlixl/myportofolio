from django.shortcuts import render
from main.forms import AchievementForm

def show_main(request):
    last_login = request.COOKIES.get(
        'last_login', 
        'Belum ada sesi login / Cookie tidak ditemukan'
        )

    context = {
        "first_name": "Leow",
        "middle_name": "Vincent",
        "last_name": "Vintizel",
        "npm": "2506611856",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "CS Student @ UI, studying theoretical computer science. I’m someone who enjoys learning by making. "
            "Most of what I do starts with curiosity and turns into something creative."
        ),
        "title_query": request.GET.get("title", "").strip(),
        "achievement_form": AchievementForm(),
        "wrong_password_achievement": request.GET.get("wrong_password_achievement", ""),
        "last_login": last_login,
    }
    return render(request, "index.html", context)
