from django.urls import path

from djangoBestFootballCardCollectibles.cards.views import CreateCardView, CardDetailView, CardUpdateView, \
    DeleteCardView, CardApprovalView, CardDisapprovalView

urlpatterns = [
    path('add', CreateCardView.as_view(), name='add-card'),
    path('details/<int:pk>/', CardDetailView.as_view(), name='card-details'),
    path('edit/<int:pk>/', CardUpdateView.as_view(), name='card-edit'),
    path('delete/<int:pk>/', DeleteCardView.as_view(), name='card-delete'),
    path('approve/<int:pk>/', CardApprovalView.as_view(), name='card-approve'),
    path('disapprove/<int:pk>/', CardDisapprovalView.as_view(), name='card-disapprove'),
]
