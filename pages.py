from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import data

class UrbanRoutesPage:
    # Locators
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")
    call_taxi_button = (By.ID, "button")
    supportive_plan_option = (By.XPATH, "//div[contains(text(), 'Supportive')])")
    payment_method = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/div[2]/div[3]")
    add_card_button = (By.XPATH, "//div[text()='Add card']")
    phone_number_field = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[1]")
    confirmation_field = (By.ID, "code")
    card_number_field = (By.ID, "number")
    card_code_field = (By.ID, "code")
    link_button = (By.XPATH, "//button[text()='Link']")
    comment_field = (By.ID, "comment")
    add_order_blanket_and_handkerchiefs_button = (By.XPATH,
                                                  '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    ordering_ice_cream_button = (By.XPATH,
                                 '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    ice_cream_counter = (By.XPATH,
                         "//div[contains(text(), 'Ice cream')]/..//div[contains(@class, 'counter')]")
    final_taxi_order_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button')
    active_plan = (By.XPATH, '//div[@class="tcard active"] //div[@class="tcard-title"]')
    phone_code = (By.ID,"code")



    def __init__(self, driver):
        self.driver = driver

    def click_link_button(self):
        self.driver.find_element(*self.link_button).click()


    def set_from_address(self,address):
        self.driver.find_element(*self.from_field).send_keys(address)

    def set_to_address(self,address):
        self.driver.find_element(*self.to_field).send_keys(address)

    def click_call_taxi_button(self):
        self.driver.find_element(*self.call_taxi_button).click()

    def input_phone_code(self,code):
        self.driver.find_element(*self.phone_code).click()

    def selecting_supportive_plan(self):
        self.driver.find_element(*self.supportive_plan_option).click()

    def filling_phone_number(self):
        from data import PHONE_NUMBER
        from helpers import retrieve_phone_code
        self.driver.find_element(*self.phone_number_field).click()
        self.driver.find_element(*self.phone_number_field).send_keys(PHONE_NUMBER)
        code = retrieve_phone_code(self)
        self.driver.find_element(*self.confirmation_field).send_keys(code)
        displayed_number = self.driver.find_element(*self.phone_number_field).get_attribute("value")
        assert displayed_number == PHONE_NUMBER


    def adding_credit_card(self):
        from data import CARD_NUMBER, CARD_CODE
        self.driver.find_element(*self.payment_method).click()
        self.driver.find_element(*self.add_card_button).click()
        self.driver.find_element(*self.card_number_field).send_keys(CARD_NUMBER)
        self.driver.find_element(*self.card_code_field).send_keys(CARD_CODE)
        from selenium.webdriver.common.keys import Keys
        self.driver.find_element(*self.card_code_field).send_keys(Keys.TAB)
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.element_to_be_clickable(*self.link_button))
        self.driver.find_element(*self.link_button).click()
        payment_method_text = self.driver.find_element(*self.payment_method).text
        assert "Card" in payment_method_text


    def writing_driver_comment(self):
        from data import MESSAGE_FOR_DRIVER
        self.driver.find_element(*self.comment_field).click()
        self.driver.find_element(*self.comment_field).send_keys(MESSAGE_FOR_DRIVER)
        entered_text = self.driver.find_element(*self.comment_field).get_attribute("value")
        assert entered_text == MESSAGE_FOR_DRIVER


    def order_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.add_order_blanket_and_handkerchiefs_button).click()
        blanket_slider = self.driver.find_element(*self.add_order_blanket_and_handkerchiefs_button)
        is_checked = blanket_slider.get_property('checked')
        assert is_checked == True


    def ordering_ice_cream(self):
        for i in range(2):
            self.driver.find_element(*self.ordering_ice_cream_button).click()
        displayed_count = self.driver.find_element(*self.ice_cream_counter).text
        assert displayed_count == "2"


    def final_taxi_order(self):
        self.driver.find_element(*self.final_taxi_order_button).click()
        car_search_modal = WebDriverWait(self.driver, 10).until(
        ec.visibility_of_element_located((By.CLASS_NAME, "order-body"))
    )
        assert car_search_modal.is_displayed()

    def active_selection_value(self):
        return self.driver.find_element(*self.active_plan).text
