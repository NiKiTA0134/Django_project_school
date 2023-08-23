from django.shortcuts import render, redirect
from .controlers import *
from .forms import *
import os
from django.urls import reverse
from .models import Course
from django.contrib.auth.decorators import login_required


def render_main_page(request):
    profile_form = ProfileForm
    profile = get_all_profiles()
    return render(request, 'main.html', context={'profile': profile, 'profile_form': profile_form})


def all_courses_page(request):
    courses = Course.objects.all()
    return render(request, 'all_courses.html', {'courses': courses})


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return render(request, 'create_profile.html', context={'profile': profile, 'profile_form': form})
    else:
        form = ProfileForm()

    return render(request, 'create_profile.html', context={'profile_form': form})


def search(request):
    search_query = request.GET.get('query')
    courses = get_courses_by_search_query(search_query)
    return render(request, 'main.html', {'search_query': search_query, 'courses': courses})


def uploadFile(request):
    # Визначення шляху до файлу на диску Z
    file_path = os.path.join('Z:', 'luk', 'Files', '9_class_algebra.pdf')

    # Використовуйте reverse() для генерації URL
    file_url = reverse('books')

    # Передача шляху до файлу та згенерованого URL у контексті
    context = {'file_path': file_path, 'file_url': file_url}
    return render(request, 'books.html', context)


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            return render(request, 'create_course.html', context={'course': course, 'course_form': form})
    else:
        form = CourseForm()

    courses = Course.objects.all()
    return render(request, 'create_course.html', context={'course_form': form, 'courses': courses})


@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'profile.html', context)