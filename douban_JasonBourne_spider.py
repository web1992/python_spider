#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    谍影重重影评
"""
import re
import urllib2

import cookielib

class douban_JasonBourne_spider(object):
    """

    """

    def __init__(self):
        self.page = 1
        self.totalPage = 24826  # 总记录数
        self.pageSize = 20  # 每页数
        self.pageCount = 0  # 总页数
        self.startIndex = 0  # 开始页数
        self.cur_url = "https://movie.douban.com/subject/26266072/comments?start={startIndex}&limit={pageSize}&sort=new_score"
        self.datas = []
        self._top_num = 1
        print "豆瓣电影爬虫准备就绪, 准备爬取数据..."

    def get_page(self, startIndex):
        """

        """
        url = self.cur_url
        try:
            _targetUrl=url.format(startIndex=startIndex, pageSize=self.pageSize)
            print _targetUrl
            # my_page = urllib2.urlopen(_targetUrl).read().decode("utf-8")
            # 创建MozillaCookieJar实例对象
            cookie = cookielib.MozillaCookieJar()
            # 从文件中读取cookie内容到变量
            cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
            # 创建请求的request
            req = urllib2.Request(_targetUrl)
            # 利用urllib2的build_opener方法创建一个opener
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
            response = opener.open(req)
            # print response.read()
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print "The server couldn't fulfill the request."
                print "Error code: %s" % e.code
            elif hasattr(e, "reason"):
                print "We failed to reach a server. Please check your url and read the Reason"
                print "Reason: %s" % e.reason
        return response.read()

    def find_title(self, my_page):
        """

        """
        temp_data = []
        movie_items = re.findall(r'<div\sclass="comment">(.*?)</div>', my_page, re.S)

        # print movie_items
        for index, item in enumerate(movie_items):
            # 评分
            _start = re.findall(r'allstar(\d{2})', item, re.S)
            # 用户的ID
            _uid = re.findall(r'https://www.douban.com/people/(\d{9,20})', item, re.S)
            if _uid:
                _unameRe = r'<a href="https://www.douban.com/people/{uid}/" class="">(.*?)</a>'.format(uid=_uid[0])
            # 用户名
                _uname = re.findall(_unameRe, item, re.S)
                _contentReg = '<p class="">(.*?)</p>'
                # 电影评论
                _content = re.findall(_contentReg, item, re.S)

                temp_data.append(_start[0]+"\t"+_uid[0]+"\t"+_uname[0]+"\t"+_content[0])

        self.datas.extend(temp_data)

    def start_spider(self):
        """
            开始抓取数据

        """
        if self.totalPage % self.pageSize == 0:
            self.pageCount = self.totalPage / self.pageSize
        else:
            self.pageCount = self.totalPage / self.pageSize + 1

        print "pageCount=", self.pageCount

        while self.page <= self.pageCount:
            my_page = self.get_page(self.startIndex)
            self.find_title(my_page)
            with open('douban_JasonBourne_yingping.txt','a')  as file:
                for _item in self.datas:
                    file.write(_item+"\n")
            self.page += 1
            self.startIndex += self.pageSize+1


def desc():
    print """
        ###############################
            Desc: 电影影评抓取
            Author: web1992
            Version: 0.0.1
            Date: 2016-08-30
        ###############################
    """


def main():
    desc()

    my_spider = douban_JasonBourne_spider()
    my_spider.start_spider()

    for item in my_spider.datas:
        print item
    print "豆瓣 谍影重重 爬虫爬取结束..."


if __name__ == '__main__':
    main()
