#coding=utf-8

from time import sleep
from public.common import mytest
from public.pages import adminIndexPage
from public.common import datainfo

class TestadminLogin(mytest.MyTest):
    """登录测试"""
    def _login(self,hh):
        """封装登录的函数"""
        adminlogin = adminIndexPage.adminIndexPage(self.dr)
        adminlogin.into_admin_page()
        sleep(2)
        adminlogin.input_login_name('gwb')
        adminlogin.input_login_pwd('gwb888')
        adminlogin.click_login_button()
        sleep(2)
        # self.assertIn(searchKey, adminlogin.return_title())

    def test_login(self):
        """登录"""
        adminlogin = adminIndexPage.adminIndexPage(self.dr)
        adminlogin.into_admin_page()
        sleep(2)
        adminlogin.input_login_name('gwb')
        adminlogin.input_login_pwd('gwb888`')
        adminlogin.click_login_button()
        sleep(5)

    # def test_login_excel(self):
    #     """使用数据驱动,进行测试"""
    #     datas = datainfo.get_xls_to_list('user.xlsx','Sheet1')
    #     datas.get('user')
    #     datas.get('pwd')
    #     for data in datas:
    #         self._login(data)
