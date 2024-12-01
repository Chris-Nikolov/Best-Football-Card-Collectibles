from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from djangoBestFootballCardCollectibles.accounts.forms import BFCCUserCreationForm
from djangoBestFootballCardCollectibles.accounts.models import Profile

# Create your views here.

UserModel = get_user_model()


class UserRegisterView(CreateView):
    model = UserModel
    form_class = BFCCUserCreationForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response
