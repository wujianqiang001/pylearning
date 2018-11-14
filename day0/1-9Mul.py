# -*- coding:utf-8 -*-
__author__ = 'changhongwei'

#方法一
#不重复的四位数只能是1234到9876
#a随机取一个四位数，b随机取一个四位数，c随机取一个个位数，若乘法成立则将a,b,c放入一个list中，判断没有重复就输出
# for a in range(1234,9876):
#     for b in range(1234,9876):
#         for c in range(1,10):
#             if b !=a and a * c ==b:
#                 alist = list(str(a)) + list(str(b))
#                 alist.append(str(c))
#                 set1 = set(alist)
#                 #print(set1)
#                 if len(set1) == 9 and '0' not in set1:
#                     print("%d*%d=%d"%(a,c,b))
# #提示一下跑完了，因为等的会比较久（试了一下有2分钟）
# print("end")


#方法二
#a随机取一个四位数，b随机取一个个位数，然后c=a*b,判断c中数字不与a和b重复即可
for a in range(1234,9876):
    for b in range(1,10):
        c = a * b
        if len(str(c)) == 4:
            #把a,b,c放到一个列表中
            alist = list(str(a)) + list(str(b)) + list(str(c))
            set1 = set(alist)
            if len(set1) == 9 and '0' not in set1:
                print("%d*%d=%d"%(a,b,c))
#这个要快很多，循环少了，挺快的
print("end")

# #方法三
# #已经手动推算了一下，中间的个位乘数只能是4，所以另外的两个四位数不包含4
# for a in range(1234,9876):
#     if "4" not in str(a):
#         b = a * 4
#         if len(str(b)) == 4 and "4" not in str(b):
#             alist = list(str(a)) + list(str(b))
#             set1 = set(alist)
#             if len(set1) == 8 and "0" not in set1:
#                 print("%d*%d=%d"%(a,4,b))
# print("end")








