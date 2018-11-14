import string
import random
# 把10个数放到list里 取出来的就删除掉。 然后再随机生成数字
# 移出已经出现的数字
def change(sourcedata, olddata):
    for each in sourcedata:
        if each in olddata:
            olddata.remove(each)
    return olddata

# 获取随机数
def getnum(str1, num):
    data = random.sample(str1, num)
    return(data)

# 获取每位数值  a,需要剔除的数据   b:原始数字组合  c:数字的位数
def getdata(a, b, c):
   numss = change(a, b)
   data = getnum(numss, c)
   return data

def typechange(d):
    data = ''
    for i in d:
        data = data+str(i)
        data33 = int(data)
    return data33

while True:
    numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    data1 = getnum(numlist, 4)
    data2 = getdata(data1, numlist, 1)
    nums2 = change(data1, numlist)
    data3 = getdata(data2, nums2, 4)
    a1 = typechange(data1)
    a2 = typechange(data2)
    a3 = typechange(data3)
    if a1 * a2 == a3:
        print(a1, a2, a3)
        break



'''
# 剔除已经取出的数字
def change(sourcedata, olddata):
    for each in sourcedata:
        olddata = olddata.replace(each, '')
    return(olddata)


# 获取随机数
def getnum(str1, num):
    data = random.sample(str1, num)
    data = ''.join(data)
    return(data)


# 获取每位数值  a,需要剔除的数据   b:原始数字组合  c:数字的位数
def getdata(a, b, c):
   numss = change(a, b)
   data = getnum(numss, c)
   return data


# 随机的数字
nums = string.digits.replace('0', '')

while True:
    data1 = getnum(nums, 4)
    data2 = getdata(data1, nums, 1)
    nums2 = change(data1, nums)
    data3 = getdata(data2, nums2, 4)

    data1 = int(data1)
    data2 = int(data2)
    data3 = int(data3)
    if data1 * data2 == data3:
        print(data1, data2, data3)
        
'''


