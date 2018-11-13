from checkIP import checkip
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
