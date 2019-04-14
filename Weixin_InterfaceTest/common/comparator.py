# -*- coding: utf-8 -*-
# @Time    : 2019-04-14 16:12
# @Author  : FangYuan
# @File    : comparator.py
import logging
import pytest


class Comparator(object):

    def __init__(self):
        pass

    def json_equal(self, live_json, std_json):
        logging.info("live_json" + str(live_json))
        logging.info("std_json" + str(std_json))
        return live_json == std_json

    def json_less_than(self,live_json,std_json):
        '''
        compare two json object, if std_json contains live_json
        (live_json <= std_json)
        return True, else return False
        :param live_json:
        :param std_json:
        :return:
        '''
        pass

    def json_more_than(self,live_json,std_json):
        '''
        compare two json object, if live_json contains std_json
        (live_json >= std_json)
        return True, else return False
        :param live_json:
        :param std_json:
        :return:
        '''
        pass

if __name__ == "__main__":
    json_compare = Comparator()
    live_json = {
        "errcode":0,
        "errmsg":"ok"
    }
    std_json = {
        "errcode": 0,
        "errmsg": "ok"
    }
    assert json_compare.json_equal(live_json, std_json)