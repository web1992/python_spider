#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
     TxtToSQL
     根据模版和字段文件生成sql语句
"""
import datetime
from string import Template
import re


class TxtToSQL:

    def __init__(self):
        print 'init'
        self.base_url = 'F:/github/python_spider/txt_to_sql/'

    """
        table 模版
    """

    def get_table_template(self):
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

    """
        字段模版
    """

    def get_field_template(self):
        _field_comment = '`${filed}` VARCHAR(256) DEFAULT NULL COMMENT \'${comment}\',\n'
        return Template(_field_comment)

    """
        字段文件读取
        文件格式：
                 # 创建时间    createDate
                 # 更新时间    update_date
    """

    def get_fields(self):
        print 'get_fields'
        _field_list = []

        with open(self.base_url+'web1992_txt_sql.txt') as f:
            _list = f.readlines()
        for line in _list:
            #print line
            _fileds = line.split()
            if len(_fileds) < 2:
                print 'line skip', line
                continue
            _f = TxtToSQL.convert_filed(_fileds[1])
            _comment_template = txtToSQL.get_field_template()
            _comment_str = _comment_template.substitute(
                comment=_fileds[0], filed=_f)
            #print _comment_str
            _field_list.append(_comment_str)
        return _field_list

    """
        转化字段命名
    """
    @staticmethod
    def convert_filed(_filed_str):
        _temp_str = ''
        # if str(_filed_str).find('_') != -1:
        if '_' in str(_filed_str):
            return _filed_str
        else:
            for _index in range(len(_filed_str)):
                _ch = str(_filed_str[_index])
                if _ch.isupper():
                    _temp_str += ('_'+_ch.lower())
                else:
                    _temp_str += _ch
            print 'conver_filed', _filed_str, '-> ', _temp_str
        return _temp_str


"""
    main
"""
if __name__ == '__main__':

    txtToSQL = TxtToSQL()

    _table_name = 'test_table'
    _table_comment = 'test'

    _sql_template = txtToSQL.get_table_template()
    _field_str = ''
    for f in txtToSQL.get_fields():
        _field_str += f

    _table_template = _sql_template.substitute(
        table_name=_table_name, comment=_table_comment, fields=_field_str)

    with open(txtToSQL.base_url+'web1992_sql_result.sql', 'w') as _resulet_f:
        _resulet_f.write(_table_template)

    print 'gen template done ...'
