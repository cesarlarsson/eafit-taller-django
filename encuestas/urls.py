from django.conf.urls import patterns, url

from django.views.generic import DetailView, ListView
from encuestas.models import Encuesta

from encuestas import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<encuesta_id>\d+)/$', views.detalles, name='detalles'),
	url(r'^(?P<pk>\d+)/resultados/$', DetailView.as_view(model=Encuesta, template_name='encuestas/resultado.html'), name='resultados'),

    url(r'^(?P<encuesta_id>\d+)/voto/$', views.voto, name='voto'),
)