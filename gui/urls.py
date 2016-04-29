from django.conf.urls import url
from gui import views

urlpatterns = [
    url(r'^reading/$', views.reading, name='reading'),
]
