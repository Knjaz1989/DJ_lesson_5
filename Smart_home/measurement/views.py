# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all().values('id', 'name', 'description')
    serializer_class = SensorSerializer


class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.prefetch_related('measurements').all()
    serializer_class = SensorSerializer


class MeasurementsView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class MeasurementView(RetrieveUpdateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

