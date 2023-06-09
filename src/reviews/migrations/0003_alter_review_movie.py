# Generated by Django 4.2 on 2023-04-15 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0013_alter_rating_movie'),
        ('reviews', '0002_review_review_date_review_updated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_set', to='films.film'),
        ),
    ]
