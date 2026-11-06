from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Achievement, Experience


class AchievementSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Achievement
        fields = [
            "id", "title", "description", "scale",
            "date_achieved", "issuer",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value)

    def validate_issuer(self, value):
        return strip_tags(value)

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())

class ExperienceSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(
        source="get_category_display",
        read_only=True,
    )
    thumbnail_url = serializers.ReadOnlyField()
    is_ongoing = serializers.ReadOnlyField()

    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = [
            "id",
            "title",
            "description",
            "category",
            "category_display",
            "thumbnail",
            "thumbnail_url",
            "started_at",
            "ended_at",
            "is_ongoing",
            "star_count",
            "is_starred",
            "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()

        if not value:
            raise serializers.ValidationError(
                "Nama experience tidak boleh kosong."
            )

        return value

    def validate_description(self, value):
        value = strip_tags(value).strip()

        if not value:
            raise serializers.ValidationError(
                "Deskripsi experience tidak boleh kosong."
            )

        return value

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")

        if request is None or not request.user.is_authenticated:
            return False

        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(
            user.username for user in obj.starred_by.all()
        )
