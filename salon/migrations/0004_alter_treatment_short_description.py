# Generated by Django 3.2.15 on 2022-09-27 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0003_treatment_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='short_description',
            field=models.CharField(max_length=225),
        ),
    ]
