from django.urls import path

from djangoBestFootballCardCollectibles.cards.views import CreateCardView, CardDetailView

urlpatterns = [
    path('add', CreateCardView.as_view(), name='add-card'),
    path('details/<int:pk>/', CardDetailView.as_view(), name='card-details'),
]
