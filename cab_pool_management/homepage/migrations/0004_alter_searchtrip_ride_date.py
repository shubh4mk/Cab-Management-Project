# Generated by Django 4.2.7 on 2024-02-06 12:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_alter_searchtrip_ride_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchtrip',
            name='ride_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 6, 18, 19, 33, 157483)),
        ),
    ]
