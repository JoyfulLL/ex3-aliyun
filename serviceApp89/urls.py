from django.urls import path
from . import views
app_name = 'serviceApp89'

urlpatterns = [
    path("download/", views.download, name="download"),
    path("platform/", views.platform, name="platform"),
    path('getDoc/<int:id>/', views.getDoc, name='getDoc'),
]
