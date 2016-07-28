from django.conf.urls import *
from django.views.generic import TemplateView
from . import views
from .views import ComingView

urlpatterns = patterns('',
        url('^.*$', ComingView.as_view(), name='comingsoon'),
)
