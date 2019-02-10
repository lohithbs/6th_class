import time

from selenium import webdriver
browser='chrome'
driver = webdriver.Chrome(executable_path="C:/Users/bsloh/PycharmProjects/s_class/drivers/chromedriver.exe")
driver.get('https://www.facebook.com')
driver.find_element_by_xpath("//input[@data-testid='royal_email']").send_keys("bslohith95@gmail.com")
driver.find_element_by_xpath("//input[@name='pass']").send_keys("123456789")
driver.find_element_by_xpath("//a[text()='Forgotten account?']").click()

