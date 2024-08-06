from django.http import HttpResponseRedirect
from django.urls import path

from . import views


def redirect_to_home(request):
    return HttpResponseRedirect("/home/")


urlpatterns = [
    path("", views.home, name="home"),
    path("examples/", views.examples, name="examples"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("contact/", views.contact, name="contact"),
]
