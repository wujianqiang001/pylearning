import os,sys
def fun(a):
    assert a == 1
def test_case():
    assert 1 == 1

def test_case1():
    assert 1 == 2

def test_case2():
    fun(2)

# if __name__ == "__main__":
#     os.system("pytest testsuite -s -k \"not case1\"")
if __name__ == "__main__":
    pyfile = os.path.basename(sys.argv[0])
    os.system("pytest %s --alluredir allure-report"%pyfile)
    os.system("allure serve -h 127.0.0.1 -p 8001 allure-report")
