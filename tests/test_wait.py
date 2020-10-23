# -*- coding: utf-8 -*-

import allure
from itest2 import Wait


class WaitDemo(object):
    num = 0
    def wait_second(self):
        self.num += 1
        return self.num


@allure.feature('验证工具')
@allure.story('IWait(显性等待)')
class TestWait(object):

    @allure.description('直到方法成立')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_until(self):
        Wait(WaitDemo(), 2).until(lambda x: x.wait_second() == 2)

    @allure.description('直到方法不成立')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_until_not(self):
        Wait(WaitDemo(), 2).until_not(lambda x: x.wait_second() == 3)
