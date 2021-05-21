# Generated by Django 3.2.1 on 2021-05-21 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_poster_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='recommends',
            field=models.ManyToManyField(to='movies.Movie'),
        ),
        migrations.AddField(
            model_name='movie',
            name='weighted_vote',
            field=models.FloatField(default=6.52),
            preserve_default=False,
        ),
    ]
