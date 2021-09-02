import q
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")


def details(request, name="Не введен пользователь"):
    item = request.GET.get("item", "Неизвестный товар")
    return HttpResponse(f"<h2>Пользователь {name} товар {item}</h2>")


def details_combo(request, name="Не введен пользователь", _id=0):
    return HttpResponse(f"<h2>Пользователь {name} имеет номер {_id}</h2>")
