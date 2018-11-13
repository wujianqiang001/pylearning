def checkip(ip):
    ips = ip.split(".")
    L = len(ips)
    flag = False
    if L == 4:
        for p in ips:
            if p.isdigit() and 0<= int(p) <=255:
                flag = True
            else:
                flag = False
                break
    return flag
