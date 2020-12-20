from pages import BasePage
import yaml
import os

os_path = os.path.dirname(os.path.abspath(__file__))


class AddContactPage(BasePage):
    _eles = yaml.safe_load(open(f'{os_path}/eles.yaml', encoding='utf-8'))

    def add_name(self, name):
        self.find_ele(self._eles['con_name_box']).send_keys(name)
        return self

    def add_alias(self, alias):
        self.find_ele(self._eles['con_alias_box']).send_keys(alias)
        return self

    def add_account(self, account):
        self.find_ele(self._eles['con_account_box']).send_keys(account)
        return self

    def add_phone(self, phone):
        self.find_ele(self._eles['con_phone_box']).send_keys(phone)
        return self

    def add_email(self, email):
        self.find_ele(self._eles['con_email_box']).send_keys(email)
        return self

    def add_job(self, job):
        self.find_ele(self._eles['con_job_box']).send_keys(job)
        return self

    def save_info(self):
        self.find_ele(self._eles['con_save_bt']).click()
        return self

    def select_post_invitation(self, flag: bool):
        if not flag:
            self.find_ele(self._eles['con_invite_tick']).click()

        return self
