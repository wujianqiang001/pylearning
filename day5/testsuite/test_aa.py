import os,sys
def test_case():
    print("test_case")
    assert 1 == 1

def test_case1():
    assert 1 == 2

#
# if __name__ == "__main__":
#     pyfile = os.path.basename(sys.argv[0]).split(".")[0]
#     os.system("pytest %s.py --alluredir allure-report"%pyfile)
#     os.system("allure serve -h 127.0.0.1 -p 8001 allure-report")
