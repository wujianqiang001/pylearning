def fun():
    def fun1():
        return 1
    return 1,2,3,[1,2,3],fun1

if __name__ == "__main__":
    f = fun()
    print(type(f))
    print(f)
    a,b,c,d,e = f
    print(e())
