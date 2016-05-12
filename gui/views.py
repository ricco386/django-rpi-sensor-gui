from django.shortcuts import render, get_object_or_404
from gui.models import Node, Measurement
import time


def dashboard(request):
    nodes = Node.objects.all()
    context = {
        'nodes': nodes
    }
    return render(request, 'gui/dashboard.html', context)


def node(request, name):
    node = get_object_or_404(Node, name=name)
    data = []

    for sensor in node.sensors.all():
        for unit in sensor.units.all():

            measurement = []
            for value in Measurement.last_day(node, sensor, unit):

                timestamp = time.mktime(value.date.timetuple())
                measurement.append([int(timestamp*1000), float(value.value)])

            data.append({
                'name': unit.name,
                'variable': unit.variable,
                'measurements': measurement
            })

    context = {
        'node': node,
        'data': data
    }
    return render(request, 'gui/node.html', context)

