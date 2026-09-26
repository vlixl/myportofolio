from django.urls import path

from main.views import *

app_name = "main"

urlpatterns = [
    path("", show_main, 
        name="show_main"),
         
    path("art/", show_art, 
        name="show_art"),

    path("education/", show_education, 
        name="show_education"),

    path("projects/add/", create_project, 
        name="create_project"),

    path("projects/", show_projects, 
        name="show_projects"),

    path("api/projects/", get_projects_json, 
        name="get_projects_json"),

    path("projects/<uuid:project_id>/delete/",delete_project,
        name="delete_project"),

    path("achievements/add/", create_achievement,
        name="create_achievement"),

    path("achievements/<uuid:achievement_id>/edit/", update_achievement,
        name="update_achievement"),

    path("achievements/<uuid:achievement_id>/delete/", delete_achievement,
        name="delete_achievement"),

    path("api/achievements/", get_achievements_json,
        name="get_achievements_json"),

    path("register/", register, 
        name="register"),

    path("login/", login_user, 
        name="login"),

    path("logout/", logout_user, 
        name="logout"),

    path("projects/<uuid:project_id>/star/", toggle_project_star,
        name="toggle_project_star"),

    path("achievements/<uuid:achievement_id>/star/", toggle_achievement_star,
        name="toggle_achievement_star"),
]