# Generated by Django 4.2.7 on 2024-02-05 19:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchtrip',
            name='ride_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 6, 1, 28, 43, 935865)),
        ),
    ]
