#coding=utf-8
#ip = input("请输入一个ip地址：")
ip = "192.168.1.1"
ip1 = ip.strip()
ip2 = ip1.split(".")
if len(ip2) == 4:
    for s in range(len(ip2)):
        if ip2[s].isdigit() == True:
            ip3 = int(ip2[s])
            if s == 0:
                if ip3 >= 1 and ip3 <= 255:
                    continue
                else:
                    print("3不合法的ip")
                    break
            else:
                if ip3 >=0 and ip3 <= 255:
                    if s == 3:
                        print("合法的ip")
                else:
                    print("4不合法的ip")
                    break
        else:
            print("2不合法的ip")
            break
else:
    print("1不合法的ip")

