#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
     DPSUtils
"""
import datetime
from string import Template

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

    @staticmethod
    def get_arr_dates():
        """
            时间 昨天
        """
        #print 'get_yesterday_date ...'
        yesterday_str = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y%m%d")
        before_yesterday_mysql_str = (datetime.datetime.now() + datetime.timedelta(days=-2)).strftime("%Y-%m-%d")
        order_date_of_easylink = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%y%m%d")
        #print 'yesterday_str= ' + yesterday_str
        #print 'before_yesterday_mysql_str= ' + before_yesterday_mysql_str
        _arr = ["\'" + before_yesterday_mysql_str + "\'", yesterday_str,order_date_of_easylink]
        return _arr

    def query_data(self):
        """
             登陆
            :return:
        """

        _task_sql_file = open(r'task.sql')
        _f_lines = _task_sql_file.readlines()
        count = 0
        for line in _f_lines:
            #print line

            if line.startswith("#"):
                continue

            if count == 0:
                self.exe_sql(DPSUtils.format_jd_qp_sql(line))

            if count == 1:
                self.exe_sql(DPSUtils.format_easylink_sql(line))

            if count == 2:
                self.exe_sql(DPSUtils.format_baofoo_sql(line))

            if count == 3:
                self.exe_sql(DPSUtils.format_yiji_sql(line))

            if count == 4:
                self.exe_sql(DPSUtils.format_yiji_remit_sql(line))

            if count == 5:
                self.exe_sql(DPSUtils.format_jd_remit_sql(line))

            count = count + 1

    @staticmethod
    def format_jd_qp_sql(sql):
        print 'format_jd_qp_sql'
        _values = DPSUtils.get_arr_dates()
        _sql_template = Template(sql)
        return _sql_template.substitute(date_format='\'%Y%m%d\'', mysql_date=_values[0], yesterday_str=_values[1])

    @staticmethod
    def format_easylink_sql(sql):
        print 'format_easylink_sql'
        _values = DPSUtils.get_arr_dates()
        _sql_template = Template(sql)
        return _sql_template.substitute(mysql_date=_values[0], order_date=_values[2])

    @staticmethod
    def format_baofoo_sql(sql):
        print 'format_baofoo_sql'
        _values = DPSUtils.get_arr_dates()
        _sql_template = Template(sql)
        return _sql_template.substitute(mysql_date=_values[0], order_date=_values[1])

    @staticmethod
    def format_yiji_sql(sql):
        print 'format_yiji_sql'
        _values = DPSUtils.get_arr_dates()
        _sql_template = Template(sql)
        return _sql_template.substitute(mysql_date=_values[0], order_date=_values[1])

    @staticmethod
    def format_yiji_remit_sql(sql):
        print 'format_yiji_remit_sql'
        _values = DPSUtils.get_arr_dates()
        _sql_template = Template(sql)
        return _sql_template.substitute(mysql_date=_values[0], order_date=_values[1])

    @staticmethod
    def format_jd_remit_sql(sql):
        print 'format_jd_remit_sql'
        _values = DPSUtils.get_arr_dates()
        _sql_template = Template(sql)
        return _sql_template.substitute(mysql_date=_values[0], order_date=_values[1])

    def exe_sql(self, sql):
        """
        执行sql
        :return:
        """
        if not self.s:
            self.s = self.login()
        #print 'Query start ...'
        query_post_data = {'sql': sql, 'db': self.db}
        r2 = self.s.post(self.query_url, query_post_data)
        resp_str = r2.text
        resp_lines = resp_str.split('+_-')
        for line in resp_lines:
            print line.replace('-_+', ' ')
        print '#########################################'

if __name__ == '__main__':
    dpsUtils = DPSUtils()
    dpsUtils.query_data()

    print 'Query done ...'
