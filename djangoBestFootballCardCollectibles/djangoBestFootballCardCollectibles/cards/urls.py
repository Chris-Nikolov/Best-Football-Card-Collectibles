from django.urls import path

from djangoBestFootballCardCollectibles.cards.views import CreateCardView

urlpatterns = [
    path('add', CreateCardView.as_view(), name='add-card'),
]
