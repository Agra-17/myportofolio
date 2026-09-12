from django.shortcuts import render
from main.models import Achievement
from main.models import Experience


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