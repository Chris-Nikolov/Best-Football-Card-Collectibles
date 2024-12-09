from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import ListView

from djangoBestFootballCardCollectibles.cards.models import Card
from djangoBestFootballCardCollectibles.web.forms import SearchForm


# Create your views here.


def index(request):
    cards = Card.objects.filter(is_approved=True).order_by('-created_at')[:6]
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
        return Card.objects.filter(is_approved=False, is_for_sale=True).order_by('created_at')


def search(request):
    form = SearchForm()
    results = []
    query = ''
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Card.objects.filter(title__icontains=query, is_approved=True).order_by('-created_at')

        paginator = Paginator(results, 5)
        page = request.GET.get('page')
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator.num_pages)

    context = {'form': form, 'results': results, 'query': query}
    return render(request, 'web/search-page.html', context)


class AllCardsView(ListView):
    model = Card
    template_name = 'web/all-cards-page.html'
    context_object_name = 'cards'
    paginate_by = 6

    def get_queryset(self):
        return Card.objects.filter(is_approved=True).order_by('-created_at')


class BrandCardsView(ListView):
    model = Card
    template_name = 'web/brand-cards-page.html'
    context_object_name = 'cards'
    paginate_by = 6

    def get_queryset(self):
        brand = self.kwargs.get('brand')
        return Card.objects.filter(is_approved=True, brand__exact=brand).order_by('-created_at')
