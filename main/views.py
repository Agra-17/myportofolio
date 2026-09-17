from main.forms import AchievementForm, ExperienceForm
from main.models import Achievement, Experience
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
    json_response = get_achievements_json(request)

    achievements = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    achievements = [project.object for project in achievements]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Agra",
        "achievements": achievements,
        "title_query": title_query,
    }
    return render(request, "achievements.html", context)

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

def get_achievements_json(request):
    title_query = request.GET.get("title", "").strip()
    achievements = Achievement.objects.all()

    if title_query:
        achievements = achievements.filter(title__icontains=title_query)

    achievements_json = serializers.serialize("json", achievements)
    return HttpResponse(achievements_json, content_type="application/json")

def delete_achievement(request, achievement_id):
    achievement = get_object_or_404(Achievement, pk=achievement_id)

    if request.method == "POST":
        achievement.delete()
        messages.success(request, "achievement berhasil dihapus!")
        return redirect("main:show_achievements")

    return redirect("main:show_achievements")

def create_experience(request):
    form = ExperienceForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        form.save()
        messages.success(request, "Experience baru berhasil ditambahkan!")
        return redirect("main:show_experience")
    context = {
        "name": "Agra",
        "form": form,
    }
    return render(request,'experience_form.html', context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")