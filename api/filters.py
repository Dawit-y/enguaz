from django_filters.rest_framework import FilterSet
from .models import AvailableBus


class AvailableBusFilter(FilterSet):
    class Meta:
        model = AvailableBus
        fields = {
            'source': ['exact'],
            'destination': ['exact'],
            'date': ['exact'],
        }