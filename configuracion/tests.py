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
        time.sleep(4)
        self.browser.find_element_by_css_selector('.btn').click() # Hacemos click en agregar
        time.sleep(4)
        self.browser.find_element_by_css_selector('.btn.menu').click() # Hacemos click en volver
        time.sleep(3)
        self.browser.find_element_by_css_selector('.btn').click() # Hacemos click en  agregar nuevamente
        time.sleep(4)
        nombre_uno = "Impacto 1"
        self.browser.find_element_by_name('nombre').send_keys(nombre_uno) #agregamos el nombre
        time.sleep(2)
        self.browser.find_element_by_name('probabilidad').send_keys(8) #agregamos la probabilidad
        time.sleep(2)
        self.browser.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        time.sleep(4)
        self.browser.find_element_by_name('pondIntensidad').send_keys(15) #agregamos la ponderacion de la intensidad
        time.sleep(2)
        self.browser.find_element_by_name('pondExtension').send_keys(20) #agregamos la ponderacion de la extension
        time.sleep(2)
        self.browser.find_element_by_name('pondDuracion').send_keys(10) #agregamos la ponderacion de la duracion
        time.sleep(2)
        self.browser.find_element_by_name('pondReversibilidad').send_keys(30) #agregamos la ponderacion de la reversibilidad
        time.sleep(2)
        self.browser.find_element_by_name('pondProbabilidad').send_keys(25) #agregamos la ponderacion de la probabilidad
        time.sleep(2)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(2)
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        confirmacion.dismiss()
        time.sleep(2)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(4)
        confirmacion.accept()

        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(4)

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
        self.browser.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        time.sleep(2)
        self.browser.find_element_by_name('pondIntensidad').send_keys(20) #agregamos la ponderacion de la intensidad
        time.sleep(2)
        self.browser.find_element_by_name('pondExtension').send_keys(20)#agregamos la ponderacion de la extension
        time.sleep(2)
        self.browser.find_element_by_name('pondDuracion').send_keys(30) #agregamos la ponderacion de la duracion
        time.sleep(2)
        self.browser.find_element_by_name('pondReversibilidad').send_keys(10) #agregamos la ponderacion de la reversibilidad
        time.sleep(2)
        self.browser.find_element_by_name('pondProbabilidad').send_keys(20)  #agregamos la ponderacion de la probabilidad
        time.sleep(2)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(2)
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()

        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(4)

        # Agregamos otro elemento pero ahora de tipo Socio-Cultural
        self.browser.find_element_by_css_selector('.btn').click() # Hacemos click en agregar
        time.sleep(4)
        nombre = "Impacto 3"
        self.browser.find_element_by_name('nombre').send_keys(nombre) #agregamos el nombre
        time.sleep(2)
        select_tipo = Select(self.browser.find_element_by_name('tipo'))
        time.sleep(2)
        select_tipo.select_by_visible_text('Socio-Cultural')
        time.sleep(2)
        self.browser.find_element_by_name('probabilidad').send_keys(4) #agregamos la probabilidad
        time.sleep(2)
        self.browser.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        time.sleep(2)
        self.browser.find_element_by_name('pondIntensidad').send_keys(20) #agregamos la ponderacion de la intensidad
        time.sleep(2)
        self.browser.find_element_by_name('pondExtension').send_keys(20)#agregamos la ponderacion de la extension
        time.sleep(2)
        self.browser.find_element_by_name('pondDuracion').send_keys(30) #agregamos la ponderacion de la duracion
        time.sleep(2)
        self.browser.find_element_by_name('pondReversibilidad').send_keys(10) #agregamos la ponderacion de la reversibilidad
        time.sleep(2)
        self.browser.find_element_by_name('pondProbabilidad').send_keys(20) #agregamos la ponderacion de la probabilidad
        time.sleep(2)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(2)
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        
        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(4)

        # Agregamos otro impacto de tipo biologico
        self.browser.find_element_by_css_selector('.btn').click() # Hacemos click en agregar
        time.sleep(4)
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
        self.browser.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        time.sleep(2)
        self.browser.find_element_by_name('pondIntensidad').send_keys(0) #agregamos la ponderacion de la intensidad
        time.sleep(2)
        self.browser.find_element_by_name('pondExtension').send_keys(0)#agregamos la ponderacion de la extension
        time.sleep(2)
        self.browser.find_element_by_name('pondDuracion').send_keys(40) #agregamos la ponderacion de la duracion
        time.sleep(2)
        self.browser.find_element_by_name('pondReversibilidad').send_keys(10) #agregamos la ponderacion de la reversibilidad
        time.sleep(2)
        self.browser.find_element_by_name('pondProbabilidad').send_keys(50) #agregamos la ponderacion de la probabilidad
        time.sleep(2)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(2)
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()

        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(4)

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
        self.browser.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        time.sleep(4)
        self.browser.find_element_by_name('pondIntensidad').send_keys(20) #agregamos la ponderacion de la intensidad
        time.sleep(2)
        self.browser.find_element_by_name('pondExtension').send_keys(20) #agregamos la ponderacion de la extension
        time.sleep(2)
        self.browser.find_element_by_name('pondDuracion').send_keys(30)  #agregamos la ponderacion de la duracion
        time.sleep(2)
        self.browser.find_element_by_name('pondReversibilidad').send_keys(10) #agregamos la ponderacion de la reversibilidad
        time.sleep(2)
        self.browser.find_element_by_name('pondProbabilidad').send_keys(20) #agregamos la ponderacion de la probabilidad
        time.sleep(2)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(2)
        confirmacion = self.browser.switch_to.alert #para las alertas del navegador
        time.sleep(2)
        confirmacion.accept()
        time.sleep(4)
        self.browser.find_element_by_name('nombre').clear()
        time.sleep(2)
        self.browser.find_element_by_name('nombre').send_keys('Impacto 5') #agregamos el nombre no repetido
        time.sleep(2)
        self.browser.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        time.sleep(4)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(4)
        confirmacion.accept()

        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(5)

        #Visualizando los datos del impacto 1 y modificandolos
        consulta = Estudio.objects.get(nombre=nombre_uno)
        time.sleep(2)
        self.browser.find_element_by_name(str(consulta.id)).click() # Hacemos click para consultar
        time.sleep(5)
        self.browser.execute_script("window.scrollTo(0, 720)") #movemos el scroll un poco
        time.sleep(10)
        self.browser.execute_script("window.scrollTo(0, 0)") #movemos el scroll un poco
        time.sleep(2)
        self.browser.find_element_by_name('nombre').clear()
        time.sleep(2)
        self.browser.find_element_by_name('nombre').send_keys("Este es un nuevo nombre") #agregamos el nombre
        time.sleep(3)
        self.browser.execute_script("window.scrollTo(0, 1080)") #movemos el scroll un poco
        time.sleep(5)
        self.browser.find_element_by_name('pondExtension').clear()
        time.sleep(2)
        self.browser.find_element_by_name('pondExtension').send_keys(0) #agregamos la ponderacion de la extension
        time.sleep(2)
        self.browser.find_element_by_name('pondDuracion').clear()
        time.sleep(2)
        self.browser.find_element_by_name('pondDuracion').send_keys(20)  #agregamos la ponderacion de la duracion
        time.sleep(2)
        self.browser.find_element_by_name('pondReversibilidad').clear()
        time.sleep(2)
        self.browser.find_element_by_name('pondReversibilidad').send_keys(40) #agregamos la ponderacion de la reversibilidad
        time.sleep(2)
        self.browser.find_element_by_name('editar').click() # Hacemos click en agregar
        time.sleep(4)
        confirmacion.accept()

        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(5)

        #Consultando los datos cambiados y Eliminando el impacto 1 cambiado
        self.browser.find_element_by_name(str(consulta.id)).click() # Hacemos click para consultar
        time.sleep(3)
        self.browser.execute_script("window.scrollTo(0, 1080)") #movemos el scroll un poco
        time.sleep(7)
        self.browser.find_element_by_name('eliminar').click() # Hacemos click en agregar
        time.sleep(4)
        confirmacion.accept()

        self.browser.get('%s%s' % (self.live_server_url, '/configuracion/index/'))
        time.sleep(10)