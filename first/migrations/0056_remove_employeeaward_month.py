# Generated by Django 4.2.1 on 2023-07-07 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0055_remove_addexpenses_time_alter_addexpenses_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeaward',
            name='month',
        ),
    ]
