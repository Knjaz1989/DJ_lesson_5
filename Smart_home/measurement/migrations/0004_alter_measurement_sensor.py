# Generated by Django 4.0 on 2022-01-03 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_alter_measurement_temperature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor', verbose_name='ID датчика'),
        ),
    ]
