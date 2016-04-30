from django.shortcuts import render
from gui.models import Node


def reading(request):
    nodes = Node.objects.all()
    context = {
        'nodes': nodes
    }
    return render(request, 'gui/reading.html', context)
