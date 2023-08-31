from django.urls import path
from .views import LoginView, RegisterView, UserProfileView

urlpatterns = [
    path('api/login/', LoginView.as_view(), name='user-login'),
    path('api/register/', RegisterView.as_view(), name='user-register'),
    path('api/profile/<int:pk>/', UserProfileView.as_view(), name='user-profile'),   
]