# Generated by Django 4.1.7 on 2023-03-22 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=1500, null=True)),
                ('country', models.CharField(max_length=50)),
                ('profile_picture', models.ImageField(default='default.jpg', upload_to='profile_picture/')),
                ('cover_picture', models.ImageField(default='default.jpg', upload_to='cover_picture')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Top4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('four', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_four', to='films.watchedmovie')),
                ('one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_one', to='films.watchedmovie')),
                ('three', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_three', to='films.watchedmovie')),
                ('two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_two', to='films.watchedmovie')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]