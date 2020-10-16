# -*- coding: utf-8 -*-

import pytest
import os

from .ext import root_dir


@pytest.fixture(scope='session', autouse=True)
def session_setup():
    path = os.path.join(root_dir, 'tmp')
    if not os.path.exists(path):
        os.mkdir(path)