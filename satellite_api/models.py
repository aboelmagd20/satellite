from django.db import models
import random
import time
from datetime import datetime

class BaseModel(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
    
    def get_timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class PowerHistory(models.Model):
    battery_level = models.FloatField()
    battery_voltage = models.FloatField()
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return f"PowerHistory: {self.battery_level}V at {self.timestamp}"

class TelemetryHistory(models.Model):
    sensor_telemetry = models.BooleanField()
    sensor_gps = models.BooleanField()
    sensor_communication = models.BooleanField()
    sensor_thermal = models.BooleanField()
    sensor_payload = models.BooleanField()
    sensor_control = models.BooleanField()
    sensor_obc = models.BooleanField()
    sensor_power = models.BooleanField()
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return f"TelemetryHistory at {self.timestamp}"

class CommunicationHistory(models.Model):
    data_rate = models.FloatField()
    latency = models.IntegerField()
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return f"CommunicationHistory: {self.status} at {self.timestamp}"

class OBCHistory(models.Model):
    cpu_usage = models.FloatField()
    memory_usage = models.FloatField()
    cpu_temperature = models.FloatField()
    memory_temperature = models.FloatField()
    uptime = models.IntegerField()
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return f"OBCHistory: CPU {self.cpu_usage}% at {self.timestamp}"

class PayloadHistory(models.Model):
    payload_type = models.CharField(max_length=50)
    compression_rate = models.FloatField()
    value = models.FloatField()
    memory_size = models.FloatField()
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return f"PayloadHistory: {self.payload_type} at {self.timestamp}"

class ThermalHistory(models.Model):
    internal_temperature = models.FloatField()
    external_temperature = models.FloatField()
    battery_temperature = models.FloatField()
    cooling_status = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return f"ThermalHistory: {self.cooling_status} at {self.timestamp}"

class GPSHistory(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    velocity = models.FloatField()
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return f"GPSHistory: {self.latitude}, {self.longitude} at {self.timestamp}"

class Power(BaseModel):
    battery_level = models.FloatField(default=0)
    battery_voltage = models.FloatField(default=0)
    
    def update_random_values(self):
        self.battery_level = round(random.uniform(0, 100), 2)  # 0-100%
        self.battery_voltage = round(random.uniform(3.3, 5.0), 2)  # 3.3-5.0V
        self.save()
        
    def to_dict(self):
        return {
            'battery_level': self.battery_level,
            'battery_voltage': self.battery_voltage,
            'timestamp': self.get_timestamp()
        }
    
    def save(self, *args, **kwargs):
        if self.pk:  # Check if the object already exists
            PowerHistory.objects.create(
                battery_level=self.battery_level,
                battery_voltage=self.battery_voltage,
                timestamp=self.timestamp
            )
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Power: {self.battery_level}%"

class Telemetry(BaseModel):
    sensor_telemetry = models.BooleanField(default=True)
    sensor_gps = models.BooleanField(default=True)
    sensor_communication = models.BooleanField(default=True)
    sensor_thermal = models.BooleanField(default=True)
    sensor_payload = models.BooleanField(default=True)
    sensor_control = models.BooleanField(default=True)
    sensor_obc = models.BooleanField(default=True)
    sensor_power = models.BooleanField(default=True)
    
    def update_random_values(self):
        self.sensor_telemetry = random.choice([True, False])
        self.sensor_gps = random.choice([True, False])
        self.sensor_communication = random.choice([True, False])
        self.sensor_thermal = random.choice([True, False])
        self.sensor_payload = random.choice([True, False])
        self.sensor_control = random.choice([True, False])
        self.sensor_obc = random.choice([True, False])
        self.sensor_power = random.choice([True, False])
        self.save()
        
    def to_dict(self):
        return {
            'sensor_telemetry': self.sensor_telemetry,
            'sensor_gps': self.sensor_gps,
            'sensor_communication': self.sensor_communication,
            'sensor_thermal': self.sensor_thermal,
            'sensor_payload': self.sensor_payload,
            'sensor_control': self.sensor_control,
            'sensor_obc': self.sensor_obc,
            'sensor_power': self.sensor_power,
            'timestamp': self.get_timestamp()
        }
    
    def save(self, *args, **kwargs):
        if self.pk:
            TelemetryHistory.objects.create(
                sensor_telemetry=self.sensor_telemetry,
                sensor_gps=self.sensor_gps,
                sensor_communication=self.sensor_communication,
                sensor_thermal=self.sensor_thermal,
                sensor_payload=self.sensor_payload,
                sensor_control=self.sensor_control,
                sensor_obc=self.sensor_obc,
                sensor_power=self.sensor_power,
                timestamp=self.timestamp
            )
        super().save(*args, **kwargs)
    
    def __str__(self):
        return "Telemetry"

class Communication(BaseModel):
    data_rate = models.FloatField(default=0)
    latency = models.IntegerField(default=0)
    status = models.CharField(max_length=50, default='Online')
    
    def update_random_values(self):
        self.data_rate = round(random.uniform(0.1, 10), 2)  # 0.1-10 Mbps
        self.latency = random.randint(50, 500)  # 50-500 ms
        self.status = random.choice(['Online', 'Degraded', 'Limited', 'Offline'])
        self.save()
        
    def to_dict(self):
        return {
            'data_rate': self.data_rate,
            'latency': self.latency,
            'status': self.status,
            'timestamp': self.get_timestamp()
        }
    
    def save(self, *args, **kwargs):
        if self.pk:
            CommunicationHistory.objects.create(
                data_rate=self.data_rate,
                latency=self.latency,
                status=self.status,
                timestamp=self.timestamp
            )
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Communication: {self.status}"

class OBC(BaseModel):
    cpu_usage = models.FloatField(default=0)
    memory_usage = models.FloatField(default=0)
    cpu_temperature = models.FloatField(default=0)
    memory_temperature = models.FloatField(default=0)
    uptime = models.IntegerField(default=0)
    
    def update_random_values(self):
        self.cpu_usage = round(random.uniform(5, 95), 2)  # 5-95%
        self.memory_usage = round(random.uniform(10, 90), 2)  # 10-90%
        self.cpu_temperature = round(random.uniform(30, 80), 2)  # 30-80°C
        self.memory_temperature = round(random.uniform(30, 70), 2)  # 30-70°C
        self.uptime += random.randint(0, 10)  # Incremental uptime in seconds
        self.save()
        
    def to_dict(self):
        return {
            'cpu_usage': self.cpu_usage,
            'memory_usage': self.memory_usage,
            'cpu_temperature': self.cpu_temperature,
            'memory_temperature': self.memory_temperature,
            'uptime': self.uptime,
            'timestamp': self.get_timestamp()
        }
    
    def save(self, *args, **kwargs):
        if self.pk:
            OBCHistory.objects.create(
                cpu_usage=self.cpu_usage,
                memory_usage=self.memory_usage,
                cpu_temperature=self.cpu_temperature,
                memory_temperature=self.memory_temperature,
                uptime=self.uptime,
                timestamp=self.timestamp
            )
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"OBC: CPU {self.cpu_usage}%"

class Payload(BaseModel):
    payload_type = models.CharField(max_length=50, default='Camera')
    compression_rate = models.FloatField(default=0)
    value = models.FloatField(default=0)
    memory_size = models.FloatField(default=0)
    
    def update_random_values(self):
        self.payload_type = random.choice(['Camera', 'Spectroscope', 'Radar', 'Magnetometer'])
        self.compression_rate = round(random.uniform(1, 10), 2)  # 1-10x
        self.value = round(random.uniform(0, 1000), 2)  # Generic sensor value
        self.memory_size = round(random.uniform(100, 1000), 2)  # 100-1000 MB
        self.save()
        
    def to_dict(self):
        return {
            'payload_type': self.payload_type,
            'compression_rate': self.compression_rate,
            'value': self.value,
            'memory_size': self.memory_size,
            'timestamp': self.get_timestamp()
        }
    
    def save(self, *args, **kwargs):
        if self.pk:
            PayloadHistory.objects.create(
                payload_type=self.payload_type,
                compression_rate=self.compression_rate,
                value=self.value,
                memory_size=self.memory_size,
                timestamp=self.timestamp
            )
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Payload: {self.payload_type}"

class Thermal(BaseModel):
    internal_temperature = models.FloatField(default=0)
    external_temperature = models.FloatField(default=0)
    battery_temperature = models.FloatField(default=0)
    cooling_status = models.CharField(max_length=50, default='Active')
    
    def update_random_values(self):
        self.internal_temperature = round(random.uniform(10, 50), 2)  # 10-50°C
        self.external_temperature = round(random.uniform(-100, 100), 2)  # -100 to 100°C
        self.battery_temperature = round(random.uniform(5, 40), 2)  # 5-40°C
        self.cooling_status = random.choice(['Active', 'Passive', 'Standby', 'Emergency'])
        self.save()
        
    def to_dict(self):
        return {
            'internal_temperature': self.internal_temperature,
            'external_temperature': self.external_temperature,
            'battery_temperature': self.battery_temperature,
            'cooling_status': self.cooling_status,
            'timestamp': self.get_timestamp()
        }
    
    def save(self, *args, **kwargs):
        if self.pk:
            ThermalHistory.objects.create(
                internal_temperature=self.internal_temperature,
                external_temperature=self.external_temperature,
                battery_temperature=self.battery_temperature,
                cooling_status=self.cooling_status,
                timestamp=self.timestamp
            )
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Thermal: {self.cooling_status}"

class GPS(BaseModel):
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    altitude = models.FloatField(default=0)
    velocity = models.FloatField(default=0)
    
    def update_random_values(self):
        self.latitude = round(random.uniform(-90, 90), 6)  # -90 to 90 degrees
        self.longitude = round(random.uniform(-180, 180), 6)  # -180 to 180 degrees
        self.altitude = round(random.uniform(400, 800), 2)  # 400-800 km
        self.velocity = round(random.uniform(7.5, 8.0), 2)  # ~7.5-8.0 km/s
        self.save()
        
    def to_dict(self):
        return {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'altitude': self.altitude,
            'velocity': self.velocity,
            'timestamp': self.get_timestamp()
        }
    
    def save(self, *args, **kwargs):
        if self.pk:
            GPSHistory.objects.create(
                latitude=self.latitude,
                longitude=self.longitude,
                altitude=self.altitude,
                velocity=self.velocity,
                timestamp=self.timestamp
            )
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"GPS: {self.latitude}, {self.longitude}"
