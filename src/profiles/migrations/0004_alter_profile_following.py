# Generated by Django 4.1.7 on 2023-04-07 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_delete_userfollowing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', to='profiles.profile'),
        ),
    ]