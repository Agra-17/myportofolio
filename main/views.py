from main.forms import AchievementForm, ExperienceForm
from main.models import Achievement, Experience
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required  # Tambahkan baris ini
from django.core.exceptions import PermissionDenied        # Tambahkan baris ini
from django.views.decorators.http import require_POST
import datetime


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Agra",
        "npm": "2506624833",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Computer Science student passionate about Data Science, Machine Learning, and AI. I enjoy solving problems, exploring data, and building technology-driven solutions."
        ),
        "last_login" : last_login,
    }
    return render(request, "index.html", context)

def show_experience(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Agra",
        "title_query": title_query,
        "is_editor": is_editor(request.user),
        "form": ExperienceForm(),
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

@login_required(login_url="/login/")
def create_achievement(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

    achievements_json = serializers.serialize("json", achievements, use_natural_foreign_keys=True)
    return HttpResponse(achievements_json, content_type="application/json")

@login_required(login_url="/login/")
def delete_achievement(request, achievement_id):
    if not request.user.is_superuser:
            raise PermissionDenied
        
    achievement = get_object_or_404(Achievement, pk=achievement_id)

    if request.method == "POST":
        achievement.delete()
        messages.success(request, "achievement berhasil dihapus!")
        return redirect("main:show_achievements")

    return redirect("main:show_achievements")

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
            raise PermissionDenied

    form = ExperienceForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        form.save()
        messages.success(request, "Experience baru berhasil ditambahkan!")
        return redirect("main:show_experience")
    context = {
        "name": "Agra",
        "form": form,
        "is_edit": False,
    }
    return render(request,'experience_form.html', context)

@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Experience berhasil diperbarui!")
        return redirect("main:show_experience")

    context = {
        "name": "Agra",
        "form": form,
        "experience": experience,
        "is_edit": True,
    }
    return render(request, 'experience_form.html', context)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
            raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.prefetch_related('starred_by').all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    data = []

    for experience in experiences:
        starred_users = list(experience.starred_by.all())
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join(user.username for user in starred_users)

        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "category": experience.get_category_display(),
                "thumbnail_url": experience.thumbnail_url,
                "started_at": experience.started_at.strftime("%b %Y") if experience.started_at else "",
                "ended_at": experience.ended_at.strftime("%b %Y") if experience.ended_at else "",
                "is_ongoing": experience.is_ongoing,
                "star_count": len(starred_users),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })
    return JsonResponse(data, safe=False)


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silahkan login")
        return redirect("main:login")

    context = {
        "name" : "Agra",
        "form" : form,
    }

    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Agra",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request, achievement_id):
    achievement = get_object_or_404(Achievement, pk=achievement_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in achievement.starred_by.all():
            achievement.starred_by.remove(request.user)
        else:
            achievement.starred_by.add(request.user)

    return redirect("main:show_achievements")

@login_required(login_url="/login/")
def toggle_experience_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

def is_editor(user):
    return user.is_authenticated and user.groups.filter(name="Editor").exists()

@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan experience."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Experience berhasil ditambahkan.", "pk": str(experience.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
