# Generated by Django 4.2.1 on 2023-06-13 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0015_managesalary_employee_managesalary_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailywork',
            name='job_type',
            field=models.ForeignKey(default=1,on_delete=django.db.models.deletion.CASCADE, to='first.job_type'),
            preserve_default=False,
        ),
    ]
