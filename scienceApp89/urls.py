from django.urls import path
from . import views

app_name = 'scienceApp89'
urlpatterns = [
    path("science/", views.science, name="science"),
]
