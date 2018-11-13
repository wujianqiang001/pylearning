def fun1():
    return "hello world"

def fun2():
    return "hello world"
    print("My God")

def fun3():
    for i in range(10):
        return i

def fun4():
    for i in range(10):
        if i == 3:
            return i

def fun5():
    for i in range(10):
        if i == 3:
            return i
        elif i == 2:
            return i

def fun6():
    ip = input("please input an ip:")
    ip_s = ip.split(".")
    L = len(ip_s)
    flag = False
    if L == 4:
        for p in ip_s:
            if p.isdigit() and 0<= int(p) <= 255:
                flag = True
            else:
                flag = False
    if flag:
        print ("This %s is a legal ip!"%ip)
    else:
        print ("This %s is an illegal ip!"%ip)

#fun6()

def fun7():
    ip = input("please input an ip:")
    ip_s = ip.split(".")
    L = len(ip_s)
    flag = False
    if L == 4:
        for p in ip_s:
            if p.isdigit() and 0<= int(p) <= 255:
                return "This %s is a legal ip!"%ip
    return "This %s is an illegal ip!"%ip

print(fun7())
