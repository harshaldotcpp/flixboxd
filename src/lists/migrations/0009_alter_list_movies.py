# Generated by Django 4.2 on 2023-04-15 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0014_film_liked_by_film_watched_by_film_watchlisted_by_and_more'),
        ('lists', '0008_list_update_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='movies',
            field=models.ManyToManyField(to='films.film'),
        ),
    ]
