#coding=utf-8

from public.common import basepage
from selenium import webdriver

class adminIndexPage(basepage.Page):

    def into_admin_page(self):
        """打开登录页面"""
        # self.dr.open('http://login.test.rusuogroup.com/login.html')
        self.dr.open('http://biz.test.rusuogroup.com')
    def input_login_name(self,values):
        """输入用户名"""
        self.dr.clear_type('xpath->/html/body/div[1]/form/div[1]/input',values)
    def input_login_pwd(self,values):
        """输入密码"""
        self.dr.clear_type('xpath->/html/body/div[1]/form/div[2]/input',values)
    def click_login_button(self):
        """点击登录按钮"""
        self.dr.click('xpath->//*[@id="login"]')
    def return_title(self):
        """返回该页面的title"""
        return self.dr.get_title()