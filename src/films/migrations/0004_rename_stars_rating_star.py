# Generated by Django 4.1.7 on 2023-03-28 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_alter_rating_stars'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='stars',
            new_name='star',
        ),
    ]