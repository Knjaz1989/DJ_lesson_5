from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):

    name = models.CharField(max_length=50, verbose_name='Название датчика')
    description = models.CharField(max_length=100, blank=True, verbose_name='Описание (необязательно)')

    def __str__(self):
        return self.name


class Measurement(models.Model):

    temperature = models.FloatField(verbose_name='Температура при измерении')
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', verbose_name='ID датчика')
    created_at = models.DateField(verbose_name='Дата измерений', auto_now=True)
    image = models.ImageField(upload_to='measurements/%Y/%m/%d' ,blank=True, default=None)

