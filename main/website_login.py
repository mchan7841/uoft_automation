"""Login """
import string
from selenium import webdriver
import yaml
import datetime
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


def program_time(url: string, start: datetime, duration: int) -> None:
    """
    Register for a selected program based on the url and date entered.
    """
    end = start + datetime.timedelta(minutes=duration)
    time_running = format_time(start) + ' - ' + format_time(end)
    driver.get("https://recreation.utoronto.ca/home/signin")
    time.sleep(2)
    # Click on a pop-up window
    driver.find_element(By.XPATH,
                        "//button[@title= 'UTORid login for faculty, staff and students']").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//button[@id = 'gdpr-cookie-accept']").click()
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@data-instance-times= '" + time_running +
                        "']//button[@class = 'btn btn-primary']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@id = 'checkoutButton']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@onclick = 'Submit()']").click()
    print("You have successfully been signed up")


def format_time(date_time: datetime) -> string:
    str_date = date_time.strftime('%I:%M %p')
    if str_date[0] == '0':
        str_date = str_date[1:]
    return str_date


uoft_login("username", "Technogull1443")
program_time("https://recreation.utoronto.ca/Program/GetProgramDetails?courseId"
             "=d02a8d46-e2d5-450b-90d9-de40a36d870c&semesterId=0ceb5a30-42f1-4069-a97b"
             "-5e015b379e14", datetime.datetime(2021, 12, 30, 19, 0), 60)
