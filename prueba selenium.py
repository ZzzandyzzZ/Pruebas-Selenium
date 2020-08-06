import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  #Acciones en objetos
from selenium.webdriver.common.by import By  #Opciones de busqueda
from selenium.webdriver.support.ui import WebDriverWait #condiciones
from selenium.webdriver.support import expected_conditions as EC #WaitKeys
from selenium.webdriver.support.ui import Select  #Opciones de seleccion
from selenium.webdriver import ActionChains #HoverAcion
import time
import cv2
path=r"E:\Programas\drivers\chromedriver_win32\chromedriver.exe"
test="login_test."
##driver= webdriver.Chrome(executable_path=path)
class login_test(unittest.TestCase):
    def setUp(self):
        self.driver=driver= webdriver.Chrome(executable_path=path)
        
    @unittest.skip("Saltando prueba")
    def test_buscar(self):
        driver=self.driver
        driver.get("http:\\www.google.com")
        self.assertIn("Google",driver.title)
        el=driver.find_element_by_name("q")
        el.send_keys("andy")
        el.send_keys(Keys.RETURN)
        time.sleep(2)
##        print(driver.page_source),
        assert "No se encontro el elemento" not in driver.page_source
  
    def test_navegar_pestañas(self):
        driver=self.driver
        driver.get("http:\\www.google.com")
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        driver.get("http:\\www.facebook.com")
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)
    
    def test_avanzar_retroceder_pagina(self):
        driver=self.driver
        driver.get("http:\\www.google.com")
        time.sleep(2)
        driver.get("http:\\www.facebook.com")
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.forward()
        
    def test_explicit_wait(self):
        driver = self.driver
        driver.get("http:\\www.google.com")
        try:
            element=WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.NAME,"q")))
##            element=driver.find_element_by_name("q")
        finally:
            print("TERMINO")

    def test_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("http:\\www.google.com")
        myDynamicElement=driver.find_element_by_name("q")

    def test_guardar_capturas(self):
        driver=self.driver
        driver.get("http:\\www.google.com")
        driver.save_screenshot("img2.png")
        time.sleep(3)
        
    def test_comparar_imagenes(self):
        img1=cv2.imread("img1.png")
        img2=cv2.imread("img2.png")
        diferencia = cv2.absdiff(img1,img2)
        gris = cv2.cvtColor(diferencia,cv2.COLOR_BGR2GRAY)
        contours,_ = cv2.findContours(gris,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            if(cv2.contourArea(c)>=20):
                posicion_x,posicion_y,ancho,alto=cv2.boundingRect(c)
                cv2.rectangle(img1,(posicion_x,posicion_y),(posicion_x+ancho,posicion_y+alto),(0,0,255),2)
        while(1):
            cv2.imshow("img1",img1)
            cv2.imshow("img2",img2)
            cv2.imshow("diferencia",diferencia)
            teclado=cv2.waitKey(5) & 0xFF
            if(teclado ==27):
                break
        cv2.destroyAllWindows()
                
    def test_mover_toggle(self):
        driver=self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")
        time.sleep(3)
        toggle=driver.find_element_by_xpath("//*[@id='main']/label[3]/div")
        toggle.click()
        time.sleep(3)
        toggle.click()
        time.sleep(3)

    def test_interactuar_select(self):
        driver=self.driver
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        select=driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select")
        time.sleep(3)
        option=select.find_elements_by_tag_name("option")
        time.sleep(3)
        for op in option:
            print(op.get_attribute("value"))
            op.click()
        seleccionar =Select(driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select"))
        seleccionar.select_by_value("5")
        time.sleep(2)
        
    def test_usar_radio_button(self):
        driver=self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
        time.sleep(2)
        radio=driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[4]")
        radio.click()
        time.sleep(2)
        radio=driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[3]")
        radio.click()
        time.sleep(2)

    def test_usar_hover_action(self):
        driver=self.driver
        driver.get("http:\\www.google.com")
        element=driver.find_element_by_link_text("Privacidad")
        hover= ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(3)

    def test_displayed_element(self):
        driver=self.driver
        driver.get("http:\\www.google.com")
        display=driver.find_element_by_name("btnI")
        print(display.is_displayed())
        print(display.is_enabled())

    def test_automatizar_hiperlink(self):
        driver=self.driver
        driver.get("http:\\www.w3schools.com")
        time.sleep(3)
        encontrar_link=driver.find_element_by_xpath("//*[@id='mySidenav']/div/a[29]")
        encontrar_link.click()
        
    def  test_css_selector(self):
        driver=self.driver
        driver.get("https://www.w3schools.com/html/")
        content=driver.find_element_by_css_selector("a.w3-blue")
        time.sleep(2)
        content.click()
        time.sleep(2)

##    def test_recuperar_datos_busqueda(self):
        
    
    def test_login(self):
        driver=self.driver
        driver.get("http:\\127.0.0.1:8000")
        self.assertIn("Talleres Ñaca",driver.title)
        ingresar=driver.find_element_by_xpath("//*[@id='navbar']/ul/li[6]/a")
        ingresar.click()
        time.sleep(3)
        user=driver.find_element_by_xpath("/html/body/div/div/div/form/div[2]/input")
        user.send_keys("ZzzandyzzZ")
        user=driver.find_element_by_xpath("/html/body/div/div/div/form/div[3]/input")
        user.send_keys("123")
        user.send_keys(Keys.RETURN)
        alert = driver.switch_to.alert
        msj=alert.text
        alert.accept()
        assert "Usuario o contraseña incorrectos" in msj      
        time.sleep(3)
##        assert "Estas en el lugar indicado" in driver.page_source
        
    def tearDown(self):
        self.driver.quit()



if __name__=='__main__':
    test+="test_login"
    unittest.main(defaultTest=test)
