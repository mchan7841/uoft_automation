"""Login """
import string
from selenium import webdriver
import yaml
import datetime
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
    try:
        element_present = EC.presence_of_element_located((By.ID, usernameid))
        WebDriverWait(driver, TIMEOUT).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
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
    try:
        element_present = EC.presence_of_element_located((By.ID, "idBtn_Back"))
        WebDriverWait(driver, TIMEOUT).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
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
    try:
        element_present = EC.presence_of_element_located((By.XPATH,
                                                          "//button[@title= 'UTORid login for "
                                                          "faculty, staff and students']"))
        WebDriverWait(driver, TIMEOUT).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable((By.XPATH,
                                                                     "//button[@title= 'UTORid "
                                                                     "login for faculty, staff and "
                                                                     "students']"
                                                                     ))).click()
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[@id = "
                                                                    "'gdpr-cookie-accept']"))
        WebDriverWait(driver, TIMEOUT).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    driver.find_element(By.XPATH, "//button[@id = 'gdpr-cookie-accept']").click()
    driver.get(url)
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//div[@data-instance-times= '"
                                                          + time_running + "']//button[@class = "
                                                                           "'btn btn-primary']"))
        WebDriverWait(driver, TIMEOUT).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    driver.find_element(By.XPATH, "//div[@data-instance-times= '" + time_running +
                        "']//button[@class = 'btn btn-primary']").click()
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[@id ="
                                                                    " 'checkoutButton']"))
        WebDriverWait(driver, TIMEOUT).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    driver.find_element(By.XPATH, "//button[@id = 'checkoutButton']").click()
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[@onclick ="
                                                                    " 'Submit()']"))
        WebDriverWait(driver, TIMEOUT).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    # Error here (element not interactable)
    WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick "
                                                                               "= 'Submit()']"
                                                                     ))).click()
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
    try:
        element_present = EC.presence_of_element_located((By.XPATH,
                                                          "//button[@title= 'UTORid login for "
                                                          "faculty, staff and students']"))
        WebDriverWait(driver, TIMEOUT).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable((By.XPATH,
                                                                     "//button[@title= 'UTORid "
                                                                     "login for faculty, staff and "
                                                                     "students']"
                                                                     ))).click()
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[@id = "
                                                                    "'gdpr-cookie-accept']"))
        WebDriverWait(driver, TIMEOUT).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    driver.find_element(By.XPATH, "//button[@id = 'gdpr-cookie-accept']").click()
    driver.get(url)
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//div[@data-instance-times= '"
                                                          + time_running + "']//button[@class = "
                                                                           "'btn btn-primary']"))
        WebDriverWait(driver, TIMEOUT).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    driver.find_element(By.XPATH, "//div[@data-instance-times= '" + time_running +
                        "']//button[@class = 'btn btn-primary']").click()

    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[@id= 'btnAccept']"))
        WebDriverWait(driver, TIMEOUT).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    driver.find_element(By.XPATH, "//button[@id= 'btnAccept']").click()
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[@id ="
                                                                    " 'checkoutButton']"))
        WebDriverWait(driver, TIMEOUT).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    driver.find_element(By.XPATH, "//button[@id = 'checkoutButton']").click()
    try:
        element_present = EC.presence_of_element_located((By.XPATH, "//button[@onclick ="
                                                                    " 'Submit()']"))
        WebDriverWait(driver, TIMEOUT).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    # Error here (element not interactable)
    WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick "
                                                                               "= 'Submit()']"
                                                                     ))).click()
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


uoft_login("username", "password")
sport_rec("https://recreation.utoronto.ca/Program/GetProgramDetails?courseId=d2a36cd8-bbb1"
          "-488d-bdbd-6b7ed1302390&semesterId=0ceb5a30-42f1-4069-a97b-5e015b379e14",
          datetime.datetime(2021, 12, 28, 18, 0), 50)
