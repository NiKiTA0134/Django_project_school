from django.urls import path
from .views import render_main_page, create_profile, search, uploadFile, create_course, all_courses_page, profile

urlpatterns = [
    path('', render_main_page, name='render_main_page'),
    path('create_profile', create_profile, name='create_profile'),
    path('search', search, name='search'),
    path('books', uploadFile, name="books"),
    path('create_course', create_course, name="create_course"),
    path('all_courses', all_courses_page, name="all_courses"),
    path('accounts/profile/', profile, name='profile'),
]
