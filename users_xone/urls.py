from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import UserCreateView, ChangePasswordView, MyTokenObtainPairView, PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
