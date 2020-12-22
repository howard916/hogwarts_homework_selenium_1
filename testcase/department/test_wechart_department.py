import time

import pytest
import allure
import yaml
import os
from pages.contact_page import AddDepartmentPage
from pages.main_page import MainPage
from pages.contact_page import ContactsPage

os_path = os.path.dirname(os.path.abspath(__file__))
test_data = yaml.safe_load(open(f'{os_path}/data.yaml', encoding='utf-8'))


@allure.feature("部门功能测试")
@pytest.mark.department
class TestDepartment:
    def setup_class(self):
        self.dep_page = AddDepartmentPage()
        MainPage().goto_contact_page()
        self.contact_page = ContactsPage()

    @allure.title('部门名称为空提示检查')
    def test_blank_department_name_error_info(self):
        self.contact_page.goto_add_department_page()
        self.dep_page.save().cancel()
        assert self.dep_page.dep_error_info('请输入部门名称')

    @allure.title('所属部门未选择提示检查')
    @pytest.mark.parametrize('dep_name', ['123'])
    def test_blank_belong_departments_error_info(self, dep_name):
        self.contact_page.goto_add_department_page()
        self.dep_page.input_dep_name(dep_name)
        self.dep_page.save().cancel()
        assert self.dep_page.dep_error_info('请选择所属部门')

    @allure.title('相同部分级别内创建相同名称的部门')
    @pytest.mark.parametrize('dep_name, exist_dep', test_data['exist_dep'])
    def test_add_duplicate_department_error_info(self, dep_name, exist_dep):
        self.contact_page.goto_add_department_page()
        self.dep_page.input_dep_name(exist_dep)
        self.dep_page.select_dep(dep_name)
        self.dep_page.save()
        assert self.dep_page.dep_error_info('该部门已存在')

    @allure.title('相同部分级别内创建相同名称的部门')
    @pytest.mark.parametrize('belong_dep, dep_name', test_data['new_dep'])
    def test_add_department(self, belong_dep, dep_name):
        self.contact_page.goto_add_department_page()
        self.dep_page.input_dep_name(dep_name)
        self.dep_page.select_dep(belong_dep)
        self.dep_page.save()
        assert self.dep_page.dep_list_check(dep_name)
