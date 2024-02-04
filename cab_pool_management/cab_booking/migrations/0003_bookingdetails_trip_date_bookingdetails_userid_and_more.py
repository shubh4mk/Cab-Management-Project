# Generated by Django 4.2.7 on 2024-02-04 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cab_booking', '0002_carsavailable_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingdetails',
            name='trip_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 4, 17, 20, 22, 875726)),
        ),
        migrations.AddField(
            model_name='bookingdetails',
            name='userID',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='availablecab',
            name='availableCapacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='availablecab',
            name='carID',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='booking_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 4, 17, 20, 22, 875726)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='carID',
            field=models.TextField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='carsavailable',
            name='carID',
            field=models.TextField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
