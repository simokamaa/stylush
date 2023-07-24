# Generated by Django 4.2.1 on 2023-06-02 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0009_remove_commission_templates_work_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='commision_rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='dailywork',
            name='job_type',
        ),
        migrations.RemoveField(
            model_name='managesalary',
            name='job_type',
        ),
        migrations.AddField(
            model_name='dailywork',
            name='commision',
            field=models.FloatField(default=25, max_length=255),
            preserve_default=False,
        ),
    ]