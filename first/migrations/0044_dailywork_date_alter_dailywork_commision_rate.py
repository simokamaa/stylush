# Generated by Django 4.2.1 on 2023-07-06 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0043_alter_dailywork_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailywork',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 6, 14, 22, 22, 219060, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dailywork',
            name='commision_rate',
            field=models.FloatField(choices=[('CHOICE A', '25'), ('CHOICE B', '30'), ('CHOICE C', '35'), ('CHOICE D', '40'), ('CHOICE B', '45')]),
        ),
    ]
