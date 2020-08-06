import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #condiciones
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

import time
import cv2
path=r"E:\Programas\drivers\chromedriver_win32\chromedriver.exe"
test="login_test."
##driver= webdriver.Chrome(executable_path=path)
class login_test(unittest.TestCase):
    def setUp(self):
        self.driver=driver= webdriver.Chrome(executable_path=path)

    def test_registro_pabellon(self):
        driver=self.driver
        driver.get("file:///C:/Users/acer/Desktop/PruebaGitHub-master/PruebaGitHub-master/index.html")
        time.sleep(2)
        distribucion=driver.find_element_by_xpath("//*[@id='navbarNav2']/ul/li[3]/a")
        distribucion.click()
        time.sleep(2)
        opciones= driver.find_element_by_xpath("//*[@id='lateI']/nav[1]/button")
        opciones.click()
        registro=driver.find_element_by_xpath("//*[@id='navbarNav']/ul/li[1]/a")
        registro.click()
        driver.implicitly_wait(3)
        try:
            pabellon=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"pabellonR")))
        finally:    
            pabellon.send_keys("Quimica")
        try:
            Guardero=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"GuarderoR")))
        finally:    
            Guardero.send_keys("Jorge Ramires")
        try:
            Telefono=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"TelefonoR")))
        finally:    
            Telefono.send_keys("959506010")
        try:
            nuevo=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"NuevoRP")))
        finally:    
            nuevo.click()
        driver.implicitly_wait(3)
        time.sleep(2)
        assert "Quimica" in driver.page_source
    def test_actualizar_pabellon(self):
        driver=self.driver
        driver.get("file:///C:/Users/acer/Desktop/PruebaGitHub-master/PruebaGitHub-master/index.html")
        time.sleep(2)
        distribucion=driver.find_element_by_xpath("//*[@id='navbarNav2']/ul/li[3]/a")
        distribucion.click()
        time.sleep(2)
        opciones= driver.find_element_by_xpath("//*[@id='lateI']/nav[1]/button")
        opciones.click()
        registro=driver.find_element_by_xpath("//*[@id='navbarNav']/ul/li[1]/a")
        registro.click()
        driver.implicitly_wait(3)
        try:
            buscar=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"pabellonR")))
            option=buscar.find_elements_by_tag_name("option")
        finally:    
            for op in option:
                if(op.get_attribute("value")=="Quimica"):
                    op.click()
            
        modificar=driver.find_element_by_name("ModificarRP")
        modificar.click()   
        try:
            Guardero=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"GuarderoR")))
        finally:
            Guardero.clear()
            Guardero.send_keys("Jorge Perez")
        guardar=driver.find_element_by_name("GuardarRP")
        guardar.click()  
        time.sleep(3)
        
        assert "Jorge Perez" in driver.page_source
        assert "Jorge Ramires" not in driver.page_source
    def test_eliminar_pabellon(self):
        driver=self.driver
        driver.get("file:///C:/Users/acer/Desktop/PruebaGitHub-master/PruebaGitHub-master/index.html")
        time.sleep(2)
        distribucion=driver.find_element_by_xpath("//*[@id='navbarNav2']/ul/li[3]/a")
        distribucion.click()
        time.sleep(2)
        opciones= driver.find_element_by_xpath("//*[@id='lateI']/nav[1]/button")
        opciones.click()
        registro=driver.find_element_by_xpath("//*[@id='navbarNav']/ul/li[1]/a")
        registro.click()
        driver.implicitly_wait(3)
        try:
            buscar=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"pabellonR")))
            option=buscar.find_elements_by_tag_name("option")
        finally:    
            for op in option:
                if(op.get_attribute("value")=="Quimica"):
                    op.click()
            
        modificar=driver.find_element_by_name("ModificarRP")
        modificar.click()   
        eliminar=driver.find_element_by_name("EliminarRP")
        eliminar.click()  
        time.sleep(3)
        
        assert "Jorge Perez" not in driver.page_source
    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    test+="test_eliminar_pabellon"
    unittest.main(defaultTest=test)






    
