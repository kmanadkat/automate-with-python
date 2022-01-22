from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://www.google.com/intl/en_in/earth/'

driver = webdriver.Chrome()
driver.get(URL)

wait = WebDriverWait(driver, 10)
launchEarthButton = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[3]/div/a')
)) 
launchEarthButton.click()