import time

from pages import BasePage
from .add_contact_page import AddContactPage
from .add_department_page import AddDepartmentPage
import yaml
import os

os_path = os.path.dirname(os.path.abspath(__file__))


class ContactsPage(BasePage):
    _eles = yaml.safe_load(open(f'{os_path}/eles.yaml', encoding='utf-8'))

    def goto_add_contact_page(self):
        self.wait_until(self._eles['contact_add_bt'])
        self.find_ele(self._eles['contact_add_bt']).click()
        return AddContactPage()

    def goto_add_department_page(self):
        self.wait_until_not(self._eles['pop_window'], wait_type='exist')
        self.find_ele(self._eles['top_add_bt']).click()
        self.find_ele(self._eles['department_add_bt']).click()
        return AddDepartmentPage()

    def get_contacts_row_info(self, name):
        ele = self._eles['contacts_list']
        find_user = self.find_ele([ele[0], ele[1] % (name, '.')])
        if find_user:
            name = self.find_ele([ele[0], ele[1] % (name, '.')]).get_attribute('title')
            job = self.find_ele([ele[0], ele[1] % (name, 'following-sibling::td[1]')]).get_attribute('title')
            department = self.find_ele([ele[0], ele[1] % (name, 'following-sibling::td[2]')]).get_attribute('title')
            phone = self.find_ele([ele[0], ele[1] % (name, 'following-sibling::td[3]')]).get_attribute('title')
            email = self.find_ele([ele[0], ele[1] % (name, 'following-sibling::td[4]')]).get_attribute('title')
            return [name, job, department, phone, email]
        else:
            print(": 列表上未找到相关人员")
            return None

    def back_main_page(self):
        self.find_ele(self._eles['main_page_dh']).click()
        from pages.main_page import MainPage
        return MainPage()
