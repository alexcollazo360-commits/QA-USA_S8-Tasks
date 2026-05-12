import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import data
import helpers
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        # Your URL reachability check should be indented here
        if helpers.is_url_reachable(data.urban_routes_url):
            cls.driver.get(data.urban_routes_url)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_select_supportive_plan(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route()
        routes_page.click_call_taxi_button()
        routes_page.select_supportive_plan()
        selected_plan = routes_page.get_selected_plan_text()
        assert "Supportive" in selected_plan

    def test_set_route(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.ADDRESS_FROM)
        routes_page.set_to(data.ADDRESS_TO)

    def test_select_comfort_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route()
        routes_page.click_call_taxi_button()
        routes_page.select_supportive_plan()
        selected_plan = routes_page.get_selected_plan_text()
        assert "Supportive" in selected_plan

    def test_fill_in_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route()
        routes_page.click_call_taxi_button()
        routes_page.select_supportive_plan()
        routes_page.click_phone_number_field()
        routes_page.enter_phone_number(data.PHONE_NUMBER)
        routes_page.click_next_button()
        code = helpers.retrieve_phone_code(self.driver)
        routes_page.enter_phone_code(code)
        routes_page.click_confirm_button()

    def test_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route()
        routes_page.click_call_taxi_button()
        routes_page.select_supportive_plan()
        routes_page.click_payment_method()
        routes_page.click_add_card()
        routes_page.enter_card_number(data.CARD_NUMBER)
        routes_page.enter_card_code(data.CARD_CODE)
        routes_page.click_outside_modal()
        routes_page.click_link_button()

    def test_write_message_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route()
        routes_page.click_call_taxi_button()
        routes_page.select_supportive_plan()
        routes_page.enter_message_for_driver(data.MESSAGE_FOR_DRIVER)
        message = routes_page.get_message_for_driver()
        assert message == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route()
        routes_page.click_call_taxi_button()
        routes_page.select_supportive_plan()
        routes_page.click_blanket_and_handkerchiefs()
        assert routes_page.is_blanket_and_handkerchiefs_selected()

    def test_order_2_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route()
        routes_page.select_supportive_plan()
        routes_page.set_phone_number()
        routes_page.add_credit_card()
        routes_page.write_message_for_driver()
        routes_page.select_blanket_and_handkerchiefs()
        for number in range(2):
            routes_page.ordering_ice_cream()
        assert routes_page.get_ice_cream_counter() == "2"

    def test_the_car_search_modal_appears(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route()
        routes_page.select_supportive_plan()
        routes_page.set_phone_number()
        routes_page.add_credit_card()
        routes_page.write_message_for_driver()
        routes_page.select_blanket_and_handkerchiefs()
        routes_page.order_2_ice_creams()
        routes_page.click_order_button()
        assert routes_page.is_car_search_modal_visible()
