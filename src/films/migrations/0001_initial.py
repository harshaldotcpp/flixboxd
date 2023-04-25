# Generated by Django 4.2 on 2023-04-23 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.IntegerField(unique=True)),
                ('original_title', models.CharField(max_length=100)),
                ('poster_path', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('release_year', models.IntegerField()),
                ('liked_by', models.ManyToManyField(blank=True, related_name='liked_movies_set', to=settings.AUTH_USER_MODEL)),
                ('watched_by', models.ManyToManyField(related_name='movies_set', to=settings.AUTH_USER_MODEL)),
                ('watchlisted_by', models.ManyToManyField(related_name='watchlist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.FloatField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.film')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DiaryLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diary_logs', to='films.film')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diary_log', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
