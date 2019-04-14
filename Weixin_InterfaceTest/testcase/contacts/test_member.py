# -*- coding: utf-8 -*-
# @Time    : 2019-04-14 12:03
# @Author  : FangYuan
# @File    : test_member.py
import pytest
import logging
from allure import MASTER_HELPER as allure
from apis.contacts.manage_member import ManageMember
from common.common_function import CommonFunction

@allure.feature("测试操作成员")
class TestDepartment(object):

    @allure.story("创建新成员")
    def test_creat_member(self):
        file_path = "/Users/mac/auto_test/Weixin_InterfaceTest/config/member_data/creat_member.yaml"
        cf = CommonFunction()
        yaml_data = cf.get_yaml_data(file_path)
        member_info = yaml_data["member_info"]["request"]
        # 生成随机id
        new_userid = cf.append_time_stamp_string(member_info.get("userid"))
        # 生成对应id的name
        new_name = new_userid + "_name"
        # 生成随机手机号
        new_mobile = cf.get_random_mobile()
        # 生成随机邮箱
        email_prefix = cf.get_random_string()
        email_postfix = member_info.get("email").split("@")[1]
        new_email = email_prefix + "@" + email_postfix
        # 更新member_info中需要保证唯一的值
        cf.update_json_value_by_key(member_info, "userid", new_userid)
        cf.update_json_value_by_key(member_info, "name", new_name)
        cf.update_json_value_by_key(member_info, "mobile", new_mobile)
        cf.update_json_value_by_key(member_info, "email", new_email)
        logging.info("成员信息：" + str(member_info))
        mm = ManageMember()
        mm.creat_member(member_info)
        res = mm.get_response()
        assert res == yaml_data["member_info"]["response"]

    @allure.story("测试读取成员信息")
    def test_read_member(self):
        mm = ManageMember()
        mm.read_member("id_20190414175740")
        res = mm.get_response()
        assert res.get("email") == "0dkGK@gzdev.com"

    @allure.story("测试更新成员信息")
    def test_update_member(self):
        mm = ManageMember()
        file_path = "/Users/mac/auto_test/Weixin_InterfaceTest/config/member_data/update_member.yaml"
        cf = CommonFunction()
        yaml_data = cf.get_yaml_data(file_path)
        update_mem_info = yaml_data["new_member_info"]["request"]
        mm.update_member(update_mem_info)
        res = mm.get_response()
        assert res == yaml_data["new_member_info"]["response"]