# -*- coding:utf-8 -*-
'''
Terminal执行以下命令
pytest -v pytest.py --junitxml=report\pytest.xml    生成XMl报告
pytest -v pytest.py --resultlog=report\pytest.txt   生成txt报告
pytest -v pytest.py --html=report\pytest.html     生成html报告
'''
import pytest

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5

def test_wcf():
    assert inc(3) > 5

def test_hy():
    assert inc(3) < 5

class TestClass:
    def test_one(self):
        assert "h" in "this"

    def test_two(self):
        x = "hello"
        assert hasattr(x,"name")
