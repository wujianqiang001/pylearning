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

def ipcheck():    
    with open("ips.txt") as f1, open("result.txt","w") as f2:
        for ip in f1:
            ip = ip.strip()
            flag = checkip(ip)
            if flag:
                f2.write("this ip: %s is a lagel!\n"%ip)
            else:
                f2.write("this ip: %s is an illagel!\n"%ip)

if __name__ == "__main__":
    ipcheck()
