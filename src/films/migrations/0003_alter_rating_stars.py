# Generated by Django 4.1.7 on 2023-03-28 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_remove_watchedmovie_rating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='stars',
            field=models.IntegerField(),
        ),
    ]
