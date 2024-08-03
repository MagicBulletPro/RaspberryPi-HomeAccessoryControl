# Generated by Django 5.0.7 on 2024-08-03 16:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accessory',
            options={'verbose_name_plural': 'Accessories'},
        ),
        migrations.AddField(
            model_name='accessory',
            name='pin_number',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='GPIO pin number'),
        ),
    ]
