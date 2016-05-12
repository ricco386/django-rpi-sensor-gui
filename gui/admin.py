from django.contrib import admin
from gui.models import Sensor, Node, Measurement, Unit


class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'variable')

admin.site.register(Unit, UnitAdmin)


class SensorAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Sensor, SensorAdmin)


class NodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'ip')

admin.site.register(Node, NodeAdmin)


class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('node', 'sensor', 'value', 'unit', 'date')
    list_filter = ('node', 'sensor', 'unit', 'date  ')

admin.site.register(Measurement, MeasurementAdmin)
