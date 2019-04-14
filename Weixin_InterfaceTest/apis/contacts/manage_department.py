# -*- coding: utf-8 -*-
# @Time    : 2019-04-07 15:20
# @Author  : FangYuan
# @File    : manage_department.py
import logging
from allure import MASTER_HELPER as allure
from apis.base_api import BaseAPI


class ManageDepartment(BaseAPI):

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

    # 创建新部门
    def creat_department(self, depart_info):
        with allure.step("获取创建新部门请求参数"):
            url = self.yaml_data["contacts"]["department"]["creat_dep_url"]
            params = {
                "access_token": self.access_token
            }
        logging.debug("url:" + str(url))
        logging.debug("params:" + str(params))
        with allure.step("发出创建新部门的请求"):
            self.send_post_json(url, depart_info, params=params)


    # 更新部门信息
    def update_department(self, depart_info):
        with allure.step("获取更新部门信息请求参数"):
            url = self.yaml_data["contacts"]["department"]["update_dep_url"]
            params = {
                "access_token": self.access_token
            }
        logging.debug("url:" + str(url))
        logging.debug("params:" + str(params))
        with allure.step("发出更新部门信息的请求"):
            self.send_post_json(url, depart_info, params=params)

    # 删除部门
    def delete_department(self, depa_id):
        with allure.step("获取删除部门请求参数"):
            url = self.yaml_data["contacts"]["department"]["delete_dep_url"]
            params = {
                "access_token": self.access_token,
                "id": depa_id
            }
        logging.debug("url:" + str(url))
        logging.debug("params:" + str(params))
        with allure.step("发出删除部门的请求"):
            self.send_get(url, params)

    # 获取部门列表
    def get_department_list(self, depa_id=None):
        with allure.step("获取部门列表请求参数"):
            url = self.yaml_data["contacts"]["department"]["get_dep_list_url"]
            if depa_id:
                params = {
                    "access_token": self.access_token,
                    "id": depa_id
                }
            else:
                params = {
                    "access_token": self.access_token
                }
        logging.debug("url:" + str(url))
        logging.debug("params:" + str(params))
        with allure.step("发出查询部门列表的请求"):
            self.send_get(url, params)