"""Helper functions for finding web elements"""

import string
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def check_by_id(element_id: string, timeout: int, driver: webdriver) -> None:
    """
    Check an element is present when searching by element id
    :param driver: The webdriver
    :param element_id: The id the driver uses to find the element
    :param timeout: How long the driver looks for the element before displaying the timeout message
    """
    try:
        element_present = EC.presence_of_element_located((By.ID, element_id))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")


def check_by_xpath(path: string, timeout: int, driver: webdriver) -> None:
    """
    Check an element is present when searching by xpath
    :param driver: The webdriver
    :param path: The path of the element
    :param timeout: How long the driver looks for the element before displaying the timeout message
    """
    try:
        element_present = EC.presence_of_element_located((By.XPATH, path))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
