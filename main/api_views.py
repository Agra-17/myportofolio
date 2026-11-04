from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (
    api_view, authentication_classes, permission_classes,
)
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from main.models import Achievement
from main.permissions import IsPortfolioOwnerOrReadOnly
from main.serializers import AchievementSerializer


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrReadOnly])
def achievement_list(request):
    if request.method in ("GET", "HEAD"):
        achievements = Achievement.objects.prefetch_related("starred_by").order_by("title", "id")
        title = request.query_params.get("title", "").strip()
        if title:
            achievements = achievements.filter(title__icontains=title)
        serializer = AchievementSerializer(
            achievements, many=True, context={"request": request},
        )
        return Response(serializer.data)

    serializer = AchievementSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrReadOnly])
def achievement_detail(request, achievement_id):
    achievement = get_object_or_404(
        Achievement.objects.prefetch_related("starred_by"), pk=achievement_id,
    )
    if request.method in ("GET", "HEAD"):
        serializer = AchievementSerializer(achievement, context={"request": request})
        return Response(serializer.data)

    if request.method == "DELETE":
        achievement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = AchievementSerializer(
        achievement, data=request.data, partial=request.method == "PATCH",
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
