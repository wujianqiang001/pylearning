flag1 = "Y"
while flag1 == "Y":
    ip = raw_input("please input an ip:")
    ip_s = ip.split(".")
    L = len(ip_s)
    flag = False
    if L == 4:
        for p in ip_s:
            if p.isdigit() and 0<= int(p) <= 255:
                flag = True
            else:
                flag = False
    if flag:
        print "This %s is a legal ip!"%ip
    else:
        print "This %s is an illegal ip!"%ip
    flag1 = raw_input("Do you continue to go on?")
