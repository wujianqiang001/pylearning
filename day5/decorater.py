def fun(fun1):
    def _deco(b):
        print("a")
        fun1(b)
    return _deco

@fun
def fun2(b):
    print(b)

fun2("abc")
