# Generated by Django 4.1.7 on 2023-04-07 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_alter_list_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listmovie',
            name='note',
            field=models.CharField(max_length=500),
        ),
    ]