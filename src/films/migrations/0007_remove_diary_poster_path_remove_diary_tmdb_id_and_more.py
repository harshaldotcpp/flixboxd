# Generated by Django 4.1.7 on 2023-03-28 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('films', '0006_list_diary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='poster_path',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='tmdb_id',
        ),
        migrations.AddField(
            model_name='diary',
            name='movies',
            field=models.ManyToManyField(to='films.watchedmovie'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]