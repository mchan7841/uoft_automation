""" Signing up for university of toronto recreation programs"""
from selenium import webdriver
import string
import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

TIMEOUT = 5


def program_time(url: string, start: datetime, duration: int) -> None:
    """
    Register for a selected program based on the url and date entered.
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
    driver.find_element(By.XPATH,
                        "//button[@title= 'UTORid login for faculty, staff and students']").click()
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

def format_time(date_time: datetime) -> string:
    str_date = date_time.strftime('%I:%M %p')
    if str_date[0] == '0':
        str_date = str_date[1:]
    return str_date
