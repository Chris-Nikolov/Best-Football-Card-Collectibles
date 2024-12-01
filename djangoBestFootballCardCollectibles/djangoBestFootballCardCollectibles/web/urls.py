from django.urls import path

from djangoBestFootballCardCollectibles.web.views import index

urlpatterns = [
    path('', index, name='index'),
]
