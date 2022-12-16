import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
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

#Seleccionamos el Buzzo Hoddie Oversize, talle S/38 color Amarillo Camomille (puede pasar que se queden sin stock de un producto y por eso falla el código al buscar un elemento que ya no está)
buzoHoddie= driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[2]/ul/li[3]/div/div[1]/a").click()
time.sleep(3)

talleBuzo= driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[3]/div[3]/form/div/table/tbody/tr[1]/td/ul/li[5]/div").click()
colorBuzo= driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[3]/div[3]/form/div/table/tbody/tr[2]/td/ul/li[3]").click()
cantidadBuzos= driver.find_element(By.NAME, "quantity")
cantidadBuzos.clear()
cantidadBuzos.send_keys('3')
añadirButton= driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[3]/div[3]/form/div/div/div[2]/button").click()
time.sleep(2)

#Validamos presencia de mensaje que confirme que el producto se añadió exitosamente

successMesaggeRequirement = ()     #Expected Result
successMesaggeObtained = ()      #Actual Result

def compareMessages():
    if successMesaggeRequirement in successMesaggeObtained:
        print("Pass--------")
    else:
        print("Fail--------")

successMessage= driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div").text
print('successMessage: ' + successMessage)
successMesaggeObtained = successMessage

successMesaggeRequirement= 'Producto añadido con éxito'

compareMessages()
time.sleep(2)

#Nos dirigimos al carrito de compras
verCarritoButton= driver.find_element(By.XPATH, "/html/body/div[4]/div/div[3]/a[1]").click()
time.sleep(2)


#Validamos que el nombre, color y talle del producto que seleccionamos se encuentren detallados en el carrito de compras
chosenProductRequirement = ()     #Expected Result
chosenProductObtained = ()      #Actual Result

def compareMessages():
    if chosenProductRequirement in chosenProductObtained:
        print("Pass--------")
    else:
        print("Fail--------")

labelProduct= driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/form/table/tbody/tr[1]/td[3]/a").text
print('labelProduct: ' + labelProduct)
chosenProductObtained = labelProduct

chosenProductRequirement= 'Hoodie Oversize - S/38, Amarillo Camomille'

compareMessages()
time.sleep(2)

#Validamos que la cantidad del producto que seleccionamos se encuentre detallada en el carrito de compras


unitsProductRequirement = ()     #Expected Result
unitsProductObtained = ()      #Actual Result

def compareUnits():
    if unitsProductRequirement in unitsProductObtained:
        print("Pass--------")
    else:
        print("Fail--------")

unitsProduct= driver.find_element(By.XPATH, "//input[@title='Cantidad']").get_attribute("value")
print('unitsProduct: ' + unitsProduct)
unitsProductObtained = unitsProduct

unitsProductRequirement= '3'

compareUnits()
time.sleep(2)


#Seguimos comprando...
seguirComprandoButton = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[2]/div/div[2]/a").click()
time.sleep(2)
driver.close()





