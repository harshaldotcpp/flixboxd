# Generated by Django 4.2 on 2023-04-13 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_alter_listmovie_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listmovie',
            old_name='name',
            new_name='title',
        ),
    ]
