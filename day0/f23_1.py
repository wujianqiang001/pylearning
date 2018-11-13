import random
def play(n):
    count = 0
    for i in range((n-1)*10+1,n*10+1):
        a = random.randint(1,n*10-1)
        b = random.randint(1,n*10-1)
        d = random.choice(["+","-"])
        if d == "+":
            c = input("%d+%d="%(a,b))
            m = True if c == str(a+b) else False
        else:
            if a > b:
                c = input("%d-%d="%(a,b))
                m = True if c == str(a-b) else False
            else:
                c = input("%d-%d="%(b,a))
                m = True if c == str(b-a) else False
        if m:
            print (u"√")
            count += 1
        else:
            print (u"×")

    if count >= 9:
        print("第%d关闯关成功"%n)
    else:
        print("第%d关闯关失败"%n)
play(3)
