"""Views configurations for the webpages"""

from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def examples(request):
    return render(request, "examples.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def pricing(request):
    return render(request, "pricing.html")


def contact(request):
    return render(request, "contact.html")
