from django.urls import path
from main import api_views

app_name = "api"
urlpatterns = [
    path("achievements/", api_views.achievement_list, name="achievement-list"),
    path("achievements/<uuid:achievement_id>/", api_views.achievement_detail, name="achievement-detail"),
]
