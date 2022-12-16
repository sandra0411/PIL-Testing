import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.maximize_window()

driver.get('https://deliverind.com.ar/')
time.sleep(3)

#Nos logueamos
userIcon= driver.find_element(By.XPATH, "/html/body/header/nav/div[4]/div[3]/div[1]/span[2]/i")
userIcon.click()
time.sleep(2)

userName= driver.find_element(By.ID, "username")
password= driver.find_element(By.ID, "password")
accederButton= driver.find_element(By.XPATH, "/html/body/header/div[2]/div/div/div[2]/div[1]/form/p[3]/button")

userName.send_keys('sandradivan4')
password.send_keys('Testeand0--')
accederButton.click()
time.sleep(5)

#Ingresamos a Catálogo
linkCatalogo= driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/section[1]/div/div/div/div/div/div[7]/div/div/a").click()
time.sleep(1)

#Ingresamos a Buzos
linkBuzos= driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[2]/section/div/div[1]/a").click()
time.sleep(1)

#Seleccionamos el Buzzo Hoddie Oversize sin especificar talle y color
buzoHoddie= driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[2]/ul/li[3]/div/div[1]/a").click()
time.sleep(3)

añadirButton= driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[3]/div[3]/form/div/div/div[2]/button").click()
time.sleep(2)

#Validamos que salta un alert con el mensaje requerido

alertMesaggeRequirement = ()     #Expected Result
alertMesaggeObtained = ()      #Actual Result

def compareMessages():
    if alertMesaggeRequirement in alertMesaggeObtained:
        print("Pass----------")
    else:
        print("Fail----------")

alertText= Alert(driver).text
print('alertText: '+ alertText)
alertMesaggeObtained= alertText

alertMesaggeRequirement= 'Elige las opciones del producto antes de añadir este producto a tu carrito.'

compareMessages()
time.sleep(2)




