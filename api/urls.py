from django.urls import path
from .views import ProfileListAPIView, PlanListAPIView, RecipeListAPIView, TagListAPIView

urlpatterns = [
    path('profiles/', ProfileListAPIView.as_view()),
    path('profiles/<int:pk>/', ProfileListAPIView.as_view()),

    path('plans/', PlanListAPIView.as_view()),

    path('recipes/', RecipeListAPIView.as_view()),

    path('tags/', TagListAPIView.as_view()),
]
