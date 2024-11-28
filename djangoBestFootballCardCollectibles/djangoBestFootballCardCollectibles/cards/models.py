from django.core.validators import MaxLengthValidator, MinValueValidator
from django.db import models
from cloudinary.models import CloudinaryField
from djangoBestFootballCardCollectibles.accounts.models import BFCCUser
from djangoBestFootballCardCollectibles.cards.validators import validate_image_size

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
    is_approved = models.BooleanField(verbose_name="Approved", default=True)
    image = CloudinaryField('image', blank=True, null=True, validators=[validate_image_size])
