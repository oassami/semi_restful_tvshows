from django.db import models
from datetime import date, time, datetime

class ShowManager(models.Manager):
    # def addShowValidation(self, post_data):
    #     errors = {}
    #     if len(post_data['title']) < 2:
    #         errors['title'] = 'Title must be at least 2 characters'
    #     if len(post_data['network']) < 3:
    #         errors['network'] = 'Network must be at least 3 characters'
    #     if len(post_data['description']) > 0 and len(post_data['description']) < 10:
    #         errors['description'] = 'Description must be at least 10 characters'
    #     if len(post_data['release_date']) < 6:
    #         errors['release_date'] = 'Release Date must be valid date.'
    #     else:
    #         release_date = date.fromisoformat(post_data['release_date'])
    #         today_date = date.today()
    #         if release_date > today_date:
    #             errors['release_date'] = 'Release Date must be in the past.'
    #     shows = Show.objects.all()
    #     for show in shows:
    #         if show.title == post_data['title']:
    #             errors['duplicate'] = 'The title already exists in the database!'
    #             return errors
    #     return errors

    def showValidation(self, post_data, req_title):
        errors = {}
        if len(post_data['title']) < 2:
            errors['title'] = 'Title must be at least 2 characters'
        if len(post_data['network']) < 3:
            errors['network'] = 'Network must be at least 3 characters'
        if len(post_data['description']) > 0 and len(post_data['description']) < 10:
            errors['description'] = 'Description must be at least 10 characters'
        if len(post_data['release_date']) < 6:
            errors['release_date'] = 'Release Date must be valid date.'
        else:
            release_date = date.fromisoformat(post_data['release_date'])
            today_date = date.today()
            if release_date > today_date:
                errors['release_date'] = 'Release Date must be in the past.'
        if req_title != post_data['title']:
            show = Show.objects.filter(title=post_data['title'])
            if show:
                errors['duplicate'] = 'The title already exists in the database!'
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

