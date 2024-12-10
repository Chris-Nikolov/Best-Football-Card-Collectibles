
from django.urls import path

from djangoBestFootballCardCollectibles.notifications.views import PurchaseView, NegotiationView, UserNotificationsView, \
    UserArchiveView, ArchiveNotificationView, ReturnNotificationView, get_unread_notifications

urlpatterns = [
    path('purchase-card/<int:card_id>/', PurchaseView.as_view(), name='purchase_card'),
    path('negotiate-card/<int:card_id>/', NegotiationView.as_view(), name='negotiate_card'),
    path('my-notifications/', UserNotificationsView.as_view(), name='my_notifications'),
    path('my-archive/', UserArchiveView.as_view(), name='my_archive'),
    path('archive/<int:n_id>/', ArchiveNotificationView.as_view(), name='archive'),
    path('return/<int:n_id>/', ReturnNotificationView.as_view(), name='return'),
    path('api/unread-notifications/', get_unread_notifications, name='unread_notifications')
]
