# Generated by Django 4.1.7 on 2023-03-28 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0009_alter_rating_stars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchedmovie',
            name='overview',
        ),
    ]
