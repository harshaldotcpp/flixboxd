# Generated by Django 4.1.7 on 2023-04-04 12:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0002_review_liked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_review_set', to=settings.AUTH_USER_MODEL),
        ),
    ]