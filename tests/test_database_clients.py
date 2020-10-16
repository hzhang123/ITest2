# -*- coding: utf-8 -*-

import allure

from itest2 import db_clients
from records import Database


@allure.feature('客户端管理')
@allure.story('DB请求')
class TestDataBaseClient(object):

    @allure.description('创建客户端，获取客户端')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_client_and_get_client(self):
        db_clients.create_client(
            'growing', 'postgresql://apps:SQ!!)VQL^]+9rtAH@easydata-release.cp9cbbjb0tpe.rds.cn-north-1.amazonaws.com.cn:7531/growing')
        assert isinstance(db_clients.client('growing'), Database)

    @allure.description('关闭所有客户端')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_close(self):
        db_clients.close_all()
