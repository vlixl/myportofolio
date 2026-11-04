from django.contrib.auth.models import Group, Permission, User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from main.models import Achievement


class AchievementAPITest(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_superuser("owner", "owner@example.com", "pw")
        self.editor = User.objects.create_user("editor", password="pw")
        self.visitor = User.objects.create_user("visitor", password="pw")
        editor_group = Group.objects.create(name="Editor")
        editor_group.permissions.add(Permission.objects.get(codename="change_achievement"))
        self.editor.groups.add(editor_group)
        self.achievement = Achievement.objects.create(
            award="1", award_label="Juara", category="Programming",
            month=8, year=2026, description="Achievement description",
        )
        self.list_url = reverse("api:achievement-list")
        self.detail_url = reverse("api:achievement-detail", args=[self.achievement.id])
        self.star_url = reverse("api:achievement-star", args=[self.achievement.id])
        self.payload = {
            "award": "2", "award_label": "Juara", "category": "Math",
            "month": 9, "year": 2026, "description": "Another achievement",
        }

    def test_public_read_and_editor_permissions(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("month_display", response.data[0])
        self.client.force_authenticate(user=self.editor)
        self.assertEqual(self.client.patch(self.detail_url, {"event": "Updated"}, format="json").status_code, 200)
        self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
        self.assertEqual(self.client.delete(self.detail_url).status_code, 403)

    def test_owner_create_delete_and_guest_protection(self):
        self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
        self.client.force_authenticate(user=self.owner)
        created = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(created.status_code, status.HTTP_201_CREATED)
        url = reverse("api:achievement-detail", args=[created.data["id"]])
        self.assertEqual(self.client.delete(url).status_code, status.HTTP_204_NO_CONTENT)

    def test_star_toggles_for_regular_user(self):
        self.client.force_authenticate(user=self.visitor)
        self.assertTrue(self.client.post(self.star_url).data["is_starred"])
        self.assertFalse(self.client.post(self.star_url).data["is_starred"])
