from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.forms import modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from djangoBestFootballCardCollectibles.cards.forms import CardForm
from djangoBestFootballCardCollectibles.cards.models import Card


# Create your views here.
class CreateCardView(CreateView):

    queryset = Card.objects.all().order_by('-created_at')
    fields = ['title', 'description', 'is_for_sale', 'price', 'brand', 'image']
    template_name = "cards/upload-card.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        card = form.save(commit=False)
        card.owner = self.request.user
        if card.price:
            card.is_for_sale = True
        if card.is_for_sale:
            card.is_approved = False
        card.save()
        return super().form_valid(form)


class CardDetailView(DetailView):
    model = Card
    template_name = 'cards/product-detail.html'
    context_object_name = 'card'


class CardUpdateView(LoginRequiredMixin, UpdateView):
    model = Card
    form_class = CardForm
    template_name = 'cards/edit-card.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return Card.objects.get(pk=self.kwargs['pk'], owner=self.request.user)

    def form_valid(self, form):
        card = form.save(commit=False)
        card.owner = self.request.user
        card.save()
        return super().form_valid(form)


class DeleteCardView(LoginRequiredMixin, DeleteView):
    model = Card
    template_name = "cards/delete-card.html"
    success_url = reverse_lazy("index")

    def get_object(self):
        card = Card.objects.get(pk=self.kwargs['pk'])
        if card.owner == self.request.user or self.request.user.is_superuser:
            return card
        else:
            raise PermissionDenied("This user don't have permission to delete this card.")


class CardApprovalView(UserPassesTestMixin, UpdateView):
    model = Card
    fields = []
    template_name = 'cards/approve-card.html'
    success_url = reverse_lazy('staff_page')

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        card = form.save(commit=False)
        card.is_approved = True
        card.save()
        return super().form_valid(form)


class CardDisapprovalView(UserPassesTestMixin, UpdateView):
    model = Card
    fields = []
    template_name = 'cards/disapprove-card.html'
    success_url = reverse_lazy('staff_page')

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        card = form.save(commit=False)
        card.is_approved = False
        card.is_for_sale = False
        card.price = None
        card.save()
        return super().form_valid(form)
