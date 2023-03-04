from django.urls import path
from .views import (
    UserCreateAPIView,
    UserUpdateAPIView,
    
    ProfileListAPIView, 
    ProfileDetailAPIView,
)

urlpatterns = [
    path('', UserCreateAPIView.as_view()),
    # path('<int:pk>/update/', UserUpdateAPIView.as_view()),
    

    path('profiles/', ProfileListAPIView.as_view()),
    path('profiles/<int:pk>/', ProfileDetailAPIView.as_view()),

]
