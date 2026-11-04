from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Achievement


class AchievementSerializer(serializers.ModelSerializer):
    month_display = serializers.SerializerMethodField()
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()
    can_change = serializers.SerializerMethodField()
    can_delete = serializers.SerializerMethodField()

    class Meta:
        model = Achievement
        fields = [
            "id", "award", "award_label", "category", "month", "month_display",
            "year", "event", "organization", "description", "star_count",
            "is_starred", "starred_by_names", "can_change", "can_delete",
        ]
        read_only_fields = ["id"]

    def _clean_required(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("This field cannot be empty.")
        return value

    def validate_award(self, value):
        return self._clean_required(value)

    def validate_award_label(self, value):
        return self._clean_required(value)

    def validate_category(self, value):
        return self._clean_required(value)

    def validate_description(self, value):
        return self._clean_required(value)

    def validate_event(self, value):
        return strip_tags(value or "").strip()

    def validate_organization(self, value):
        return strip_tags(value or "").strip()

    def get_month_display(self, obj):
        return obj.get_month_display()

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        return bool(
            request and request.user.is_authenticated
            and request.user in obj.starred_by.all()
        )

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())

    def get_can_change(self, obj):
        request = self.context.get("request")
        return bool(request and request.user.has_perm("main.change_achievement"))

    def get_can_delete(self, obj):
        request = self.context.get("request")
        return bool(request and request.user.is_superuser)
