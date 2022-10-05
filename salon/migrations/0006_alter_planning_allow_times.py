# Generated by Django 3.2.15 on 2022-10-05 13:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0005_planning'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planning',
            name='allow_times',
            field=models.TextField(default='', validators=[django.core.validators.RegexValidator('^(?:[01]\\d|2[1-3]):[0-5]\\d(?::[0-5]\\d)?(?:,(?:[01]\\d|2[1-3]):[0-5]\\d(?::[0-5]\\d)?)*$', 'Please enter comma seperated times, without spaces, like so: 12:00,13:15')]),
        ),
    ]
