#coding=utf-8
import random
def add(x,y):
     return x+y
def sub(x,y):
     return x-y

def chuangguan(x):
     n1=int(x)
     cmds = {'+': add, '-': sub}
     con1 = 0
     con2 = 0
     print("第%d关闯关开始" % (n1 / 10))
     print("%d以内的数字相加减，共10题，答对9题，闯关成功，进入下一关！" % (n1))
     while con1 < 10:
          m = [random.randint(1, n1) for i in range(2)]
          m.sort(reverse=True)
          n = random.choice("+-")
          sh = "%s %s %s =" % (m[0], n, m[1])
          anwser = cmds[n](*m)
          result = int(input(sh))
          if anwser == result:
               print("✔")
               con2 += 1
               if con1==9 and con2>=9:
                    print("第%d关闯关成功"%(n1/10))

          else:
               print("×")
               if con1==9 and con2<9:
                    print("闯关失败")
                    return False
          con1 += 1
     else:
          return True

i=1
while i <11:
    f=chuangguan(i*10)
    if f==False:
        yn = input("是否继续游戏？(y/n)")
        if yn=="y":
            i=1
            continue
        else:
            break
    i +=1
