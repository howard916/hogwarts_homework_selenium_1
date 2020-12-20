from pages import BasePage
import yaml
import os

os_path = os.path.dirname(os.path.abspath(__file__))


class AddDepartmentPage(BasePage):
    _eles = yaml.safe_load(open(f'{os_path}/eles.yaml', encoding='utf-8'))

    def input_department_name(self, name):
        ...

    def select_belong_department(self, b_department):
        ...

    def save(self):
        ...

    def dep_name_error_info(self):
        ...
        # todo: 必填处理提示

    def dep_belong_list_error(self):
        ...
        # todo: 必填处理提示
