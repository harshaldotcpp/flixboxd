# Generated by Django 4.2 on 2023-04-20 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_review_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='likes_count',
            field=models.IntegerField(default=1),
        ),
    ]
