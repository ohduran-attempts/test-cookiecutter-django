from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "test_cookiecutter_django.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
