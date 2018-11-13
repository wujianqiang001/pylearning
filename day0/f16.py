f = open("test.txt", "w") #内置函数open(),"test.txt"是新建的文本,"w"是操作模式，即写操作
f.write("hello world! long long ago") #往文本test.txt中写入hello world!
f.close()#关闭操作

f = open("test.txt", "r")#"r"是读操作，当读操作时，也可以省略r,即 f = open("test.txt")
line = f.read()#读取文本中的内容
f.close()
print(line)

f = open("test.txt", "a")
f.write("I am Fine!")
f.close()

f = open("test.txt")
line = f.readlines()
f.close()
print(line)

f = open("test.txt", "a")
f.write("\nI am Fine!")
f.close()

f = open("test.txt")
line = f.readlines()
f.close()
print(line)

f = open("test.txt")
line = f.read()
f.close()
print(line)
