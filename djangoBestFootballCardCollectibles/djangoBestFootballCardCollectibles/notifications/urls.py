
from django.urls import path

from djangoBestFootballCardCollectibles.notifications.views import PurchaseView, NegotiationView, UserNotificationsView

urlpatterns = [
    path('purchase-card/<int:card_id>/', PurchaseView.as_view(), name='purchase_card'),
    path('negotiate-card/<int:card_id>/', NegotiationView.as_view(), name='negotiate_card'),
    path('my-notifications/', UserNotificationsView.as_view(), name='my_notifications'),
]
