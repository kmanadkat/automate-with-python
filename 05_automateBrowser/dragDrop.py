from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 


URL = 'http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html'

# Initialize Driver
driver = webdriver.Chrome()
driver.get(URL)

# Define Source & Destination
source_1 = driver.find_element(By.XPATH, '//*[@id="box1"]')
dest_1 = driver.find_element(By.XPATH, '//*[@id="box101"]')

# Perform Drag n Drop
actions = ActionChains(driver)
actions.drag_and_drop(source_1, dest_1).perform()