""" Signing up for university of toronto recreation programs"""
import time
import string
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from helper import check_by_xpath


def registration(url: string, start: datetime, duration: int, driver: webdriver, timeout: int) -> \
        None:
    """
        Register for a selected program
        :param timeout: How long the webdriver will search for web elements
        :param driver: The webdriver
        :param url The url of the program of target enrollment
        :param start The start time of the program in the format of a datetime object
        :param duration The duration of the program in minutes
        """
    end = start + datetime.timedelta(minutes=duration)
    time_running = format_time(start) + ' - ' + format_time(end)
    driver.get("https://recreation.utoronto.ca/home/signin")
    check_by_xpath("//button[@title= 'UTORid login for faculty, staff and students']", timeout,
                   driver)
    time.sleep(1)
    WebDriverWait(driver, timeout) \
        .until(EC.element_to_be_clickable((By.XPATH, "//button[@title= 'UTORid login for faculty,"
                                                     " staff and students']"))).click()
    check_by_xpath("//button[@id = 'gdpr-cookie-accept']", timeout, driver)
    driver.find_element(By.XPATH, "//button[@id = 'gdpr-cookie-accept']").click()
    driver.get(url)
    check_by_xpath("//div[@data-instance-times= '" + time_running + "']//button[@class = "
                                                                    "'btn btn-primary']", timeout,
                   driver)
    driver.find_element(By.XPATH, "//div[@data-instance-times= '" + time_running +
                        "']//button[@class = 'btn btn-primary']").click()


def hart_house(url: string, start: datetime, duration: int, driver: webdriver, timeout: int) -> \
        None:
    """
    Checkout for a hrat house program.
    :param timeout: How long the webdriver will search for web elements
    :param driver: The webdriver
    :param url The url of the program of target enrollment
    :param start The start time of the program in the format of a datetime object
    :param duration The duration of the program in minutes
    """
    registration(url, start, duration, driver, timeout)
    check_by_xpath("//button[@id = 'checkoutButton']", timeout, driver)
    driver.find_element(By.XPATH, "//button[@id = 'checkoutButton']").click()
    check_by_xpath("//button[@onclick = 'Submit()']", timeout, driver)
    WebDriverWait(driver, timeout) \
        .until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick = 'Submit()']"))).click()
    print("You have successfully been signed up")


def sport_rec(url: string, start: datetime, duration: int, driver: webdriver, timeout: int) -> None:
    """
    Checkout for a sport & rec program.
    :param timeout: How long the webdriver will search for web elements
    :param driver: The webdriver
    :param url The url of the program of target enrollment
    :param start The start time of the program in the format of a datetime object
    :param duration The duration of the program in minutes
    """
    registration(url, start, duration, driver, timeout)
    check_by_xpath("//button[@id= 'btnAccept']", timeout, driver)
    time.sleep(1)
    WebDriverWait(driver, timeout) \
        .until(EC.element_to_be_clickable((By.XPATH, "//button[@id= 'btnAccept']"))).click()
    check_by_xpath("//button[@id = 'checkoutButton']", timeout, driver)
    driver.find_element(By.XPATH, "//button[@id = 'checkoutButton']").click()
    check_by_xpath("//button[@onclick = 'Submit()']", timeout, driver)
    WebDriverWait(driver, timeout) \
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
