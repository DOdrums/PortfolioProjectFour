# Generated by Django 3.2.15 on 2022-10-07 10:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0008_auto_20221006_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planning',
            old_name='disabled_days',
            new_name='disabled_dates',
        ),
        migrations.AddField(
            model_name='planning',
            name='disabled_weekdays',
            field=models.TextField(default='', validators=[django.core.validators.RegexValidator('^[0-6](,[0-6])*$')]),
        ),
    ]
