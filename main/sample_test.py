"""Sample python script for recreation"""

import yaml
import datetime
from selenium import webdriver
from website_login import uoft_login
from recreation import sport_rec

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
sport_rec("https://recreation.utoronto.ca/Program/GetProgramDetails?courseId=d2a36cd8-bbb1-488d-"
          "bdbd-6b7ed1302390&semesterId=0ceb5a30-42f1-4069-a97b-5e015b379e14",
          datetime.datetime(2021, 12, 28, 17, 0), 50, driver, TIMEOUT)
