def count():
    a = ["a", "b", "a", "b", "a", "c"]
    d = {}
    for key in a:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1

    return d

c = count()
print(c)
