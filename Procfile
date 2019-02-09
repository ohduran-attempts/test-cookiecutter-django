web: gunicorn config.wsgi:application
worker: celery worker --app=test_cookiecutter_django.taskapp --loglevel=info
