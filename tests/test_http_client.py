# -*- coding: utf-8 -*-

import allure
import os

from itest2 import http_clients, Resources
from itest2.core.itest_session import ItestSession
from .ext import root_dir


@allure.feature('客户端管理')
@allure.story('Http请求')
class TestHttpClient(object):

    @allure.description('创建客户端，获取客户端')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_client_and_get_client(self):
        rs = Resources(os.path.join(root_dir, 'tmp'), ext='json')
        http_clients.create_client(
            name="test", base_url="https://trains.ctrip.com")
        client = http_clients.client('test')
        assert isinstance(client, ItestSession)
        r = client.get('/trainBooking/ajax/getNotice', status_code=200,
                   schema_file=rs.get_path('test_getNotice'))

    @allure.description('关闭所有客户端')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_close_all(self):
        http_clients.close_all()
