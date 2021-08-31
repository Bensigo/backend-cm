from django.apps import AppConfig


class BtcRateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'btc_rate'
    def ready(self):
        from .scheduler import run
        run()
