"""Login """
import string
from selenium import webdriver
import yaml
import datetime
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 5

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
    check_by_id(usernameid, TIMEOUT)
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
    check_by_id("idBtn_Back", TIMEOUT)
    driver.find_element(By.ID, "idBtn_Back").click()


def hart_house(url: string, start: datetime, duration: int) -> None:
    """
    Register for a selected program at the hart house based on the url and date entered.\
    :param url
    :param start The start time of the program in the format of a datetime object
    :param duration The duration of the program in minutes
    """
    end = start + datetime.timedelta(minutes=duration)
    time_running = format_time(start) + ' - ' + format_time(end)
    driver.get("https://recreation.utoronto.ca/home/signin")
    check_by_xpath("//button[@title= 'UTORid login for faculty, staff and students']", TIMEOUT)
    time.sleep(1)
    WebDriverWait(driver, TIMEOUT) \
        .until(EC.element_to_be_clickable((By.XPATH, "//button[@title= 'UTORid login for faculty,"
                                                     " staff and students']"))).click()
    check_by_xpath("//button[@id = 'gdpr-cookie-accept']", TIMEOUT)
    driver.find_element(By.XPATH, "//button[@id = 'gdpr-cookie-accept']").click()
    driver.get(url)
    check_by_xpath("//div[@data-instance-times= '" + time_running + "']//button[@class = "
                                                                    "'btn btn-primary']", TIMEOUT)
    driver.find_element(By.XPATH, "//div[@data-instance-times= '" + time_running +
                        "']//button[@class = 'btn btn-primary']").click()
    check_by_xpath("//button[@id = 'checkoutButton']", TIMEOUT)
    driver.find_element(By.XPATH, "//button[@id = 'checkoutButton']").click()
    check_by_xpath("//button[@onclick = 'Submit()']", TIMEOUT)
    WebDriverWait(driver, TIMEOUT) \
        .until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick = 'Submit()']"))).click()
    print("You have successfully been signed up")


def sport_rec(url: string, start: datetime, duration: int) -> None:
    """
    Register for a selected program at the hart house based on the url and date entered.\
    :param url
    :param start The start time of the program in the format of a datetime object
    :param duration The duration of the program in minutes
    """
    end = start + datetime.timedelta(minutes=duration)
    time_running = format_time(start) + ' - ' + format_time(end)
    driver.get("https://recreation.utoronto.ca/home/signin")
    check_by_xpath("//button[@title= 'UTORid login for faculty, staff and students']", TIMEOUT)
    time.sleep(1)
    WebDriverWait(driver, TIMEOUT) \
        .until(EC.element_to_be_clickable((By.XPATH, "//button[@title= 'UTORid login for faculty,"
                                                     " staff and students']"))).click()
    check_by_xpath("//button[@id = 'gdpr-cookie-accept']", TIMEOUT)
    driver.find_element(By.XPATH, "//button[@id = 'gdpr-cookie-accept']").click()
    driver.get(url)
    check_by_xpath("//div[@data-instance-times= '" + time_running + "']//button[@class = "
                                                                    "'btn btn-primary']", TIMEOUT)
    driver.find_element(By.XPATH, "//div[@data-instance-times= '" + time_running +
                        "']//button[@class = 'btn btn-primary']").click()

    check_by_xpath("//button[@id= 'btnAccept']", TIMEOUT)
    time.sleep(1)
    WebDriverWait(driver, TIMEOUT) \
        .until(EC.element_to_be_clickable((By.XPATH, "//button[@id= 'btnAccept']"))).click()
    check_by_xpath("//button[@id = 'checkoutButton']", TIMEOUT)
    driver.find_element(By.XPATH, "//button[@id = 'checkoutButton']").click()
    check_by_xpath("//button[@onclick = 'Submit()']", TIMEOUT)
    WebDriverWait(driver, TIMEOUT) \
        .until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick = 'Submit()']"))).click()
    print("You have successfully been signed up")


def format_time(date_time: datetime) -> string:
    """
    A function that reformats datetime objects into a string usable to find the web element
    :param date_time: A datetime object
    :return: Returns the formatted date time object
    """
    str_date = date_time.strftime('%I:%M %p')
    if str_date[0] == '0':
        str_date = str_date[1:]
    return str_date


def check_by_id(element_id: string, timeout: int) -> None:
    """
    Check an element is present when searching by element id
    :param element_id: The id the driver uses to find the element
    :param timeout: How long the driver looks for the element before displaying the timeout message
    """
    try:
        element_present = EC.presence_of_element_located((By.ID, element_id))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")


def check_by_xpath(path: string, timeout: int) -> None:
    """
    Check an element is present when searching by xpath
    :param path: The path of the element
    :param timeout: How long the driver looks for the element before displaying the timeout message
    """
    try:
        element_present = EC.presence_of_element_located((By.XPATH, path))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")


uoft_login("username", "password")
sport_rec("https://recreation.utoronto.ca/Program/GetProgramDetails?courseId=d2a36cd8-bbb1-488d-"
          "bdbd-6b7ed1302390&semesterId=0ceb5a30-42f1-4069-a97b-5e015b379e14",
          datetime.datetime(2021, 12, 28, 17, 0), 50)
