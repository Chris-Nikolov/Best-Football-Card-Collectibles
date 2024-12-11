from django.db import models

from djangoBestFootballCardCollectibles.accounts.models import BFCCUser
from djangoBestFootballCardCollectibles.cards.models import Card


# Create your models here.

class Report(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Reason")
    content = models.TextField(max_length=1000, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(BFCCUser, related_name='report_maker', on_delete=models.CASCADE)
