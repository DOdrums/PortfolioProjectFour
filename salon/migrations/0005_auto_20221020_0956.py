# Generated by Django 3.2.15 on 2022-10-20 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0004_alter_appointment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='first_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='last_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='phone_number',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
