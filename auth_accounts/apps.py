from django.apps import AppConfig


class AuthAccountsConfig(AppConfig):
    name = 'auth_accounts'

    def ready(self):
            import auth_accounts.signals
