ip = "127.0.0.q"
ip_s = ip.split(".")
L = len(ip_s)
count = 0
if L == 4:
    for p in ip_s:
        if p.isdigit() and 0<= int(p) <= 255:
            count += 1

if count == 4:
    print "This ip is a legal ip!"
else:
    print "This ip is an illegal ip!"
