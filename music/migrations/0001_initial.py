# Generated by Django 4.0.4 on 2022-05-07 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_title', models.TextField()),
                ('music_lyrics', models.TextField()),
                ('music_nation', models.TextField()),
                ('music_path', models.TextField()),
                ('image_path', models.TextField()),
                ('youtube_path', models.TextField()),
                ('senti1', models.TextField()),
                ('senti2', models.TextField()),
                ('senti3', models.TextField()),
                ('senti4', models.TextField()),
                ('senti5', models.TextField()),
                ('music_genre', models.TextField()),
            ],
        ),
    ]
