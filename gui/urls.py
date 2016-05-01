from django.conf.urls import url
from gui import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
]
