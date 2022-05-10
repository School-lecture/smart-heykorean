from django.db import models
from django.utils import timezone


class Event(models.Model):
    edate = models.TextField()
    singer = models.TextField()
    location = models.TextField()
    link = models.TextField()


class Add(models.Model):
    edate = models.TextField()
    singer = models.TextField()
    location = models.TextField()
    link = models.TextField()


class Music(models.Model):
    music_num = models.IntegerField(primary_key=True)
    music_title = models.TextField()
    music_singer = models.TextField()
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


class Playlist(models.Model):
    playlist_num = models.IntegerField(primary_key=True)
    id = models.TextField()
    music_num = models.TextField()
    playlist_name = models.TextField()
    playlist_date = models.DateTimeField(default=timezone.now)
