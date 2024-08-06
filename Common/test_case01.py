import json
import os
import requests
import pytest
import warnings
from time import sleep
from Common.common import read_yaml
# from Files.Test_File import logout, loggin, URL, resultDir, reportDir, token
from Files.Test_File import Requests as R

warnings.filterwarnings("ignore", category=PendingDeprecationWarning)


def setup_module(module):
    global token
    res = requests.post(url=R.URL, json=R.loggin)
    if res.status_code == 200:
        token = json.loads(res.text)['message']['token']
        print("获取到的token为：%s" % (token))
        print("\n登录成功！")
    else:
        print("\n登录失败！")


def teardown_module(module):
    res = requests.post(url=R.URL, json=R.logout)
    if res.status_code == 200:
        print("\n退出登录成功！")
    else:
        print("\n退出登录失败！")


@pytest.mark.parametrize('data', read_yaml('../Common/test.yaml'))
def test_01(data):
    data['token'] = token
    print(f"\n{data}")
    res = requests.post(url=R.URL, json=data)
    print(res.text)
    assert json.loads(res.text)['retcode'] == 0
    sleep(1)


if __name__ == "__main__":
    pytest.main(['-vs', 'test_case01.py', '--alluredir', R.resultDir])
    os.system(R.reportDir)


