from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', ServicesList.as_view(), name='services-list')
]