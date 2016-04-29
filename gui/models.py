from __future__ import unicode_literals
from django.db import models


class Unit(models.Model):
    """
    Unit types that are available in sensor
    """
    name = models.CharField('Name', max_length=64)

    def __str__(self):
        return self.name


class Sensor(models.Model):
    """
    Sensors that can send data
    """
    name = models.CharField('Name', max_length=64)
    desc = models.CharField('Description', max_length=256)
    units = models.ManyToManyField(Unit)

    def __str__(self):
        return self.name


class Node(models.Model):
    """
    Nodes registered to communicate with app
    """
    name = models.CharField('Name', max_length=64)
    token = models.CharField(max_length=40)
    desc = models.CharField('Description', max_length=256)
    sensors = models.ManyToManyField(Sensor)

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
