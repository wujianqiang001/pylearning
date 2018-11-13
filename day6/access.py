import pickle
with open("access.txt","wb+") as f:
    data = {"a":"A","b":"B"}
    pickle.dump(data, f)

with open("access.txt","rb+") as f:
    data = pickle.load(f)
    print(data)

import shelve
dbase = shelve.open("mydbase")
object1 = ["The","bright",("side","of"),["life"]]
object2 = {"name":"Brian","age":33,"motto":object1}
dbase["brian"]=object2
dbase["knight"]={"name":"Knight","motto":"Ni!"}
dbase.close()
dbase = shelve.open("mydbase")
print(len(dbase))
print(dbase.keys())
print(dbase["knight"])
