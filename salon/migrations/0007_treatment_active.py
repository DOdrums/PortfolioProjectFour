# Generated by Django 3.2.15 on 2022-10-25 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0006_alter_appointment_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]