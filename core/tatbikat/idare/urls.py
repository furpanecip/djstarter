from django.urls import path

from .views import idare

urlpatterns = [
    path("", idare, name="idare"),
]
