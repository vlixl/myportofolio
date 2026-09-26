from decimal import Decimal

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Achievement, Education, Experience, Music, Photo


class MainTest(TestCase):

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)


class MainModelTest(TestCase):
    def setUp(self):

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
