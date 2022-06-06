from rest_framework import serializers
from .models import Rental


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            '_id',
            'price_pw',
            'price_pm',
            'location',
            'property_type',
            'url',
        )
        model = Rental
