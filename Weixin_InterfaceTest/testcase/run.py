# -*- coding: utf-8 -*-
# @Time    : 2019-04-07 17:16
# @Author  : FangYuan
# @File    : run.py
import sys
import os
import pytest
import subprocess
import logging
from common.common_function import CommonFunction

# 添加项目路径到pythonPATH
sys.path.append(os.path.dirname(sys.modules[__name__].__file__))

# 设置loging
fileHandler = logging.FileHandler(filename="../logs/uiauto.log", encoding="utf-8")
logging.getLogger().setLevel(0)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
fileHandler.setFormatter(formatter)

logging.getLogger().addHandler(fileHandler)

if __name__ == "__main__":

    # allure 报告生成路径
    cf = CommonFunction()
    report_path = "../reporters/" + str(cf.append_time_stamp_string("report"))
    report_html_path = report_path + "/html"

    # 生成 allure 测试报告
    pytest.main(['-sq', '--disable-warnings', '--alluredir', report_path, '../testcase/contacts'])
    command = "allure generate --clean " + report_path + " -o " + report_html_path
    print(subprocess.getstatusoutput(command))