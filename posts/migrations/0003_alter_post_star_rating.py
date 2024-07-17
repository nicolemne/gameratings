# Generated by Django 3.2.25 on 2024-07-17 18:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_star_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='star_rating',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]
