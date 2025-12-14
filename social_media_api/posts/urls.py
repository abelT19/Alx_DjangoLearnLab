from django.urls import path
from .views import RegisterView, CustomAuthToken, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),"feed/"
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
]

