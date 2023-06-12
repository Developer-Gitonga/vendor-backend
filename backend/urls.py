from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

urlpatterns = [
    path('tasks/',TaskViewSet.as_view(),name = "task")
]