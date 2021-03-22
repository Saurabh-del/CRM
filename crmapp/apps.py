from django.apps import AppConfig


class CrmappConfig(AppConfig):
    name = 'crmapp'

    def ready(self):
        import crmapp.signals
