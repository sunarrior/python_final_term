# Generated by Django 4.0.3 on 2022-06-17 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkingmanage', '0003_alter_vehicle_log'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='log',
        ),
    ]
