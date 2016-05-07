from django.shortcuts import render, get_object_or_404
from gui.models import Node


def dashboard(request):
    nodes = Node.objects.all()
    context = {
        'nodes': nodes
    }
    return render(request, 'gui/dashboard.html', context)


def node(request, name):
    node = get_object_or_404(Node, name=name)
    context = {
        'node': node
    }
    return render(request, 'gui/node.html', context)

