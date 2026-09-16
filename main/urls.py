from django.urls import path

from main.views import achievement_list, show_main, show_experience, create_achievement

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("achievements/", achievement_list, name="show_achievements"),
    path("achievements/add/", create_achievement, name="create_achievements")
]