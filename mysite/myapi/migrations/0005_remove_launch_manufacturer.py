# Generated by Django 3.1 on 2020-09-01 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_remove_launch_flight_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='launch',
            name='manufacturer',
        ),
    ]
