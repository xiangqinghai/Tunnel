from common import yaml_load
import requests
import pytest




class TestDaping:
    """参数只有url"""
    @pytest.mark.parametrize("common",yaml_load.load('test_data/tunnel_Large_screen.yaml'))
    def test_01_sysTime(self,common):
        """获取系统时间"""

        method = common['request']['method']
        HOST = common["request"]["HOST"]
        url = HOST+common["request"]["url"]
        name = common['name']
        rep = requests.request(method,url)
        Actual_results_state = rep.json()['state']
        Expected_results = common["validdate"]["equals"]["status_code"]
        if Actual_results_state == Expected_results:
            print("用例名称:"+name+",状态码相等,用例执行成功")
        else:
            assert Actual_results_state == Expected_results
            print("用例名称:"+name+",状态码不相等,用例执行失败")



    @pytest.mark.parametrize("urldata", yaml_load.load('test_data/get_url_data.yaml'))
    def test_03_login(self,urldata):
        """参数有url和data"""
        method = urldata['request']['method']
        HOST = urldata["request"]["HOST"]
        url = HOST + urldata["request"]["url"]
        data = urldata["request"]["data"]
        name = urldata['name']
        rep = requests.request(method, url, data=data)
        Actual_results_state = rep.json()['state']
        Expected_results = urldata["validdate"]["equals"]["status_code"]
        if Actual_results_state == Expected_results:
            print("用例名称:" + name + ",状态码相等,用例执行成功")
        else:
            assert Actual_results_state == Expected_results
            print("用例名称:" + name + ",状态码不相等,用例执行失败,"+rep.text)

















































