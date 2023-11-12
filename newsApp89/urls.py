from django.urls import path
from . import views

app_name = 'newsApp89'

urlpatterns = [
    path('news/<str:newName>/', views.news, name='news'),
    path('newDetail/<int:id>/', views.newDetail, name='newDetail'),
    path('search/', views.search, name='search'),
]
