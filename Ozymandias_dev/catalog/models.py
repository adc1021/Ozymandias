from django.db import models
from django.urls import reverse
# Create your models here.

class Creator(models.Model):
    username = models.CharField(max_length=50)
    subscribers =  models.IntegerField()

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Video(models.Model):
    title = models.CharField(max_length=150, help_text='Enter Title')
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name='videos')
    url = models.TextField()
    description = models.TextField()
    length = models.IntegerField()
    views = models.IntegerField()
    likes = models.IntegerField()
    genre = models.ManyToManyField('Genre')
    publish_date = models.DateField()
    personal_rating = models.FloatField(validators=MaxValueValidator(5))

    class Meta:
        ordering = ['-publish_date', 'personal_rating']

    def get_absolute_url(self):
       # """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
       # """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title 
