# Generated by Django 4.1.7 on 2023-03-22 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_top4_four_alter_top4_one_alter_top4_three_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover_picture',
            field=models.ImageField(default='default.png', upload_to='cover_picture'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='default.png', upload_to='profile_picture/'),
        ),
    ]