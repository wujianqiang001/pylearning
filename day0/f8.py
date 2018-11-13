def newline(n, s):
    if n <1:
        for i in range(1, s):
            print(i, end = ' ')
    else:
        for i in range(1, s):
            print(i, end = ' ')
            if not i%n:
                print("\n")

newline(8,40)
