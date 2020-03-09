from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_fights, name='get_fights'),
]
