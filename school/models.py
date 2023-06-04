from django.db import models


# Create your models here.
class Profile(models.Model):
    people = models.TextField(max_length=128)
    age = models.TextField()
    average_mark = models.TextField()

    def __str__(self):
        return self.people