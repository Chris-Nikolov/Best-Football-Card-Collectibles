from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from djangoBestFootballCardCollectibles.accounts.models import Profile

UserModel = get_user_model()


class BFCCUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')


class BFCCUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'email', )
