import yaml
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex
from driver import Driver
import os

os_path = os.path.dirname(os.path.abspath(__file__)).replace('/pages', '')


class BasePage(Driver):
    def __init__(self):
        self.black_list = yaml.safe_load(open(f'{os_path}/pages/black_list.yaml'))

    def find_ele(self, by: list):
        try:
            return self.driver.find_element(*by)
        except:
            # 异常处理状态进入
            self.handle_exception()
            try:
                return self.driver.find_element(*by)
            except:
                print(f': 未定位到元素 -> {by}')
                return None

    def find_eles(self, by: list):
        return self.driver.find_elements(*by)

    def handle_exception(self):
        # 隐式等待设置为0, 加快页面元素判断.
        self.driver.implicitly_wait(0)

        # 遍历黑名单的元素, 检查是否存在, 如存在则点击.
        # for i in self.black_list:
        #     if len(self.find_eles(*i)) >= 1:
        #         self.find_ele(*i).click()
        # 推导式写法. 这种写法只适用当前简单的逻辑判断, 当遇到复杂的逻辑情况还是需要用for循环调用
        [self.find_ele(*i).click() for i in self.black_list if len(self.find_eles(*i)) >= 1]

        # 黑名单判断完成后, 恢复隐式等待5s
        self.driver.implicitly_wait(5)

    def wait_until(self, by: list, wait_time=5, wait_type='click'):
        try:
            if wait_type == 'click':
                return WebDriverWait(self.driver, wait_time).until(ex.element_to_be_clickable(by))
            elif wait_type == 'view':
                return WebDriverWait(self.driver, wait_time).until(ex.visibility_of_element_located(by))
            else:
                print(": wait_type is not accept")
                return None

        except TimeoutException:
            print(f': wait until time out -> {by}')

        except:
            print(f': Wait Until error -> {by}')
