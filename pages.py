from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import data

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
class UrbanRoutesPage:
    url = "https://cnt-454f7ae7-680d-406d-9eda-09733da61cce.containerhub.tripleten-services.com"
    # Locators
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")
    call_taxi_button = (By.ID, "button")

def __init__(self, driver):
    self.driver = driver

def set_from_address(self, address):
    from_field = (By.ID, "from")
    pass

def set_to_address(self, address):
    to_field = (By.ID, "to")
    pass

def click_call_taxi_button(self):
    call_taxi_button = (By.XPATH, "//button[text()='Call a taxi']")
    pass

def selecting_supportive_plan(self):
    supportive_plan_option = self.driver.find_element(By.XPATH, "//div[@class='tcard active']")
    supportive_plan_option.click()


def filling_phone_number(self):
    from data import phone_number
    from helpers import retrieve_phone_code

    phone_number_field = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[1]")
    self.driver.find_element(*phone_number_field).click()
    self.driver.find_element(*phone_number_field).send_keys(phone_number)

    # Retrieve SMS verification code
    code = retrieve_phone_code()

    # Enter the code into confirmation field
    confirmation_field = (By.ID, "code")  # You'll need to find the correct locator
    self.driver.find_element(*confirmation_field).send_keys(code)

    # Assert that the phone number is properly reflected
    displayed_number = self.driver.find_element(*phone_number_field).get_attribute("value")
    assert displayed_number == phone_number


def Adding_credit_card(self):
    from data import card_number, card_code

    # Click on Payment Method
    payment_method = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/div[2]/div[3]")
    self.driver.find_element(*payment_method).click()

    # Click on Add Card
    add_card_button = (By.XPATH, "//div[text()='Add card']")
    self.driver.find_element(*add_card_button).click()

    # Enter valid Card Number
    card_number_field = (By.ID, "number")  # You need to find the correct locator
    self.driver.find_element(*card_number_field).send_keys(card_number)

    # Enter Card Code
    card_code_field = (By.ID, "code")  # You need to find the correct locator
    self.driver.find_element(*card_code_field).send_keys(card_code)

    # Use TAB to change focus from Code field
    from selenium.webdriver.common.keys import Keys
    self.driver.find_element(*card_code_field).send_keys(Keys.TAB)

    # Wait for Link button to become clickable
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    link_button = (By.XPATH, "//button[text()='Link']")
    wait = WebDriverWait(self.driver, 10)
    wait.until(EC.element_to_be_clickable(link_button))

    # Click Link button
    self.driver.find_element(*link_button).click()

    # Assert that payment method changed to "Card"
    payment_method_text = self.driver.find_element(*payment_method).text
    assert "Card" in payment_method_text


def Writing_driver_comment(self):
    from data import message_for_driver

    # Locate the comment input field
    comment_field = (By.ID, "comment")  # You need to find the correct locator

    # Click on the comment field and enter the custom message
    self.driver.find_element(*comment_field).click()
    self.driver.find_element(*comment_field).send_keys(message_for_driver)

    # Assert that the message is stored correctly
    entered_text = self.driver.find_element(*comment_field).get_attribute("value")
    assert entered_text == message_for_driver


def order_blanket_and_handkerchiefs(self):
    # Click on the "Add Blanket and Handkerchiefs" slider
    add_order_blanket_and_handkerchiefs_button = (By.XPATH,
                                                  '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    self.driver.find_element(*add_order_blanket_and_handkerchiefs_button).click()

    # Verify that the selection is confirmed using the correct assertion
    blanket_slider = self.driver.find_element(*add_order_blanket_and_handkerchiefs_button)
    is_checked = blanket_slider.get_property('checked')
    assert is_checked == True


def ordering_ice_cream(self):
    # Locate the ice cream plus button
    ordering_ice_cream_button = (By.XPATH,
                                 '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')

    # Use range() to add 2 ice creams using a loop
    for i in range(2):
        self.driver.find_element(*ordering_ice_cream_button).click()

    # Retrieve the count displayed
    ice_cream_counter = (By.XPATH,
                         "//div[contains(text(), 'Ice cream')]/..//div[contains(@class, 'counter')]")  # You need to find the correct locator
    displayed_count = self.driver.find_element(*ice_cream_counter).text

    # Assert that the displayed count matches 2
    assert displayed_count == "2"


def Final_taxi_order(self):
    final_taxi_order_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button')
    final_taxi_order_button.click()

    # Wait for and assert that the car search modal appears
    car_search_modal = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "order-body"))
    )
    assert car_search_modal.is_displayed()







