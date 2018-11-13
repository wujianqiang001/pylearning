import random
x = 1                             #初始化循外层循环（关数）
while x >0:                       #循环条件
    print('第',x,'关闯关开始')
    print(x*10,'以内的数字相加减，共10题，答对9道，闯关成功，进入下一关')
    count = 0                     #初始化统计正确的题目数
    for i in range(10):           #10层循环
        a = random.randint(0,x*10)#随机数
        b = random.randint(0,x*10)
        d = '+-'                  #定义加减符号
        c = random.sample(d,1)    #随机取符号
        print(a,c[0],b,'= ')      #打印等式
        result = int(input())     #输入结果
        if result == a+b or result == a-b: #判断结果是否正确
            count += 1                     #正确count+1
    if count >= 9:                         #如果count 大于9 进入下一关
        print('第1关闯关成功，进入下一关')
        x += 1                             #闯关数自增
    else:                               
        print ('闯关失败')
        print('是否继续玩，继续请输入Y，否则输入N结束游戏')
        games = input()                   #判断是否结束游戏
        if games == 'Y':
            x = 1                         #调回第一关
            continue                      #跳过本次循环
        elif games == 'N':
            print('游戏结束')             #结束游戏
            break
        else:
            print('无效')
