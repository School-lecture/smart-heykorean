# Generated by Django 4.0.4 on 2022-05-11 06:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('music_num', models.IntegerField(primary_key=True, serialize=False)),
                ('music_title', models.TextField()),
                ('music_singer', models.TextField()),
                ('music_lyrics', models.TextField()),
                ('music_nation', models.TextField()),
                ('music_path', models.TextField()),
                ('image_path', models.TextField()),
                ('youtube_path', models.TextField()),
                ('senti1', models.IntegerField()),
                ('senti2', models.IntegerField()),
                ('senti3', models.IntegerField()),
                ('senti4', models.IntegerField()),
                ('senti5', models.IntegerField()),
                ('music_genre', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('playlist_num', models.IntegerField(primary_key=True, serialize=False)),
                ('id', models.TextField()),
                ('music_num', models.TextField()),
                ('playlist_name', models.TextField()),
                ('playlist_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
