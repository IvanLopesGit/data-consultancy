"""Views configurations for the webpages"""

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
