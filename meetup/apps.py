from django.apps import AppConfig


class MeetupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'meetup'

    def ready(self):
        import meetup.signals  # noqa
