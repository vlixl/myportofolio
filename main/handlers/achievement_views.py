# Basic Libraries
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from main.models import Achievement
from main.forms import AchievementForm 

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
 
    title_query = request.GET.get("title", "").strip()
    achievements = Achievement.objects.prefetch_related("starred_by").all()

    if title_query:
        achievements = achievements.filter(event__icontains=title_query)

    can_change = request.user.has_perm("main.change_achievement")
    can_delete = request.user.has_perm("main.delete_achievement")

    data = []
    for achievement in achievements:
        starred_users = list(achievement.starred_by.all())
        is_starred = (
            request.user.is_authenticated and request.user in starred_users
        )

        data.append({
            "pk": str(achievement.id),
            "fields": {
                "award": achievement.award,
                "award_label": achievement.award_label,
                "category": achievement.category,
                "month": achievement.month,
                "month_display": achievement.get_month_display(),
                "year": achievement.year,
                "event": achievement.event,
                "organization": achievement.organization,
                "description": achievement.description,
                "star_count": len(starred_users),
                "is_starred": is_starred,
                "starred_by_names": ", ".join(u.username for u in starred_users),
                "can_change": can_change,
                "can_delete": can_delete,
            },
        })

    return JsonResponse(data, safe=False)


@require_POST
def create_achievement_ajax(request):
    """Menambah achievement lewat AJAX. Respons: 201, 400, atau 403."""
    # Permission dicek di view, bukan hanya dengan menyembunyikan tombol.
    if not request.user.has_perm("main.add_achievement"):
        return JsonResponse(
            {"message": "Anda tidak memiliki izin untuk menambahkan achievement."},
            status=403,
        )

    form = AchievementForm(request.POST)
    if form.is_valid():
        achievement = form.save()
        return JsonResponse(
            {"message": "Achievement berhasil ditambahkan.", "pk": str(achievement.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@login_required
def toggle_achievement_star(request, achievement_id):
    achievement = get_object_or_404(Achievement, pk=achievement_id)

    if request.method == "POST":
        if request.user in achievement.starred_by.all():
            achievement.starred_by.remove(request.user)
        else:
            achievement.starred_by.add(request.user)

    return redirect("main:show_main")