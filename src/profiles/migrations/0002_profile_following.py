# Generated by Django 4.1.7 on 2023-03-26 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(blank=True, null=True, related_name='followers', to='profiles.profile'),
        ),
    ]
