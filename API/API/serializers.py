from rest_framework import serializers
from .models import Driver , an_asigned_truck

class DriverSerializer(serializers.ModelSerializer):
    truck = serializers.SlugRelatedField(many=True,read_only=True, slug_field='number_plate')
    city_district = serializers.StringRelatedField()
    class Meta:
        model = Driver
        fields = '__all__'

class DriverSerializer0(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'