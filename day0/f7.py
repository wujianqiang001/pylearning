def switchnum(num):
    _s = str(num)
    _L = []
    for i in range(0,len(_s),3):
        _L.append(_s[i:i+3])
    print _L
    print ".".join(_L)

def switchnum_1(num):
    _s = str(num)
    _L = []
    for i in range(0,len(_s),3):
        _L.append(_s[i:i+3])
    return ".".join(_L)
    
_i = 123456789123456789123456
print "======================="
switchnum(_i)


print "="*22
switchnum_1(_i)

print "="*22
a = switchnum(_i)
print "a>>>>>>>>>>>>>>>>>>"
print a

print "="*22
b = switchnum_1(_i)
print "b>>>>>>>>>>>>>>>>>>"
print b
