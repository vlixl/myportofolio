from django.forms import ModelForm, TextInput, Textarea, URLInput
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

from main.models import Project, Achievement

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data["tech_stack"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

class AchievementForm(ModelForm):
    class Meta:
        model = Achievement

        fields = [
            "award",
            "award_label",
            "category",
            "month",
            "year",
            "event",
            "organization",
            "description",
        ]

        labels = {
            "award": "Award",
            "award_label": "Award Label",
            "category": "Category",
            "month": "Month",
            "year": "Year",
            "event": "Event",
            "organization": "Organization",
            "description": "Description",
        }

    # Pembersihan input (XSS): hapus tag HTML dari setiap field teks di sisi server.
    @staticmethod
    def _clean_text(value):
        return strip_tags(value or "").strip()

    def _clean_required_text(self, field_name, label):
        value = self._clean_text(self.cleaned_data[field_name])
        if not value:
            raise ValidationError(f"{label} tidak boleh kosong atau hanya berisi tag HTML.")
        return value

    def clean_award(self):
        return self._clean_required_text("award", "Award")

    def clean_award_label(self):
        return self._clean_required_text("award_label", "Award label")

    def clean_category(self):
        return self._clean_required_text("category", "Category")

    def clean_event(self):
        return self._clean_text(self.cleaned_data["event"])

    def clean_organization(self):
        return self._clean_text(self.cleaned_data["organization"])

    def clean_description(self):
        return self._clean_required_text("description", "Description")

