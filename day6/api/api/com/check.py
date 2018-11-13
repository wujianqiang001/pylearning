#断言用例 与实际结果
def check_pytest(expection,content):#参数为实际结果与预期结果
    for k in expection:#遍历预期结果
        if isinstance(k,str):#判断是否为字典
            assert expection == content#断言结果
        elif isinstance(expection[0],dict):
            assert expection == content
        else:
            for k1 in expection[k]:#遍历二层结果
                if not isinstance(expection[k][k1],dict):#二层是否为字典
                    assert expection[k][k1] == content[k][k1]
                else:
                    for k2 in expection[k][k1]:
                        assert expection[k][k1][k2] == content[k][k1][k2]

