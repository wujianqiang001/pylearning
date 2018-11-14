ip = "192.168.1"
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
    print("this ip is a lagel!")
else:
    print("this ip is an illagel!")
        
