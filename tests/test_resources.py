# -*- coding: utf-8 -*-

import allure
import os
from itest2 import Resources
from .ext import root_dir


@allure.feature('客户端管理')
@allure.story('Resources')
class TestResources(object):

    @allure.description('文件路径获取')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_path(self):
        md = Resources(ext="md")
        md.get_path('README')
        md = Resources(root_dir, 'md')
        md.get_path('README')
