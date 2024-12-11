from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, View
from django.templatetags.static import static

from djangoBestFootballCardCollectibles.accounts.forms import BFCCUserCreationForm, ProfileEditForm, \
    DeactivateProfileForm
from djangoBestFootballCardCollectibles.accounts.mixins import AnonymousRequiredMixin
from djangoBestFootballCardCollectibles.accounts.models import Profile
from djangoBestFootballCardCollectibles.cards.models import Card

# Create your views here.

UserModel = get_user_model()


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


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile.html'

    def get_object(self):

        return Profile.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        profile = self.get_object()

        context['profile'] = profile
        context['cards'] = Card.objects.filter(owner=self.request.user).order_by('-created_at')

        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):

    model = Profile

    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit.html'
    success_url = reverse_lazy('details')

    def get_object(self):

        return Profile.objects.get(user=self.request.user)


class DeactivateProfileView(LoginRequiredMixin, View):
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):

        form = DeactivateProfileForm()

        return render(request, 'accounts/profile-delete.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = DeactivateProfileForm(request.POST)

        if form.is_valid():

            user = request.user
            user.is_active = False
            user.save()

            Card.objects.filter(owner=user).update(is_approved=False)

            return redirect(self.success_url)


class ProfilesView(DetailView):

    model = Profile
    template_name = 'accounts/profile-pk.html'

    def get_object(self):

        return Profile.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        context['profile'] = profile
        context['cards'] = Card.objects.filter(owner=profile.user, is_approved=True).order_by('-created_at')

        return context
