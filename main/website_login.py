"""Login """
import string
from selenium import webdriver
import yaml
import time
from selenium.webdriver.common.by import By
with open("login.yml", "r") as stream:
    try:
        conf = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

utorid = conf['uoft_user']['utorid']
password = conf['uoft_user']['password']

driver = webdriver.Chrome()


def login(url: string, usernameid: string, username: string, passwordid: string,
          password: string, submitid: string) -> None:
    """
    Basic login function.
    :param url: Url of the website
    :param usernameid: Element id of the username field
    :param username: The users username
    :param passwordid: Element id of the password field
    :param password: The users password
    :param submitid: The element id of the submit button
    """
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.ID, usernameid).send_keys(username)
    driver.find_element(By.ID, passwordid).send_keys(password)
    driver.find_element(By.NAME, submitid).click()


def uoft_login(utorid: string, password: string) -> None:
    """
    A function that logs a user into their University of Toronto account
    :param utorid: The users utorid
    :param password: The users password
    """
    url = "https://mail.utoronto.ca/"
    usernameid = "username"
    passwordid = "password"
    submitid = "_eventId_proceed"
    login(url, usernameid, utorid, passwordid, password, submitid)
    time.sleep(4)
    driver.find_element(By.ID, "idBtn_Back").click()
