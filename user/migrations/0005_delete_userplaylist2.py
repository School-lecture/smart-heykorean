# Generated by Django 4.0.4 on 2022-05-11 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_usermusic_userplaylist_userplaylist2_delete_music_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserPlaylist2',
        ),
    ]