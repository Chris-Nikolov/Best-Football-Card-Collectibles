from django.db import models

from djangoBestFootballCardCollectibles.accounts.models import BFCCUser
from djangoBestFootballCardCollectibles.cards.models import Card


# Create your models here.

class Favorite(models.Model):
    user = models.ForeignKey(BFCCUser, on_delete=models.CASCADE, related_name='favorites')
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='liked_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'card')
