_i = 123456789123456789
_s = str(_i)
_L = []
for i in range(0,len(_s),3):
    _L.append(_s[i:i+3])
print _L
print ".".join(_L)
