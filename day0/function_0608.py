
import string,random,copy
D= {"version":123456,"add_domains":
    [{"1fdix.1bka.axy1.com":{"host":"1fdix.1bka.axy1.com","preproy":"switch","TLL":0}},
     {"rus1f.07hf.2xms.com":{"host":"rus1f.07hf.2xms.com","preproy":"switch","TLL":1}},
     {"cqphe.r7mw.nh6u.com":{"host":"cqphe.r7mw.nh6u.com","preproy":"switch","TLL":2}},
     {"sz8al.d69n.2b6o.com":{"host":"sz8al.d69n.2b6o.com","preproy":"switch","TLL":3}},
     ]}

def getRandom():
    a= string.digits
    b= string.ascii_lowercase
    c =a+b
    list=random.sample(c,4)
    str = "".join(list)
    return str

def host():
    list1 = []
    for i in range(3):
        ran= getRandom()
        list1.append(ran)
    list1.append("com")
    list = ".".join(list1)
    return list

dlist=[{"1fdix.1bka.axy1.com":{"host":"1fdix.1bka.axy1.com","preproy":"switch","TLL":0}},
     {"rus1f.07hf.2xms.com":{"host":"rus1f.07hf.2xms.com","preproy":"switch","TLL":1}},
     {"cqphe.r7mw.nh6u.com":{"host":"cqphe.r7mw.nh6u.com","preproy":"switch","TLL":2}},
     {"sz8al.d69n.2b6o.com":{"host":"sz8al.d69n.2b6o.com","preproy":"switch","TLL":3}},
     ]
for i in range(10):
    list = host()
    dic = {list: {"host": list, "preproy": "switch", "TLL": 0}}
    dlist.append(dic)
D1 = copy.copy(D)
D1["add_domains"]=dlist
print (D1)
#print D
