from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

PATH = ".\chromedriver.exe"
service = Service(executable_path=PATH)
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(2)

try:
    lang = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "langSelect-EN"))
    )
    lang.click()
except:
    driver.quit()

time.sleep(2)

try:
    cookie = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "bigCookie"))
    )
except:
    driver.quit()

try:
    cookie_count = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "cookies"))
    )
except:
    driver.quit()

time.sleep(2)

items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1,-1,-1)]

for i in range(5000):
    actions = ActionChains(driver)
    for i in range(10):
        actions.double_click(cookie)
    actions.perform()

    count = int(cookie_count.text.split(" ")[0].replace(',',''))
    for item in items:
        value = item.text
        if(count >= int(value.replace(',',''))):
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()

cookie.click()
time.sleep(10)
driver.quit()
