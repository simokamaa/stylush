# Generated by Django 4.2.1 on 2023-08-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0062_employee_initializer_all_amount_income_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_initializer',
            name='all_amount_income',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='employee_initializer',
            name='company_amount_income',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='employee_initializer',
            name='consolidated_employee_income',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='back_id_image',
            field=models.ImageField(default='a.png', upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='front_id_image',
            field=models.ImageField(default='a.png', upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='image',
            field=models.ImageField(default='a.png', upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='kra_pin',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='next_of_kin_first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='next_of_kin_last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='next_of_kin_middle_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='next_of_kin_phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='next_of_kin_relationship',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='salary_type',
            field=models.CharField(blank=True, choices=[('COMMISION', 'Commision'), ('FIXED', 'Fixed')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='total_income',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='profile_image',
            field=models.ImageField(default='a.png', upload_to='upload/'),
        ),
    ]
