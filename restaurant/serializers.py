# serializers.py
from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ('date', 'booking_reference', 'num_guests')