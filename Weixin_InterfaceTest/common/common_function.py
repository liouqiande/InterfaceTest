# -*- coding: utf-8 -*-
# @Time    : 2019-04-07 10:47
# @Author  : FangYuan
# @File    : common_function.py
import os
import random

import yaml
import logging
import time


class CommonFunction(object):

    # 读取 yaml 文件内容
    def get_yaml_data(self, file_path):
        if file_path:
            with open(file_path, 'rb') as f:
                file_data = f.read()
                yaml_data = yaml.load(file_data)
            return yaml_data
        else:
            logging.info("The yaml file is not exist.")

    # 将内容写入 yaml 文件
    def write_yaml(self, file_name, content):
        # 确定 yaml 文件的写入路径
        config_path = "/Users/mac/auto_test/Weixin_InterfaceTest/config"
        yamlpath = os.path.join(config_path, file_name)

        # 写入到yaml文件
        with open(yamlpath, "w", encoding="utf-8") as f:
            yaml.dump(content, f)

    # 更新json中的值
    def update_json_value_by_key(self,json_obj,key,new_value):
        json_obj[key] = new_value
        return json_obj

    # 在原有值上加上时间戳
    def append_time_stamp_string(self,old_value):
        return old_value + "_" + time.strftime("%Y%m%d%H%M%S")

    # 生成随机手机号
    def get_random_mobile(self):
        phone_list = ['139', '188', '185', '136', '158', '151', '131', '130']
        return random.choice(phone_list) + "".join(random.choice("0123456789") for i in range(8))

    # 生成随机字符串（用来替换邮箱前缀）
    def get_random_string(self, length=5):
        low_case = [chr(i) for i in range(65, 91)]
        up_case = [chr(i) for i in range(97, 123)]
        all_string = "".join(low_case)+"".join(up_case)+"0123456789"
        return "".join(random.choice(all_string) for i in range(length))






if __name__ == "__main__":
    file_path = "/Users/mac/auto_test/Weixin_InterfaceTest/config/config_data.yaml"
    cf = CommonFunction()
    yaml_data = cf.get_yaml_data(file_path)
    # print(yaml_data.get("contacts").get("department").get("creat_department").get("creat_dep_url"))
    print(yaml_data["contacts"]["department"]["creat_department"]["creat_dep_url"])
    # content = {
    #     "contact_access_token": "djfidafja;fijefjei",
    #     "other_access_token": "12"
    # }
    # cf = CommonFunction()
    # cf.write_yaml("test.yaml", content)
