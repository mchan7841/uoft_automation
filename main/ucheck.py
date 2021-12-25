from selenium import webdriver
import yaml
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def ucheck():
    driver.get("https://ucheck.utoronto.ca/")
    time.sleep(6)
    driver.find_element(By.CLASS_NAME, "MuiButton-label").click()
    time.sleep(3)
    driver.find_element(By.ID, 'root').click()
