from selenium import webdriver
import data
import helpers
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            cls.driver.get(data.URBAN_ROUTES_URL)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_select_supportive_plan(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from_address(data.ADDRESS_FROM)
        routes_page.set_to_address(data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.selecting_supportive_plan()
        assert routes_page.active_selection_value == 'Supportive'

    def test_set_route(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from_address(data.ADDRESS_FROM)
        routes_page.set_to_address(data.ADDRESS_TO)


    def test_fill_in_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from_address(data.ADDRESS_FROM)
        routes_page.set_to_address(data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.selecting_supportive_plan()
        routes_page.filling_phone_number()
        code = helpers.retrieve_phone_code(self.driver)
        routes_page.phone_code(code)
        routes_page.final_taxi_order()

    def test_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from_address(data.ADDRESS_FROM)
        routes_page.set_to_address(data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.selecting_supportive_plan()
        routes_page.adding_credit_card()
        routes_page.click_link_button()

    def test_write_message_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from_address(data.ADDRESS_FROM)
        routes_page.set_to_address(data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.selecting_supportive_plan()
        routes_page.writing_driver_comment()
        message = routes_page.writing_driver_comment()
        assert message == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from_address(data.ADDRESS_FROM)
        routes_page.set_to_address(data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        routes_page.selecting_supportive_plan()
        routes_page.order_blanket_and_handkerchiefs()
        assert routes_page.order_blanket_and_handkerchiefs()

    def test_order_2_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from_address(data.ADDRESS_FROM)
        routes_page.set_to_address(data.ADDRESS_TO)
        routes_page.selecting_supportive_plan()
        routes_page.filling_phone_number()
        routes_page.adding_credit_card()
        routes_page.writing_driver_comment()
        routes_page.order_blanket_and_handkerchiefs()
        for number in range(2):
            routes_page.ordering_ice_cream()
        assert routes_page.ordering_ice_cream() == "2"

    def test_the_car_search_modal_appears(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from_address(data.ADDRESS_FROM)
        routes_page.set_to_address(data.ADDRESS_TO)
        routes_page.selecting_supportive_plan()
        routes_page.filling_phone_number()
        routes_page.adding_credit_card()
        routes_page.writing_driver_comment()
        routes_page.order_blanket_and_handkerchiefs()
        routes_page.ordering_ice_cream()
        routes_page.final_taxi_order()
        assert routes_page.final_taxi_order()
