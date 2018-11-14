import string
import random
def teRandom(can):
    num = string.digits
    a = string.ascii_lowercase
    basestring = '%s%s' % (num, a)
    v3 = []
    for i in range(can):
        j = 3 * i
        for j in range(3 * can):
            if j == 0 | j % 3 == 0:
                baseKey1 = random.sample(basestring, 5)
            elif j % 3 == 1:
                baseKey2 = random.sample(basestring, 4)
            else:
                baseKey3 = random.sample(basestring, 4)

        b1 = "".join(baseKey1)
        b2 = "".join(baseKey2)
        b3 = "".join(baseKey3)
        key1 = b1 + "." + b2 + '.' + b3 + '.' + "com"

        value1 = {}
        value1['host'] = key1
        value1['preproy'] = 'switch'
        value1['TLL'] = i
        v2 = {}
        v2[key1] = value1
        v3.append(v2)
    v4 = {}
    v4["version"] = 123456
    v4["add_domains"] = v3
    print(v4)

#参数必须是3的倍数
teRandom(9)
{'version': 123456, 'add_domains':
    [{'zb9yg.wsgt.wq4j.com': {'host': 'zb9yg.wsgt.wq4j.com', 'preproy': 'switch', 'TLL': 0}},
     {'j3mlw.7tym.1rki.com': {'host': 'j3mlw.7tym.1rki.com', 'preproy': 'switch', 'TLL': 1}},
     {'p4amt.a28u.kl6v.com': {'host': 'p4amt.a28u.kl6v.com', 'preproy': 'switch', 'TLL': 2}},
     {'g2swr.cvg9.jpqg.com': {'host': 'g2swr.cvg9.jpqg.com', 'preproy': 'switch', 'TLL': 3}},
     {'de1zp.qpz8.n70e.com': {'host': 'de1zp.qpz8.n70e.com', 'preproy': 'switch', 'TLL': 4}},
     {'tbds8.k8mt.52rq.com': {'host': 'tbds8.k8mt.52rq.com', 'preproy': 'switch', 'TLL': 5}},
     {'l4nc0.feil.ghvl.com': {'host': 'l4nc0.feil.ghvl.com', 'preproy': 'switch', 'TLL': 6}},
     {'g498r.ac1o.yuk3.com': {'host': 'g498r.ac1o.yuk3.com', 'preproy': 'switch', 'TLL': 7}},
     {'jk35l.jw24.3mh8.com': {'host': 'jk35l.jw24.3mh8.com', 'preproy': 'switch', 'TLL': 8}}]}


