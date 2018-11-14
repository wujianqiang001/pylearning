def cal1():
    for a in range(1234,9876):#根据需求，乘数的最小值是1234，最大值是9876
        for b in range(1,10):#被乘数是1到9之间的值
            c = a*b#计算结果
            if len(str(c)) == 4:#结果必须长度为4位
                s = str(a)+str(b)+str(c)#把乘数、被乘数、结果链接成字符串
                if len(set(s)) == 9 and "0" not in s:#集合set()的作用是去重，
                                                     #去重后的长度必须是9，
                                                     #且不包含0
                    print("%d*%d=%d"%(a,b,c))

def cal21():
    data = [x for x in range(1,10)]#通过列表表达式，生成一组包含1-9数字的列表
                                   #其实，python3中，直接data = range(1,10)，效果是一样的
    fourdatas = []
    for a in data:
        for b in data:
            for c in data:
                for d in data:#通过多重循环，取出四个数字
                    if a not in [b,c,d] and b not in [c,d] and c!=d:#判断四个数字不重复
                       fourdata = str(a)+str(b)+str(c)+str(d)#四个数字拼接成字符串
                       fourdatas.append(int(fourdata))#把1-9所有不重复的四个数字穷举出来
    for d in fourdatas:#循环每个值，作为乘数
        for i in range(1,10):#被乘数
            if str(i) not in str(d):#判断被乘数不在乘数中
               result = i * d
               if result in fourdatas and result !=d and str(i) not in str(result):
                   #判断结果是否是4个不重复数字，且结果不等于乘数，且被乘数不在结果中
                   flag = True
                   for a in str(d):
                       if a in str(result):
                          flag = False#这个循环判断，是判断乘数和结果没有重复的数字
                   if flag:
                      print("%d * %d = %d"%(d,i,result))

def getdata():
    data = range(1,10)
    for a in data:
        for b in data:
            for c in data:
                for d in data:#通过多重循环，取出四个数字
                    if a not in [b,c,d] and b not in [c,d] and c!=d:#判断四个数字不重复
                       yield str(a)+str(b)+str(c)+str(d)#四个数字拼接成字符串,并且生成迭代器

def cal2():
    fourdatas = getdata()#该函数是一个迭代器函数，效率相关更高些
    for d in fourdatas:#循环每个值，作为乘数
        for i in range(1,10):#被乘数
            if str(i) not in d:#判断被乘数不在乘数中
               result = i * int(d)
               s = d+str(i)+str(result)
               if len(set(s))==9 and "0" not in s and len(str(result)) == 4:
                   print("%s * %d = %d"%(d,i,result))
            
def cal31():
    from itertools import permutations
    p = "123456789"
    s = permutations(p)#该方法是穷举1-9的所有不重复的排列组合情况
    for s1 in s:
        a = "".join(s1[:4])#前四个值，并拼接成字符串
        b = s1[4]
        c = "".join(s1[-4:])#后四个值，并拼接成字符串
        if int(a) * int(b) == int(c):
            print(a,b,c)

def cal3():
    from itertools import permutations
    p = "123456789"
    s = permutations(p)#该方法是穷举1-9的所有不重复的排列组合情况
    for s1 in s:
        a,b,c = map("".join,[s1[:4],s1[4],s1[-4:]])
        if int(a) * int(b) == int(c):
            print(a,b,c)
            
if __name__ == "__main__":
    cal2()#
