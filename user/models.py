from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=55)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    phone_num = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user'

class Event(models.Model):
    event_num = models.IntegerField(primary_key=True)
    date1 = models.CharField(max_length=50)
    singer = models.CharField(max_length=50)
    loacation = models.CharField(max_length=50)
    link = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'event'

class UserMusic(models.Model):
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
    music_genre = models.TextField()

    class Meta:
        managed = False
        db_table = 'user_music'


class UserPlaylist(models.Model):
    playlist_num = models.IntegerField(primary_key=True)
    id = models.TextField()
    music_num = models.TextField()
    playlist_name = models.TextField()
    playlist_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_playlist'
