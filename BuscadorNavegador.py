from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def realizar_busqueda_en_navegador(consulta):
    # Inicializar el controlador del navegador
    driver = webdriver.Chrome()

    try:
        # Abrir el navegador
        driver.get("https://www.google.com")
        
        # Encontrar el campo de busqueda por nombre 
        campo_busqueda = driver.find_element("name", "q")

        # Ingresar la consulta en el campo de busqueda
        campo_busqueda.send_keys(consulta)  

        # Presionar la tecla Enter
        campo_busqueda.send_keys(Keys.ENTER)

        # Esperar unos segundos
        time.sleep(10)

    finally:
        # Cerrar el navegador
        driver.quit()
