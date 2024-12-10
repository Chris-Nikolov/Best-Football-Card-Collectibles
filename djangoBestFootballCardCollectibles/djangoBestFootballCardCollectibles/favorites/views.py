from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .models import Card, Favorite


@login_required
def add_to_favorites(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    Favorite.objects.get_or_create(user=request.user, card=card)
    messages.success(request, f'Card "{card.title}" has been added to your favorites.')
    return redirect('card-details', pk=card_id)


@login_required
def remove_from_favorites(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    favorite = get_object_or_404(Favorite, user=request.user, card=card)
    favorite.delete()
    return redirect('my-favorites', pk=card_id)


class FavoriteListView(LoginRequiredMixin, ListView):
    model = Favorite
    template_name = 'favorites/favorite-cards-page.html'
    context_object_name = 'favorites'
    paginate_by = 5

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user).select_related('card')
