from django.db import models


# Create your models here.
class Profile(models.Model):
    people = models.TextField(max_length=128)
    age = models.TextField()
    average_mark = models.TextField()

    def __str__(self):
        return self.people


class Course(models.Model):
    name = models.TextField(max_length=128)
    title = models.TextField(max_length=256)
    class_teacher = models.TextField(max_length=128)
    code = models.TextField(max_length=64)

    def __str__(self):
        return self.name