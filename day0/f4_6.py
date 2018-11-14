def checkip(ip):
    ips = ip.strip().split(".")
    L = len(ips)
    if L == 4:
        for p in ips:
            if p.isdigit() and 0<= int(p) <= 255:
                pass
            else:
                return False
        else:
            return True
    else:
        return False
    
f = open("ips.txt","r")
for ip in f:
    ip = ip.strip()
    flag = checkip(ip)
    if flag:
        print("this ip: %s is a lagel!"%ip)
    else:
        print("this ip: %s is an illagel!"%ip)
