
def checkorder(orders):
    orders = orders.split("|")
    L = len(orders)
    if L != 8:
        print "orders %s 'length is not 8"%("|".join(orders))
    else:
        order_id = orders[0]
        s_name = orders[1]
        p_name = orders[6]
        c_name = orders[7]
        L1 = len(order_id)
        if L1 == 8:
            if order_id[:3].isalpha() and order_id[3:].isdigit():
                #if order_name[0].lower() == orders[0]:
                if order_id.startswith(s_name.lower()[0]) and order_id[1] == p_name.lower()[0] \
                   and order_id[2] == c_name.lower()[0]:
                    print "order_id %s is a legal"%order_id
                else:
                    print "order_id %s is a illegal"%order_id
            else:
                print "order_id %s is a illegal"%order_id
        else:
            print "order_id %s is a illegal"%order_id
        

f = open("test_orders.txt", "r")
lines = f.readlines()
f.close()       
for line in lines:
    order = line.strip()
    checkorder(order)
    
