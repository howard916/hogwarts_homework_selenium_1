from pages import BasePage
from pages.contact_page import ContactsPage
import yaml
import os

os_path = os.path.dirname(os.path.abspath(__file__))


class MainPage(BasePage):
    eles = yaml.safe_load(open(f'{os_path}/eles.yaml', encoding='utf-8'))

    def goto_contact_page(self):
        self.find_ele(self.eles['dh_contacts']).click()
        return ContactsPage()
