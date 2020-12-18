import pytest
import allure
import yaml
import os
from pages.main_page import MainPage

os_path = os.path.dirname(os.path.abspath(__file__))
test_data = yaml.safe_load(open(f'{os_path}/contact_data.yaml', encoding='utf-8'))


@allure.feature("联系人功能测试")
@pytest.mark.usefixtures("web_start")
class TestContacts:

    @allure.title("联系人添加")
    @pytest.mark.contacts
    @pytest.mark.parametrize("user_info", test_data, ids=[name[2] for name in test_data])
    def test_add_contacts(self, user_info):
        name, alias, account, phone, email, job, department = user_info
        with allure.step("测试创建账号"):
            contact_page = MainPage().goto_contact_page()
            contact_page.goto_add_contact_page()
            contact_page.add_name(name)
            contact_page.add_alias(alias)
            contact_page.add_account(account)
            contact_page.add_phone(phone)
            contact_page.add_email(email)
            contact_page.add_job(job)
            contact_page.save_info()

        with allure.step('检查列表人员信息'):
            list_check = contact_page.get_row_info(name)

        assert [name, job, department, phone, email] == list_check, "联系人添加验证结果错误"
