from django.conf.urls import url
from gui import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^node/(?P<name>\w+)$', views.node, name='node'),
]
