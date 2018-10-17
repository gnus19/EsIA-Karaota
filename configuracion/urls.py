from django.urls import path
from django.conf.urls import url
from configuracion.views import *
from . import views

urlpatterns = [
	url(r'^index/$', views.index, name='index'),
	url(r'^agregar_estudio/$', EstudioCreate.as_view(), name='agregar_estudio'),
	url(r'^editar_estudio/(?P<pk>\d+)/$', EstudioUpdate.as_view(), name='editar_estudio'),
	url(r'^eliminar_estudio/(?P<pk>\d+)/$', views.eliminar_estudio, name='eliminar_estudio'),
	url(r'^calcular_datos/(?P<pk>\d+)/$', views.calcular_datos, name='calcular_datos'),
]
