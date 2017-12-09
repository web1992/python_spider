#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
     DPSUtils
"""
import requests


class DPSUtils:
    def __init__(self):
        self.user_name = ''
        self.pwd = ''
        self.login_url = ''
        self.query_url = ''
        self.s = None
        self.sql = ''
        self.db = ''
        # 配置
        self.read_config()
        # 如果配置文件没有,输入
        self.get_user_name_pwd()

    def read_config(self):
        # 初始化
        print 'read config ...'
        _file = open(r'pwd.pwd')
        lines = _file.readlines()
        self.user_name = lines[0]
        self.pwd = lines[1]
        self.login_url = lines[2]
        self.query_url = lines[3]
        self.db = lines[4]
        self.sql = lines[5]

    def get_user_name_pwd(self):
        """
            输入用户名和密码,也可以写死
            :return:
        """
        print 'get_user_name_pwd ...'
        while not self.user_name:
            _user_name = raw_input("enter your user name: ")
            if not _user_name:
                continue
            else:
                self.user_name = _user_name
                while not self.pwd:
                    _pwd = raw_input("enter your password: ")
                    if not _pwd:
                        continue
                    else:
                        self.pwd = _pwd

    def login(self):
        """
                    登陆
                   :return:
        """
        print 'login init ...'
        login_data = {'username': self.user_name, 'password': self.pwd}
        s = requests.session()
        s.post(self.login_url, login_data)
        print 'login end ...'
        return s

    def query_data(self):
        """
             登陆
            :return:
        """
        if not self.s:
            s = self.login()
        print 'Query start ...'

        query_post_data = {'sql': self.sql, 'db': self.db}
        r2 = s.post(self.query_url, query_post_data)
        resp_str = r2.text
        resp_lines = resp_str.split('+_-')
        for line in resp_lines:
            print line.replace('-_+', ' ')


if __name__ == '__main__':
    dpsUtils = DPSUtils()
    dpsUtils.query_data()

    print 'Query done ...'
