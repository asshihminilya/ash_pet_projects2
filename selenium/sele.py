from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
# ваши опции здесь
options.add_experimental_option('detach', True)
service = Service("C:\\Users\\assh.dev\\PycharmProjects\\Task\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://stepik.org/lesson/761647/step/2?auth=login&unit=763770")
