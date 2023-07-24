# Generated by Django 4.2.1 on 2023-06-30 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0031_alter_manager_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('DORMANT', 'Dormant')], max_length=50),
        ),
    ]