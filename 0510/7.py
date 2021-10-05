import random


def rand(a, b, c, d):
    i = 0
    while i < d:
        yield random.choice(a) + " " + random.choice(b) + " " + random.choice(c)
        i += 1


for i in rand(["asd", "qwe", "zxc", "rty"], ["123", "345", "567", "987"], ["zzz", "xxx", "ccc", "qqq"], 20):
    print(i)
