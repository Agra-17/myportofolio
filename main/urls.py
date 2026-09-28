from django.urls import path

from main.views import (
    achievement_list,
    show_main,
    show_experience,
    create_achievement,
    get_achievements_json,
    delete_achievement,
    create_experience,
    get_experience_json,
    delete_experience,
    update_experience,
    register,
    login_user,
    logout_user,
    toggle_star,
    toggle_experience_star,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("achievements/", achievement_list, name="show_achievements"),
    path("achievements/add/", create_achievement, name="create_achievements"),
    path("api/achievements/", get_achievements_json, name="get_achievements_json"),
    path("achievements/<uuid:achievement_id>/delete/", delete_achievement, name="delete_achievement"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/edit/", update_experience, name="update_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("achievements/<uuid:achievement_id>/star/", toggle_star,name="toggle_star",),
    path("experience/<uuid:experience_id>/star/", toggle_experience_star,name="toggle_experience_star",),
    
]