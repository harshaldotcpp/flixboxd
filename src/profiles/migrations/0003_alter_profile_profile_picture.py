# Generated by Django 4.2 on 2023-04-18 10:35

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_top4movies_alter_top4_user_alter_top4_four_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=django_resized.forms.ResizedImageField(crop=None, default='default.png', force_format=None, keep_meta=True, quality=-1, scale=None, size=[1920, 1080], upload_to='profile_picture/'),
        ),
    ]