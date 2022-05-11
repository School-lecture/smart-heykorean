# Generated by Django 4.0.4 on 2022-05-10 12:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('smartapp', '0003_music'),
    ]

    operations = [
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
