ip = "192.168.1.34"
ip = ip.strip()
ips = ip.split(".")
L = len(ips)
if L == 4:
    for p in ips:
        if not p.isdigit() or (0 > int(p) or int(p) > 255):
            print("this ip is an illagel!")
            break
    else:
         print("this ip is a lagel!")
else:
    print("this ip is an illagel!")

    
