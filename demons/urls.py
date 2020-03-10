from django.urls import path

from . import views


urlpatterns = [
    path('get-demons/', views.get_demons, name='get_demons'),
    path('search-demons/', views.search_demons, name='search_demons'),
]
