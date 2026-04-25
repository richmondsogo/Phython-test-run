from datetime import datetime

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView  
from django.contrib.auth import logout
from django.views.generic.edit import CreateView 
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect


class SignupView(CreateView): 
    form_class = UserCreationForm
    template_name = 'home/signup.html'
    success_url = '/login'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list') 
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(TemplateView):
    template_name = 'home/logout.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs) 

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'
    redirect_authenticated_user = True


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'current_time': datetime.now()}  

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'
