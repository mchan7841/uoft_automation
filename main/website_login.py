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


def login(url, usernameid, username, passwordid, password, submitid):
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.ID, usernameid).send_keys(username)
    driver.find_element(By.ID, passwordid).send_keys(password)
    driver.find_element(By.NAME, submitid).click()


def uoft_login(utorid, password):
    url = "https://mail.utoronto.ca/"
    usernameid = "username"
    passwordid = "password"
    submitid = "_eventId_proceed"
    login(url, usernameid, utorid, passwordid, password, submitid)
    time.sleep(4)
    driver.find_element(By.ID, "idBtn_Back").click()
