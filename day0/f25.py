import os
with open("delete.txt") as f1:
    words = []
    for line in f1:
        line = line.strip()
        if not line[0].isdigit():
            words.append(line)
with open("delete1.txt","a") as f2:
    for line in words:
        f2.write(line+"\n")

os.remove("delete.txt")
os.rename("delete1.txt","delete.txt")
