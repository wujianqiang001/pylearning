def checkip(ip):
    ip = ip.strip()
    ips = ip.split(".")
    L = len(ips)
    if L == 4:
        for p in ips:
            if p.isdigit() and 0<= int(p) <= 255:
                flag = True
            else:
                flag = False
                break
    else:
        flag = False
    if flag:
        print("this ip: "+ip+" is a lagel!")
    else:
        print("this ip: "+ip+" is an illagel!")

checkip("127.0.0.1")
checkip("127.0.0.345")
checkip("127.0.*.1")
