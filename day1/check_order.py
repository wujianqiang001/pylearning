#order_id = "atb12345|apple|5.50|2|1|11.00|tony|beijing"
import sys
flag = "Y"
while flag == "Y":
    count = 0
    while count < 3:
        orders = raw_input("please input a order_id>>>")
        orders = orders.split("|")
        if len(orders) == 8:
            break
        else:
            count += 1#count = count + 1
            continue
    else:
        sys.exit()
            
    order_id = orders[0]
    s_name = orders[1]
    p_name = orders[6]
    c_name = orders[7]
    L = len(order_id)
    if L == 8:
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

    flag = raw_input("Do you continue? please input Y\n")
