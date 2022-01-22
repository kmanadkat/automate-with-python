from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Driver
driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

# Fill Form
usernameField = driver.find_element(By.XPATH, '//*[@id="user-name"]')
usernameField.send_keys('standard_user')
passwordField = driver.find_element(By.XPATH, '//*[@id="password"]')
passwordField.send_keys('secret_sauce')

# Click Login Button
loginButton = driver.find_element(By.XPATH, '//*[@id="login-button"]')
loginButton.click()