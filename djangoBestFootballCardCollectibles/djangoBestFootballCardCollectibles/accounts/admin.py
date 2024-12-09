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
    list_display = ('email', 'is_staff', 'is_active',)
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (('Account', {'fields': ('email', 'password')}),
                 ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),)
    add_fieldsets = (
        ('Account', {
            "classes": ('wide', 'collapse'),
            "fields": ('email', 'password1', 'password2', 'is_staff', 'is_superuser', 'groups'),
        }),
    )
