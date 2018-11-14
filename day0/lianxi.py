import string
import random
B = {"version": 123456}
C = {}
E = {}
List = []
s = string.digits+string.ascii_lowercase
def zd(n):
    for i in range(n):
        a = "".join(random.sample(s, 5))
        b = "".join(random.sample(s, 4))
        c = "".join(random.sample(s, 4))
        y = a + "." + b + "." + c + ".com"
        E["host"] = y
        E["preproy"] = "switch"
        E["TLL"] = i
        D = E.copy()
        C[D["host"]] = D
    List.append(C)
    B["add_domains"] = List
    return B
print(zd(4))
