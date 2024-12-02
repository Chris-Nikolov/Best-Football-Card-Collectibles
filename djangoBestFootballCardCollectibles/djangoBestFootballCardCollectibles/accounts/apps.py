from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'djangoBestFootballCardCollectibles.accounts'

    def ready(self):
        import djangoBestFootballCardCollectibles.accounts.signals
