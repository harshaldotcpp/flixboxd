# Generated by Django 4.2 on 2023-04-15 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0009_alter_list_movies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='note_by',
        ),
        migrations.RemoveField(
            model_name='note',
            name='note_on',
        ),
        migrations.DeleteModel(
            name='ListMovie',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]
