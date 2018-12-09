import unittest
import requests
from 第3天 import db


class TestUserReg(unittest.TestCase):

    def test_user_reg_normal(self):
        NAME = "张三丰"
        if db.check_user(NAME):  # 环境准备
            db.del_user(NAME)
        url = 'http://115.28.108.130:5000/api/user/reg/'
        data = {"name": NAME, "password": "123456"}
        res = requests.post(url=url, json=data)
        self.assertEqual("成功", res.json()["msg"])
        self.assertTrue(db.check_user(NAME))

        db.del_user(NAME)   # 环境清理

    def test_user_reg_use_exist(self):
        url = 'http://115.28.108.130:5000/api/user/reg/'
        data = {"name": "张三", "password": "123456"}
        res = requests.post(url=url, json=data)
        self.assertEqual("失败，用户已存在", res.json()["msg"])