# -*- coding: utf-8 -*-

import allure
import os
from itest2 import json_schema
from .ext import root_dir


@allure.feature('验证工具')
@allure.story('JsonSchema')
class TestJsonSchema(object):

    @allure.description('JsonSchema校验')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_generate_and_validate(self):

        instance = {"test": 1}
        schema = json_schema.generate(instance)
        json_schema.validate(instance, schema)

    @allure.description('JsonSchema文件生成与校验')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_generate_and_validate_with_file(self):

        schema_file_path = os.path.join(
            root_dir, 'tmp/test_generate_and_validate_with_file.json')
        instance = {"test": 1}
        json_schema.generate_to_file(instance, schema_file_path)
        json_schema.validate_from_file(instance, schema_file_path)
