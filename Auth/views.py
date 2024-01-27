from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url='signin'



class SignInView(LoginView):
    template_name = 'signin.html'


class SignOutView(LogoutView):
    next_page = reverse_lazy('index')


def entry(request):
    return render(request, "index.html")
