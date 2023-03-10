from django.db import models
from django.urls import reverse
# Create your models here.

class Creator(models.Model):
    username = models.CharField(max_length=50)
    subscribers =  models.IntegerField()
    videos =


class Video(models.Model):
    title = models.CharField(max_length=150, help_text='Enter Title')
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name='videos')
    description = models.TextField()
    length = models.IntegerField()
    views = models.IntegerField()
    likes = models.IntegerField()
    genre = models.ManyToManyField('Genre')
    language = CharField(max_length=50)
    publish_date = models.Datefield()
    personal_rating = models.FloatField()

    class Meta:
        ordering = ['-publish_date', 'personal_rating']

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
