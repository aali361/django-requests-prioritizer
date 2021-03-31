from django.urls import path

from . import views

urlpatterns = [
    path('calculate/', views.ResourceManager.as_view()),
]
