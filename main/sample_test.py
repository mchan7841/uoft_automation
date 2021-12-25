from selenium import webdriver
import yaml
import time
from selenium.webdriver.common.by import By
import website_login
with open("login.yml", "r") as stream:
    try:
        conf = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

utorid = conf['uoft_user']['utorid']
password = conf['uoft_user']['password']

website_login.uoft_login(utorid, password)
