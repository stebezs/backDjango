# Generated by Django 3.1 on 2020-09-01 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20200901_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='launch',
            name='flight_id',
        ),
        migrations.RemoveField(
            model_name='launch',
            name='landing_vehicle',
        ),
    ]
