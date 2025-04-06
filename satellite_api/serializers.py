# satellite_api/serializers.py
from rest_framework import serializers
from .models import Power, Telemetry, Communication, OBC, Payload, Thermal, GPS

class PowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Power
        fields = '__all__'

class TelemetrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Telemetry
        fields = '__all__'

class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = '__all__'

class OBCSerializer(serializers.ModelSerializer):
    class Meta:
        model = OBC
        fields = '__all__'

class PayloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payload
        fields = '__all__'

class ThermalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thermal
        fields = '__all__'

class GPSSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPS
        fields = '__all__'