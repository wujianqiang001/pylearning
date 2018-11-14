def checksame(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] ==s[j]:
                return False

    return True

L =[]
for a in range(1234, 4568):
    for b in range(2,10):
        c=a*b
        s=str(a)+str(b)+str(c)
        if len(s) == 9:
            L.append(s)
for i in L:
    if checksame(i) and ('0' not in i):
        print(i)

########################################
def checksame(s):
    for i in s:
        if s.count(i)>1:
            return False
    return True

for a in range(1234, 4568):
    for b in range(2,10):
        c=a*b
        s=str(a)+str(b)+str(c)
        if len(s) == 9 and ('0' not in s) and checksame(s):
            print(s)
