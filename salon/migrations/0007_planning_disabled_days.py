# Generated by Django 3.2.15 on 2022-10-06 10:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0006_alter_planning_allow_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='planning',
            name='disabled_days',
            field=models.TextField(default='', validators=[django.core.validators.RegexValidator('^(\\s{0,})(\\d{2}\\.\\d{2}\\.\\d{4})(,\\d{2}\\.\\d{2}\\.\\d{4}){1,}(\\s){0,}$')]),
        ),
    ]
