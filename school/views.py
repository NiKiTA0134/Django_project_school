from django.shortcuts import render, redirect
from .controlers import *
from .forms import *


def render_main_page(request):
    profile_form = ProfileForm
    profile = get_all_profiles()
    return render(request, 'main.html', context={'profile': profile, 'profile_form': profile_form})


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
    profiles = qet_questions_by_search_query(search_query)
    print(profiles)
    return render(request, 'main.html', {'profiles': profiles})