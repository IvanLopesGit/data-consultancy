from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('simulation/', views.simulation, name='simulation'),
    # path('pricing/', views.pricing, name='pricing'),
]
