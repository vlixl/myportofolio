from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

User = get_user_model()
editor, _ = Group.objects.get_or_create(name="Editor")


# EDITOR PERMISSIONS

view_achievement = Permission.objects.get(
    codename="view_achievement",
    content_type__app_label="main",
)

view_photo = Permission.objects.get(
    codename="view_photo",
    content_type__app_label="main",
)

view_music = Permission.objects.get(
    codename="view_music",
    content_type__app_label="main",
)

view_education = Permission.objects.get(
    codename="view_education",
    content_type__app_label="main",
)

view_project = Permission.objects.get(
    codename="view_project",
    content_type__app_label="main",
)

view_project = Permission.objects.get(
    codename="view_project",
    content_type__app_label="main",
)

change_achievement = Permission.objects.get(
    codename="change_achievement",
    content_type__app_label="main",
)

editor.permissions.add(
    view_achievement,
    view_photo,
    view_music,
    view_education,
    view_project,
)


# =====================
# USER SEEDING
# =====================

User.objects.all().delete()

# Normal Users
user1, _ = User.objects.get_or_create(
    username="user1"
)

user1.set_password("user1_password")
user1.save()

user2, _ = User.objects.get_or_create(
    username="user2"
)

user2.set_password("user_password")
user2.save()


# Editor User
editor_user, _ = User.objects.get_or_create(
    username="editor"
)

editor_user.set_password("editor_password")
editor_user.save()

editor_user.groups.add(editor)


# Superuser
superuser, _ = User.objects.get_or_create(
    username="superuser"
)

superuser.set_password("superuser_password")
superuser.is_staff = True
superuser.is_superuser = True
superuser.save()