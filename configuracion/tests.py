from django.test import LiveServerTestCase, Client
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from configuracion.models import *
from selenium.webdriver.support.ui import Select
import time

class PruebaFormularioEstudio(LiveServerTestCase):

    def setUp(self):
        # Es llamado al iniciar el browser
        self.browser = webdriver.Firefox() #Pruebas de navegador con selenium
        self.browser.maximize_window()
        self.client = Client() #Pruebas con testing tools de django
        super(PruebaFormularioEstudio, self).setUp()

    def tearDown(self):
        # Llama al tearDown al cerrar el browser
        self.browser.quit()
        super(PruebaFormularioEstudio, self).tearDown()

    def test_llenar_formulario(self):
        # LLenamos la tabla con datos
        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(2)
        self.browser.find_element_by_css_selector('.btn').click() # Hacemos click en agregar
        time.sleep(2)
        self.browser.find_element_by_css_selector('.btn.menu').click() # Hacemos click en volver
        time.sleep(2)
        self.browser.find_element_by_css_selector('.btn').click() # Hacemos click en  agregar nuevamente
        time.sleep(2)
        nombre = "Impacto 1"
        self.browser.find_element_by_name('nombre').send_keys(nombre) #agregamos el nombre
        time.sleep(2)
        self.browser.find_element_by_name('probabilidad').send_keys(8) #agregamos la probabilidad
        time.sleep(2)
        self.browser.find_element_by_name('pondIntensidad').send_keys(15) #agregamos la ponderacion
        time.sleep(2)
        self.browser.find_element_by_name('pondExtension').send_keys(20) #agregamos la ponderacion de la extension
        time.sleep(2)
        self.browser.find_element_by_name('pondDuracion').send_keys(10)
        time.sleep(2)
        self.browser.find_element_by_name('pondReversibilidad').send_keys(30)
        time.sleep(2)
        self.browser.find_element_by_name('pondProbabilidad').send_keys(25)
        time.sleep(2)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(2)
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        confirmacion.dismiss()
        time.sleep(2)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(2)
        confirmacion.accept()

        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(2)

        # Volvemos a agregar otro elemento pero ahora de tipo Biologico
        self.browser.find_element_by_css_selector('.btn').click() # Hacemos click en agregar
        time.sleep(5)
        nombre = "Impacto 2"
        self.browser.find_element_by_name('nombre').send_keys(nombre) #agregamos el nombre
        time.sleep(2)
        select_tipo = Select(self.browser.find_element_by_name('tipo'))
        time.sleep(2)
        select_tipo.select_by_visible_text('Biologico')
        time.sleep(2)
        self.browser.find_element_by_name('probabilidad').send_keys(4) #agregamos la probabilidad
        time.sleep(2)
        self.browser.find_element_by_name('pondIntensidad').send_keys(20) #agregamos la ponderacion
        time.sleep(2)
        self.browser.find_element_by_name('pondExtension').send_keys(20)#agregamos la ponderacion de la extension
        time.sleep(2)
        self.browser.find_element_by_name('pondDuracion').send_keys(30)
        time.sleep(2)
        self.browser.find_element_by_name('pondReversibilidad').send_keys(10)
        time.sleep(2)
        self.browser.find_element_by_name('pondProbabilidad').send_keys(20)
        time.sleep(2)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(2)
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()

        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(2)

        # Agregamos otro elemento pero ahora de tipo Socio-Cultural
        self.browser.find_element_by_css_selector('.btn').click() # Hacemos click en agregar
        time.sleep(3)
        nombre = "Impacto 3"
        self.browser.find_element_by_name('nombre').send_keys(nombre) #agregamos el nombre
        time.sleep(2)
        select_tipo = Select(self.browser.find_element_by_name('tipo'))
        time.sleep(2)
        select_tipo.select_by_visible_text('Socio-Cultural')
        time.sleep(2)
        self.browser.find_element_by_name('probabilidad').send_keys(4) #agregamos la probabilidad
        time.sleep(2)
        self.browser.find_element_by_name('pondIntensidad').send_keys(20) #agregamos la ponderacion
        time.sleep(2)
        self.browser.find_element_by_name('pondExtension').send_keys(20)#agregamos la ponderacion de la extension
        time.sleep(2)
        self.browser.find_element_by_name('pondDuracion').send_keys(30)
        time.sleep(2)
        self.browser.find_element_by_name('pondReversibilidad').send_keys(10)
        time.sleep(2)
        self.browser.find_element_by_name('pondProbabilidad').send_keys(20)
        time.sleep(2)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(2)
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        
        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(2)

        # Agregamos otro impacto de tipo biologico
        self.browser.find_element_by_css_selector('.btn').click() # Hacemos click en agregar
        time.sleep(3)
        nombre = "Impacto 4"
        self.browser.find_element_by_name('nombre').send_keys(nombre) #agregamos el nombre
        time.sleep(2)
        select_tipo = Select(self.browser.find_element_by_name('tipo'))
        time.sleep(2)
        select_tipo.select_by_visible_text('Biologico')
        time.sleep(2)
        select_relevancia = Select(self.browser.find_element_by_name('valoracion_relevancia'))
        time.sleep(2)
        select_relevancia.select_by_visible_text('Medio')
        time.sleep(2)
        select_tipo_relevancia = Select(self.browser.find_element_by_name('tipo_relevancia'))
        time.sleep(2)
        select_tipo_relevancia.select_by_visible_text('Indirecto')
        time.sleep(2)
        self.browser.find_element_by_name('probabilidad').send_keys(6) #agregamos la probabilidad
        time.sleep(2)
        self.browser.find_element_by_name('pondIntensidad').send_keys(0) #agregamos la ponderacion
        time.sleep(2)
        self.browser.find_element_by_name('pondExtension').send_keys(0)#agregamos la ponderacion de la extension
        time.sleep(2)
        self.browser.find_element_by_name('pondDuracion').send_keys(40)
        time.sleep(2)
        self.browser.find_element_by_name('pondReversibilidad').send_keys(10)
        time.sleep(2)
        self.browser.find_element_by_name('pondProbabilidad').send_keys(50)
        time.sleep(2)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(2)
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()

        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(2)

        #Intentamos agregar un impacto que ya se encuentra registrado
        self.browser.find_element_by_css_selector('.btn').click() # Hacemos click en agregar
        time.sleep(3)
        nombre = "Impacto 3"
        self.browser.find_element_by_name('nombre').send_keys(nombre) #agregamos el nombre
        time.sleep(2)
        select_tipo = Select(self.browser.find_element_by_name('tipo'))
        time.sleep(2)
        select_tipo.select_by_visible_text('Fisico')
        time.sleep(2)
        self.browser.find_element_by_name('probabilidad').send_keys(4) #agregamos la probabilidad
        time.sleep(2)
        self.browser.find_element_by_name('pondIntensidad').send_keys(20) #agregamos la ponderacion
        time.sleep(2)
        self.browser.find_element_by_name('pondExtension').send_keys(20) #agregamos la ponderacion de la extension
        time.sleep(2)
        self.browser.find_element_by_name('pondDuracion').send_keys(30) 
        time.sleep(2)
        self.browser.find_element_by_name('pondReversibilidad').send_keys(10)
        time.sleep(2)
        self.browser.find_element_by_name('pondProbabilidad').send_keys(20)
        time.sleep(2)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(2)
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        time.sleep(4)
        self.browser.find_element_by_name('nombre').send_keys('Impacto 5') #agregamos el nombre nno repetido
        time.sleep(2)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(2)
        confirmacion.accept()

        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(5)