from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

driver = webdriver.Firefox()
driver.get("https://notion.so")
assert "Notion" in driver.title
login_button = None
try:
    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="notion-app"]/div/div[1]/div[1]/div/nav/div[5]/a[1]')))
except Exception as e:
    logging.exception(e)
    driver.close()

if login_button is None:
    driver.close()
else:
    login_button.click()
