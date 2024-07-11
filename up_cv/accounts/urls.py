from django.urls import path
from .views import (LoginView, LogoutView, SuccessView, SignUpView,
                    UserUpdateView, ChangePasswordView)

app_name = "accounts"

urlpatterns = [
    path('log-in/', LoginView.as_view(), name='login'),
    path('log-out/', LogoutView.as_view(), name='logout'),
    path('sign-up/', SignUpView.as_view(), name='signup'),
    path('success/', SuccessView.as_view(), name='success'),
    path('update/', UserUpdateView.as_view(), name='update'),
    path('change-password/', ChangePasswordView.as_view(),
         name='change_password'),
]
