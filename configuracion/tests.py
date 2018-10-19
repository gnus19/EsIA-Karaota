from django.test import LiveServerTestCase, Client
from selenium import webdriver
from configuracion.models import *
import time

class PruebaFormularioEstudio(LiveServerTestCase):

    def setUp(self):
    	# Es llamado al iniciar el browser
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        self.client = Client()
        super(PruebaFormularioEstudio, self).setUp()

    def tearDown(self):
    	# Llama al tearDown al cerrar el browser
        self.browser.quit()
        super(PruebaFormularioEstudio, self).tearDown()

    def test_http_reponse_ok_tabla(self):
    	# Estatu Ok HTTP de la pagina de la tabla
    	response = self.client.get('http://127.0.0.1:8000/configuracion/index/')
    	self.assertEquals(response.status_code, 200)

    def test_http_reponse_ok_formulario(self):
    	# Estatu Ok HTTP del formulario
    	response = self.client.get('http://127.0.0.1:8000/configuracion/agregar_estudio/')
    	self.assertEquals(response.status_code, 200)

    def test_templates_correctos_tabla(self):
    	# Carga exitosa de los Templates
    	response = self.client.get('http://127.0.0.1:8000/configuracion/index/')
    	self.assertTemplateUsed(response, 'configuracion/index.html')
    	self.assertTemplateUsed(response, 'configuracion/base.html')

    def test_templates_correctos_formulario(self):
    	# Carga exitosa de los Templates
    	response = self.client.get('http://127.0.0.1:8000/configuracion/agregar_estudio/')
    	self.assertTemplateUsed(response, 'configuracion/agregar_estudio.html')
    	self.assertTemplateUsed(response, 'configuracion/base.html')

    # def test_estudio_submit(self):
    # 	# Llenado del formulario para agregar estudio
    # 	return True
