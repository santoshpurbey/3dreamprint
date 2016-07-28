from django.conf.urls import *
from django.views.generic import TemplateView
from rest_framework import routers
from . import views
from .views import IndexView

urlpatterns = patterns('',
        url('^.*$', IndexView.as_view(), name='index'),
)
