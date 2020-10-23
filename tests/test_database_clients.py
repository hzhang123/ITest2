# -*- coding: utf-8 -*-

import allure

from itest2 import db_client_manage
from records import Database


@allure.feature('客户端管理')
@allure.story('DB请求')
class TestDataBaseClient(object):

    @allure.description('创建客户端，获取客户端')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_client_and_get_client(self):
        db_client_manage.create_client(
            'moon', 'postgresql://postgres:123456@127.0.0.1:5432/moon')
        assert isinstance(db_client_manage.client('moon'), Database)

    @allure.description('关闭所有客户端')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_close(self):
        db_client_manage.close_all()
