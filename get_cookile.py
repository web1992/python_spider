#!/usr/bin/env python
# -*- coding:utf-8 -*-

import cookielib
import urllib2

# https://movie.douban.com/subject/26266072/comments?start=210&limit=20&sort=new_score
# 创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
# 从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# 创建请求的request
req = urllib2.Request("https://movie.douban.com/subject/26266072/comments?start=210&limit=20&sort=new_score")
# 利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()

