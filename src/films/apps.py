from django.apps import AppConfig


class FilmsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'films'

    def ready(self):
        import films.signals