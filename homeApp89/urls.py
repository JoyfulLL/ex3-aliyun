from django.urls import path
from . import views

app_name = 'homeApp89'
urlpatterns = [
    path("home/", views.home, name="home"),
]
