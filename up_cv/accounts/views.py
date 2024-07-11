from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import User
from .forms import SignUpForm


class LoginView(LoginView):
    """Logs User In. Extends Django's default LoginView
    from django.contrib.auth.views"""
    template_name = 'accounts/login.html'
    next_page = reverse_lazy("accounts:success")


class LogoutView(LogoutView):
    """Logs User Out. Extends Django's default LogoutView
    from django.contrib.auth.views"""
    next_page = reverse_lazy("accounts:login")


class SuccessView(LoginRequiredMixin, TemplateView):
    """Handles successful user login."""
    login_url = reverse_lazy("accounts:login")
    template_name = "accounts/after_page.html"


class SignUpView(CreateView):
    """Sign Ups new users."""
    model = User
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:login")


class UserUpdateView(UpdateView):
    """Modifies User details."""
    model = User
    fields = ('email', 'first_name', 'last_name')
    template_name = "accounts/update.html"
    success_url = reverse_lazy("accounts:success")

    def get_object(self):
        return self.request.user


class ChangePasswordView(PasswordChangeView):
    """Changes logged in user's password."""
    form_class = PasswordChangeForm
    success_url = reverse_lazy("accounts:success")
    template_name = 'accounts/change_password.html'
