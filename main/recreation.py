""" Signing up for university of toronto recreation programs"""
from selenium import webdriver
import yaml
import time
from selenium.webdriver.common.by import By
import string

driver = webdriver.Chrome()


def auto(url: string) -> None:
    """
    Register for a selected program based on the url and date entered.
    """
    driver.get(url)
    driver.find_element(By.ID, 'loginLink').click()
    driver.find_element(By.CLASS_NAME,
                        'btn btn-primary btn-block btn-external-login btn-sign-in '
                        'btn-sso-shibboleth')
