# -*- coding: utf-8 -*-
import os

import pytest

if __name__ == '__main__':
    pytest.main(["-vs",'test_case/test.py','--alluredir', './allure-results'])
    os.system("allure generate ./allure-results/ -o ./allure-report/ --clean")