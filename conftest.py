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
    # 启动debug的浏览器
    d.debug_start()
    d.debug_driver.get(cf.get('Test', 'main_url'))
    f = open(f'{os_path}/pages/cookies.yaml', 'w', encoding='utf-8')
    # 获取cookie并直接存储到yaml文件中
    yaml.dump(Driver().debug_driver.get_cookies(), f)


@pytest.fixture(scope='session', autouse=True)
def web_start():
    # cookie复用
    get_cookies()
    d = Driver()
    d.start()
    d.driver.get(cf.get('Test', 'login_url'))
    # 导入复用的cookie
    [d.driver.add_cookie(cookie) for cookie in yaml.safe_load(open(f"{os_path}/pages/cookies.yaml", encoding='utf-8'))]
    # 启动浏览器
    d.driver.get(cf.get('Test', 'main_url'))
    yield
    time.sleep(5)
    d.driver.close()
