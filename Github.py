# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
import time

# this is main function
def main():
    service = Service(executable_path="./chromedriver")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://github.com/login')
    email = driver.find_element("xpath", '//*[@id="login_field"]')
    email.send_keys('Your Email Address')
    password = driver.find_element("xpath", '//*[@id="password"]')
    password.send_keys('Your Password')
    submit = driver.find_element("xpath", '//*[@name="commit"]')
    submit.click()
    time.sleep(1000)

if __name__ == '__main__':
    main()
