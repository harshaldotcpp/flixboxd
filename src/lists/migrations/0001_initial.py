# Generated by Django 4.1.7 on 2023-04-08 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ListMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.IntegerField()),
                ('note', models.CharField(max_length=500)),
                ('poster_path', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=1000)),
                ('date', models.DateField(auto_now=True)),
                ('liked_by', models.ManyToManyField(related_name='liked_list_set', to=settings.AUTH_USER_MODEL)),
                ('movies', models.ManyToManyField(to='lists.listmovie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
