from django.shortcuts import render

from djangoBestFootballCardCollectibles.cards.models import Card


# Create your views here.


def index(request):
    cards = Card.objects.filter(is_approved=True).order_by('-created_at')
    context = {"cards": cards}
    return render(request, 'web/index.html', context)
