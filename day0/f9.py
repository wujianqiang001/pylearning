import string, random
def getservername():
    a = string.ascii_lowercase
    b = string.digits
    c = a + b
    d = "".join(c)
    _L = []
    for i in range(3):
        if i == 0:
            _L.append("".join(random.sample(d, 5)))
        else:
            _L.append("".join(random.sample(d, 4)))
    _L.append("com")
    sn = ".".join(_L)
    return sn

servername = getservername()
print (servername)
