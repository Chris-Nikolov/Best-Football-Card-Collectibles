from django import forms
from .models import Card


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'description', 'is_for_sale', 'price', 'brand', 'image']
