from django.urls import path

from main.views import ( 
    show_main, 
    show_art, 
    show_education, 
    create_project, 
    show_projects, 
    get_projects_json, 
    delete_project,
    create_achievement, 
    update_achievement,
    delete_achievement,
    get_achievements_json,
    )

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
]