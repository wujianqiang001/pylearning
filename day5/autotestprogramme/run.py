#!/usr/bin/env python
# coding=utf-8
import pytest,os

if __name__ == "__main__":
    pytest.main(["testsuite/", "-k", "openapi_live"])
    # pytest.main("testsuite/ -k \"openapi_live or anti_cc\"")
    # os.system("python3 -m pytest testsuite/ -k \"openapi_live\"")
