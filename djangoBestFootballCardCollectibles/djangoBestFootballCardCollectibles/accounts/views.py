from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from djangoBestFootballCardCollectibles.accounts.forms import BFCCUserCreationForm
from djangoBestFootballCardCollectibles.accounts.models import Profile

# Create your views here.

UserModel = get_user_model()


class AnonymousRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'You are already logged in!')
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class UserRegisterView(AnonymousRequiredMixin, CreateView):
    model = UserModel
    form_class = BFCCUserCreationForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response


class UserLoginView(AnonymousRequiredMixin, LoginView):
    template_name = 'accounts/login.html'


class UserLogoutView(LogoutView):
    next_page = 'index'
