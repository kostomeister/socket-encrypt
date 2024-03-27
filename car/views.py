from rest_framework import viewsets

from car.models import Car
from car.serializers import CarSerializer


class CarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
