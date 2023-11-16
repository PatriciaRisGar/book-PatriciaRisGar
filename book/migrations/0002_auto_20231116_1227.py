# Generated by Django 3.2.23 on 2023-11-16 11:27

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='update_at',
            field=models.DateField(auto_now=True),
        ),
    ]
