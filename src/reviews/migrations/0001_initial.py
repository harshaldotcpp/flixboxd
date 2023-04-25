# Generated by Django 4.2 on 2023-04-23 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('films', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('likes_count', models.IntegerField(default=0)),
                ('liked_by', models.ManyToManyField(related_name='liked_review_set', to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_set', to='films.film')),
                ('review_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
