def getphone():
    with open("phones.log") as f:
        for line in f:
            line = line.strip()
            yield line
def countphones():
    ps = getphone()
    pscount = {}
    for p in ps:
        if p not in  pscount:
            pscount[p] = 1
        else:
            pscount[p] += 1
    return pscount
if __name__ == '__main__':
    pscount = countphones()
    pssort = sorted(pscount.items(), key=lambda x: x[1], reverse=True)
    print(len(pssort))
    for k, v in pssort:
        print(k, v)


