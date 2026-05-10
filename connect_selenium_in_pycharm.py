from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# Open the Urban Routes home page
driver.get(" https://cnt-fe3de25e-bce5-45ac-931e-33fb4b0cc01f.containerhub.tripleten-services.com ")

# Check url contains tripleten-services.com
assert "tripleten-services.com" in driver.current_url

# Close the browser
driver.quit()


