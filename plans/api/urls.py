from django.urls import path
from .views import (
    PlanListCreateAPIView, 
    PlanDetailAPIView,

    RecipeListAPIView, 
    RecipeDetailAPIView,

    TagListAPIView,
    TagDetailAPIView,
)

urlpatterns = [
    path('', PlanListCreateAPIView.as_view()),
    path('<int:pk>/', PlanDetailAPIView.as_view()),

    path('recipes/', RecipeListAPIView.as_view()),
    path('recipes/<int:pk>/', RecipeDetailAPIView.as_view()),

    path('tags/', TagListAPIView.as_view()),
    path('tags/<int:pk>/', TagDetailAPIView.as_view()),
]
