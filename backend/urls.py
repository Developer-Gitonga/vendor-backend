from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [
    path('tasks/',TaskViewSet.as_view(),name = "task"),
    path('catalogue/',CatalogueViewSet.as_view(), name = "catalogue"),
    path('product/', ProductViewSet.as_view(), name= "product")
    # path('tasks/<int:pk>/', TaskViewSet.as_view(),name = "task-detail")
]