# Generated by Django 4.1.7 on 2023-04-02 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0010_remove_watchedmovie_overview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchedmovie',
            name='cover_path',
        ),
        migrations.RemoveField(
            model_name='watchedmovie',
            name='release_date',
        ),
        migrations.RemoveField(
            model_name='watchedmovie',
            name='tagline',
        ),
    ]
