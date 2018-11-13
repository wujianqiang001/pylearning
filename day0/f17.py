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

with open("ips.txt") as f:
    for ip in f:
        ip = ip.strip()
        result = checkip(ip)
        #if result:
        #    cs = "legal"
        #else:
        #    cs = "illegal"
        cs = "legal" if result else "illegal"
        with open("report.txt","a") as f:
            f.write("%s--------is %s\n"%(ip,cs))
