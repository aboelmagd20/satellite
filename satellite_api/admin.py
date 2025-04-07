from django.contrib import admin
from .models import PowerHistory, TelemetryHistory, CommunicationHistory, OBCHistory, PayloadHistory, ThermalHistory, GPSHistory

# Basic admin registration
admin.site.register(PowerHistory)
admin.site.register(TelemetryHistory)
admin.site.register(CommunicationHistory)
admin.site.register(OBCHistory)
admin.site.register(PayloadHistory)
admin.site.register(ThermalHistory)
admin.site.register(GPSHistory)

# Alternative: Custom admin classes for more control

class PowerAdmin(admin.ModelAdmin):
    list_display = ('battery_level', 'battery_voltage', 'timestamp')
    readonly_fields = ('timestamp',)

class TelemetryAdmin(admin.ModelAdmin):
    list_display = ('sensor_telemetry', 'sensor_gps', 'sensor_communication', 'timestamp')
    readonly_fields = ('timestamp',)

class CommunicationAdmin(admin.ModelAdmin):
    list_display = ('data_rate', 'latency', 'status', 'timestamp')
    readonly_fields = ('timestamp',)

class OBCAdmin(admin.ModelAdmin):
    list_display = ('cpu_usage', 'memory_usage', 'uptime', 'timestamp')
    readonly_fields = ('timestamp',)

class PayloadAdmin(admin.ModelAdmin):
    list_display = ('payload_type', 'compression_rate', 'value', 'memory_size', 'timestamp')
    readonly_fields = ('timestamp',)

class ThermalAdmin(admin.ModelAdmin):
    list_display = ('internal_temperature', 'external_temperature', 'battery_temperature', 'cooling_status', 'timestamp')
    readonly_fields = ('timestamp',)

class GPSAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude', 'altitude', 'velocity', 'timestamp')
    readonly_fields = ('timestamp',)
