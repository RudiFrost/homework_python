import random


def rand(a, b, c):
    r = []
    for i in range(20):
        r.append(random.choice(a) + " " + random.choice(b) + " " + random.choice(c))
    return r


print(rand(["asd", "qwe", "zxc", "rty"], ["123", "345", "567", "987"], ["zzz", "xxx", "ccc", "qqq"]))
