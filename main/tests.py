from decimal import Decimal

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Achievement, Education, Experience, Music, Photo


class MainTest(TestCase):
    # def setUp(self):
    #     self.experience = Experience.objects.create(
    #         title="Asisten Dosen PBP",
    #         description="Membantu mahasiswa memahami pengembangan web.",
    #         category="part-time",
    #     )

    # def test_main_url_is_accessible(self):
    #     response = self.client.get(reverse("main:show_main"))

    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "index.html")
    #     self.assertNotContains(response, self.experience.title)
    #     self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    # def test_experience_model(self):
    #     self.assertEqual(str(self.experience), "Asisten Dosen PBP")
    #     self.assertEqual(self.experience.category, "part-time")
    #     self.assertTrue(self.experience.is_ongoing)

    # def test_experience_page(self):
    #     response = self.client.get(reverse("main:show_experience"))

    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "experience.html")
    #     self.assertContains(response, self.experience.title)
    #     self.assertContains(response, self.experience.description)
    #     self.assertContains(response, "Part-Time")
    #     self.assertContains(response, "Sedang berlangsung")
    #     self.assertContains(response, f'href="{reverse("main:show_main")}"')

    # def test_empty_experience_page(self):
    #     Experience.objects.all().delete()
    #     response = self.client.get(reverse("main:show_experience"))

    #     self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    # def test_completed_experience(self):
    #     self.experience.ended_at = timezone.now()
    #     self.experience.save()
    #     response = self.client.get(reverse("main:show_experience"))

    #     self.assertFalse(self.experience.is_ongoing)
    #     self.assertContains(response, "Selesai")
    #     self.assertNotContains(response, "Sedang berlangsung")


class MainModelTest(TestCase):
    def setUp(self):
        # self.experience = Experience.objects.create(
        #     title="Asisten Dosen PBP",
        #     description="Membantu mahasiswa memahami pengembangan web.",
        #     category="part-time",
        # )

        self.music = Music.objects.create(
            title="Komposisi Pertama",
            description="Komposisi piano sederhana.",
            link="https://example.com/music",
        )

        self.education = Education.objects.create(
            school="Universitas Indonesia",
            start_year=2025,
            grade=Decimal("4.00"),
            description="Mahasiswa Ilmu Komputer.",
        )

        self.achievement = Achievement.objects.create(
            award="1",
            award_label="Juara",
            category="Pemrograman",
            month=8,
            year=2026,
            event="Lomba Pemrograman",
            organization="Universitas Indonesia",
            description="Meraih juara pertama dalam lomba pemrograman.",
        )

        self.photo = Photo.objects.create(
            image="img/photos/bedroom.avif",
            description="Foto kamar tidur.",
            track=1,
            position=1,
        )

    # Experience
    # def test_experience_category_display(self):
    #     self.assertEqual(self.experience.get_category_display(), "Part-Time")

    # def test_experience_default_category(self):
    #     experience = Experience.objects.create(
    #         title="Software Engineer",
    #         description="Mengembangkan aplikasi web.",
    #     )

    #     self.assertEqual(experience.category, "full-time")
    #     self.assertEqual(experience.get_category_display(), "Full-Time")
    #     self.assertTrue(experience.is_ongoing)

    # def test_experience_start_time_is_preserved(self):
    #     started_at = self.experience.started_at
    #     self.assertIsNotNone(started_at)

    #     self.experience.title = "Asisten Dosen SDA"
    #     self.experience.save()
    #     self.experience.refresh_from_db()

    #     self.assertEqual(self.experience.started_at, started_at)

    # def test_experience_completed_status(self):
    #     self.experience.ended_at = timezone.now()
    #     self.experience.save()
    #     self.experience.refresh_from_db()

    #     self.assertFalse(self.experience.is_ongoing)

    # def test_experience_invalid_category(self):
    #     self.experience.category = "invalid"

    #     with self.assertRaises(ValidationError) as error:
    #         self.experience.full_clean()

    #     self.assertIn("category", error.exception.message_dict)

    # Music
    def test_music_model(self):
        self.music.refresh_from_db()

        self.assertEqual(str(self.music), "Komposisi Pertama")
        self.assertEqual(self.music.description, "Komposisi piano sederhana.")
        self.assertEqual(self.music.link, "https://example.com/music")

    def test_music_invalid_link(self):
        self.music.link = "bukan-url"

        with self.assertRaises(ValidationError) as error:
            self.music.full_clean()

        self.assertIn("link", error.exception.message_dict)

    def test_music_title_too_long(self):
        self.music.title = "A" * 256

        with self.assertRaises(ValidationError) as error:
            self.music.full_clean()

        self.assertIn("title", error.exception.message_dict)

    # Education
    def test_education_model(self):
        self.education.refresh_from_db()

        self.assertEqual(str(self.education), "Universitas Indonesia")
        self.assertEqual(self.education.start_year, 2025)
        self.assertEqual(self.education.grade, Decimal("4.00"))
        self.assertTrue(self.education.is_ongoing)

    def test_completed_education(self):
        self.education.end_year = 2029
        self.education.save()
        self.education.refresh_from_db()

        self.assertEqual(self.education.end_year, 2029)
        self.assertFalse(self.education.is_ongoing)

    def test_education_optional_fields(self):
        self.education.end_year = None
        self.education.grade = None
        self.education.logo = None
        self.education.full_clean()
        self.education.save()
        self.education.refresh_from_db()

        self.assertIsNone(self.education.end_year)
        self.assertIsNone(self.education.grade)
        self.assertIsNone(self.education.logo)
        self.assertTrue(self.education.is_ongoing)

    # Achievement
    def test_achievement_model(self):
        self.assertEqual(str(self.achievement), "1 Juara, Pemrograman")
        self.assertEqual(self.achievement.year, 2026)

    def test_achievement_month_display(self):
        self.assertEqual(self.achievement.get_month_display(), "August")

    def test_achievement_invalid_month(self):
        self.achievement.month = 13

        with self.assertRaises(ValidationError) as error:
            self.achievement.full_clean()

        self.assertIn("month", error.exception.message_dict)

    def test_achievement_optional_fields(self):
        self.achievement.event = ""
        self.achievement.organization = ""
        self.achievement.full_clean()
        self.achievement.save()
        self.achievement.refresh_from_db()

        self.assertEqual(self.achievement.event, "")
        self.assertEqual(self.achievement.organization, "")

    # Photo
    def test_photo_model(self):
        self.photo.refresh_from_db()

        self.assertEqual(self.photo.image, "img/photos/bedroom.avif")
        self.assertEqual(self.photo.description, "Foto kamar tidur.")
        self.assertEqual(self.photo.track, 1)
        self.assertEqual(self.photo.position, 1)

    def test_photo_negative_track(self):
        self.photo.track = -1

        with self.assertRaises(ValidationError) as error:
            self.photo.full_clean()

        self.assertIn("track", error.exception.message_dict)

    def test_photo_negative_position(self):
        self.photo.position = -1

        with self.assertRaises(ValidationError) as error:
            self.photo.full_clean()

        self.assertIn("position", error.exception.message_dict)
