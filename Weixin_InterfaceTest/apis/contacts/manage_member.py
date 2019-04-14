# -*- coding: utf-8 -*-
# @Time    : 2019-04-07 18:49
# @Author  : FangYuan
# @File    : manage_member.py
import logging
from allure import MASTER_HELPER as allure
from apis.base_api import BaseAPI


class ManageMember(BaseAPI):

    def __init__(self):
        BaseAPI.__init__(self)
        logging.info("Init department management API")
        # 确定应用名与token配置文件地址
        application_name = "contacts"
        token_path = "/Users/mac/auto_test/Weixin_InterfaceTest/config/contacts_access_token.yaml"
        # 判断 token 是否过期，如果过期自动重新请求
        self.judgment_access_token_is_valid(application_name, token_path)
        # 获取最新的 access_token
        self.access_token = self.cf.get_yaml_data(token_path).get("access_token")

    # 创建成员
    def creat_member(self, member_info):
        with allure.step("获取创建新成员请求参数"):
            url = self.yaml_data["contacts"]["member"]["creat_mem_url"]
            params = {
                "access_token": self.access_token
            }
        logging.debug("url:" + str(url))
        logging.debug("params:" + str(params))
        with allure.step("发出创建新成员的请求"):
            self.send_post_json(url, member_info, params=params)

    # 读取成员
    def read_member(self, userid):
        with allure.step("获取读取成员请求参数"):
            url = self.yaml_data["contacts"]["member"]["get_mem_list"]
            params = {
                "access_token": self.access_token,
                "userid": userid
            }
        logging.debug("url:" + str(url))
        logging.debug("params:" + str(params))
        with allure.step("发出读取成员的请求"):
            self.send_get(url, params=params)

    # 更新成员
    def update_member(self,update_mem_info):
        with allure.step("获取更新成员请求参数"):
            url = self.yaml_data["contacts"]["member"]["update_mem_url"]
            params = {
                "access_token": self.access_token
            }
        logging.debug("url:" + str(url))
        logging.debug("params:" + str(params))
        with allure.step("发出更新成员的请求"):
            self.send_post_json(url, update_mem_info, params=params)

    # 删除成员
    def delete_member(self, userid):
        with allure.step("获取删除成员请求参数"):
            url = self.yaml_data["contacts"]["member"]["delete_mem_url"]
            params = {
                "access_token": self.access_token,
                "userid": userid
            }
        logging.debug("url:" + str(url))
        logging.debug("params:" + str(params))
        with allure.step("发出删除成员的请求"):
            self.send_get(url, params=params)

    # 批量删除成员
    def delete_member_many(self, useridlist):
        with allure.step("获取删除成员请求参数"):
            url = self.yaml_data["contacts"]["member"]["delete_mem_url"]
            params = {
                "access_token": self.access_token,
            }
        logging.debug("url:" + str(url))
        logging.debug("params:" + str(params))
        with allure.step("发出删除成员的请求"):
            self.send_post_json(url, useridlist, params=params)
