from selenium import webdriver
import yaml
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def auto():
    driver.get('https://recreation.utoronto.ca/')
    driver.find_element(By.ID, 'loginLink').click()
    driver.find_element(By.CLASS_NAME,
                        'btn btn-primary btn-block btn-external-login btn-sign-in btn-sso-shibboleth')
