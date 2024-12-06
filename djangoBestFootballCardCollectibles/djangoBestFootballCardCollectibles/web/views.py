from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView

from djangoBestFootballCardCollectibles.cards.models import Card


# Create your views here.


def index(request):
    cards = Card.objects.filter(is_approved=True).order_by('-created_at')
    context = {"cards": cards}
    return render(request, 'web/index.html', context)


class StaffPageView(UserPassesTestMixin, ListView):
    model = Card
    template_name = 'web/staff_page.html'
    context_object_name = 'cards'
    paginate_by = 5

    def test_func(self):
        return self.request.user.is_staff

    def get_queryset(self):
        return Card.objects.filter(is_approved=False, is_for_sale=True).order_by('-created_at')
