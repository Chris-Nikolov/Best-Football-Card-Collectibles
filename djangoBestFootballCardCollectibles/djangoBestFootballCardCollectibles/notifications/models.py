from django.db import models

from djangoBestFootballCardCollectibles.accounts.models import BFCCUser
from djangoBestFootballCardCollectibles.cards.models import Card


# Create your models here.

class Notifications(models.Model):
    receiver = models.ForeignKey(BFCCUser, on_delete=models.CASCADE, related_name='received_notifications')
    sender = models.ForeignKey(BFCCUser, on_delete=models.CASCADE, related_name='sent_notifications')
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_archived = models.BooleanField(default=False)
