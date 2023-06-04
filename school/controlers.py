from django.db.models import Q
from .models import Profile


def get_all_profiles():
    return Profile.objects.all()


def qet_questions_by_search_query(query):
    return Profile.objects.filter(Q(people__icontains=query) or Q(age__icontains=query))