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

def main(ip):
    flag = checkip(ip)
    if flag:
        print("this ip: %s is a lagel!"%ip)
    else:
        print("this ip: %s is an illagel!"%ip)

def main1(ip):
    flag = checkip(ip)
    if flag:
        print("this ip: "+ip+" is a lagel!")
    else:
        print("this ip: "+ip+" is an illagel!")

def main2(ip):
    flag = checkip(ip)
    if flag:
        return 200
    else:
        return 403
    
main("127.0.0.1")
main("127.0.0.345")
main("127.0.*.1")
main("127.0.1")
main("127.0.1.23.34")

main1("127.0.0.1")
main1("127.0.0.345")
main1("127.0.*.1")
