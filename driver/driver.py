from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
import configparser
import os

os_path = os.path.dirname(os.path.abspath(__file__)).replace(r'driver', '')


class Driver:
    driver: WebDriver = None
    debug_driver: WebDriver = None

    @classmethod
    def start(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)

    @classmethod
    def debug_start(cls):
        cf = configparser.ConfigParser()
        cf.read(f'{os_path}/config.ini')
        debug_port = cf.get('Debug', 'port')
        opt = webdriver.ChromeOptions()
        opt.debugger_address = f"localhost:{debug_port}"
        cls.debug_driver = webdriver.Chrome(options=opt)
        cls.debug_driver.implicitly_wait(5)
