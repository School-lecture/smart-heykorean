from django.db import models


# Create your models here.

class Music(models.Model):
    music_title = models.CharField(max_length=100)
    music_lyrics = models.TextField()
    music_nation = models.TextField()
    music_path = models.TextField()
    image_path = models.TextField()
    youtube_path = models.TextField()
    senti1 = models.TextField()
    senti2 = models.TextField()
    senti3 = models.TextField()
    senti4 = models.TextField()
    senti5 = models.TextField()
    music_genre = models.TextField()
