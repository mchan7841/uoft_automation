""" Signing up for university of toronto recreation programs"""
from selenium import webdriver
import yaml
import time
from selenium.webdriver.common.by import By
import string
import datetime
import calendar

driver = webdriver.Chrome()


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
