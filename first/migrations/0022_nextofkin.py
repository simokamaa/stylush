# Generated by Django 4.2.1 on 2023-06-26 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0021_rename_job_type_dailywork_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='nextofkin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('national_id', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('relationship', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
            ],
        ),
    ]
