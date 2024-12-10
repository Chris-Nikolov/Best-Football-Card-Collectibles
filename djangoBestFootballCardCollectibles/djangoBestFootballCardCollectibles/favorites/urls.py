from django.urls import path
from .views import add_to_favorites, remove_from_favorites, FavoriteListView

urlpatterns = [
    path('add-to-favorites/<int:card_id>/', add_to_favorites, name='add_to_favorites'),
    path('remove-from-favorites/<int:card_id>/', remove_from_favorites, name='remove_from_favorites'),
    path('', FavoriteListView.as_view(), name='my-favorites'),
]
