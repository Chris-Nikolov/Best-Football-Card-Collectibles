from django.core.validators import MaxLengthValidator, MinValueValidator
from django.db import models

from djangoBestFootballCardCollectibles.accounts.models import BFCCUser


# Create your models here.


class Card(models.Model):
    BRAND_CHOICES = (
        ('Topps', 'Topps'),
        ('Panini', 'Panini'),
        ('Futera', 'Futera'),
        ('Other', 'Other'),
    )
    title = models.CharField(verbose_name="Title", validators=[MaxLengthValidator(200)])
    description = models.TextField(verbose_name="Description", validators=[MaxLengthValidator(2000)])
    is_for_sale = models.BooleanField(verbose_name="For Sale", default=False)
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(0.01)], null=True, blank=True)
    brand = models.CharField(verbose_name="Brand", choices=BRAND_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(BFCCUser, verbose_name="Owner", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Image", upload_to="cards/%Y/%m/%d", blank=True, null=True)
    # TODO CHECK LATER

