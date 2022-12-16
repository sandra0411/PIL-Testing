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

userIconLogin= driver.find_element(By.XPATH, "/html/body/header/nav/div[4]/div[3]/div[1]/a").click()
time.sleep(5)

#Verificamos que el logueo fue exitoso

mesaggeRequirement = ()     #Expected Result
mesaggeObtained = ()      #Actual Result

def compareMessages():
    if mesaggeRequirement in mesaggeObtained:
        print("Pass--------")
    else:
        print("Fail--------")

pageMessage= driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/p[1]").text
print('pageMessage: ' + pageMessage)
mesaggeObtained = pageMessage

mesaggeRequirement= 'sandradivan4'

compareMessages()
time.sleep(2)

#Realizamos la búsqueda de un producto
searchIcon = driver.find_element(By.XPATH, "/html/body/header/nav/div[4]/div[3]/div[1]/span[1]").click()
time.sleep(2)

inputSearch = driver.find_element(By.ID, "search")
inputSearch.send_keys('Buzo Oversize')
inputSearch.send_keys(Keys.ENTER)
time.sleep(3)

#Comprobamos que el primer resultado obtenido coincide con la búsqueda realizada

productRequirement = ()     #Expected Result
productObtained = ()      #Actual Result

def compareProducts():
    if productRequirement in productObtained:
        print("Pass--------")
    else:
        print("Fail--------")


firstResultText= driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[2]/ul/li[1]/div/div[2]/h2").text

print('firstResultText: ' + firstResultText)
productObtained = firstResultText

productRequirement= 'Buzo Oversize'

compareProducts()
time.sleep(2)

driver.close()