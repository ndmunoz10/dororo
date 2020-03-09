from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_companion_items, name='get_companion_items'),
]
