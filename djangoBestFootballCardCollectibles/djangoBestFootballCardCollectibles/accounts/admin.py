from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from djangoBestFootballCardCollectibles.accounts.forms import BFCCUserChangeForm, BFCCUserCreationForm

# Register your models here.

UserModel = get_user_model()


@admin.register(UserModel)
class BFCCUserAdmin(UserAdmin):
    form = BFCCUserChangeForm
    add_form = BFCCUserCreationForm
    model = UserModel
    list_display = ('username', 'email', 'is_staff', 'is_active',)
    search_fields = ('username', 'email')
    ordering = ('username', 'email',)
    fieldsets = (('Account', {'fields': ('username', 'email', 'password')}),
                 ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),)
    add_fieldsets = (
        ('Acc', {
            "classes": ('wide', 'collapse'),
            "fields": ('username', 'email', 'password1', 'password2'),
        }),
    )