# -*- coding: utf-8 -*-
# @Time    : 2019-04-07 18:21
# @Author  : FangYuan
# @File    : test_department.py
import pytest
import logging
from allure import MASTER_HELPER as allure
from apis.contacts.manage_department import ManageDepartment

@allure.feature("测试操作部门")
class TestDepartment(object):

    @pytest.mark.parametrize("name, parentid, order, id",
                             [("测试部", 1, 3, 3),
                              ("产品部", 1, 4, 4),
                              ("研发部", 1, 5, 5),
                              ("财务部", 1, 6, 6)])
    @allure.story("创建新部门")
    @pytest.mark.run(order=1)
    def test_creat_depa(self,name,parentid,order,id):
        '''
        这是创建新部门的测试用例
        :param name: 部门名称
        :param parentid: 父部门id
        :param order: 在父部门中的次序值
        :param id: 部门id
        :return: None
        '''
        depa_info = {
            "name": name,
            "parentid": parentid,
            "order": order,
            "id": id
        }
        logging.info("部门信息：" + str(depa_info))
        md = ManageDepartment()
        md.creat_department(depa_info)
        res = md.get_response()
        assert res.get("errmsg") == "created"

    @pytest.mark.parametrize("id, name, parentid, order",
                             [(3, "测试部update", 1, 3),
                              (4, "产品部update", 1, 4),
                              (5, "研发部update", 1, 5),
                              (6, "财务部update", 1, 6)])
    @allure.story("更新部门信息")
    @pytest.mark.run(order=2)
    def test_update_depa(self, id, name, parentid, order):
        '''
        这是更新部门信息的测试用例
        :param id: 部门id
        :param name: 部门名称
        :param parentid: 父部门id
        :param order: 在父部门中的次序值
        :return: None
        '''
        depa_info = {
            "id": id,
            "name": name,
            "parentid": parentid,
            "order": order
        }
        logging.info("部门信息：" + str(depa_info))
        md = ManageDepartment()
        md.update_department(depa_info)
        res = md.get_response()
        assert res.get("errmsg") == "updated"

    @pytest.mark.parametrize("id", [None, 3, 4, 5, 6])
    @allure.story("查询部门")
    @pytest.mark.run(order=3)
    def test_get_depa_list(self, id):
        '''
        这是测试查询部门信息的测试用例
        :param id: 部门id，不传时查询全部门信息
        :return: None
        '''
        md = ManageDepartment()
        md.get_department_list(id)
        res = md.get_response()
        assert res.get("errmsg") == "ok"
        if id:
            logging.info("要查询的部门id为：" + str(res.get("department")[0].get("id")))
            assert res.get("department")[0].get("id") == id
        else:
            logging.info("查询全部部门信息")
            assert res.get("department")[0].get("id") == 1

    @pytest.mark.parametrize("id", [3, 4, 5, 6])
    @allure.story("删除部门")
    @pytest.mark.run(order=4)
    def test_delete_depa(self, id):
        '''
        这是测试删除部门的测试用例
        :param id: 部门id
        :return: None
        '''
        logging.info("要删除的部门id为："+str(id))
        md = ManageDepartment()
        md.delete_department(id)
        res = md.get_response()
        assert res.get("errmsg") == "deleted"