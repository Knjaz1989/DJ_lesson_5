from rest_framework import serializers
from .models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['temperature','created_at', 'sensor', 'image']
        extra_kwargs = {
            'sensor': {'write_only': True}
        }


class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
