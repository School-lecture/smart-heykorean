from django.db import models


# Create your models here.

class Music(models.Model):
    music_title = models.CharField(max_length=100)
    music_lyrics = models.TextField()
    music_nation = models.TextField()
    music_path = models.TextField()
    image_path = models.TextField()
    youtube_path = models.TextField()
    senti1 = models.IntegerField()
    senti2 = models.IntegerField()
    senti3 = models.IntegerField()
    senti4 = models.IntegerField()
    senti5 = models.IntegerField()
    music_genre = models.TextField()
