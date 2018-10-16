from django.urls import path
from django.conf.urls import url
from configuracion.views import *
from . import views

urlpatterns = [
	url(r'^index/$', views.index, name='index'),
	url(r'^agregar_estudio/$', EstudioCreate.as_view(), name='agregar_estudio'),
]
