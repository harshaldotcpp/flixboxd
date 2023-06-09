# Generated by Django 4.2 on 2023-04-15 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('films', '0009_film'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchedmovie',
            name='director',
        ),
        migrations.RemoveField(
            model_name='watchedmovie',
            name='original_title',
        ),
        migrations.RemoveField(
            model_name='watchedmovie',
            name='poster_path',
        ),
        migrations.RemoveField(
            model_name='watchedmovie',
            name='release_year',
        ),
        migrations.AddField(
            model_name='watchedmovie',
            name='watchlisted_by',
            field=models.ManyToManyField(related_name='watchlist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='watchedmovie',
            name='tmdb_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='films.film'),
        ),
        migrations.DeleteModel(
            name='Watchlist',
        ),
    ]
