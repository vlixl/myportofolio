from django.urls import path

from main.views import show_main, show_art, show_education

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    # path("experience/", show_experience, name="show_experience"),
    path("art/", show_art, name="show_art"),
    path("education/", show_education, name="show_education"),
]