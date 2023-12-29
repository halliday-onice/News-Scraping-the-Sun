from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

website = "https://g1.globo.com/economia"
path = "/opt/homebrew/bin/chromedriver"

service = Service(executable_path = path)
driver = webdriver.Chrome(service = service)

driver.get(website)

#command + shift + c - localiza pelo cursor o item da página
containers = WebDriverWait(driver, 10).until(
     EC.presence_of_all_elements_located((By.XPATH,'//span[@class="bstn-hl-title gui-color-primary gui-color-hover gui-color-primary-bg-after"]'))
)

#containers = driver.find_elements(by = "xpath", value = '//div[@class = "teaser__copy-container"]')
if containers:
    print('found')
    print(containers)


driver.quit()