from django.apps import AppConfig


class TechnoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'techno'


    def ready(self) -> None:
        from . import signals