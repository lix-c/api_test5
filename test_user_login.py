import unittest
import requests
from 第3天 import db

class TestUserLogin(unittest.TestCase):
    @unittest.skipUnless(db.check_user("张三"),"跳过该测试用例")
    def test_user_login_normal(self):
        url = 'http://115.28.108.130:5000/api/user/login/'
        data = {"name": "张三", "password": "123456"}
        res = requests.post(url=url, data=data)
        self.assertIn("登录成功", res.text)

    def test_user_login_password_wrong(self):
        url = 'http://115.28.108.130:5000/api/user/login/'
        data = {"name": "张三好", "password": "1234567"}
        res = requests.post(url=url, data=data)
        self.assertIn("用户名或密码错误", res.text)

if __name__ == "__main__":
    unittest.main(verbosity=2)