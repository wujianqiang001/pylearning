
ip = raw_input('Plase input a ip:')
#print(len(ip))
p = ip.split('.')
#print(p)
#print(len(p))
#for w in p:
    #print(w.isdigit())
    #num = int(w)
    #print(num)

if len(ip) < 7 or len(ip) > 15:
    print('The ip is illegal.')
elif len(p) !=4:
    print('The ip is illegal.')
else:
    for w in p:
        #print(w.isdigit())
        #print(w)
        if not w.isdigit():
            print('The ip is illegal.')
            break
        elif int(w) < 0 or int(w) > 255:
            print('The ip is illegal.')
            break
    else:
        print('The ip is legal.')




