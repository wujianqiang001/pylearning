#coding=utf-8
import pytest
from htds_interface_agin_test.testcase.case import Case

case = Case()

def setup_module(module):
    case.set_env("url")
    case.load_data("interface_testcase.xlsx")
def test_login_normal():
    return case.run_case("login","test_login_normal")
def test_note_normal():
    return case.run_case("note","test_note_normal")
def test_outbound():
    return case.run_case("outbound","test_outbound_normal")
if __name__ == '__main__':
    pytest.main(["-q","test_case.py"])

