# Generated by Django 4.1.7 on 2023-04-08 19:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_rename_movies_diarylog_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='diarylog',
            name='created_at',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
