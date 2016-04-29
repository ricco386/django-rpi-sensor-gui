from django.contrib import admin
from gui.models import Sensor, Node, Measurement, Unit

admin.site.register(Sensor)
admin.site.register(Node)
admin.site.register(Unit)


class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('node', 'sensor', 'value', 'unit', 'date')

admin.site.register(Measurement, MeasurementAdmin)
