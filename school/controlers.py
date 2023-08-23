from django.db.models import Q
from .models import Profile, Course


def get_all_profiles():
    return Profile.objects.all()


def get_all_course():
    return Course.objects.all()


def qet_questions_by_search_query(query):
    return Profile.objects.filter(Q(people__icontains=query) or Q(age__icontains=query))


def get_courses_by_search_query(query):
    return Course.objects.filter(Q(name__icontains=query) or Q(class_teacher__icontains=query))