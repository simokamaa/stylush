# Generated by Django 4.2.1 on 2023-06-28 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0027_alter_commision_saraly_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commision_saraly',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
