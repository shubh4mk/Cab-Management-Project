# Generated by Django 4.2.7 on 2024-02-05 10:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cab_booking', '0018_poolridebooking_alter_bookingdetails_booking_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdetails',
            name='booking_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 5, 15, 57, 41, 137165)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='trip_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 5, 15, 57, 41, 137165)),
        ),
        migrations.AlterField(
            model_name='poolridebooking',
            name='booking_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 5, 15, 57, 41, 137165)),
        ),
        migrations.AlterField(
            model_name='poolridebooking',
            name='trip_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 5, 15, 57, 41, 137165)),
        ),
    ]