
from django.shortcuts import render
from main.models import Photo, Education, Music

def show_art(request):
    context = {
        "music_list": Music.objects.all(),
        "photo_tracks":[
            Photo.objects.filter(track=number).order_by("position")
            for number in range(1, 4)
        ],
    }
    return render(request, "art.html", context)

def show_education(request):
    context = {
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)