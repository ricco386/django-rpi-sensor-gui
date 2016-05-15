from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta


class Unit(models.Model):
    """
    Unit types that are available in sensor
    """
    name = models.CharField('Name', max_length=64)
    variable = models.CharField('Variable', max_length=4)

    def __str__(self):
        return self.name


class Sensor(models.Model):
    """
    Sensors that can send data
    """
    name = models.CharField('Name', max_length=64)
    desc = models.CharField('Description', max_length=256, blank=True)
    units = models.ManyToManyField(Unit)

    def __str__(self):
        return self.name


class Node(models.Model):
    """
    Nodes registered to communicate with app
    """
    name = models.CharField('Name', max_length=64)
    token = models.CharField(max_length=40, blank=True)
    desc = models.CharField('Description', max_length=256, blank=True)
    location = models.CharField('Location', max_length=256, blank=True)
    ip = models.GenericIPAddressField('IP')
    sensors = models.ManyToManyField(Sensor)

    def get_last_measurement(self):
        data = {}

        for sensor in self.sensors.all():
            for unit in sensor.units.all():
                measurement = Measurement.objects.filter(unit=unit.id, sensor=sensor.id, node=self.id).last()

                if measurement:
                    data[unit.name] = {
                        'value': measurement.value,
                        'date': measurement.date,
                    }

        return data

    class Meta:
        unique_together = ('name', 'token')

    def __str__(self):
        return self.name


class Measurement(models.Model):
    """
    Sensor data send to the app
    """
    node = models.ForeignKey(Node)
    sensor = models.ForeignKey(Sensor)
    date = models.DateTimeField(auto_now_add=True)
    value = models.CharField(max_length=128)
    unit = models.ForeignKey(Unit)

    class Meta:
        ordering = ('node', 'sensor', 'date')

    def __str__(self):
        return "%s %s" % (self.node, self.sensor)

    @classmethod
    def last_day(cls, node, sensor, unit):
        return cls.objects.filter(unit=unit.id, sensor=sensor.id, node=node.id).filter(
            date__gte=(timezone.now() - timedelta(hours=24)))

