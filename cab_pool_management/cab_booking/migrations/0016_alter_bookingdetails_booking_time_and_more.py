# Generated by Django 4.2.7 on 2024-02-04 21:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cab_booking', '0015_alter_bookingdetails_booking_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdetails',
            name='booking_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 5, 2, 41, 32, 871193)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='rideStatus',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='trip_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 5, 2, 41, 32, 871193)),
        ),
    ]
