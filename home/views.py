from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.shortcuts import redirect
from .forms import SignupForm

class SignupInterfaceView(CreateView):
    form_class = SignupForm
    template_name = 'home/signup.html'
    success_url = '/portfolio'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/portfolio')
        return super().get(request, *args, **kwargs)

class HomeView(TemplateView):
    template_name = 'home/home_page.html'
    extra_context = {}

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

