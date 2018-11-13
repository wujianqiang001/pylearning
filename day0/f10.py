def fun():
    return 1, 2

#print(fun())


a = [[1,2,3,4,5],[2,3,4,5,6]]
b = [[1,2,33,4,5],[2,3,5,5,6]]

for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] != b[i][j]:
            print (a[i][j], b[i][j])
