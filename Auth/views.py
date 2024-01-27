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
    success_url=reverse_lazy('home.base')




class SignInView(LoginView):
    template_name = 'signin.html'


class SignOutView(LogoutView):
    next_page = reverse_lazy('signout')



class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'authorised.html'
    login_url = '/signin'


def Homepage(request):
    return render(request, "index.html")
