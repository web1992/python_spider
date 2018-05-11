#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
     TxtSQL
"""
import datetime
from string import Template
import chardet
import re


class TxtSQL:

    def __init__(self):
        print 'init'

    def get_template(self):
        print 'get_template'
        _file = open(r'sql.template')
        _template = _file.readlines()
        print str(_template)
        _sql_template = Template(_template)
        return _sql_template

if __name__ == '__main__':

    _table_name = 'test_table'
    _comment = 'test'
    _filed_str =''
    _filed_comment='''
       `${filed}` VARCHAR(200) DEFAULT NULL COMMENT '${comment}',
    '''
   
    f = open('txt_sql.txt','r')  
    result = list()  
    for line in open('txt_sql.txt','r'):  
        line = f.readline() 
        print line
        type = chardet.detect(line)
        print line
        text1 = line.decode(type["encoding"])
        _fileds= text1.split('\t')
        _comment_f = Template(_filed_comment)
        _comment_str = _comment_f.substitute(comment=_fileds[0],filed=_fileds[1])
        _filed_str+=_comment_str
    print result
    
    f.close()
    
    txtSQL = TxtSQL()
    _sql_template = txtSQL.get_template()
    ##_result = _sql_template.substitute(table_name=_table_name, comment=_comment)
    _resulet_f = open('result-readline.txt', 'w')
    print _filed_str
    _resulet_f.write(_filed_str)
    print 'gen template ...'
