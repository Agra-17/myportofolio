from django.shortcuts import render

nama = "Muh. Agra Putra Davyza Chaniago"

def landing_page(request):
    return render(request, "index.html")