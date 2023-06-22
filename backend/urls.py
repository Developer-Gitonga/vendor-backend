from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'backend'

urlpatterns = [
    path('tasks/',TaskViewSet.as_view(),name = "task"),
    path('catalogue/',CatalogueViewSet.as_view(), name = "catalogue"),
    path('product/', ProductViewSet.as_view(), name= "product"),
    path('tasks/<int:pk>/', TaskViewSet.as_view(),name = "task-detail"),
    path('catalogue/<int:pk>/', CatalogueViewSet.as_view(),name = "task-detail"),
    path('product/<int:pk>/', ProductViewSet.as_view(),name = "task-detail")

]