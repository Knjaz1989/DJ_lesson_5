# Generated by Django 4.0 on 2022-01-03 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0004_alter_measurement_sensor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='created_at',
            field=models.DateField(auto_now=True, verbose_name='Дата измерений'),
        ),
    ]
