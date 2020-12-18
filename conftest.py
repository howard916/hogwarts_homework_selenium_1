import time
from driver import Driver
import pytest
import yaml
import configparser
import os

os_path = os.path.dirname(os.path.abspath(__file__))
cf = configparser.ConfigParser()
cf.read(f'{os_path}/config.ini')


def get_cookies():
    d = Driver()
    d.debug_start()
    d.debug_driver.get(cf.get('Test', 'main_url'))
    f = open(f'{os_path}/pages/cookies.yaml', 'w', encoding='utf-8')
    yaml.dump(Driver().debug_driver.get_cookies(), f)


@pytest.fixture(scope='session', autouse=True)
def web_start():
    get_cookies()
    d = Driver()
    d.start()
    d.driver.get(cf.get('Test', 'login_url'))
    [d.driver.add_cookie(cookie) for cookie in yaml.safe_load(open(f"{os_path}/pages/cookies.yaml", encoding='utf-8'))]
    d.driver.get(cf.get('Test', 'main_url'))
    yield
    time.sleep(5)
    d.driver.close()
