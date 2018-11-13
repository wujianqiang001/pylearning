#!/usr/bin/env python
# coding=utf-8
import pytest
import requests
@pytest.fixture(name="brower",scope="session")
def cs():
    s = requests.session()
    s.post("")
    yield s