ip = "192.168.1"
ip = ip.strip()
ips = ip.split(".")
count = 0
for p in ips:
    if p.isdigit() and 0<= int(p) <= 255:
        count += 1
        
if count == 4:
    print("this ip is a lagel!")
else:
    print("this ip is an illagel!")
