# Generated by Django 4.1.7 on 2023-03-28 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0008_diarylog_delete_diary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='stars',
            field=models.FloatField(),
        ),
    ]
