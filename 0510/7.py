import random


def rand(a, b, c):
    while True:
        yield random.choice(a) + " " + random.choice(b) + " " + random.choice(c)


q = 0
for i in rand(["asd", "qwe", "zxc", "rty"], ["123", "345", "567", "987"], ["zzz", "xxx", "ccc", "qqq"]):
    if q > 20:
        break
    print(i)
    q += 1
