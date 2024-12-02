from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

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

