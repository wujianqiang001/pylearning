ip = "192.168.1.345"
ip = ip.strip()
ips = ip.split(".")
L = len(ips)
if L == 4:
    for s in range(L): 
        if ips[s].isdigit() and (0<= int(ips[s]) <= 255):
            if s == 3:
                print("this ip is a lagel!")
        else:
            print("this ip is an illagel!")
            break
else:
    print("this ip is an illagel!")
