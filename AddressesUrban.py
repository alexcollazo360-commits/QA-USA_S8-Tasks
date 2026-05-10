import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get(" SERVER URL ")

# Pause execution for 2 seconds to allow the page to load fully
time.sleep(2)

# Find the FROM field and fill it in
driver.find_element(By.ID, "from").send_keys("East 2nd Street, 601")

# Find the TO field and fill it in
driver.find_element(By.ID, "to").send_keys("1300 1st St")

time.sleep(2)

# Find the "Call a taxi" button and click on it
driver.find_element(By.XPATH, "//button[@class='button round']").click()

# Add an explicit wait for the field to load
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, "comment")))

# Write a comment to the driver
driver.find_element(By.ID, "comment").send_keys("Hello")

time.sleep(2)

# Check that your comment is what you expect it to be
assert driver.find_element(By.ID, "comment").get_attribute("value") == "Hello"

driver.quit()