# Generated by Django 4.1.7 on 2023-03-24 07:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchedmovie',
            name='watched_by',
            field=models.ManyToManyField(related_name='movies_set', to=settings.AUTH_USER_MODEL),
        ),
    ]