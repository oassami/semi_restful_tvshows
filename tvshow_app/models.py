from django.db import models
from datetime import date, time, datetime

class ShowManager(models.Manager):
    def addShowValidation(self, post_date):
        errors = {}
        if len(post_date['title']) < 2:
            errors['title'] = 'Title must be at least 2 characters'
        if len(post_date['network']) < 3:
            errors['network'] = 'Network must be at least 3 characters'
        if len(post_date['description']) > 0 and len(post_date['description']) < 10:
            errors['description'] = 'Description must be at least 10 characters'
        if len(post_date['release_date']) < 6:
            errors['release_date'] = 'Release Date must be valid date.'
        else:
            release_date = date.fromisoformat(post_date['release_date'])
            today_date = date.today()
            if release_date > today_date:
                errors['release_date'] = 'Release Date must be in the past.'
        shows = Show.objects.all()
        for show in shows:
            if show.title == post_date['title']:
                errors['duplicate'] = 'This title already exists in the database!'
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

