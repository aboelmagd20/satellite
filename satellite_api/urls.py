from django.urls import path
from .views import (
    PowerView, TelemetryView, CommunicationView, OBCView,
    PayloadView, ThermalView, GPSView, AllDataView
)
from .views import dashboard
urlpatterns = [
    path('power/', PowerView.as_view(), name='power'),
    path('telemetry/', TelemetryView.as_view(), name='telemetry'),
    path('communication/', CommunicationView.as_view(), name='communication'),
    path('obc/', OBCView.as_view(), name='obc'),
    path('payload/', PayloadView.as_view(), name='payload'),
    path('thermal/', ThermalView.as_view(), name='thermal'),
    path('gps/', GPSView.as_view(), name='gps'),
    path('all/', AllDataView.as_view(), name='all-data'),
    path('dashboard/', dashboard, name='dashboard'),
]