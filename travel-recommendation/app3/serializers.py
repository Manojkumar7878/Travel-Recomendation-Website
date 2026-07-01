from rest_framework import serializers
from .models import BusRoute, Datas, Place

class BusRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusRoute
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datas
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
        