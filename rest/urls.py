from django.urls import path

from .views import index

app_name = "users"
urlpatterns = [
    path("", view=index, name="index"),
]
