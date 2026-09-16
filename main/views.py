from main.forms import AchievementForm
from main.models import Achievement
from main.models import Experience
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render


def show_main(request):
    context = {
        "name": "Agra",
        "npm": "2506624833",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Computer Science student passionate about Data Science, Machine Learning, and AI. I enjoy solving problems, exploring data, and building technology-driven solutions."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Agra",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def achievement_list(request):
    achievements = Achievement.objects.all()
    context = {
        'name': "Agra",
        'achievements' : achievements,
    }

    return render(request, 'achievements.html', context)

def create_achievement(request):
    form = AchievementForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Achievement baru berhasil ditambahkan!")
        return redirect("main:show_achievements")

    context = {
        "name": "Agra",
        "form": form,
    }
    return render(request, "achievements_form.html", context)