#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import urllib
import cookielib

filename = 'cookie.txt'

# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# 次登录方式是手机验证码登录，登录成功后，会在 cookie.txt 写入cookie
postdata = urllib.urlencode({
    'form_email': '18921097324',
    # 'form_password': 'qq123456',
    'source': 'movie',
    'login_type': 'sms',
    'redir': 'https://movie.douban.com/',
    'form_password': '65c33e',
})
# 登录教务系统的URL
loginUrl = 'https://accounts.douban.com/login'
# 模拟登录，并把cookie保存到变量
result = opener.open(loginUrl, postdata)
# 保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
# 大于 210 页时，需要登录才能访问，这里如果 result 有返回的页面内容，则说cookie 登录正确
gradeUrl = 'https://movie.douban.com/subject/26266072/comments?start=210&limit=20&sort=new_score'
# 请求访问成绩查询网址
result = opener.open(gradeUrl)
print result.read()
