# -*- coding: utf-8 -*-
# @Time    : 2019-04-07 10:43
# @Author  : FangYuan
# @File    : base_api.py

import requests
from allure import MASTER_HELPER as allure
from common.common_function import CommonFunction


class BaseAPI(object):

    def __init__(self):
        self.cf = CommonFunction()
        # 配置文件路径
        with allure.step("获取配置文件路径"):
            file_path = "/Users/mac/auto_test/Weixin_InterfaceTest/config/config_data.yaml"
        # 获取配置文件内容
        with allure.step("获取配置文件内容"):
            self.yaml_data = self.cf.get_yaml_data(file_path)

    # 发送data格式为json的post请求
    def send_post_json(self,url,json_obj,params=None):
        if params:
            self.res = requests.post(url,json=json_obj,params=params)
        else:
            self.res = requests.post(url, json=json_obj)

    # 发送 get 请求
    def send_get(self, url, params):
        self.res = requests.get(url, params=params)

    # 获取响应数据
    def get_response(self):
        return self.res.json()

    # 获取应用 access_token
    def get_access_token(self, application_name):
        with allure.step("获取 access_token 请求参数"):
            token_url = self.yaml_data["token_url"]
            corp_id = self.yaml_data["corp_id"]
            application_secret = self.yaml_data[application_name]["secret"]
        # 构造请求参数
        with allure.step("构造获取token请求参数"):
            params = {
                "corpid": corp_id,
                "corpsecret": application_secret
            }
        with allure.step("发送 access_token 请求"):
            res = requests.get(token_url, params=params)
        # 获取 access_token
        with allure.step("获取 access_token"):
            access_token = res.json().get("access_token")
        # 将获取的 access_token 写入该应用专属配置文件
        with allure.step("将获取的 access_token 写入该应用专属配置文件"):
            yaml_filename = str(application_name) + "_access_token.yaml"
            content = {
                "access_token": access_token
            }
            self.cf.write_yaml(yaml_filename, content)

    # 判断 access_token 是否有效
    def judgment_access_token_is_valid(self, application_name, token_path):
        with allure.step("判断已经存在的yaml文件中的 access_token 是否有效"):
            url = self.yaml_data["ip_url"]
            access_token = self.cf.get_yaml_data(token_path).get("access_token")
            params = {
                    "access_token": access_token
            }
            res = requests.get(url, params=params)
            if res.json().get("errcode") == 40014 or res.json().get("errcode") == 41001:
                with allure.step("token 失效，重新请求"):
                    self.get_access_token(application_name)


if __name__ == "__main__":
    base = BaseAPI()
    application_name = "contacts"
    token_path = "/Users/mac/auto_test/Weixin_InterfaceTest/config/contacts_access_token.yaml"
    base.judgment_access_token_is_valid(application_name, token_path)