ip = 123456789123
ip = str(ip)
ip = [ip[i:i+3] for i in range(0,12,3)]
print ip
print ".".join(ip)