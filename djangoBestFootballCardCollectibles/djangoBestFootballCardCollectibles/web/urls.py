from django.urls import path

from djangoBestFootballCardCollectibles.web.views import index, StaffPageView, search, AllCardsView

urlpatterns = [
    path('', index, name='index'),
    path('staff-page/', StaffPageView.as_view(), name='staff_page'),
    path('search-results/', search, name='search'),
    path('all-cards/', AllCardsView.as_view(), name='all_cards'),
]
