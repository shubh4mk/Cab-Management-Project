# Generated by Django 4.2.7 on 2024-02-04 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cab_booking', '0010_rename_cabid_availablecab_carid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availablecab',
            name='id',
        ),
        migrations.AlterField(
            model_name='availablecab',
            name='carID',
            field=models.TextField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='booking_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 4, 20, 54, 41, 219195)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='trip_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 4, 20, 54, 41, 219195)),
        ),
    ]