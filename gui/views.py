from django.shortcuts import render
from gui.models import Node


def dashboard(request):
    nodes = Node.objects.all()
    context = {
        'nodes': nodes
    }
    return render(request, 'gui/dashboard.html', context)
