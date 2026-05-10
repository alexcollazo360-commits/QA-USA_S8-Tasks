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
        # Create page object instance
        routes_page = UrbanRoutesPage(self.driver)

        # Set the "from" address
        routes_page.set_from_address("East 2nd Street, 601")

        # Set the "to" address
        routes_page.set_to_address("1300 1st St")

        # Click the "Call a Taxi" button
        routes_page.click_call_taxi_button()

        # Click on the Supportive plan option
        routes_page.click_supportive_plan()

        # Retrieve the active selection value
        selected_plan = routes_page.get_selected_plan_text()

        # Assert that the correct plan is selected
        assert "Supportive" in selected_plan
@classmethod
def teardown_class(cls):
    cls.driver.quit()

