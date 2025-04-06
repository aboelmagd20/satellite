from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Power, Telemetry, Communication, OBC, Payload, Thermal, GPS
from .serializers import (
    PowerSerializer, TelemetrySerializer, CommunicationSerializer,
    OBCSerializer, PayloadSerializer, ThermalSerializer, GPSSerializer
)
from django.shortcuts import render
class PowerView(APIView):
    def get(self, request):
        # Get or create the Power instance
        power, created = Power.objects.get_or_create(pk=1)
        
        # Update with random values
        power.update_random_values()
        
        # Return the data
        return Response(power.to_dict())

class TelemetryView(APIView):
    def get(self, request):
        telemetry, created = Telemetry.objects.get_or_create(pk=1)
        telemetry.update_random_values()
        return Response(telemetry.to_dict())

class CommunicationView(APIView):
    def get(self, request):
        communication, created = Communication.objects.get_or_create(pk=1)
        communication.update_random_values()
        return Response(communication.to_dict())

class OBCView(APIView):
    def get(self, request):
        obc, created = OBC.objects.get_or_create(pk=1)
        obc.update_random_values()
        return Response(obc.to_dict())

class PayloadView(APIView):
    def get(self, request):
        payload, created = Payload.objects.get_or_create(pk=1)
        payload.update_random_values()
        return Response(payload.to_dict())

class ThermalView(APIView):
    def get(self, request):
        thermal, created = Thermal.objects.get_or_create(pk=1)
        thermal.update_random_values()
        return Response(thermal.to_dict())

class GPSView(APIView):
    def get(self, request):
        gps, created = GPS.objects.get_or_create(pk=1)
        gps.update_random_values()
        return Response(gps.to_dict())

class AllDataView(APIView):
    def get(self, request):
        # Get or create all instances
        power, _ = Power.objects.get_or_create(pk=1)
        telemetry, _ = Telemetry.objects.get_or_create(pk=1)
        communication, _ = Communication.objects.get_or_create(pk=1)
        obc, _ = OBC.objects.get_or_create(pk=1)
        payload, _ = Payload.objects.get_or_create(pk=1)
        thermal, _ = Thermal.objects.get_or_create(pk=1)
        gps, _ = GPS.objects.get_or_create(pk=1)
        
        # Update all with random values
        power.update_random_values()
        telemetry.update_random_values()
        communication.update_random_values()
        obc.update_random_values()
        payload.update_random_values()
        thermal.update_random_values()
        gps.update_random_values()
        
        # Combine all data
        data = {
            'power': power.to_dict(),
            'telemetry': telemetry.to_dict(),
            'communication': communication.to_dict(),
            'obc': obc.to_dict(),
            'payload': payload.to_dict(),
            'thermal': thermal.to_dict(),
            'gps': gps.to_dict(),
        }
        
        return Response(data)
    
def dashboard(request):
    return render(request, 'satellite_api/dashboard.html')