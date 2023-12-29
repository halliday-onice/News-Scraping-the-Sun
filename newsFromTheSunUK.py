from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

website = "https://www.thesun.co.uk"
path = "/opt/homebrew/bin/chromedriver"

service = Service(executable_path = path)
driver = webdriver.Chrome(service = service)

driver.get(website)

#command + shift + c - localiza pelo cursor o item da página
containers = WebDriverWait(driver, 10).until(
     EC.presence_of_all_elements_located((By.XPATH,'//div[@class = "teaser__copy-container"]'))
)

#containers = driver.find_elements(by = "xpath", value = '//div[@class = "teaser__copy-container"]')
if containers:
    print('found')
titles = []
subtitles = []
links = []
for container in containers:
      title = container.find_element(by = "xpath", value = './/a').text
      subtitle = container.find_element(by = "xpath", value = './/h3').text

      link = container.find_element(by = "xpath", value = './/a').get_attribute("href")

      titles.append(title)
      subtitles.append(subtitle)
      links.append(link)


news_dict = {'Title': titles,'Subtitle': subtitles, 'Links': links}
df_headlines = pd.DataFrame(news_dict)
df_headlines.to_csv('HeadlineNews.csv')

driver.quit()