# Generated by Django 4.0.3 on 2022-06-18 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingmanage', '0006_remove_user_vehicle_remove_vehicle_log_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='color',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
