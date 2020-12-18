from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex
from driver import Driver
import allure
import os
import uuid

os_path = os.path.dirname(os.path.abspath(__file__)).replace('/pages', '')


class BasePage(Driver):
    def find_ele(self, by: list):
        try:
            return self.driver.find_element(*by)
        except:
            self.handle_exception(by)
            try:
                return self.driver.find_element(*by)
            except:
                print(f': 未定位到元素 -> {by}')
                return None

    def find_eles(self, by: list):
        return self.driver.find_elements(*by)

    def handle_exception(self, by: list):
        ...

    def wait_until(self, by: list):
        try:
            return WebDriverWait(self.driver, 5).until(ex.element_to_be_clickable(by))

        except TimeoutException:
            print(f': wait until time out -> {by}')

        except:
            print(f': Wait Until error -> {by}')
