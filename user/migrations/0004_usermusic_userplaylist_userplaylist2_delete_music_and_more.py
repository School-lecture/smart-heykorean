# Generated by Django 4.0.4 on 2022-05-11 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_music_playlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMusic',
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
            options={
                'db_table': 'user_music',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserPlaylist',
            fields=[
                ('playlist_num', models.IntegerField(primary_key=True, serialize=False)),
                ('id', models.TextField()),
                ('music_num', models.TextField()),
                ('playlist_name', models.TextField()),
                ('playlist_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'user_playlist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserPlaylist2',
            fields=[
                ('playlist_num', models.IntegerField(primary_key=True, serialize=False)),
                ('id', models.TextField()),
                ('music_num', models.TextField()),
                ('playlist_name', models.TextField()),
                ('playlist_date', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Music',
        ),
        migrations.DeleteModel(
            name='Playlist',
        ),
    ]