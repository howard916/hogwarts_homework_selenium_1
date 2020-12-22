from pages import BasePage
import yaml
import os

os_path = os.path.dirname(os.path.abspath(__file__))


class AddDepartmentPage(BasePage):
    _eles = yaml.safe_load(open(f'{os_path}/eles.yaml', encoding='utf-8'))

    def input_dep_name(self, name):
        self.find_ele(self._eles['dep_name_box']).send_keys(name)
        return self

    def select_dep(self, b_department):
        self.find_ele(self._eles['dep_droplist']).click()
        list_ele = self._eles['dep_list_select']
        self.find_ele([list_ele[0], list_ele[1] % b_department]).click()
        return self

    def save(self):
        self.find_ele(self._eles['dep_save_bt']).click()
        return self

    def cancel(self):
        self.find_ele(self._eles['dep_cancel_bt']).click()

    def dep_error_info(self, info):
        ele = self._eles['dep_error_info']
        return self.wait_until([ele[0], ele[1] % info], wait_type='view')

    def dep_list_check(self, name):
        ele = self._eles['dep_name_check']
        return self.wait_until([ele[0], ele[1] % name], wait_type='view')
