# Generated by Django 4.0.4 on 2022-05-13 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0003_alter_musicmusic_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MusicMusic',
        ),
        migrations.DeleteModel(
            name='PlaylistPlaylist',
        ),
    ]
