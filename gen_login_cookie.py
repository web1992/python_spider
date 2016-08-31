#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
     模拟豆瓣电影登陆，获取cookie ，存入文件
"""
import urllib2
import urllib
import cookielib

class DouBanCookie:
    def __init__(self):
        # cookie 存放的文件
        self.filename = 'cookie.txt'
        # 豆瓣用户名
        self.user_name = ''
        # 豆瓣的密码
        self.pwd = ''
        # 登录豆瓣电影的URL
        self.login_url = 'https://accounts.douban.com/login'

    def input_user_name_pwd(self):
        """
            输入用户名和密码,也可以写死
            :return:
        """
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

    def gen_cookie(self):
        """
             登陆生成cookie
            :return:
        """
        # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
        cookie = cookielib.MozillaCookieJar(self.filename)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        # 此登录方式是手机验证码登录，登录成功后，会在 cookie.txt 写入cookie
        _post_data = urllib.urlencode({
            'form_email': self.user_name,
            'source': 'movie',
            'login_type': 'sms',
            'redir': 'https://movie.douban.com/',
            'form_password': self.pwd,  # 手机验证码
        })

        # 模拟登录，并把cookie保存到变量
        result = opener.open(self.login_url, _post_data)
        print 'result=', result.read()
        # 保存cookie到cookie.txt中
        cookie.save(ignore_discard=True, ignore_expires=True)
        # 大于 210 页时，需要登录才能访问，这里如果 result 有返回的页面内容，则说cookie 登录正确
        test_url = 'https://movie.douban.com/subject/26266072/comments?start=210&limit=20&sort=new_score'
        # 发个请求
        result = opener.open(test_url)
        # print result.read()


if __name__ == '__main__':
    _douBan_cookie = DouBanCookie()

    _douBan_cookie.input_user_name_pwd()

    _douBan_cookie.gen_cookie()
    print 'gen cookie suc'
