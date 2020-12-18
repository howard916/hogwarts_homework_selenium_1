from pages import BasePage
import yaml
import os

os_path = os.path.dirname(os.path.abspath(__file__))


class ContactsPage(BasePage):
    eles = yaml.safe_load(open(f'{os_path}/eles.yaml', encoding='utf-8'))

    def goto_add_contact_page(self):
        self.wait_until(self.eles['contact_add_bt'])
        self.find_ele(self.eles['contact_add_bt']).click()
        return self

    def add_name(self, name):
        self.find_ele(self.eles['name_box']).send_keys(name)
        return self

    def add_alias(self, alias):
        self.find_ele(self.eles['alias_box']).send_keys(alias)
        return self

    def add_account(self, account):
        self.find_ele(self.eles['account_box']).send_keys(account)
        return self

    def add_phone(self, phone):
        self.find_ele(self.eles['phone_box']).send_keys(phone)
        return self

    def add_email(self, email):
        self.find_ele(self.eles['email_box']).send_keys(email)
        return self

    def add_job(self, job):
        self.find_ele(self.eles['job_box']).send_keys(job)
        return self

    def save_info(self):
        self.find_ele(self.eles['save_bt']).click()
        return self

    def select_post_invitation(self, flag: bool):
        if not flag:
            self.find_ele(self.eles['invite_tick']).click()

        return self

    def get_row_info(self, name):
        ele = self.eles['name_list']
        name = self.find_ele([ele[0], ele[1] % (name, '.')]).get_attribute('title')
        if name:
            job = self.find_ele([ele[0], ele[1] % (name, 'following-sibling::td[1]')]).get_attribute('title')
            department = self.find_ele([ele[0], ele[1] % (name, 'following-sibling::td[2]')]).get_attribute('title')
            phone = self.find_ele([ele[0], ele[1] % (name, 'following-sibling::td[3]')]).get_attribute('title')
            email = self.find_ele([ele[0], ele[1] % (name, 'following-sibling::td[4]')]).get_attribute('title')
            return [name, job, department, phone, email]
        else:
            return None
