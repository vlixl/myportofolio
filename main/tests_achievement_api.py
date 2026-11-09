from django.contrib.auth.models import Group, Permission, User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
import uuid

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


    def test_anonymous_user_can_read_and_search(self):
        self.achievement.event = "Mathematics Olympiad"
        self.achievement.save()

        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["award"], "1")
        self.assertFalse(response.data["is_starred"])

        response = self.client.get(self.list_url, {"title": "olympiad"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(self.list_url, {"title": "nonexistent"})
        self.assertEqual(response.data, [])


    def test_guest_and_regular_user_cannot_modify_database(self):
        for user in (None, self.visitor):
            with self.subTest(user=user):
                self.client.force_authenticate(user=user)

                response = self.client.post(
                    self.list_url, self.payload, format="json"
                )
                self.assertEqual(response.status_code, 403)

                response = self.client.patch(
                    self.detail_url,
                    {"description": "Unauthorized change"},
                    format="json",
                )
                self.assertEqual(response.status_code, 403)

                response = self.client.delete(self.detail_url)
                self.assertEqual(response.status_code, 403)

                self.assertEqual(Achievement.objects.count(), 1)
                self.achievement.refresh_from_db()
                self.assertEqual(
                    self.achievement.description,
                    "Achievement description",
                )


    def test_editor_can_patch_without_changing_other_fields(self):
        self.client.force_authenticate(user=self.editor)

        response = self.client.patch(
            self.detail_url,
            {"event": "Updated event"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.achievement.refresh_from_db()
        self.assertEqual(self.achievement.event, "Updated event")
        self.assertEqual(self.achievement.category, "Programming")
        self.assertEqual(
            self.achievement.description, "Achievement description"
        )


    def test_editor_cannot_create_or_delete(self):
        self.client.force_authenticate(user=self.editor)

        response = self.client.post(
            self.list_url, self.payload, format="json"
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Achievement.objects.count(), 1)

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 403)
        self.assertTrue(
            Achievement.objects.filter(pk=self.achievement.pk).exists()
        )


    def test_invalid_input_is_rejected_without_saving(self):
        self.client.force_authenticate(user=self.owner)

        invalid_cases = [
            ({"award": "   "}, "award"),
            ({"category": "<script></script>"}, "category"),
            ({"description": "<b></b>"}, "description"),
            ({"month": 13}, "month"),
        ]

        for changes, field in invalid_cases:
            with self.subTest(field=field):
                response = self.client.post(
                    self.list_url,
                    {**self.payload, **changes},
                    format="json",
                )

                self.assertEqual(
                    response.status_code, status.HTTP_400_BAD_REQUEST
                )
                self.assertIn(field, response.data)
                self.assertEqual(Achievement.objects.count(), 1)


    def test_serializer_strips_html_and_ignores_readonly_fields(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.post(
            self.list_url,
            {
                **self.payload,
                "award": "<b>Winner</b>",
                "description": "<i>Excellent work</i>",
                "star_count": 999,
                "is_starred": True,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["award"], "Winner")
        self.assertEqual(
            response.data["description"], "Excellent work"
        )
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])


    def test_anonymous_user_cannot_star(self):
        response = self.client.post(self.star_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.achievement.starred_by.count(), 0)


    def test_session_authentication_enforces_csrf(self):
        client = APIClient(enforce_csrf_checks=True)

        logged_in = client.login(username="owner", password="pw")
        self.assertTrue(logged_in)

        response = client.post(
            self.list_url,
            self.payload,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Achievement.objects.count(), 1)

