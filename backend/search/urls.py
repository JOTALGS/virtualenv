from django.urls import path

from . import api


urlpatterns = [
    path('users/<str:input>/', api.autofill_users, name='search'),
    path('suggestions/', api.suggest_users, name='search'),
]