from django.shortcuts import render
from gui.models import Measurement


def reading(request):
    temp = Measurement.objects.filter(unit='1').last()
    hum = Measurement.objects.filter(unit='2').last()

    context = {
        'temp': temp.value,
        'hum': hum.value
    }
    return render(request, 'node/reading.html', context)
