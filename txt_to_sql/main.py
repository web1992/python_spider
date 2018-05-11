#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
     TxtSQL
"""
import datetime
from string import Template
import re


class TxtSQL:

    def __init__(self):
        print 'init'

    def get_template(self):
        print 'get_template'
        _base_table = '''
            CREATE TABLE `${table_name}` (
                `oid` BIGINT(20) NOT NULL AUTO_INCREMENT,
                ${fields}
                `remark` VARCHAR(128) DEFAULT NULL COMMENT '备注',
                `batch_no` VARCHAR(64) DEFAULT NULL COMMENT '批处理号',
                `exclusive_code` VARCHAR(64) DEFAULT NULL COMMENT '排他编码',
                `created_at` DATETIME DEFAULT NULL COMMENT '创建时间',
                `updated_at` DATETIME DEFAULT NULL COMMENT '更新时间',
                `created_by` VARCHAR(64) DEFAULT NULL COMMENT '创建人',
                `updated_by` VARCHAR(64) DEFAULT NULL COMMENT '修改人',
                `delete_flag` char(1) DEFAULT NULL COMMENT '删除标记',
                PRIMARY KEY (`oid`)
            )  COMMENT='${comment}';
        '''
        return Template(_base_table)


if __name__ == '__main__':

    _table_name = 'test_table'
    _table_comment = 'test'
    _filed_str = ''
    _filed_comment = '`${filed}` VARCHAR(200) DEFAULT NULL COMMENT \'${comment}\',\n'

    _field_list = []
    with open(r'/Users/zl/Documents/code/python_utils/txt_to_sql/txt_sql.txt') as f:
        _list = f.readlines()
    for line in _list:
        #print line
        _fileds = line.split()
        _comment_template = Template(_filed_comment)
        _comment_str = _comment_template.substitute(
            comment=_fileds[0], filed=_fileds[1])
        #print _comment_str
        _field_list.append(_comment_str)

    txtSQL = TxtSQL()
    _sql_template = txtSQL.get_template()
    _field_str = ''
    for f in _field_list:
        _field_str = (f+_field_str)
    _table_template = _sql_template.substitute(
        table_name=_table_name, comment=_table_comment, fields=_field_str)
    print 'len=', len(_field_list)

    #print _table_template
    with open('/Users/zl/Documents/code/python_utils/txt_to_sql/sql_result.txt', 'w') as _resulet_f:
        _resulet_f.write(_table_template)
    print 'gen template done ...'
