import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


options = Options()
#options.add_argument("--headless=new")  #режим без открытия браузера
options.add_experimental_option('detach', True)
service = Service("C:\\Users\\assh.dev\\PycharmProjects\\Task\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)



login = 'knauf@test.me'
password_knauf = 'Q12345678q'
base_url = "https://tms-master.stage.trucker.group"
driver.get(base_url) #url базовый
driver.implicitly_wait(10)


user_name = driver.find_element(by=By.XPATH, value='//*[@id="form_item_email"]') #Поиск поля логина
user_name.send_keys(login)
print('Input Login')

password = driver.find_element(by=By.XPATH, value='//input[@type="password"]') #Поиск поля пароля
password.send_keys(password_knauf)
print('Input password')

password.send_keys(Keys.ENTER) #имитация нажатия кнопки энтер

#warning = driver.find_element(by = By.XPATH, value = '//span[@data-autotest-id="sign-in-error"]')
#value_warning = warning.text

#assert value_warning == "Неверно указана эл. почта или пароль"
#print('Неверный пароль')

print('Autorithation OK')
driver.implicitly_wait(10)



orders = driver.find_element(by=By.XPATH, value = '//*[@id="app"]/section/div[1]/section/aside/div/div/div[1]/ul/li[1]/div/span/div/div[1]/span')
orders.click()
driver.implicitly_wait(10)
print('Переход к заказам')


new_orders = driver.find_element(by = By.XPATH, value = '//*[@id="app"]/section/div[1]/section/section/div/div[1]/div/div/span/div/button/span')
new_orders.click()
driver.implicitly_wait(10)

#driver.refresh() #обновление браузера



