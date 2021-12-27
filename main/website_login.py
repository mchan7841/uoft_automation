"""Login """
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from helper import check_by_id


def login(url: string, usernameid: string, username: string, passwordid: string,
          password: string, submitid: string, driver: webdriver, timeout: int) -> None:
    """
    Basic login function.
    :param timeout: Search timeout for web elements
    :param driver: The webdriver
    :param url: Url of the website
    :param usernameid: Element id of the username field
    :param username: The users username
    :param passwordid: Element id of the password field
    :param password: The users password
    :param submitid: The element id of the submit button
    """
    driver.get(url)
    check_by_id(usernameid, timeout, driver)
    driver.find_element(By.ID, usernameid).send_keys(username)
    driver.find_element(By.ID, passwordid).send_keys(password)
    driver.find_element(By.NAME, submitid).click()


def uoft_login(utorid: string, password: string, driver: webdriver, timeout: int) -> None:
    """
    A function that logs a user into their University of Toronto account
    :param timeout: Search timeout for web elements
    :param driver: The webdriver
    :param driver: The webdriver
    :param utorid: The users utorid
    :param password: The users password
    """
    url = "https://mail.utoronto.ca/"
    usernameid = "username"
    passwordid = "password"
    submitid = "_eventId_proceed"
    login(url, usernameid, utorid, passwordid, password, submitid, driver, timeout)
    check_by_id("idBtn_Back", timeout, driver)
    driver.find_element(By.ID, "idBtn_Back").click()
