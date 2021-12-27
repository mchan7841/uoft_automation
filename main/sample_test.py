"""Sample python script for recreation"""
import yaml
import datetime
from selenium import webdriver
from ucheck import ucheck
from recreation import sport_rec
from website_login import uoft_login

DAYS = 2
TIMEOUT = 5

with open("login.yml", "r") as stream:
    try:
        conf = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

utorid = conf['uoft_user']['utorid']
password = conf['uoft_user']['password']

driver = webdriver.Chrome()

uoft_login(utorid, password, driver, TIMEOUT)
ucheck(driver, TIMEOUT)
sport_rec("url", datetime.datetime(2021, 12, 28, 17, 0), 50, driver, TIMEOUT)

# Add check for failed registration (Timeslot doesn't exist or HTML 500 errors)
