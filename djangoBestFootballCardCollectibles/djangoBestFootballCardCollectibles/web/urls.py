from django.urls import path

from djangoBestFootballCardCollectibles.web.views import index, StaffPageView

urlpatterns = [
    path('', index, name='index'),
    path('staff-page/', StaffPageView.as_view(), name='staff_page')
]
