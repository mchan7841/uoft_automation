""" Ucheck """
import time
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from helper import check_by_class
from helper import check_by_xpath


def ucheck(driver: webdriver, timeout: int) -> None:
    """
    If someone has not had any symptoms of COVID-19 or been in close contact with anyone with
    COVID-19, automatically fill out ucheck.
    """
    driver.get("https://ucheck.utoronto.ca/")
    check_by_class("MuiButton-label", timeout, driver)
    time.sleep(0.5)
    driver.find_element(By.CLASS_NAME, "MuiButton-label").click()
    check_by_xpath("//*[contains(text(), 'Yes')]", timeout, driver)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Yes')]").click()
    time.sleep(0.5)
    ucheck_button("//div[@id= 'ebdd2acd-87ff-47aa-a7d2-059677987580-noFocus']"
                  "//label[@class = 'sc-paWCZ gCjDTA']", timeout, driver)
    ucheck_button("//div[@id= '5c2a5703-ce69-40aa-bf5a-5ddd81335aa9-noFocus']"
                  "//label[@class = 'sc-paWCZ gCjDTA']", timeout, driver)
    ucheck_button("//div[@id= '296a215c-8f44-4ca0-b2bc-6861ddabec3b-noFocus']"
                  "//label[@class = 'sc-paWCZ gCjDTA']", timeout, driver)
    ucheck_button("//div[@id= 'c2a1ba3f-0113-49a6-95cc-aeede171963a-noFocus']"
                  "//label[@class = 'sc-paWCZ gCjDTA']", timeout, driver)
    ucheck_button("//div[@id= '11985099-8548-4dc6-944f-bb4ea9c9494b-noFocus']"
                  "//label[@class = 'sc-paWCZ gCjDTA']", timeout, driver)
    ucheck_button("//div[@id= '156f6b12-1f8a-491c-9261-2dd73aef9d6a-noFocus']"
                  "//label[@class = 'sc-paWCZ gCjDTA']", timeout, driver)
    ucheck_button("//div[@id= '801d8c6a-6523-437e-bb6d-fa4092dacab1-noFocus']"
                  "//label[@class = 'sc-paWCZ gCjDTA']", timeout, driver)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Submit')]").click()


def ucheck_button(path: string, timeout: int, driver: webdriver) -> None:
    """
    Checks a ucheck button based on a path
    :param path: The path of the element
    :param timeout: The timeout in seconds
    :param driver: The webdriver
    """
    check_by_xpath(path, timeout, driver)
    time.sleep(0.5)
    driver.find_element(By.XPATH, path).click()
