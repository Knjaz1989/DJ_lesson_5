from django.urls import path
from .views import SensorsView, SensorView, MeasurementsView, MeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('sensors/<int:pk>/', SensorView.as_view()),
    path('measurements/', MeasurementsView.as_view()),
    path('measurements/<int:pk>/', MeasurementView.as_view()),
    # path('/measurements')
]
