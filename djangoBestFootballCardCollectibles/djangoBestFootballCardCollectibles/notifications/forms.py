from django import forms
from .models import Notifications


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notifications
        fields = []
