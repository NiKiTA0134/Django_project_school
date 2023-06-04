from django.urls import path
from .views import render_main_page, create_profile, search

urlpatterns = [
    path('', render_main_page, name='render_main_page'),
    path('create_profile', create_profile, name='create_profile'),
    path('search', search, name='search'),
]
