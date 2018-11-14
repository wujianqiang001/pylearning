#三种方式实现斐波那契数列
def fun1(n):
    "方法一：使用直接循环方式"
    i = 0
    j = 1
    L = [0]
    for k in range(n):
        m = i + j
        i = j
        j = m
        L.append(m)
    return L

def fun2(n):
    "方法二：使用列表特点方式"
    L = [0,1]
    for i in range(n):
        L.append(L[-2]+L[-1])

    return L

def fun3(n):
    "方法三：使用递归函数方式"
    def fibs(n):
        if n <= 1:
            return n
        else:
            return fibs(n-1)+fibs(n-2)
    L = []
    for i in range(n+2):
        L.append(fibs(i))
    return L

if __name__ == "__main__":
    f1 = fun1(10)
    f2 = fun2(10)
    f3 = fun3(10)
    print(f1,f2,f3)  
        
