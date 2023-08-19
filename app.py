from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


url = "https://selenium-python.readthedocs.io/locating-elements.html#locating-elements"

driver = webdriver.Chrome()
driver.get(url)

# titles = driver.find_elements(By.CLASS_NAME, 'section')

# list_of_titles = []

# for title in titles:
#     header = title.find_element(By.TAG_NAME, 'h2')
#     list_of_titles.append(header.text)


# print(list_of_titles)


link = driver.find_element(By.LINK_TEXT, '1. Installation')
link.click()

try:
    second_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'virtualenv'))
    )
    second_link.click()
except:
    driver.quit()


